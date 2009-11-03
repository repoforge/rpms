# $Id$
# Authority: dag

%define real_name libshout

Summary: Library for communicating with and sending data to an icecast server
Name: libshout109
Version: 1.0.9
Release: 3.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://developer.icecast.org/libshout/

Source: http://developer.icecast.org/libshout/releases/libshout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libshout <= %{version}
Provides: libshout = %{version}-%{release}

%description
Libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.


%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
test -d %{buildroot}/usr/doc && rm -rf %{buildroot}/usr/doc

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES COPYING README
%{_libdir}/*.so.*
%exclude %{_includedir}/*
%exclude %{_libdir}/*.a
%exclude %exclude %{_libdir}/*.la
%exclude %{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.9-3.2
- Rebuild for Fedora Core 5.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 1.0.9-1
- Forked to libshout109.

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

