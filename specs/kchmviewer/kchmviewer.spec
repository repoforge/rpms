# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%define desktop_vendor rpmforge

Summary: CHM file viewer
Name: kchmviewer
Version: 2.0
Release: 2
License: GPL
Group: Applications/Publishing
URL: http://kchmviewer.sourceforge.net/

Source: http://dl.sf.net/kchmviewer/kchmviewer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel >= 3.2, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
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
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org>  2.0-1
- Updated to release 2.0.

* Mon Nov 28 2005 Dries Verachtert <dries@ulyssis.org>  1.3-1
- Upgrade to release 1.3.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org>  1.2-1
- Upgrade to release 1.2.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org>  1.1-1
- Upgrade to release 1.1.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org>  1.0-1
- Upgrade to release 1.0.

* Tue Jul 26 2005 Dries Verachtert <dries@ulyssis.org> 0.9.1-1
- First packaging.
