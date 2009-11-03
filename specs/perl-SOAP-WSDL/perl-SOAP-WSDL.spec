# $Id$
# Authority: dries
# Upstream: Martin Kutter <martin,kutter$fen-net,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SOAP-WSDL
%define real_version 2.000010

Summary: SOAP with WSDL support
Name: perl-SOAP-WSDL
Version: 2.00.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SOAP-WSDL/

Source: http://www.cpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Class::Std::Fast) >= 0.0.5
BuildRequires: perl(Cwd)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Storable)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Parser::Expat)
Requires: perl >= 2:5.8.0

%description
A WSDL-driven message preprocessor for SOAP::Lite.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes HACKING LICENSE MANIFEST META.yml README TODO example/
%doc %{_mandir}/man1/wsdl2perl.pl.1*
%doc %{_mandir}/man3/SOAP::WSDL.3pm*
%doc %{_mandir}/man3/SOAP::WSDL::*.3pm*
%{_bindir}/wsdl2perl.pl
%dir %{perl_vendorlib}/SOAP/
%{perl_vendorlib}/SOAP/WSDL/
%{perl_vendorlib}/SOAP/WSDL.pm

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 2.00.10-1
- Updated to release 2.00.10.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.00.01-1
- Updated to release 2.00.01.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
