# $Id$
# Authority: dries
# Upstream: Alex Pankratov <ap$swapped,cc>

Summary: File signing and signature verification utility
Name: sign
Version: 1.0.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/File
URL: http://swapped.cc/sign/

Source: http://swapped.cc/sign/files/sign-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
sign is a file processing tool. sign reads from the files
(including stdin) and writes to the files (including stdout). It can be used
to append signatures to the files or to verify and/or strip them.

Between signing and verifying latter will account for a bulk of usage. When
checking the signature, sign will check for both intergrity and authenticity
of the file. An integrity check is done by validating SHA-1 hash embedded
into the signature, and an authenticity is ensured by checking signer's
credentials against a trusted list.

sign adopts OpenSSH-style authentication model, where the trust hierarchy
is flat (no certificates), an authentication is done with public keys and
the list of trusted keys is grown gradually on as-needed basis.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/sign %{buildroot}%{_bindir}/sign
%{__ln_s} -f sign %{buildroot}%{_bindir}/unsign
%{__install} -Dp -m0644 man/sign.1 %{buildroot}%{_mandir}/man1/sign.1
%{__install} -Dp -m0644 man/sign.1 %{buildroot}%{_mandir}/man1/unsign.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Updated to release 1.0.7.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Updated to release 1.0.5.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Updated to release 1.0.3.

* Wed May 05 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.2
- Initial package.
