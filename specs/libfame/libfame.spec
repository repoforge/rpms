# $Id$
# Authority: matthias

Summary: Fast Assembly MPEG Encoding library
Name: libfame
Version: 0.9.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://fame.sourceforge.net/
Source: http://dl.sf.net/fame/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libtool

%description
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.


%package devel
Summary: Development files and static libraries for libfame
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.

This package contains the files necessary to build programs that use the
libfame library.


%prep
%setup


%build
%{__libtoolize} --force
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Workaround for direct <libfame/fame.h> includes.
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

