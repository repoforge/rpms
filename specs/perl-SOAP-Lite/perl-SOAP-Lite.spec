# $Id: $
# Authority: dries
# Upstream: Byrne Reese <cpancontact$majordomo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-Lite

Summary: Interface to SOAP
Name: perl-SOAP-Lite
Version: 0.66.1
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Lite/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-XML-Parser, perl-Crypt-SSLeay, perl-Compress-Zlib

%description
SOAP::Lite for Perl is a collection of Perl modules which provides a simple 
and lightweight interface to the Simple Object Access Protocol (SOAP) both 
on client and server side.

%prep
%setup -n %{real_name}-%{version}

%build
(echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}") || echo "ignore warnings"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*/*/.packlist
# remove dependency on MQSeries
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/SOAP/Transport/MQ.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man?/*
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
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.66.1-1
- Updated to release 0.66.1.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.60a
- Initial package.
