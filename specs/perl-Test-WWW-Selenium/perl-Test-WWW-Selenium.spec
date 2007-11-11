# $Id$
# Authority: dries
# Upstream: Luke Closs <cpan$5thplane,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Selenium

Summary: Test applications using Selenium Remote Control
Name: perl-Test-WWW-Selenium
Version: 1.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Selenium/

Source: http://www.cpan.org/modules/by-module/Test/Test-WWW-Selenium-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)(Test::More) >= 0.42
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Pod)

%description
Test applications using Selenium Remote Control.

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
%doc Changes README
%doc %{_mandir}/man3/*WWW::Selenium*
%{perl_vendorlib}/Test/WWW/Selenium.pm
%{perl_vendorlib}/WWW/Selenium.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
