# $Id$

Summary: DVD menu navigation library
Name: libdvdnav
Version: 0.1.9
Release: 3.fr
Group: System Environment/Libraries
License: GPL
URL: http://dvd.sourceforge.net/
Source: http://dl.sf.net/dvd/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: doxygen, m4

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
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/dvdnav-config
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/dvdnav

%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.9-2.fr
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

