# $Id$
# Authority: dries
# Upstream: Paul Stodghill <stodghil$cs,cornell,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-Clean

Summary: Simply deploy SOAP clients and servers
Name: perl-SOAP-Clean
Version: 0.02
Release: 2.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-Clean/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-Clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Provides: perl(SOAP::Clean::Processes)

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorlib}/SOAP/ChangeLog
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorlib}/SOAP/Clean.pm
%{perl_vendorlib}/SOAP/Clean/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-2.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-2
- Fix requires/provides.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
