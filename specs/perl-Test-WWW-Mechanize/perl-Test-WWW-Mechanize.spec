# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-WWW-Mechanize

Summary: Testing-specific WWW::Mechanize subclass
Name: perl-Test-WWW-Mechanize
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-WWW-Mechanize/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-WWW-Mechanize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp::Assert::More)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Server::Simple) >= 0.42
BuildRequires: perl(HTTP::Server::Simple::CGI)
#BuildRequires: perl(Test::Builder::Tester) >= 1.09
BuildRequires: perl(Test::Builder::Tester) 
BuildRequires: perl(Test::LongString) >= 0.12
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::file)
BuildRequires: perl(WWW::Mechanize) >= 1.24
BuildRequires: perl >= 5.008
Requires: perl(Carp::Assert::More)
Requires: perl(HTML::TreeBuilder)
Requires: perl(HTTP::Server::Simple) >= 0.42
Requires: perl(HTTP::Server::Simple::CGI)
Requires: perl(Test::Builder::Tester) >= 1.09
Requires: perl(Test::LongString) >= 0.12
Requires: perl(Test::More)
Requires: perl(URI::file)
Requires: perl(WWW::Mechanize) >= 1.24
Requires: perl >= 5.008

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Test-WWW-Mechanize is a Perl module implements
a testing-specific WWW::Mechanize subclass.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc %{_mandir}/man3/Test::WWW::Mechanize.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/WWW/
#%{perl_vendorlib}/Test/WWW/Mechanize/
%{perl_vendorlib}/Test/WWW/Mechanize.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.30-1
- Updated to version 1.30.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.24-1
- Updated to version 1.24.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
