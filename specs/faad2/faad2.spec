# $Id$
# Authority: matthias

%{?el4:%define _without_sysfs 1}
%{?fc3:%define _without_sysfs 1}
%{?fc2:%define _without_sysfs 1}
%{?fc1:%define _without_sysfs 1}
%{?el3:%define _without_sysfs 1}
%{?rh9:%define _without_sysfs 1}
%{?rh7:%define _without_sysfs 1}
%{?el2:%define _without_sysfs 1}

Summary: Library and frontend for decoding MPEG2/4 AAC
Name: faad2
Version: 2.6.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.audiocoding.com/

Source: http://dl.sf.net/faac/faad2-%{version}.tar.gz
Patch0: faad2-2.5-buildfix.patch
Patch1: faad2-2.5-faacDec.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake, libtool
BuildRequires: gcc-c++, zlib-devel
%{!?_without_sysfs:BuildRequires: libsysfs-devel}

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
#patch0 -p1 -b .buildfix
#patch1 -p1 -b .faacDec

### Required to make automake < 1.7 work
%{__perl} -pi -e 's|dnl AC_PROG_CXX|AC_PROG_CXX|' configure.in

%build
# This is what the README.linux file recommends
autoreconf -vif
%configure --disable-static \
    --with-drm
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README* TODO
%{_bindir}/faad
%{_libdir}/libfaad.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/faad.h
%{_includedir}/neaacdec.h
%{_libdir}/libfaad.so
%exclude %{_libdir}/libfaad.la

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 2.6.1-1
- Updated to release 2.6.1.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 2.5-2
- Add patch to remove backwards compatibility in the header so that we can
  easily identify and patch all programs requiring a rebuild.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 2.5-1
- Update to 2.5.
- Completely remove xmms/bmp plugin, it's a real mess anyway. Use audacious.
- Rip out libmp4v2 too, it's best as a separate package.
- Add libsysfs-devel build requirement, as it seems configure checks for it.

* Wed Apr 12 2006 Matthias Saou <http://freshrpms.net/> 2.0-8
- Include patch to #include <sys/types.h> in mp4.h to fix building against
  the included libmp4v2 (faac, maybe others).

* Mon Apr 10 2006 Matthias Saou <http://freshrpms.net/> 2.0-7
- Remove explicit xmms requirement, since we really only require the libs.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 2.0-6
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  2 2006 Dries Verachtert <dries@ulyssis.org> 2.0-5
- Also install mp4ff_int_types.h because it is needed by mp4ff.h, thanks to
  Ramses Smeyers.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 2.0-4
- (Re-?)Add 64bit and symbol patches, thanks to Nicholas Miell.

* Wed Apr 20 2005 Matthias Saou <http://freshrpms.net/> 2.0-3
- Downgrade to 2.0 with gcc 3.4 and 4 patches from dev.gentoo.org, the libmp4v2
  is now internal again, no need for the external mpeg4ip mess... should fix
  many issues, like gtkpod AAC support.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net/> 2.0-2.20040923
- Use the snapshot from 20040923 that videolan provides.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 2.0-2.15092004
- Update to 15092004 snapshot to fix compilation on FC3.
- Disable static libs since they fail to be stripped :-( #88417.
- Remove merged makefile separator patch.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.0-2
- Rebuild for Fedora Core 2.

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 2.0-1
- Update to 2.0 final.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.5.rc3
- Added xmms-%{name} provides to the xmms-aac sub-package.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 2.0-0.4.rc3
- Added missing zlib-devel build dependency.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 2.0-0.3.rc3
- Update to 2.0-rc3.
- Remove systems.h include from mpeg4ip.h.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.0-0.2.rc1
- Rebuild for Fedora Core 1.

* Tue Aug 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0rc1.
- Introduced LD_LIBRARY_PATH workaround.
- Removed optional xmms plugin build, it seems mandatory now.
- Added gtk+ build dep for the xmms plugin.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Added xmms plugin build.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Now exclude .la file.
- Update to latest CVS checkout to fix compile problem.

* Fri Aug 10 2002 Alexander Kurpiers <a.kurpiers@nt.tu-darmstadt.de>
- changes to compile v1.1 release

* Tue Jun 18 2002 Alexander Kurpiers <a.kurpiers@nt.tu-darmstadt.de>
- First RPM.

