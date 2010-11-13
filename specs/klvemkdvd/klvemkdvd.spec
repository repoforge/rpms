# $Id$

# Authority: dries
# Upstream:

# ExcludeDist: el3 fc1


%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

Summary: Gui for lvemkdvd
Name: klvemkdvd
Version: 0.4
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://lvempeg.sourceforge.net/klvemkdvd.html

Source: http://dl.sf.net/lvempeg/klvemkdvd-%{version}.src.tgz
Patch0: gcc34-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}
Requires: lve, dvd+rw-tools, dvdauthor

%description
klvemkdvd is able to build (and burn) DVD filesystems from
various mpeg media files using lve tools and some other
programs.

the main intention of klvemkdvd is to build DVDs from
project files (edit lists) created with lve editor.
But it can use other kind of mpegs (VOB, TS, PS, PVA, ...)
as input also.

At all it's a GUI replacement for the command line tool
lvemkdvd (much easier to handle) and is a extension to the
lve package.

%prep
%setup
%patch0 -p1

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{?fc1:for i in $(find . -type f | egrep '\.ui'); do sed -i 's/version="3.2"/version="3.1"/g;' $i; done}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/applnk/Utilities/klvemkdvd.desktop
%{_datadir}/apps/klvemkdvd/klvemkdvdui.rc
%{_datadir}/doc/HTML/en/klvemkdvd
%{_datadir}/icons/*/*/apps/klvemkdvd.png

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Tue Jun 1 2004 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
