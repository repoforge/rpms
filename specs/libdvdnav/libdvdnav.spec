# $Id$
# Authority: matthias
# Upstream: <dvd-devel$lists,sourceforge,net>

Summary: DVD menu navigation library
Name: libdvdnav
Version: 0.1.10
Release: 3%{?dist}
Group: System Environment/Libraries
License: GPL
URL: http://dvd.sourceforge.net/
Source: http://dl.sf.net/dvd/libdvdnav-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: doxygen, m4, gcc-c++

%description
The libdvdnav library provides support to applications wishing to make use
of advanced DVD features.


%package devel
Summary: Development files for the libdvdnav DVD menu navigation library
Group: Development/Libraries
Requires: %{name} = %{version}, libdvdread-devel

%description devel
The libdvdnav library provides support to applications wishing to make use
of advanced DVD features.

This package contains the libraries and header files needed to develop
applications which will use libdvdnav.


%prep
%setup


%build
%configure \
    --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, 0755)
%{_bindir}/dvdnav-config
%{_includedir}/dvdnav/
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/dvdnav.m4


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.1.10-3
- Release bump to drop the disttag number in FC5 build.

* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 0.1.10-2
- Added missing /sbin/ldconfig calls.

* Thu Jul 08 2004 Dag Wieers <dag@wieers.com> - 0.1.10-1
- Added --program-prefix to %%configure.
- Updated to release 0.1.10.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.1.9-3
- Rebuild for Fedora Core 2.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.9-2
- Rebuild for Fedora Core 1.

* Mon Aug  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.9.
- Removed libdvdread dependency.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Rebuild against new libdvdread.

* Sun Jan 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to latest CVS since xine 1beta2 needs version 0.1.4.

* Wed Oct 23 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Split devel package.

* Mon Aug 20 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Sun Mar 18 2002 Daniel Caujolle-Bert <f1rmb@users.sourceforge.net>
- Add missing files. Fix rpm generation.

* Tue Mar 12 2002 Rich Wareham <richwareham@users.sourceforge.net>
- Canabalisation to form libdvdnav spec file.

* Sun Sep 09 2001 Thomas Vander Stichele <thomas@apestaart.org>
- first spec file

