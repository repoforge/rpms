# $Id: $
# Authority: dries

Summary: Shows the status of the keyboard indicator LED's in the KDE Panel
Name: kleds
Version: 0.8.0
Release: 2
License: GPL
Group: User Interface/Desktops
URL: http://www.hansmatzen.de/english/kleds.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: http://www.hansmatzen.de/software/kleds/kleds-%{version}.tar.bz2
BuildRequires: gcc, gcc-c++, qt-devel, kdelibs-devel, XFree86-devel, zlib-devel, libart_lgpl-devel, make, arts-devel, gettext, libpng-devel, libjpeg-devel

# Screenshot: http://www.hansmatzen.de/pics/kleds_ss01.png
# ScreenshotURL: http://www.hansmatzen.de/english/kleds.html#screenshots

%description
KLeds is a little program for the KDE Desktop Environment. It shows 
up in the KDE Panel and displays the current state of the keyboard 
indicator LED's (NumLock, ScrollLock and CapsLock).

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%{__make} install-strip DESTDIR=${RPM_BUILD_ROOT}

%files
%doc AUTHORS COPYING NEWS README TODO
%defattr(-,root,root,0755)
%{_bindir}/kleds
%{_bindir}/kledsd
%{_datadir}/locale/de/LC_MESSAGES/kleds.mo

%changelog
* Thu Dec 11 2003 Dries Verachtert <dries@ulyssis.org> 0.8.0-2
- added some BuildRequires

* Sun Nov 30 2003 Dries Verachtert <dries@ulyssis.org> 0.8.0-1
- first packaging for Fedora Core 1
