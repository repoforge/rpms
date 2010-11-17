# $Id$
# Authority: dag
# Upstream: Mark Summerfield <summer$qtrac,eu>

### EL6 ships with perl-Image-Xbm-1.08-12.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Xbm

Summary: Perl module to load, create, manipulate and save xbm image files
Name: perl-Image-Xbm
Version: 1.08
Release: 1%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Xbm/

Source: http://www.cpan.org/modules/by-module/Image/Image-Xbm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Image-Xbm is a Perl module to load, create, manipulate and
save xbm image files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/Image::Xbm.3pm*
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Xbm/
%{perl_vendorlib}/Image/Xbm.pm

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Fixed the license (Thanks to David Necas !)

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
