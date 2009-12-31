# $Id$
# Authority: dries
# Upstream: Luke Closs <cpan$5thplane,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Selenium

Summary: Test applications using Selenium Remote Control
Name: perl-Test-WWW-Selenium
Version: 1.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Selenium/

Source: http://www.cpan.org/authors/id/L/LU/LUKEC/Test-WWW-Selenium-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Mock::LWP)
#BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(URI::Escape) >= 1.31
Requires: perl(LWP::UserAgent)
Requires: perl(URI::Escape) >= 1.31

%filter_from_requires /^perl*/d
%filter_setup

%description
Test applications using Selenium Remote Control.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes README todo.txt
%doc %{_mandir}/man3/Test::WWW::Selenium.3pm*
%doc %{_mandir}/man3/WWW::Selenium.3pm*
%doc %{_mandir}/man3/WWW::Selenium::Util.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
%{perl_vendorlib}/Test/WWW/Selenium.pm
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Selenium.pm
%{perl_vendorlib}/WWW/Selenium/Util.pm
%{perl_vendorlib}/Test/WWW/mypod2html.pl

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.21-1
- Updated to version 1.21.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 1.20-1
- Updated to version 1.20.

* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 1.19-1
- Updated to version 1.19.

* Fri Sep  4 2009 Christoph Maser <cmr@financial.com> - 1.18-1
- Updated to version 1.18.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.17-1
- Updated to version 1.17.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
