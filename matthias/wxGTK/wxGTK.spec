%define x11libdir %{_prefix}/X11R6/%{_lib}

Name:           wxGTK
Version:        2.6.2
Release:        0%{?dist}
Summary:        GTK2 port of the wxWidgets GUI library
# The wxWindows licence is the LGPL with a specific exemption allowing
# distribution of derived binaries under any terms. (This will eventually
# change to be "wxWidgets License" once that is approved by OSI.)
License:        wxWidgets Library Licence
Group:          System Environment/Libraries
URL:            http://www.wxwidgets.org/
Source0:        http://dl.sf.net/wxwindows/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel, zlib-devel >= 1.1.4
BuildRequires:  libpng-devel, libjpeg-devel, libtiff-devel
BuildRequires:  expat-devel, SDL-devel, libgnomeprintui22-devel
BuildRequires:  xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU
#BuildRequires:  mesa-libGL-devel, mesa-libGLU-devel

# all of these are for previous Fedora Extras sub-packages
Obsoletes:      wxGTK2 < %{version}-%{release}
Provides:       wxGTK2 = %{version}-%{release}
Obsoletes:      wxGTK-common < %{version}-%{release}
Provides:       wxGTK-common = %{version}-%{release}
Obsoletes:      wxGTK2-xrc < %{version}-%{release}
Obsoletes:      wxGTK-xrc < %{version}-%{release}
Provides:       wxGTK2-xrc = %{version}-%{release}
Provides:       wxGTK-xrc = %{version}-%{release}
Obsoletes:      wxGTK2-stc < %{version}-%{release}
Obsoletes:      wxGTK-stc < %{version}-%{release}
Provides:       wxGTK2-stc = %{version}-%{release}
Provides:       wxGTK-stc = %{version}-%{release}

%description
wxWidgets/GTK2 is the GTK2 port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        devel
Group:          Development/Libraries
Summary:        Development files for the wxGTK2 library
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-gl = %{version}-%{release}
Requires:       gtk2-devel
Obsoletes:      wxGTK2-devel < %{version}-%{release}
Provides:       wxGTK2-devel = %{version}-%{release}
Obsoletes:      wxGTK-common-devel < %{version}-%{release}
Provides:       wxGTK-common-devel = %{version}-%{release}

%description devel
This package include files needed to link with the wxGTK2 library.


%package        gl
Summary:        OpenGL add-on for the wxWidgets library
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}
Obsoletes:      wxGTK2-gl < %{version}-%{release}
Provides:       wxGTK2-gl = %{version}-%{release}

%description gl
OpenGL add-on for the wxWidgets library.


%prep
%setup
sed -i -e 's|/usr/lib\b|%{_libdir}|' wx-config.in configure


%build
# --disable-optimise prevents our $RPM_OPT_FLAGS being overridden
# (see OPTIMISE in configure).
export GDK_USE_XFT=1
%configure \
    --x-libraries=%{x11libdir} \
    --with-gtk=2 \
    --with-opengl \
    --with-sdl \
    --with-gnomeprint \
    --enable-shared \
    --enable-soname \
    --disable-optimise \
    --enable-debug_info \
    --enable-unicode \
    --enable-compat22
make %{?_smp_mflags}
make %{?_smp_mflags} -C contrib/src/stc
make %{?_smp_mflags} -C contrib/src/ogl
make %{?_smp_mflags} -C contrib/src/gizmos
make %{?_smp_mflags} -C contrib/src/animate


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%makeinstall -C contrib/src/stc
%makeinstall -C contrib/src/ogl
%makeinstall -C contrib/src/gizmos
%makeinstall -C contrib/src/animate

# this ends up being a symlink into the buildroot directly --
# not what we want!
rm $RPM_BUILD_ROOT%{_bindir}/wx-config
ln -s %{_libdir}/wx/config/gtk2-unicode-release-2.6 $RPM_BUILD_ROOT%{_bindir}/wx-config

%find_lang wxstd
%find_lang wxmsw
cat wxmsw.lang >> wxstd.lang


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post gl -p /sbin/ldconfig
%postun gl -p /sbin/ldconfig


