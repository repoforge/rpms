# $Id: $

# Authority: dries
# Upstream: bastian@kde.org
# Screenshot: http://extragear.kde.org/apps/kiosktool/kiosktool3.png
# ScreenshotURL: http://extragear.kde.org/apps/kiosktool.php

Summary: KIOSK administration admin tool
Name: kiosktool
Version: 0.7
Release: 1
License: GPL
Group: Applications/
URL: http://extragear.kde.org/apps/kiosktool.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.kde.org/pub/kde/stable/apps/KDE3.x/admin/kiosktool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc, make
BuildRequires: gcc-c++, XFree86-devel
BuildRequires: qt-devel
%{?fc2:BuildRequires: libselinux-devel}

%description
A Point and Click tool for system administrators to enable KDE's KIOSK features
or otherwise preconfigure KDE for groups of users. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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
%{_bindir}/*
%{_datadir}/applnk/Utilities/kiosktool.desktop
%{_datadir}/apps/kiosktool
%{_datadir}/icons/crystalsvg/*/apps/kiosktool.png


%changelog
* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Update to version 0.7.

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Update to version 0.5.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Initial package.
