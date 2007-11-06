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

Source: http://search.cpan.org//CPAN/authors/id/L/LU/LUKEC/Test-WWW-Selenium-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker), perl(Test::More) >= 0.42
BuildRequires: perl(Test::Exception), perl(Test::Pod)

%description
Test applications using Selenium Remote Control.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

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
