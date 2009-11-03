# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Typesafe Signal Framework for C++
Name: libsigc++
Version: 1.2.5
Release: 4%{?dist}
### Needs epoch as el2 comes with version 1:1.0.3 ;-(
%{?el2:Epoch: 1}
License: LGPL
Group: System Environment/Libraries
URL: http://libsigc.sourceforge.net/
Source: http://dl.sf.net/libsigc/libsigc++-%{version}.tar.gz
Patch: libsigc++-1.2.5-pc-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: libsigc++-examples <= %{version}
BuildRequires: gcc-c++, m4
BuildRequires: libtool, autoconf, automake

%description
This library implements a full callback system for use in widget libraries,
abstract interfaces, and general programming. Originally part of the Gtk--
widget set, libsigc++ is now a separate library to provide for more general
use. It is the most complete library of its kind with the ablity to connect
an abstract callback to a class method, function, or function object. It
contains adaptor classes for connection of dissimilar callbacks and has an
ease of use unmatched by other C++ callback libraries.

Package gtkmm2, which is a C++ binding to the GTK2 library, uses libsigc++.


%package devel
Summary: Development tools for the Typesafe Signal Framework for C++
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
The libsigc++-devel package contains the static libraries and header files
needed for development with libsigc++.


%prep
%setup
%patch -p1 -b .pc


%build
%{__aclocal} -I scripts
%{__libtoolize} -c -f
%{__autoconf}
%{__automake} -a -c -f
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Clean up the docs
find doc -name "Makefile*" | xargs rm -f


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FEATURES IDEAS NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/sigc++*


%changelog
* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 1.2.5-4
- Force libtoolize/autoconf/automake to build on x86_64.
- Add libsigc++-1.2.5-pc-cflags.patch patch from Fedora Extras to fix lib vs.
  lib64 issue from .pc file.

* Fri May 21 2004 Matthias Saou <http://freshrpms.net/> 1.2.5-3
- Rebuild for Fedora Core 2.

* Thu Nov 12 2003 Matthias Saou <http://freshrpms.net/> 1.2.5-2
- Rebuild for Fedora Core 1.

* Fri May 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.5.

* Sun Apr 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.4, and fork 1.0.4 as libsigc++10.

* Fri Apr  4 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Tue Oct  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4.
- Spec file cleanup.

* Mon Aug 06 2001 Havoc Pennington <hp@redhat.com>
- Obsolete libsigc++-examples, #50890

* Wed Jul 18 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- remove Package: line and fix spelling error

* Thu May 31 2001 Tim Powers <timp@redhat.com>
- moved examples into the devel package

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- updated to 1.0.3

* Wed Sep 13 2000 Tim Powers <timp@redhat.com>
- update to 1.0.1

* Wed Aug 9 2000 Tim Powers <timp@redhat.com>
- added Serial so that we can upgrade from the Helix packages

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- fixed bug #15056

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri May 12 2000 Tim Powers <timp@redhat.com>
- rebuilt for Powertools 7.0

* Sat Apr 15 2000 Dmitry V. Levin <ldv@fandra.org>
- updated Url and Source fileds
- 1.0.0 stable release

* Sat Jan 22 2000 Dmitry V. Levin <ldv@fandra.org>
- filtering out -fno-rtti and -fno-exceptions options from $RPM_OPT_FLAGS
- minor install section cleanup

* Wed Jan 19 2000 Allan Rae <rae@lyx.org>
- autogen just creates configure, not runs it, so cleaned that up too.

* Wed Jan 19 2000 Dmitry V. Levin <ldv@fandra.org>
- minor attr fix
- removed unnecessary curly braces
- fixed Herbert's adjustement

* Sat Jan 15 2000 Dmitry V. Levin <ldv@fandra.org>
- minor package dependence fix

* Sat Dec 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- fixed typo of mine
- added traditional CUSTOM_RELEASE stuff
- added SMP support

* Thu Dec 23 1999 Herbert Valerio Riedel <hvr@gnu.org>
- adjusted spec file to get tests.Makefile and examples.Makefile from scripts/

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- split into three packages: %name, %name-devel and %name-examples

* Thu Aug 12 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- updated source field and merged conflicts between revisions.

* Tue Aug 10 1999 Dmitry V. Levin <ldv@fandra.org>
- updated Prefix and BuildRoot fields

* Thu Aug  5 1999 Herbert Valerio Riedel <hvr@hvrlab.dhs.org>
- made sure configure works on all alphas

* Wed Jul  7 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Added autoconf macro for sigc.

* Fri Jun 11 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Made into a .in to keep version field up to date
- Still need to do release by hand

* Mon Jun  7 1999 Dmitry V. Levin <ldv@fandra.org>
- added Vendor and Packager fields

* Sat Jun  5 1999 Dmitry V. Levin <ldv@fandra.org>
- updated to 0.8.0

* Tue Jun  1 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
