# $Id: $

# Authority: dries

Summary: KDE irc program
Name: kmyirc
Version: 0.2.9
Release: 4
License: GPL
Group: Applications/Internet
URL: http://www.kmyirc.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kmyirc/kmyirc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: libart_lgpl-devel, gettext, arts-devel, libjpeg-devel, libpng-devel, XFree86-devel, gcc, gcc-c++, make, kdelibs-devel, qt-devel, zlib-devel, XFree86-devel

# Screenshot: http://www.kmyirc.de/images/screenshots/thumb_kmyirc-01.png
# ScreenshotURL: http://www.kmyirc.de/screenshots.php?handed=0

%description
An irc client for KDE.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
export DESTDIR=$RPM_BUILD_ROOT
make install


%files
%defattr(-,root,root,0755)
%doc COPYING AUTHORS INSTALL README TODO
%{_bindir}/kmyirc
%{_libdir}/lib*
%{_datadir}/apps/kmyirc/icons/*
%{_datadir}/apps/kmyirc/pics/*
%{_datadir}/doc/HTML/en/kmyirc
%{_datadir}/applnk/Internet/kmyirc.desktop
%{_datadir}/icons/locolor/32x32/apps/kmyirc.png
%{_datadir}/icons/locolor/16x16/apps/kmyirc.png
%{_datadir}/config/kmyircrc
%{_datadir}/locale/de/LC_MESSAGES/kmyirc.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/kmyirc.mo

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.2.9-4
- cleanup of spec file, fix

* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-3
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-2
- cleanup of spec file

* Sat Nov 29 2003 Dries Verachtert <dries@ulyssis.org> 0.2.9-1
- first packaging for Fedora Core 1
