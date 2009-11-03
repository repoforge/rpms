# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%define desktop_vendor rpmforge

Summary: Graphical FTP client for the K Desktop Environment.
Name: kftpgrabber
Version: 0.8.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kftp.org/

Source: http://www.kftp.org/uploads/files/kftpgrabber-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.3.2, kdelibs-devel >= 3.2.0, openssl-devel >= 0.9.7
BuildRequires: libpng-devel, libart_lgpl-devel, desktop-file-utils, gcc-c++
BuildRequires: arts-devel, libjpeg-devel, gettext, zlib-devel
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
KFTPGrabber is a graphical FTP client for KDE. It provides a nice GUI
for all file transfer operations, it supports encrypted connections
(both SSL and SFTP), site-to-site (FXP) transfers, a complete bookmark
system and also has a built in support for Zeroconf site discovery.

%prep
%setup

%build
source  /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source  /etc/profile.d/qt.sh
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 755)
%doc %{_docdir}/HTML/en/kftpgrabber/
%{_bindir}/kftpgrabber
%{_datadir}/applications/kde/kftpgrabber.desktop
%{_datadir}/apps/kftpgrabber/
%{_datadir}/icons/hicolor/*/apps/kftpgrabber.png
%{_datadir}/services/kftpimportplugin_gftp.desktop
%{_datadir}/servicetypes/kftpbookmarkimportplugin.desktop
%{_includedir}/kftpgrabber/
### .la files are needed by kftpgrabber
%{_libdir}/libkftpinterfaces.la
%{_libdir}/libkftpinterfaces.so
%{_libdir}/libkftpinterfaces.so.*
%{_libdir}/kde3/kftpimportplugin_gftp.la
%{_libdir}/kde3/kftpimportplugin_gftp.so

%changelog
* Tue Jan 30 2007 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.0-4
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Nov 26 2004 Dries Verachtert <dries@ulyssis.org - 0.5.0-3
- Update to release 0.5.0.

* Tue Nov 02 2004 Dag Wieers <dag@wieers.com> - 0.5.0-2.beta1
- Included .la files. (Dries Verachtert)
- Added contributed SPEC files. (Kevin Smith)
