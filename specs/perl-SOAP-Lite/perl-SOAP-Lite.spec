# $Id: $

# Authority: dries
# Upstream: Byrne Reese <cpancontact$majordomo,com>

%define real_name SOAP-Lite
%define dir_version 0.60
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to SOAP
Name: perl-SOAP-Lite
Version: 0.60a
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Lite/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/B/BY/BYRNE/SOAP/SOAP-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-XML-Parser, perl-Crypt-SSLeay, perl-Compress-Zlib

%description
SOAP::Lite for Perl is a collection of Perl modules which provides a simple 
and lightweight interface to the Simple Object Access Protocol (SOAP) both 
on client and server side.

%prep
%setup -n %{real_name}-%{dir_version}

%build
(echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}") || echo "ignore warnings"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%{_mandir}/man?/*
%{_bindir}/SOAPsh.pl
%{_bindir}/XMLRPCsh.pl
%{_bindir}/stubmaker.pl
%{perl_vendorlib}/Apache
%{perl_vendorlib}/IO
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/UDDI
%{perl_vendorlib}/XML
%{perl_vendorlib}/XMLRPC

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.60a
- Initial package.
