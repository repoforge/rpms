# $Id$
# Authority: dag
# Upstream: Anthony G Persaud <apersaud$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Nmap-Parser

Summary: Perl module to parse nmap scan data
Name: perl-Nmap-Parser
Version: 1.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Nmap-Parser/

Source: http://www.cpan.org/modules/by-module/Nmap/Nmap-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Nmap-Parser is a Perl module to parse nmap scan data.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Nmap::Parser.3pm*
%dir %{perl_vendorlib}/Nmap/
%{perl_vendorlib}/Nmap/Parser.pm

%changelog
* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.11-1
- Initial package. (using DAR)
