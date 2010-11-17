# $Id: $
# Authority: dries
# Upstream: Byrne Reese <cpancontact$majordomo,com>

### EL6 ships with perl-SOAP-Lite-0.710.10-2.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-Lite

Summary: Interface to SOAP
Name: perl-SOAP-Lite
Version: 0.711
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Lite/

Source: http://search.cpan.org/CPAN/authors/id/M/MK/MKUTTER/SOAP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FCGI)
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Socket::SSL)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(XML::Parser) >= 2.23
BuildRequires: perl(constant)
BuildRequires: perl(version)
BuildRequires: perl >= 5.006
Requires: perl(Compress::Zlib)
Requires: perl(FCGI)
Requires: perl(HTTP::Daemon)
Requires: perl(IO::File)
Requires: perl(IO::Socket::SSL)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Scalar::Util)
Requires: perl(Task::Weaken)
Requires: perl(Test::More)
Requires: perl(URI)
Requires: perl(XML::Parser) >= 2.23
Requires: perl(constant)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup


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
%{__make} test

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
%{perl_vendorlib}/SOAP/
%{perl_vendorlib}/UDDI/
%{perl_vendorlib}/XML/
%{perl_vendorlib}/XMLRPC/

%changelog
* Wed May 26 2010 Christoph Maser <cmaser@gmx.de> - 0.711-1
- Updated to version 0.711.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 0.710.08-1
- Updated to release 0.710.08.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.710.07-1
- Updated to release 0.710.07.

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
