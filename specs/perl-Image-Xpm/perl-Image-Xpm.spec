# $Id$
# Authority: dries
# Upstream: Mark Summerfield <summer$qtrac,eu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Xpm

Summary: Load, create, manipulate and save xpm image files
Name: perl-Image-Xpm
Version: 1.09
Release: 2.2%{?dist}
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Xpm/

Source: http://www.cpan.org/modules/by-module/Image/Image-Xpm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can load, create, manipulate and save xpm image files.

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
%doc %{_mandir}/man3/Image::Xpm.3pm*
%dir %{perl_vendorlib}/Image/
#%{perl_vendorlib}/Image/Xpm/
%{perl_vendorlib}/Image/Xpm.pm

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-2
- Fixed the license (Thanks to David Necas !)

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Initial package.
