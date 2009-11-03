# $Id$
# Authority: dries
# Upstream: Pierre Denis <pdenis$fotango,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WSDL-Generator

Summary: Generate wsdl file automagically
Name: perl-WSDL-Generator
Version: 0.04
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WSDL-Generator/

Source: http://www.cpan.org/authors/id/P/PD/PDENIS/WSDL-Generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
You know folks out there who use another language than Perl (huh?) and
you want to release a SOAP server for them

   1/ that's very kind of you
   2/ you need to generate a wsdl file
   3/ this module can help
Because Perl is dynamically typed, it is a fantastic language to write SOAP
clients, but that makes perl not-so-easy to use as SOAP server queried by
statically typed languages such as Delphi, Java, C++, VB...
These languages need a WSDL file to communicate with your server.
The WSDL file contains all the data structure definition necessary to interact
with the server. It contains also the namespace and URL as well.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HowTo-SOAPLite.txt README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WSDL/Generator.pm
%{perl_vendorlib}/WSDL/WSDLTest.pm
%{perl_vendorlib}/WSDL/Generator/*

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
