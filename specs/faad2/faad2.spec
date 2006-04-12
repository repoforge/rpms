# $Id$
# Authority: matthias

%define xmmsinputdir %(xmms-config --input-plugin-dir 2>/dev/null || echo %{_libdir}/xmms/Input)
#define prever       rc3
#define date         20040923

Summary: Library and frontend for decoding MPEG2/4 AAC
Name: faad2
Version: 2.0
Release: 8%{?prever:.%{prever}}%{?date:.%{date}}
License: GPL
Group: Applications/Multimedia
URL: http://www.audiocoding.com/
%if %{?date:1}0
#Source: http://www.audiocoding.com/snapshot/faad2-%{date}.tar.bz2
Source: http://download.videolan.org/pub/videolan/vlc/0.8.1/contrib/faad2-%{date}.tar.bz2
%else
Source: http://dl.sf.net/faac/%{name}-%{version}%{?prever:-%{prever}}.tar.gz
%endif
Patch0: faad2-2.0-Makefile-separator.patch
Patch1: faad2-2.0-gcc34.patch
Patch2: faad2-2.0-xmms-noext.patch
Patch3: faad2-2.0-gcc4.patch
Patch4: faad2-2.0-configure-mpeg4ip.patch
Patch5: faad2-2.0-64bit.patch
Patch6: faad2-2.0-symbol.patch
Patch7: faad2-2.0-mp4ff_int_types.patch
Patch8: faad2-2.0-systypes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, automake, libtool
BuildRequires: gcc-c++, zlib-devel, libsndfile-devel >= 1.0.0
BuildRequires: xmms-devel, id3lib-devel, gtk+-devel

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.


%package -n xmms-aac
Summary: X MultiMedia System input plugin to play AAC files
Group: Applications/Multimedia
Requires: %{name} = %{version}
Provides: xmms-%{name} = %{version}-%{release}

%description -n xmms-aac
This xmms plugin reads AAC files with and without ID3 tags (version 2.x).
AAC files are MPEG2 or MPEG4 files that can be found in MPEG4 audio files
(.mp4). MPEG4 files with AAC inside can be read by RealPlayer or Quicktime.


%package devel
Summary: Development libraries of the FAAD 2 AAC decoder
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains development files and documentation for libfaad.


%prep
%if %{?date:1}0
%setup -n %{name}-%{date}
%else
%setup -n %{name}
%endif
%patch0 -p1 -b .makefilesep
%patch1 -p1 -b .gcc34
%patch2 -p1 -b .noext
%patch3 -p1 -b .gcc4
%patch4 -p0 -b .mpeg4ip
%patch5 -p1 -b .64bit
%patch6 -p1 -b .symbol
%patch7 -p1 -b .mp4ff_int_types
%patch8 -p1 -b .systypes


%build
test -x configure || sh bootstrap
%configure \
    --disable-static \
    --with-xmms \
    --with-mpeg4ip \
    --with-drm \
    --with-mp4v2
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# Remove this wrong include
%{__perl} -pi -e 's|#include <systems.h>||g' \
    %{buildroot}%{_includedir}/mpeg4ip.h


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files -n xmms-aac
%defattr(-, root, root, 0755)
%doc plugins/xmms/AUTHORS plugins/xmms/NEWS
%doc plugins/xmms/README plugins/xmms/TODO
#exclude %{xmmsinputdir}/*.a
%exclude %{xmmsinputdir}/*.la
%{xmmsinputdir}/*.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
#{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
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

