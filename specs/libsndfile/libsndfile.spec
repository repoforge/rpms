# $Id$
# Authority: matthias

### EL6 ships with libsndfile-1.0.20-3.el6
# ExclusiveDist: el2 el3 el4 el5

%{?fc1: %define _without_alsa 1}
%{?el3: %define _without_alsa 1}
%{?rh9: %define _without_alsa 1}
%{?rh8: %define _without_alsa 1}
%{?rh7: %define _without_alsa 1}
%{?el2: %define _without_alsa 1}
%{?yd3: %define _without_alsa 1}

Summary: Library for reading and writing files containing sampled sound
Name: libsndfile
Version: 1.0.17
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.mega-nerd.com/libsndfile/
Source: http://www.mega-nerd.com/libsndfile/libsndfile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_flac:BuildRequires: flac-devel}

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%package devel
Summary: Header files and development documentation for libsndfile
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

This package contains the header files, static libraries and development
documentation for libsndfile.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} _docs
%makeinstall htmldocdir="`pwd`/_docs"
# Clean up examples for inclusion in docs
%{__rm} -rf examples/{.deps,.libs/,*.o}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%doc _docs/* examples/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/octave/
%exclude %{_libdir}/*.la

%changelog
* Thu Aug 31 2006 Matthias Saou <http://freshrpms.net/> 1.0.17-1
- Update to 1.0.17.

* Tue May  2 2006 Matthias Saou <http://freshrpms.net/> 1.0.16-1
- Update to 1.0.16.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.15-1
- Update to 1.0.15.

* Wed Feb 22 2006 Matthias Saou <http://freshrpms.net/> 1.0.14-1
- Update to 1.0.14.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 1.0.13-1
- Update to 1.0.13.

* Fri Sep 30 2005 Matthias Saou <http://freshrpms.net/> 1.0.12-1
- Update to 1.0.12.
- Enabled new FLAC support (not sqlite3, though).

* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 1.0.11-2
- No longer exclude octave *.m files: Can't find the reason why they were,
  maybe in the PLD spec used as the starting point?

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.11-1
- Update to 1.0.11.
- Add alsa-lib-devel build dependency.

* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 1.0.10-2
- Remove .libs from the included examples.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net/> 1.0.10-1
- Update to 1.0.10.
- Added "examples" directory to the devel package.
- Added htmldocdir install workaround.

* Tue Mar 30 2004 Matthias Saou <http://freshrpms.net/> 1.0.9-1
- Update to 1.0.9.

* Mon Mar 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.8-1
- Update to 1.0.8.

* Wed Feb 25 2004 Matthias Saou <http://freshrpms.net/> 1.0.7-1
- Update to 1.0.7.
- Updated the URL and Source tags.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-1
- Update to 1.0.6.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.5-2
- Rebuild for Fedora Core 1.

* Sun May  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Spec file adapted from the PLD one.
- Update to 1.0.4.

