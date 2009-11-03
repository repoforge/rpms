# $Id$
# Authority: dries
# Upstream: Alexandr Ciornii <alexchorny$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-NCopy

Summary: Copy files
Name: perl-File-NCopy
Version: 0.36
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-NCopy/

Source: http://www.cpan.org/modules/by-module/File/File-NCopy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Easy functions for copying files.

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
%doc Changes Contributing.txt MANIFEST META.yml
%doc %{_mandir}/man3/File::NCopy.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/NCopy/
%{perl_vendorlib}/File/NCopy.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
