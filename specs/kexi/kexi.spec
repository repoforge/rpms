# $Id: $

# Authority: dries
# Upstream: 
# Screenshot: http://www.koffice.org/kexi/pics/relations.png
# ScreenshotURL: http://www.koffice.org/kexi/screenshots.php

%define real_version 0.1beta5

Summary: Integrated environment for managing data.
Name: kexi
Version: 0.1
Release: beta5.1
License: GPL
Group: Applications/Databases
URL: http://www.koffice.org/kexi/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://ftp.scarlet.be/pub/kde/unstable/apps/KDE3.x/office/kexi-%{real_version}.tar.bz2
Source2: http://www.kexi-project.org/fixes/keximainwindowimpl.cpp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, 
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
BuildRequires: postgresql-devel, mysql-devel
BuildRequires: sqlite-devel, libpqxx-devel
%{?fc2:BuildRequires: libselinux-devel}

%description
Kexi is an integrated environment for managing data. It helps in creating
database schemas, inserting, querying and processing data. As Kexi is a real
member of the KDE and KOffice projects, it integrates fluently into both. It
is designed to be fully usable also without KDE on Unix, MS Windows and Mac
OS X platforms. 

%prep
%setup -n kexi-%{real_version}

%build
%configure --enable-debug=full
%{__sed} -i 's/-lpqxx/-lpqxx -lpq/g;'  kexi/kexidb/drivers/pqxx/Makefile
%{__cp} -f %{SOURCE2} kexi/main/keximainwindowimpl.cpp
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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

%changelog
* Tue Nov 02 2004 Dries Verachtert <dries@ulyssis.org> - 1.0beta5-1
- Initial package.
