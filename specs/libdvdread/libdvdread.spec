# $Id$
# Authority: matthias

# Define when building a CVS shapshot
%define	cvs	-cvs

Summary: Library for reading DVD video disks
Name: libdvdread
Version: 0.9.4
Release: 8%{?cvs:cvs}
License: GPL
Group: System Environment/Libraries
URL: http://www.dtek.chalmers.se/groups/dvd/
Source: http://www.dtek.chalmers.se/groups/dvd/dist/libdvdread-%{version}%{?cvs}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libdvdcss >= 1.2.5
# The old libtool included b0rkes the build on an x86_64 FC3 mach root
BuildRequires: libtool, autoconf, automake, gcc-c++

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
autoreconf --force --install --symlink

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
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


