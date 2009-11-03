# $Id$
# Authority: dries
# Screenshot: http://www.newbreedsoftware.com/tuxpaint/screenshots/example_simple-t.png
# ScreenshotURL: http://www.newbreedsoftware.com/tuxpaint/screenshots/

# ExcludeDist: el3

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Drawing program designed for young children
Name: tuxpaint
Version: 0.9.15
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.newbreedsoftware.com/tuxpaint/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source0: http://dl.sf.net/tuxpaint/tuxpaint-%{version}.tar.gz
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel, SDL-devel, SDL_ttf-devel
BuildRequires: SDL_image-devel, SDL_mixer-devel, gnome-libs-devel

%description
Tux Paint is a free drawing program designed for young children (kids ages 3
and up). It has a simple, easy-to-use interface, fun sound effects, and an
encouraging cartoon mascot who helps guide children as they use the program.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%{__make} %{?_smp_mflags} \
	PREFIX=%{_prefix} \
	GNOME_PREFIX=`gnome-config --prefix` \
	KDE_PREFIX=`kde-config --install apps --expandvars` \
	KDE_ICON_PREFIX=`kde-config --install icon --expandvars`

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall PREFIX=%{buildroot}%{_prefix} \
	GNOME_PREFIX=%{buildroot}`gnome-config --prefix` \
	KDE_PREFIX=%{buildroot}`kde-config --install apps --expandvars` \
	KDE_ICON_PREFIX=%{buildroot}`kde-config --install icon --expandvars`
%{__rm} -Rf `find %{buildroot} -type d | egrep 'CVS$'`
%{__mv} %{buildroot}%{_datadir}/doc/tuxpaint tuxpaintdocs
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc tuxpaintdocs/*
/usr/X11R6/include/X11/pixmaps/tuxpaint.xpm
%{_bindir}/tuxpaint
%{_bindir}/tuxpaint-import
%config(noreplace) /usr/etc/tuxpaint/tuxpaint.conf
%{_datadir}/applnk/Graphics/tuxpaint.desktop
%{_datadir}/gnome/apps/Graphics/tuxpaint.desktop
%{_datadir}/icons/*/*/apps/tuxpaint.png
%{_datadir}/icons/*/*/apps/tuxpaint.svg
%{_mandir}/man1/tuxpaint*
%{_mandir}/pl/man1/tuxpaint*
%{_datadir}/pixmaps/tuxpaint.png
%{_datadir}/tuxpaint

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.15-1
- Updated to release 0.9.15.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.14-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sun Oct 31 2004 Dries Verachtert <dries@ulyssis.org> 0.9.14-1
- Update to release 0.9.14.

* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.9.13-1
- Initial packaging

