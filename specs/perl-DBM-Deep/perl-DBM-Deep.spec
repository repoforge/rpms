# $Id$
# Authority: dag
# Upstream: Rob Kinyon <rob,kinyon$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBM-Deep

Summary: Perl module that implements a pure perl multi-level hash/array DBM that supports transactions
Name: perl-DBM-Deep
Version: 1.0001
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBM-Deep/

Source: http://www.cpan.org/modules/by-module/DBM/DBM-Deep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
DBM-Deep is a Perl module that implements a pure perl multi-level
hash/array DBM that supports transactions.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/DBM/
%{perl_vendorlib}/DBM/Deep/
%{perl_vendorlib}/DBM/Deep.pm
%{perl_vendorlib}/DBM/Deep.pod

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.0001-1
- Initial package. (using DAR)
