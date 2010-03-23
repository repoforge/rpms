# $Id$
# Authority: matthias


Summary: Library for communicating with and sending data to an icecast server
Name: libshout
Version: 2.2.2
Release: 2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.icecast.org/

Source: http://svn.xiph.org/releases/libshout/libshout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvorbis-devel, pkgconfig
Requires: speex

%description
Libshout is a library for communicating with and sending data to an
icecast server. It handles the socket connection, the timing of the
data, and prevents bad data from getting to the icecast server.

%package devel
Summary: Development files for the libshout icecast library
Group: Development/Libraries
Requires: %{name} = %{version}, libvorbis-devel, speex-devel, pkgconfig

%description devel
This package contains the header files needed for developing applications
that send data to an icecast server.  Install libshout-devel if you want to
develop applications using libshout.

%prep
%setup

%build
%configure \
    --disable-static \
%{?rh9:--disable-thread}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
# Remove those docs, we include the same nicely
test -d %{buildroot}%{_datadir}/doc && %{__rm} -rf %{buildroot}%{_datadir}/doc

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL NEWS README examples/
%{_libdir}/libshout.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/shout.m4
%{_includedir}/shout/
%{_libdir}/pkgconfig/shout.pc
%{_libdir}/libshout.so
%exclude %{_libdir}/libshout.la

%changelog
* Tue Mar 23 2010 Steve Huff <shuff@vecna.org> - 2.2.2-2
- Captured missing speex dependency.

* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Wed Jan 04 2005 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

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

