# $Id$

# Authority: dries
# Upstream: Paul Stodghill <stodghil$cs,cornell,edu>

%define real_name SOAP-Clean
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Simply deploy SOAP clients and servers
Name: perl-SOAP-Clean
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Clean/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STODGHIL/SOAP-Clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
SOAP::Clean is a set of modules for quickly and simply deploying SOAP
client and servers. On the server-side, it is intended to enable legacy,
command-line oriented applications to be made into Web Services with
little or no modification. On the client-side, it is intended to make
Web Services look like legacy, command-line oriented applications!

SOAP::Clean was original developed to provide a framework for
computational scientists to use one another's components, without having
to download and compile each others codes. The name SOAP::Clean comes
from the fact that it is designed for entire XML documents and non-XML
files to be embedded within SOAP requests and responses without losing
their integrety. These files are passed directly to the legacy
application on the server and stored directly to disk on the client.

SOAP::Clean is _not_ intended for implementing "servlets". In
particular, it makes absolutely no attempt to map XML data types into
convenient Perl datatypes. Nor does it allow arbitrary Perl functions on
the server to be invoked by SOAP requests. If need this functionality, I
recommend SOAP::Lite.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog
%doc %{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorlib}/SOAP/Clean.pm
%{perl_vendorlib}/SOAP/Clean/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorlib}/SOAP/ChangeLog
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
