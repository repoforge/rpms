# $Id$

# Authority: dries
# Upstream:
# Screenshot: http://www.koffice.org/kexi/pics/relations.png
# ScreenshotURL: http://www.koffice.org/kexi/screenshots.php

# ExcludeDist: el3
# Tag: test


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

%{?fc2:%define _without_qt_config 1}
%{?fc1:%define _without_qt_config 1}
%{?el3:%define _without_qt_config 1}
%{?rh9:%define _without_qt_config 1}
%{?rh8:%define _without_qt_config 1}
%{?rh7:%define _without_qt_config 1}
%{?el2:%define _without_qt_config 1}
%{?rh6:%define _without_qt_config 1}
%{?yd3:%define _without_qt_config 1}


Summary: Integrated environment for managing data.
Name: kexi
Version: 0.9
Release: 2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://www.koffice.org/kexi/

Source: http://ftp.belnet.be/packages/kde/stable/apps/KDE3.x/database/kexi-%{version}.tar.bz2
Patch: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel
BuildRequires: gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
BuildRequires: postgresql-devel, mysql-devel
BuildRequires: sqlite-devel, libpqxx-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}
%{!?_without_qt_config:BuildRequires: qt-config}

%description
Kexi is an integrated environment for managing data. It helps in creating
database schemas, inserting, querying and processing data. As Kexi is a real
member of the KDE and KOffice projects, it integrates fluently into both. It
is designed to be fully usable also without KDE on Unix, MS Windows and Mac
OS X platforms.

%prep
%setup -n kexi-%{version}
%patch -p1

%build
source /etc/profile.d/qt.sh
%configure --enable-debug=full
%{__sed} -i 's/-lpqxx/-lpqxx -lpq/g;'  kexi/kexidb/drivers/pqxx/Makefile
#%{__cp} -fp %{SOURCE2} kexi/main/keximainwindowimpl.cpp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL README
%{_bindir}/*
%{_libdir}/*.so*
%{_libdir}/*.la
%{_libdir}/kde3/*.so*
%{_libdir}/kde3/*.la
%{_datadir}/config/magic/kexi.magic
%{_datadir}/config/kexirc
%{_datadir}/servicetypes/*.desktop
%{_datadir}/services/*.desktop
%{_datadir}/services/*/*.desktop
%{_datadir}/apps/kformdesigner
%{_datadir}/apps/kexi
%{_datadir}/apps/kformdesigner_part
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/applnk/Utilities/kformdesigner.desktop
%{_datadir}/applications/kde/kexi.desktop
%{_datadir}/icons/crystalsvg/*/apps/kexi.*
%{_datadir}/icons/crystalsvg/*/mimetypes/*.png
%{_includedir}/kexidb

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Update to release 0.9.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-0.beta1
- Update to release 0.9-0.beta1.

* Tue Nov 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.1beta5-1
- Initial package.
