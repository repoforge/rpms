# $Id: libshout.spec,v 1.1 2004/02/26 17:54:30 thias Exp $

Summary: Library for communicating with and sending data to an icecast server
Name: libshout
Version: 1.0.9
Release: 3.fr
License: LGPL
Group: System Environment/Libraries
URL: http://developer.icecast.org/libshout/
Source: http://developer.icecast.org/libshout/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.


%package devel
Summary: Development files for the libshout icecast library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files needed for developing applications
that send data to an icecast server.  Install libshout-devel if you want to
develop applications using libshout.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
test -d %{buildroot}/usr/doc && rm -rf %{buildroot}/usr/doc

%clean 
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS CHANGES COPYING README
%{_libdir}/*.so.*

%files devel
%doc doc/*.html doc/*.css
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 1.0.9-3.fr
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

