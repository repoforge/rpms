# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name perl-ldap
#define real_name Net-LDAP

Summary: Interface to LDAP for Perl
Name: perl-LDAP
Version: 0.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-LDAP/

Source: http://www.cpan.org/modules/by-module/Net/perl-ldap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(Authen::SASL) >= 2.0
BuildRequires: perl(Convert::ASN1)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket::SSL) > 0.81
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(URI::ldap) >= 1.1
BuildRequires: perl(XML::SAX::Base)
Requires: perl >= 0:5.004
Requires: perl(IO::Socket::SSL)

Obsoletes: perl-ldap <= %{version}-%{release}
Obsoletes: perl-Net-LDAP <= %{version}-%{release}
Provides: perl-ldap = %{version}-%{release}
Provides: perl-Net-LDAP = %{version}-%{release}

%description
This package contains a perl module with an interface to LDAP.

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
find bin/ contrib/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS Changes INSTALL MANIFEST META.yml README SIGNATURE TODO install-nomake bin/ contrib/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Net/
%{perl_vendorlib}/Bundle/Net/LDAP.pm
%dir %{perl_vendorlib}/LWP/
%dir %{perl_vendorlib}/LWP/Protocol/
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/LDAP/
%{perl_vendorlib}/Net/LDAP.pm
%{perl_vendorlib}/Net/LDAP.pod
%{perl_vendorlib}/Net/LDAPI.pm
%{perl_vendorlib}/Net/LDAPS.pm

%changelog
* Fri Aug 17 2007 Dag Wieers <dag@wieers.com> - 0.34-1
- Renamed package to perl-LDAP to match upstream.
  (though distribution is called perl-ldap and module is perl-Net-LDAP !)

* Wed Aug 16 2006 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
