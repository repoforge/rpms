# $Id$
# Authority: dries
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-HomeDir

Summary: Find your home and other directories, on any platform
Name: perl-File-HomeDir
Version: 0.67
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-HomeDir/

Source: http://www.cpan.org/modules/by-module/File/File-HomeDir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47
Requires: perl >= 0:5.005

%description
Find your home and other directories, on any platform.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/File::HomeDir.3pm*
%doc %{_mandir}/man3/File::HomeDir::*.3pm*
%dir %{perl_vendorlib}/File/
%{perl_vendorlib}/File/HomeDir/
%{perl_vendorlib}/File/HomeDir.pm

%changelog
* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.67-1
- Updated to release 0.67.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.65-1
- Updated to release 0.65.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Updated to release 0.62.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
