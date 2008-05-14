# $Id: $
# Authority: dries
# Upstream: Byrne Reese <cpancontact$majordomo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-Lite
%define real_version 0.710005

Summary: Interface to SOAP
Name: perl-SOAP-Lite
Version: 0.710.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Lite/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(XML::Parser)

%description
SOAP::Lite for Perl is a collection of Perl modules which provides a simple
and lightweight interface to the Simple Object Access Protocol (SOAP) both
on client and server side.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Replace /bin/env by /usr/bin/env (so it works on RH7 and EL2 as well)
%{__perl} -pi -e 's|^#!/.*bin/env|#!%{_bindir}/env|i;' bin/*.pl


%build
(echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}") || echo "ignore warnings"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

### Remove dependency on MQSeries
%{__rm} -f %{buildroot}%{perl_vendorlib}/SOAP/Transport/MQ.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes HACKING MANIFEST META.yml README ReleaseNotes.txt examples/
%doc %{_mandir}/man1/SOAPsh.pl.1*
%doc %{_mandir}/man1/XMLRPCsh.pl.1*
%doc %{_mandir}/man1/stubmaker.pl.1*
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/SOAP/
%{_bindir}/SOAPsh.pl
%{_bindir}/XMLRPCsh.pl
%{_bindir}/stubmaker.pl
%{perl_vendorlib}/Apache/
%{perl_vendorlib}/IO/
%{perl_vendorlib}/OldDocs/
%{perl_vendorlib}/SOAP/
%{perl_vendorlib}/UDDI/
%{perl_vendorlib}/XML/
%{perl_vendorlib}/XMLRPC/

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.710.05-1
- Updated to release 0.710.05.

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.69-1
- Updated to release 0.69.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.66.1-1
- Updated to release 0.66.1.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.60a
- Initial package.
