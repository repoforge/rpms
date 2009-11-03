# $Id$
# Authority: dag
# Upstream: Dirk Eddelbuettel <edd$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-YahooQuote

Summary: Perl module to get stock quotes from Yahoo! Finance
Name: perl-Finance-YahooQuote
Version: 0.22
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-YahooQuote/

Source: http://www.cpan.org/modules/by-module/Finance/Finance-YahooQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Finance-YahooQuote is a Perl module to get stock quotes from Yahoo! Finance.

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
%doc CHANGES ChangeLog GNU-LICENSE MANIFEST META.yml README
%doc %{_mandir}/man1/yahooquote.1*
%doc %{_mandir}/man3/Finance::YahooQuote.3pm*
%{_bindir}/yahooquote
%dir %{perl_vendorlib}/Finance/
%{perl_vendorlib}/Finance/YahooQuote.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