%files -f wxstd.lang
%defattr(-,root,root,-)
%doc CHANGES*.txt COPYING.LIB LICENCE.txt README*.txt
%{_libdir}/libwx_baseu-*.so.*
%{_libdir}/libwx_baseu_net-*.so.*
%{_libdir}/libwx_baseu_xml-*.so.*
%{_libdir}/libwx_gtk2u_adv-*.so.*
%{_libdir}/libwx_gtk2u_animate-*.so.*
%{_libdir}/libwx_gtk2u_core-*.so.*
%{_libdir}/libwx_gtk2u_gizmos-*.so.*
%{_libdir}/libwx_gtk2u_gizmos_xrc*.so.*
%{_libdir}/libwx_gtk2u_html-*.so.*
%{_libdir}/libwx_gtk2u_media-*.so.*
%{_libdir}/libwx_gtk2u_ogl-*.so.*
%{_libdir}/libwx_gtk2u_xrc-*.so.*
%{_libdir}/libwx_gtk2u_stc-*.so.*
%{_libdir}/libwx_gtk2u_qa-*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/wx-config
%{_bindir}/wxrc*
%{_includedir}/wx-2.6
%{_libdir}/libwx_*.so
%dir %{_libdir}/wx/
%dir %{_libdir}/wx/include/
%{_libdir}/wx/include/gtk2*
%dir %{_libdir}/wx/config/
%{_libdir}/wx/config/gtk2*
%{_datadir}/aclocal/*
%{_datadir}/bakefile/presets/

%files gl
%defattr(-,root,root,-)
%{_libdir}/libwx_gtk2u_gl-*.so.*


%changelog
* Tue Oct 04 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.6.2-0.1
- Update to 2.6.2.
- Include the sample wx bakefiles.
- Include new .mo files.
- From Paul Johnson:
  Change license to wxWidgets due to concerns over trademark infringement.
  Add dist tag.
- From Tom Callaway: Build and include libwx_gtk2u_animate-2.6.

* Thu Jul 14 2005 Matthew Miller <mattdm@mattdm.org> - 2.6.1-0.1
- update to 2.6.1
- from Michael Schwendt in 2.4.2-11 package: build-require
  xorg-x11-Mesa-libGL and xorg-x11-Mesa-libGLU (the libGL and libGLU
  deps aren't provided in FC3, so not using that).
- from Thorsten Leemhuis in 2.4.2-12 package: sed -i -e
  's|/usr/lib\b|%%{_libdir}|' in configure also to fix x86_64
- properly include older 2.4.x changelog

* Wed Apr 27 2005 Matthew Miller <mattdm@mattdm.org> - 2.6.0-0.1
- include libwx_gtk2u_gizmos_xrc in file listing

* Wed Apr 27 2005 Matthew Miller <mattdm@mattdm.org> - 2.6.0-0.0
- update to 2.6.0 final release
- configure now wants "--with-gtk=2" instead of "--enable-gtk2".

* Wed Apr 13 2005 Matthew Miller <mattdm@mattdm.org> - 2.5.5-0.2
- removed provides: wxWidgets/wxWidgets devel -- handy for compatibility
  with unmodified generic source packages, but not so good for
  repeatable builds.

* Wed Apr 13 2005 Matthew Miller <mattdm@mattdm.org> - 2.5.5-0.1
- whoops -- forgot to remove a reference to the "common" package
- version-release for obsoletes/provides

* Tue Apr 12 2005 Matthew Miller <mattdm@mattdm.org> - 2.5.5-0
- remove BU-specific oddities for fedora an idea for a simplied future....

* Tue Apr 12 2005 Matthew Miller <mattdm@bu.edu> - 2.5.5-bu45.2
- whoops -- forgot "Provides: wxGTK2-devel".

* Tue Apr 12 2005 Matthew Miller <mattdm@bu.edu> - 2.5.5-bu45.1
- update to 2.5.5

* Sat Mar  5 2005 Matthew Miller <mattdm@bu.edu> - 2.5.4-bu45.3
- Obsolete & provide GTK-xrc, wxGTK-stc, to provide clean upgrade path

* Tue Mar  1 2005 Matthew Miller <mattdm@bu.edu> - 2.5.4-bu45.2
- enable wxWindows 2.2 compatibility (for compatibility with 2.4 rpm,
  ironically).

* Tue Mar  1 2005 Matthew Miller <mattdm@bu.edu> - 2.5.4-bu45.1
- update to 2.5.4 -- the devel version is where all the fun is.
- rebase to updated FE 2.4.2 package
- license isn't "BSD" -- it's "wxWindows Library Licence".
- make gtk2-only -- gtk 1.0.x is no longer supported, and 1.2.x is
  being phased out. 2.x is the way to go.
- all current patches no longer necessary (upstream)
- roll "common" subpackage in to main package -- no longer makes sense
  to split it out with gtk+ gone
- use SDL, which will make this use Alsa for sound. I believe.
- add gnomeprint support
- add enable-debug_info for debuginfo package
- enable unicode
- use GDK_USE_XFT to enable Pango and fontconfig
- xrc moved from contrib to base -- making it no longer a subpackage
- making stc part of base too -- it's tiny, and doesn't introduce any
  additional deps
- leaving gl as a subpackage, though, since it's the only part that
  requires GL libs.
- add 'ogl' 2d drawing lib from contrib (needed for wxPython)
- add 'gizmos' from contrib (needed for wxPython)
- make wx-config actually part of the package, since there's no need
  to mess with moving it around
- the various afm fonts are gone in 2.5....
- use configure macro
- add provides for wxWidgets and wxWidgets-devel, because that
  seems like a good idea.

* Sun Jan 23 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.4.2-8
- Fix wx-config for x86_64 (#145508).
- Honor $RPM_OPT_FLAGS better, as well as %%{__cc} and %%{__cxx}.

* Mon Dec  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 2.4.2-7
- Patch to avoid aclocal >= 1.8 warnings from wxwin.m4.
- Move unversioned *.so links for -gl, -stc and -xrc to -devel, make -devel
  require them.

* Wed Nov 10 2004 Matthias Saou <http://freshrpms.net/> 2.4.2-6
- Bump release to provide Extras upgrade path.
- Fix spaces/tabs in spec.
- Remove unneeded zero epochs.
- Add full source URL.

* Tue Jun 22 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.2-0.fdr.2
- s/wxWindows/wxWidgets/
- Fix release tag.

* Sat May 22 2004 Noa Resare <noa@resare.com> - 0:2.4.2-0.fdr.1.3
- Merged fix from wxGTK cvs head, now works with recent gtk2

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.2-0.fdr.1
- Update to 2.4.2.

* Mon Aug  4 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.1-0.fdr.4
- Borrow Matthias Saou's -gl and -stc subpackages.

* Mon Jun 16 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.3
- Removed libwx_gtk2_xrc*so* from wxGTK2/wxGTK2-devel packages

* Sun Jun 15 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.2
- Removed *-devel postun scriptlets (from Ville Skyttä)

* Sat Jun 14 2003 Dams <anvil[AT]livna.org> 0:2.4.1-0.fdr.1
- Updated to 2.4.1

* Wed May 28 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.7
- Added xrc contrib in separate packages

* Wed May 21 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.6
- Corrected typo in postun devel

* Wed May 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.0-0.fdr.5
- Make -devel packages require the corresponding GTK devel package.
- Save .spec in UTF-8.
- Fixes from Dams:
- Don't build --with-unicode, it breaks stuff (as was already noted by Dams).
- Don't remove wx-config symlinks on upgrades.
- Remove duplicates from docs.

* Tue May 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.4.0-0.fdr.4
- Split into subpackages, spec file rewrite.
- Use bzipped upstream tarball.
- Clean up BuildRequirement versions.

* Fri May  9 2003 Dams <anvil[AT]livna.org> 0:2.4.0-0.fdr.3
- Now build/include both gtk/gtk2 libs
- buildroot -> RPM_BUILD_ROOT

* Mon Mar  3 2003 Dams <anvil@livna.org>
- Initial build.
- Disable unicode as it breaks lmule
- use the %find_lang macro for locale
