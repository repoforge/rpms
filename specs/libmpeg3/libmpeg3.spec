# $Id$

# Authority: dag

Summary: LibMPEG3 decodes the many many derivatives of MPEG standards
Name: libmpeg3
Version: 1.5.2
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://heroinewarrior.com/libmpeg3.php3

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/heroines/%{name}-%{version}-src.tar.bz2
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

%{__perl} -pi.orig -e '
		s|^USE_MMX = 0|USE_MMX = 1|;
		s| /usr/bin$| \$(DESTDIR)\$(bindir)|;
	' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
		%{buildroot}%{_bindir} \
		%{buildroot}%{_includedir}
%{__install} -m0755 i686/mpeg3dump i686/mpeg3cat i686/mpeg3toc %{buildroot}%{_bindir}
%{__install} -m0755 i686/libmpeg3.a %{buildroot}%{_libdir}
%{__install} -m0644 libmpeg3.h mpeg3private.h mpeg3protos.h %{buildroot}%{_includedir}

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
* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.5.2-0
- Updated to release 1.5.2.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
