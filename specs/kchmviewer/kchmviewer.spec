# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge

Summary: CHM file viewer
Name: kchmviewer
Version: 1.1
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://kchmviewer.sourceforge.net/

Source: http://dl.sf.net/kchmviewer/kchmviewer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel >= 3.2, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}
%{?el4:BuildRequires: libselinux-devel}
%{?fc4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
Kchmviewer is a CHM file viewer for KDE.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure --with-kde LDFLAGS=-L/usr/X11R6/lib/
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source  /etc/profile.d/qt.sh
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%{_bindir}/kchmviewer
%{_datadir}/applnk/kchmviewer.desktop
%{_libdir}/kde3/kio_msits*
%{_datadir}/services/msits.protocol

%changelog
* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org>  1.1-1
- Upgrade to release 1.1.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org>  1.0-1
- Upgrade to release 1.0.

* Tue Jul 26 2005 Dries Verachtert <dries@ulyssis.org> 0.9.1-1
- First packaging.
