# $Id$

# Authority: dag

%define real_name Net-DNS

Summary: Net-DNS Perl module
Name: perl-Net-DNS
Version: 0.38
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/C/CR/CREIN/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Digest::HMAC)
%{!?rhel21:BuildRequires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?rhel21:BuildRequires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}
Requires: perl >= 0:5.00503, perl(Digest::HMAC)
%{!?rhel21:Requires: perl(Digest::MD5) >= 2.12, perl(MIME::Base64) >= 2.11}
%{?rhel21:Requires: perl-Digest-MD5 >= 2.12, perl-MIME-Base64 >= 2.11}

%description
Net-DNS Perl module

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
%doc Changes README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.38-0
- Updated to release 0.38.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 0.33-0
- Initial package. (using DAR)
