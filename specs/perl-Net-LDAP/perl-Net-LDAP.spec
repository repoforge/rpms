# $Id$

# Authority: dag

%define real_name perl-ldap

Summary: set of Perl classes implementing an LDAP client
Name: perl-Net-LDAP
Version: 0.2701
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-LDAP/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/G/GB/GBARR/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503, perl(Carp), perl(Convert::ASN1), perl(Data::Dumper)
Requires: perl(Exporter), perl(Getopt::Std), perl(MIME::Base64)
#Requires: perl(IO::Socket::SSL)
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
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CREDITS MANIFEST RELEASE_NOTES README TODO contrib/
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Mon Feb 03 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
