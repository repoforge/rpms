# $Id$
# Authority: dag

# ExcludeDist: el4

%define real_name Digest-SHA1

Summary: Digest-SHA1 Perl module
Name: perl-Digest-SHA1
Version: 2.07
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA1/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/Digest-SHA1-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

The Digest::SHA1 module provide a procedural interface for simple use,
as well as an object oriented interface that can handle messages of
arbitrary length and which can read files directly.

A binary digest will be 20 bytes long. A hex digest will be 40
characters long. A base64 digest will be 27 characters long.

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

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
%doc Changes MANIFEST README fip180-1*
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Mar 18 2004 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.03-0
- Initial package. (using DAR)
