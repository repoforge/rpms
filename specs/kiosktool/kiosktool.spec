# $Id$
# Authority: dries
# Upstream: <bastian$kde,org>

# Screenshot: http://extragear.kde.org/apps/kiosktool/kiosktool3.png
# ScreenshotURL: http://extragear.kde.org/apps/kiosktool.php

##ExcludeDist: el3 fc1


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: KIOSK administration admin tool
Name: kiosktool
Version: 0.9
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://extragear.kde.org/apps/kiosktool.php

Source: ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/admin/kiosktool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc, make
BuildRequires: gcc-c++, qt-devel >= 3.2
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
A Point and Click tool for system administrators to enable KDE's KIOSK features
or otherwise preconfigure KDE for groups of users.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/kiosktool*
%{_datadir}/applnk/Utilities/kiosktool.desktop
%{_datadir}/apps/kiosktool
%{_datadir}/icons/crystalsvg/*/apps/kiosktool.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Thu Jan 27 2005 Dag Wieers <dag@wieers.com> - 0.9-1
- Update to version 0.9.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Update to version 0.7.

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Update to version 0.5.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Initial package.
