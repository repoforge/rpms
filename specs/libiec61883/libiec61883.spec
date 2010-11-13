# $Id$
# Authority: matthias

### EL6 ships with libiec61883-1.2.0-4.el6
### EL5 ships with libiec61883-1.0.0-11.fc6
# ExclusiveDist: el2 rh7 rh9 el3 el4

Summary: Streaming library for IEEE1394
Name: libiec61883
Version: 1.0.0
Release: 0%{?dist}
License: LGPL
URL: http://linux1394.org/
Group: System Environment/Libraries
Source: http://www.linux1394.org/dl/libiec61883-%{version}.tar.gz
Patch0: libiec61883-1.0.0-installtests.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Works only with newer libraw1394 versions
Requires: libraw1394 >= 1.2.0
BuildRequires: libraw1394-devel >= 1.2.0
BuildRequires: autoconf, automake, libtool

%description
The libiec61883 library provides an higher level API for streaming DV,
MPEG-2 and audio over IEEE1394.  Based on the libraw1394 isochronous
functionality, this library acts as a filter that accepts DV-frames,
MPEG-2 frames or audio samples from the application and breaks these
down to isochronous packets, which are transmitted using libraw1394.


%package devel
Summary: Development files for libiec61883
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, libraw1394-devel >= 1.2.0

%description devel
Development files needed to build applications against libiec61883.


%package utils
Summary: Utilities for use with libiec61883
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description utils
Utilities that make use of iec61883.


%prep
%setup
%patch0 -p1 -b .installtests


%build
autoreconf
%configure
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libiec61883.so.*

%files devel
%defattr(-,root,root,0755)
%exclude %{_libdir}/libiec61883.a
%exclude %{_libdir}/libiec61883.la
%{_libdir}/libiec61883.so
%{_includedir}/libiec61883/
%{_libdir}/pkgconfig/libiec61883.pc

%files utils
%defattr(-,root,root,0755)
%{_bindir}/*


%changelog
* Sat Dec 10 2005 Matthias Saou <http://freshrpms.net/> 1.0.0-0
- Spec file cleanup.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Warren Togami <wtogami@redhat.com> 1.0.0-9
- incorporate some spec improvements from Matthias (#172105)

* Mon Sep 19 2005 Warren Togami <wtogami@redhat.com> 1.0.0-8
- split -devel for pkgconfig chain
- remove .a and .la
- exclude s390 and s390x

* Tue Apr  5 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fixes for building properly on x86_64.

* Mon Mar 28 2005 Jarod Wilson <jarod@wilsonet.com>
- Fixed utils so they build properly

* Sat Feb 26 2005 Jarod Wilson <jarod@wilsonet.com>
- Rolled in utils

* Wed Feb 23 2005 Jarod Wilson <jarod@wilsonet.com>
- Initial build

