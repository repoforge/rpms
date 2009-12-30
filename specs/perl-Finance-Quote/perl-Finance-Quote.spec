# $Id$
# Authority: dag
# Upstream: David Hampton <hampton$employees,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-Quote

Summary: Perl module to get stock and mutual fund quotes from various exchanges
Name: perl-Finance-Quote
Version: 1.17
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-Quote/

Source: http://search.cpan.org/CPAN/authors/id/E/EC/ECOCODE/Finance-Quote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Crypt::SSLeay)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::TableExtract)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(HTTP::Request::Common)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.005
Requires: perl(Crypt::SSLeay)
Requires: perl(HTML::TableExtract)
Requires: perl(HTML::TreeBuilder)
Requires: perl(HTTP::Request::Common)
Requires: perl(LWP::UserAgent)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup


%description
Finance-Quote is a Perl module to get stock and mutual fund quotes
from various exchanges.

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
%doc ChangeLog Documentation/FAQ Documentation/README INSTALL MANIFEST META.yml
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Finance/
%{perl_vendorlib}/Finance/Quote/
%{perl_vendorlib}/Finance/Quote.pm

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.17-1
- Updated to version 1.17.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
