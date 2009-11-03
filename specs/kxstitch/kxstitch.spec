# $Id$

# Authority: dries
# Upstream:
# Screenshot: http://kxstitch.sourceforge.net/image/mainview.png
# ScreenshotURL: http://kxstitch.sourceforge.net/screenshots.shtml

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: Cross stitch patterns editor
Name: kxstitch
Version: 0.8
Release: 1%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://kxstitch.sourceforge.net/index.shtml

Source: http://dl.sf.net/kxstitch/kxstitch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel
BuildRequires: gcc-c++, gettext, zlib-devel
BuildRequires: qt-devel, libjpeg-devel, kdelibs-devel
BuildRequires: ImageMagick-c++-devel
BuildRequires: libexif-devel, libexif
%{!?_without_selinux:BuildRequires: libselinux-devel}
BuildRequires: libexif-devel, libexif

%description
KXStitch allows the creation and editing of cross stitch patterns.

%prep
%setup
%{__perl} -pi -e "s|/usr/share/man|\\\$(mandir)|g;" kxstitch/Makefile*

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
# %{__perl} -pi -e "s|/usr/share/man|\\\$(mandir)|g;" kxstitch/Makefile*
%makeinstall 
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/kxstitch*
%{_bindir}/kxstitch
%{_datadir}/apps/kxstitch/
%{_datadir}/applnk/Graphics/kxstitch.desktop
%{_datadir}/mimelnk/application/kxstitch.desktop
%{_datadir}/icons/*/*/apps/kxstitch.png
%{_datadir}/doc/HTML/en/kxstitch/

%changelog
* Fri Jan 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
