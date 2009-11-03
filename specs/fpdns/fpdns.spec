# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS-Fingerprint

Summary: Fingerprinting DNS servers
Name: fpdns
Version: 0.9.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.rfc.se/fpdns/

#Source: http://www.rfc.se/fpdns/distfiles/fpdns-%{version}.tar.gz
Source: http://www.rfc.se/fpdns/distfiles/Net-DNS-Fingerprint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
fpdns is a tool to fingerprint DNS servers. Requirements for protocol behaviour
of DNS implementations is widely documented in the case of 'common' dns
messages. The DNS protocol is over 20 years old and since its inception, there
have been over 40 independent DNS implementations, while some implementations
have over 20 versions.

The methodology used to identify individual nameserver implementations is based
on "borderline" protocol behaviour. The DNS protocol offers a multitude of
message bits, response types, opcodes, classes, query types and label types in
a fashion that makes some mutually exclusive while some are not used in a query
messages at all. Not every implementation offers the full set of features the
DNS protocol set currently has. Some implementations offer features outside the
protocol set, and there are implementations that do not conform to standards.

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
%doc %{_mandir}/man1/fpdns.1*
%{_bindir}/fpdns
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/DNS/
%{perl_vendorlib}/Net/DNS/Fingerprint.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
