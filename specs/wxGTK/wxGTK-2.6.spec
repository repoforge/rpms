# $Id: wxGTK.spec 3663 2005-10-20 04:38:29Z dries $
# Authority: dag

Summary: The GTK port of the wxWindows library
Name: wxGTK
Version: 2.6.4
Release: 1%{?dist}
License: wxWidgets Library Licence
Group: System Environment/Libraries
URL: http://www.wxwindows.org/

Source: http://dl.sf.net/wxwindows/wxGTK-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: GConf2-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: SDL-devel
BuildRequires: zlib-devel >= 1.1.4

# all packages providing an implementation of wxWindows library (regardless of
# the toolkit used) should provide the (virtual) wxwin package, this makes it
# possible to require wxwin instead of requiring "wxgtk or wxmotif or wxqt..."
Provides: wxwin
Obsoletes: wxBase <= %{version}-%{release}
Obsoletes: wxGTK-gl <= %{version}-%{release}
Obsoletes: wxGTK-stc <= %{version}-%{release}
Obsoletes: wxGTK-xrc <= %{version}-%{release}
Provides: wxBase = %{version}-%{release}
Provides: wxGTK-gl = %{version}-%{release}
Provides: wxGTK-stc = %{version}-%{release}
Provides: wxGTK-xrc = %{version}-%{release}

%description
wxWindows is a free C++ library for cross-platform GUI development.
With wxWindows, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-gl = %{version}-%{release}
Requires: gtk2-devel, pkgconfig
Requires: libpng-devel, libjpeg-devel, libtiff-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%description devel
Header files for wxGTK, the GTK port of the wxWindows library.

%prep
%setup
#%{__perl} -pi.orig -e 's| /usr/lib| %{_libdir} %{_prefix}/X11R6/%{_lib}|g' configure

%build
export GDK_USE_XFT="1"
%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --disable-optimise \
    --disable-rpath \
    --enable-compat24 \
    --enable-display \
    --enable-graphics_ctx \
    --enable-mediactrl \
    --enable-no_deps \
    --enable-shared \
    --enable-soname \
    --enable-sound \
    --enable-timer \
    --enable-unicode \
    --with-opengl \
    --with-sdl
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} -C contrib/src/gizmos
%{__make} %{?_smp_mflags} -C contrib/src/ogl
%{__make} %{?_smp_mflags} -C contrib/src/stc
%{__make} %{?_smp_mflags} -C contrib/src/svg

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} install DESTDIR="%{buildroot}" -C contrib/src/gizmos
%{__make} install DESTDIR="%{buildroot}" -C contrib/src/ogl
%{__make} install DESTDIR="%{buildroot}" -C contrib/src/stc
%{__make} install DESTDIR="%{buildroot}" -C contrib/src/svg
%find_lang wxstd
%find_lang wxmsw
%{__cat} wxstd.lang wxmsw.lang >>wx.lang

### Overwrite wrong symlink (includes buildroot)
%{__ln_s} -f ../%{_lib}/wx/config/gtk2-unicode-release-2.6 %{buildroot}%{_bindir}/wx-config

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f wx.lang
%defattr(-, root, root, 0755)
%doc COPYING.LIB *.txt
%{_libdir}/libwx_*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc COPYING.LIB *.txt
%{_bindir}/wx-config
%{_bindir}/wxrc
%{_bindir}/wxrc-2.6
%{_datadir}/aclocal/*.m4
%dir %{_datadir}/bakefile/
%dir %{_datadir}/bakefile/presets/
%{_datadir}/bakefile/presets/wx*.bkl
%{_includedir}/wx-2.6/
%{_libdir}/wx/
%{_libdir}/libwx_*.so

%changelog
* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 2.6.4-1
- Updated to release 2.6.4.

* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 2.6.3-1
- Updated to release 2.6.3.

* Sun Dec 18 2005 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Updated to release 2.6.2.

* Fri Nov 5  2004 Matthias Saou <http://freshrpms.net/> 2.4.2-5
- Moved .so symlinks to devel and require all other sub-libs.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 2.4.2-4
- Rebuilt for Fedora Core 2.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-3
- Revert back to gtk+, as gtk2 makes too many apps crash :-(

* Wed Nov 12 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-2
- Disable unicode as it breaks building for most applications (thanks to
  Fabrice Bellet).

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.4.2-1
- Rebuild for Fedora Core 1.
- Update to 2.4.2.
- Switch to gtk2 by default.

* Sun Jun 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.1.

* Thu May 29 2003 Matthias Saou <http://freshrpms.net/>
- Fixed dependencies by adding --enable-soname thanks to Fabrice Bellet.
- Added stc sub-package thanks to Jean-Michel POURE.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added xrc sub-package thanks to Bruno Postle.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.0

* Sun Aug  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt without the NVIDIA_GLX package to fix dependencies.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup.

