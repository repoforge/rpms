# $Id$
# Authority: matthias

%{?dist: %{expand: %%define %dist 1}}

Summary: Library for communicating with and sending data to an icecast server
Name: libshout
Version: 2.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.icecast.org/
Source: http://www.icecast.org/files/libshout/libshout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libvorbis-devel, pkgconfig

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents bad data from getting to the icecast server.


%package devel
Summary: Development files for the libshout icecast library
Group: Development/Libraries
Requires: %{name} = %{version}, libvorbis-devel, pkgconfig

%description devel
This package contains the header files needed for developing applications
that send data to an icecast server.  Install libshout-devel if you want to
develop applications using libshout.


%prep
%setup


%build
%configure %{?rh9:--disable-thread}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Remove those docs, we include the same nicely
test -d %{buildroot}%{_datadir}/doc && %{__rm} -rf %{buildroot}%{_datadir}/doc


%clean 
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc COPYING README examples/example.c
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4


%changelog
* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 2.0-1
- Rebuild for Fedora Core 2.
- Update to 2.0, major spec changes to match.

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 1.0.9-3
- Rebuild for Fedora Core 1.

* Thu Aug 28 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Excluded .la file.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Wed Sep 18 2002 Thomas Vander Stichele <thomas@apestaart.org>
- Adopted for GStreamer and cleaned up
- removed examples from devel
- added .so and .a to devel
- removed autogen

* Tue Mar 21 2000 Jeremy Katz <katzj@icecast.org>
- split into libshout and libshout-devel packages

* Tue Mar 21 2000 Jack Moffitt <jack@icecast.org>
- new version

* Wed Mar 15 2000 Jack Moffitt <jack@icecast.org>
- More files to get installed

* Wed Mar 15 2000 Jeremy Katz <katzj@icecast.org>
- Clean up the spec file a tad
- Do an ldconfig after installing the lib

* Tue Mar 14 2000 Jack Moffitt <jack@icecast.org>
- First official rpm build, using 1.0.0

