# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name perl-ldap

Summary: set of Perl classes implementing an LDAP client
Name: perl-Net-LDAP
Version: 0.3202
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-LDAP/

Source: http://www.cpan.org/modules/by-module/Net/perl-ldap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(IO::Socket::SSL), perl(Convert::ASN1)
BuildRequires: perl(Authen::SASL), perl(Digest::MD5), perl(URI::ldap), perl(XML::SAX::Base)
BuildRequires: perl(MIME::Base64), perl(URI)
Requires: perl >= 0:5.00503, perl(Carp), perl(Convert::ASN1), perl(Data::Dumper)
Requires: perl(Exporter), perl(Getopt::Std), perl(MIME::Base64), perl(Authen::SASL)
Requires: perl(IO::Socket::SSL)
AutoReq: no

Obsoletes: perl-ldap
Provides: %{real_name}

%description
Net-LDAP is a set of Perl classes implementing an LDAP client. The aim of
the perl-ldap project is to implement a very portable LDAP client in perl
by relying on as little compiled code as possible.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes contrib/ CREDITS MANIFEST README TODO
%doc %{_mandir}/man?/*
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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3202-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 27 2005 Dag Wieers <dag@wieers.com> - 0.3202-1
- Updated to release 0.3202.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com> - 0.2701-0
- Initial package. (using DAR)
