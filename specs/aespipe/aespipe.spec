# $Id$
# Authority: dag

Summary: AES-based encryption tool for tar/cpio and loop-aes images
Name: aespipe
Version: 2.3d
Release: 1
License: GPL
Group: Applications/System
URL: http://loop-aes.sourceforge.net/

Source: http://loop-aes.sourceforge.net/aespipe/aespipe-v%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
aespipe is an encryption tool that reads from standard input and
writes to standard output. It uses the AES (Rijndael) cipher.

It can be used as an encryption filter, to create and restore
encrypted tar/cpio backup archives and to read/write and convert
loop-AES compatible encrypted images.

aespipe can be used for non-destructive in-place encryption of
existing disk partitions for use with the loop-AES encrypted loopback
kernel module.

%prep
%setup -n %{name}-v%{version}

%build
%{__aclocal}
%{__autoconf}
%configure
%ifarch x86_64
%{__make} amd64
%endif
%ifarch %{ix86}
%{__make} x86
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 aespipe %{buildroot}%{_bindir}/aespipe
%{__install} -Dp -m0755 bz2aespipe %{buildroot}%{_bindir}/bz2aespipe
%{__install} -Dp -m0444 aespipe.1 %{buildroot}%{_mandir}/man1/aespipe.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man1/*
%{_bindir}/aespipe
%{_bindir}/bz2aespipe

%changelog
* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 2.3d-1
- Initial package. (using DAR)
