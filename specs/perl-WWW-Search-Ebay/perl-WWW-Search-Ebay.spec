# $Id$
# Authority: dries
# Upstream: Martin Thurn <mthurn$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Search-Ebay

Summary: Backend for searching www.ebay.com
Name: perl-WWW-Search-Ebay
Version: 2.242
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search-Ebay/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Search-Ebay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.005
BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Date::Manip)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Capture::Stderr)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(WWW::Search::Test) >= 2.265
Requires: perl >= 0:5.005

%description
This is a backend for use with the WWW::Search module for searching on Ebay.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/WWW::Search::Ebay.3pm*
%doc %{_mandir}/man3/WWW::Search::Ebay::*.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Search/
%{perl_vendorlib}/WWW/Search/Ebay/
%{perl_vendorlib}/WWW/Search/Ebay.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 2.242-1
- Updated to release 2.242.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 2.234-1
- Updated to release 2.234.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 2.232-1
- Updated to release 2.232.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.231-1
- Updated to release 2.231.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.229-1
- Updated to release 2.229.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.226-1
- Updated to release 2.226.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.223-1
- Updated to release 2.223.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.222-1
- Updated to release 2.222.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.218-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.218-1
- Updated to release 2.218.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.215-1
- Updated to release 2.215.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.206-1
- Updated to release 2.206.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.205-1
- Updated to release 2.205.

* Tue Dec 14 2004 Dries Verachtert <dries@ulyssis.org> - 2.204-1
- Updated to release 2.204.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 2.196-1
- Update to release 2.196.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.194-1
- Initial package.
