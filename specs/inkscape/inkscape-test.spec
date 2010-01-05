# $Id$
# Authority: dag
# Upstream: <inkscape-devel$lists,sf,net>

# Tag: test

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Vector drawing application
Name: inkscape
Version: 0.47
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://inkscape.sourceforge.net/

Source: http://dl.sf.net/inkscape/inkscape-%{version}.tar.gz
Patch0: inkscape-20090410svn-uniconv.patch
# Patch1: inkscape-20090410svn-formats.patch
Patch1: inkscape-20091229ay-el5.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cairomm-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnome-vfs2-devel >= 2.0
BuildRequires: gsl
BuildRequires: gsl-devel
BuildRequires: gtk2-devel >= 2.8
BuildRequires: gtkmm2
BuildRequires: gtkmm24-devel
BuildRequires: glibmm24-devel
BuildRequires: intltool
BuildRequires: lcms-devel >= 1.13
BuildRequires: libgc-devel
BuildRequires: libpng-devel
BuildRequires: libsigc++-devel
BuildRequires: libsigc++20-devel
BuildRequires: libwpg-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: loudmouth-devel >= 1.0
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig
BuildRequires: poppler-devel
BuildRequires: python-devel
BuildRequires: zlib-devel
#%{?_without_modxorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{?_without_modxorg:BuildRequires: XFree86-devel, xorg-x11-Mesa-libGLU}
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel}
Requires: gsl
Requires: perl(Image::Magick)
Requires: pstoedit

%description
Inkscape is an SVG based generic vector-drawing program.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure \
    --enable-inkboard \
    --enable-lcms \
    --enable-poppler-cairo \
    --enable-static="no" \
    --with-gnome-vfs \
    --with-inkjar \
    --with-perl \
    --with-python \
    --with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* HACKING*txt NEWS README TRANSLATORS
%doc %{_mandir}/man1/inkscape.1*
%doc %{_mandir}/man1/inkview.1*
%doc %{_mandir}/*/man1/inkscape.1*
#%doc %{_mandir}/*/man1/inkview.1*
%{_bindir}/inkscape
%{_bindir}/inkview
%{_datadir}/applications/inkscape.desktop
%{_datadir}/inkscape/
%{_datadir}/pixmaps/inkscape.png

%changelog
* Tue Dec 29 2009 Akemi Yagi <amyagi@gmail.com> - 0.47-1
- Updated to release 0.47.
- Applied el5 patch.

* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Sun Jul 29 2007 Dag Wieers <dag@wieers.com> - 0.45-2
- Rebuild against libgc-7.0.

* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.45-1
- Updated to release 0.45.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.44.1-1
- Updated to release 0.44.1.

* Sat Jun 24 2006 Dag Wieers <dag@wieers.com> - 0.44-1
- Updated to release 0.44.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Mon Dec 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-2
- Fixes by Brent Terp.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Updated to release 0.42.

* Thu Feb 10 2005 Dag Wieers <dag@wieers.com> - 0.41-1
- Updated to release 0.41.

* Tue Nov 30 2004 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.39-1
- Updated to release 0.39.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.38.1-1
- Updated to release 0.38.1.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.37-0
- Updated to release 0.37.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 0.36-0
- Updated to release 0.36.

* Thu May 01 2003 Christian Schaller <uraeus@gnome.org>
- Fix up the spec file for current release.

* Mon Sep 23 2002 Dag Wieers <dag@wieers.com> - 0.2.6-1
- Updated to release 0.2.6.

* Thu Sep 12 2002 Dag Wieers <dag@wieers.com> - 0.2.5-1
- Updated to release 0.2.5.
- Changed SPEC to benefit from macros.
