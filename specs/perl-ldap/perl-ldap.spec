# $Id$
# Authority: dries
# Upstream: Graham Barr <gbarr$pobox,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name perl-ldap

Summary: Interface to LDAP for Perl
Name: perl-ldap
Version: 0.31
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ldap/

Source: http://www.cpan.org/modules/by-module/perl/perl-ldap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl(Convert::ASN1), perl(XML::SAX::Base),  perl(IO::Socket::SSL)

%description
This package contains a perl module with an interface to LDAP.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_vendorarch} %{buildroot}%{perl_archlib}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS README RELEASE_NOTES TODO
%{_mandir}/man3/*
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Net/
%{perl_vendorlib}/Bundle/Net/LDAP.pm
%dir %{perl_vendorlib}/LWP/
%dir %{perl_vendorlib}/LWP/Protocol/
%{perl_vendorlib}/LWP/Protocol/ldap.pm
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/LDAP*

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
