# $Id$

# Authority: dries
# Upstream:
# Screenshot: http://krusader.sourceforge.net/scr/thumbs/krusader-150cvs_01.png
# ScreenshotURL: http://krusader.sourceforge.net/scr.php

# ExcludeDist: el3 fc1

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: File manager
Name: krusader
Version: 1.70.0
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://krusader.sourceforge.net/

Source: http://dl.sf.net/krusader/krusader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, autoconf, automake
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
Krusader is an advanced twin-panel (commander-style) file-manager for KDE
3.x (similar to Midnight or Total Commander) but with many extras. It
provides all the file-management features you could possibly want.
 Plus: extensive archive handling, mounted filesystem support, FTP, advanced
search module, viewer/editor, directory synchronisation, file content
comparisons, powerful batch renaming and much much more.
 It supports the following archive formats: tar, zip, bzip2, gzip, rar, ace,
arj and rpm and can handle other KIOSlaves such as smb:// or fish://
 It is (almost) completely customizable, very user friendly, fast and looks
great on your desktop! :-)

%prep
%setup
%{__perl} -pi -e "s|class vfs;|class ListPanelFunc;\nclass vfs;|g;" krusader/Panel/listpanel.h
%{__perl} -pi -e "s|^class KMountMan|class KMountManGUI;\nclass KMountMan|g;" krusader/MountMan/kmountman.h
%{__perl} -pi -e "s|class ListPanel;|class ListPanel;\nclass KrDetailedViewItem;|g;" krusader/Panel/krdetailedview.h


%build
export KDEDIR=/usr
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export KDEDIR=/usr
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%{__rm} -f %{buildroot}%{_datadir}/mimelnk/application/x-ace.desktop
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applnk/krusader*.desktop
%{_datadir}/icons/*/*/apps/krusader*.png
%{_datadir}/apps/krusader
%{_datadir}/doc/HTML/en/krusader
%{_datadir}/services/krarc.protocol
%{_libdir}/kde3/kio_krarc.*
%{_libdir}/kde3/kio_iso*
%{_datadir}/apps/konqueror/servicemenus/isoservice.desktop
%{_datadir}/config/kio_isorc
%{_datadir}/services/iso.protocol

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.70.0-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Feb 15 2006 Dries Verachtert <dries@ulyssis.org> - 1.70.0-1
- Update to release 1.70.0.

* Tue Jun 21 2005 Dries Verachtert <dries@ulyssis.org> - 1.60.0-1
- Update to release 1.60.0.

* Tue Dec 14 2004 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Update to version 1.51.

* Mon Nov 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.50-1
- Update to version 1.50.

* Wed Jul 21 2004 Dries Verachtert <dries@ulyssis.org> - 1.40-1
- Update to version 1.40.

* Thu Jun 3 2004 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Initial package.
