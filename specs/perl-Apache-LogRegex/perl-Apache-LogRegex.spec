# $Id$
# Authority: dag
# Upstream: Peter Hickman <peterhi$ntlworld,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-LogRegex

Summary: Perl module to parse a line from an Apache logfile into a hash
Name: perl-Apache-LogRegex
Version: 1.4
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-LogRegex/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-LogRegex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Apache-LogRegex is a perl module to parse a line from an Apache
logfile into a hash.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Apache::LogRegex.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/LogRegex.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
