# $Id$
# Authority: dag
# Upstream: <broadcast$earthling,net>

Summary: Decoder of various derivatives of MPEG standards
Name: libmpeg3
Version: 1.5.4
Release: 3
License: GPL
Group: System Environment/Libraries
URL: http://heroinewarrior.com/libmpeg3.php3
Source: http://dl.sf.net/heroines/libmpeg3-%{version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: nasm

%description
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

libmpeg3 currently decodes:
 - MPEG-1 Layer II/III Audio and program streams
 - MPEG-2 Layer III Audio, program streams and transport streams
 - MPEG-1 and MPEG-2 Video
 - AC3 Audio
 - IFO files
 - VOB files

%prep
%setup

%build
# With gcc 3.4 (FC3), build fails with -O2 and also with -fPIC :-(
export CFLAGS="`echo "%{optflags}" | sed 's/-O./-O1/'`"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 */mpeg3dump */mpeg3cat */mpeg3toc \
    %{buildroot}%{_bindir}/

%{__install} -d -m0755 %{buildroot}%{_includedir}
%{__install} -m0644 libmpeg3.h mpeg3private.h mpeg3protos.h \
    %{buildroot}%{_includedir}

%{__install} -D -m0755 */libmpeg3.a %{buildroot}%{_libdir}/libmpeg3.a

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING docs/
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*.h

%changelog
* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 1.5.4-3
- Remove unneeded /usr/bin fix, since we don't use "make install".
- Replace -O? with -O1 in optflags since build fails with O2 and gcc 3.4.
- Make nasm mandatory : The configure script won't run without it anyway.

* Sat Jun 26 2004 Dag Wieers <dag@wieers.com> - 1.5.4-2
- Fixes for x86_64.

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 1.5.4-1
- Updated to release 1.5.4.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.5.2-0
- Updated to release 1.5.2.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
