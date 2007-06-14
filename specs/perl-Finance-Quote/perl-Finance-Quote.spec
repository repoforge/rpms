# $Id$
# Authority: dag
# Upstream: David Hampton <hampton$employees,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-Quote

Summary: Perl module to get stock and mutual fund quotes from various exchanges
Name: perl-Finance-Quote
Version: 1.13
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-Quote/

Source: http://www.cpan.org/modules/by-module/Finance/Finance-Quote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

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
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Initial package. (using DAR)
