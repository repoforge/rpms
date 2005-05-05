# $Id$
# Authority: matthias

Summary: Fast Assembly MPEG Encoding library
Name: libfame
Version: 0.9.1
Release: 6
License: LGPL
Group: System Environment/Libraries
URL: http://fame.sourceforge.net/
Source: http://dl.sf.net/fame/%{name}-%{version}.tar.gz
Patch0: libfame-0.9.1-fstrict-aliasing.patch
Patch1: http://www.linuxfromscratch.org/blfs/downloads/svn/libfame-0.9.1-gcc34-1.patch
Patch2: libfame-0.9.1-underquoted.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.


%package devel
Summary: Development files and static libraries for libfame
Group: Development/Libraries
Requires: %{name} = %{version}
BuildRequires: autoconf, automake, libtool

%description devel
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.

This package contains the files necessary to build programs that use the
libfame library.


%prep
%setup
%patch0 -p1 -b .fstrict-aliasing
%patch1 -p1 -b .mmxone
%patch2 -p1 -b .m4
./autogen.sh

# Fix lib stuff for lib64
%{__perl} -pi.orig -e 's|/lib"|/%{_lib}"|g' configure.in


%build
# Compile a special MMX & SSE enabled lib first
%ifarch %{ix86}
    %configure --enable-sse --enable-mmx
    %{__make} %{?_smp_mflags}
    %{__mkdir} sse2/
    %{__mv} src/.libs/libfame*.so.* sse2/
    %{__make} clean
%endif

# Now, the normal build
%configure --disable-mmx
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install the MMX & SSE build in its special dir
%ifarch %{ix86}
    %{__mkdir_p} %{buildroot}%{_libdir}/sse2
    %{__cp} -ap sse2/* %{buildroot}%{_libdir}/sse2/
%endif

# Workaround for direct <libfame/fame.h> includes (include/libfame -> .)
%{__ln_s} . %{buildroot}%{_includedir}/%{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING README TODO 
%{_libdir}/*.so.*
%ifarch %{ix86}
    %{_libdir}/sse2/*.so.*
%endif

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/%{name}-config
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man3/*


%changelog
* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 0.9.1-6
- Run plain "./autogen.sh" instead of autoreconf to avoid libm problem on
  x86_64 (weird one!).
- Actually really apply the last patch too...

* Sun May  1 2005 Matthias Saou <http://freshrpms.net/> 0.9.1-5
- Patch the m4 file to fix underquoted warning.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-4
- Add libfame-0.9.1-gcc34-1.patch to fix "undefined symbol: _mmx_one".

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-3
- Add libfame-0.9.1-fstrict-aliasing.patch to actually make the lib work,
  thanks to Nicholas Miell.

* Tue Aug 31 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-2
- Add specially compiled MMX & SSE lib on x86.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-1
- Update to 0.9.1.
- Updated the Source URL.

* Fri Dec  5 2003 Matthias Saou <http://freshrpms.net/> 0.9.0-4
- Added /usr/include/libfame -> . symlink as a workaround for MPlayer.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.9.0-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- release 2

* Mon Jun 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adapted from PLD spec file for GStreamer packaging

