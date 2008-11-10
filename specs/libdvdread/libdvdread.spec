# $Id$
# Authority: matthias

Summary: Library for reading DVD video disks
Name: libdvdread
Version: 0.9.7
Release: 1%{?cvs:cvs}
License: GPL
Group: System Environment/Libraries
URL: http://www.dtek.chalmers.se/groups/dvd/

Source: http://www.dtek.chalmers.se/groups/dvd/dist/libdvdread-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
Requires: libdvdcss >= 1.2.5

%description
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.
It parses IFO files, reads NAV-blocks, and performs CSS authentication
and descrambling.

%package devel
Summary: Development files from the libdvdread library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.
It parses IFO files, reads NAV-blocks, and performs CSS authentication
and descrambling.

You will need to install these development files if you intend to rebuild
programs that use this library.

%prep
%setup -n %{name}-%{version}%{?cvs}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/libdvdread.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/dvdread/
%{_libdir}/libdvdread.so
%exclude %{_libdir}/libdvdread.la

%changelog
* Fri Oct  6 2006 Matthias Saou <http://freshrpms.net/> 0.9.7-1
- Update to 0.9.7.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.9.5-2
- Disable/remove static library, nothing seems to use it.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 0.9.5-1
- Update to 0.9.5.
- Remove no longer needed "autoreconf --force --install --symlink" call.

* Mon Sep 19 2005 Matthias Saou <http://freshrpms.net/> 0.9.4-8cvs
- Update to 0.9.4-cvs pre-release.
- Remove udffindfile patch, projects shouldn't need it.

* Tue Apr 19 2005 Dries Verachtert <dries@ulyssis.org> 0.9.4-7
- Added a patch provided by Ralf Ertzinger so certain symbols
  are exported again.

* Fri Feb  4 2005 Matthias Saou <http://freshrpms.net/> 0.9.4-6
- Force libtoolize/auto* to fix x86_64 build, thanks to Nicholas Miell.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.9.4-5
- Rebuild for Fedora Core 2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.4-4
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Updated to the latest cvs release.
- Rebuilt for Red Hat Linux 8.0.
- Updated URLs.

* Mon May 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.

* Wed May 15 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the libdvdcss.so.0/1/2 problem again.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Back to using libdvdcss 1.1.1, now it's all merged and fine.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Sat Jan 12 2002 Matthias Saou <http://freshrpms.net/>
- Reverted back to using libdvdcss 0.0.3.ogle3 since it works MUCH better
  than 1.0.x. Doh!

* Tue Nov 13 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt against libdvdcss 1.0.0 (added a patch).

* Mon Oct 29 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Thu Oct 11 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated to version 0.9.2

* Tue Sep 25 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Added small patch to fix the ldopen of libdvdcss

* Tue Sep 18 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated to version 0.9.1

* Fri Sep 14 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Split into normal and devel package

* Thu Sep 6 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- Updated to version 0.9.0

* Tue Jul 03 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- initial version


