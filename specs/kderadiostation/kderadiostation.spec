# $Id: $

# Authority: dries

Summary: Tool which presents you a list of internet streaming radio stations
Name: kderadiostation
Version: 0.5
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://kderadiostation.coolprojects.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://kderadiostation.coolprojects.org/source/kderadiostation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel

# Screenshot: http://kderadiostation.coolprojects.org/shots/kderadioshot1.thumb.png
# ScreenshotURL: http://kderadiostation.coolprojects.org/screenshots.html

%description
This tool presents you a list of internet streaming radio stations. Just
select your favorite one, and xmms or noatun will pick up the right stream.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib/kde3/libkradiopart* $RPM_BUILD_ROOT/usr/lib/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-,root,root,0755)
%doc README
%{_bindir}/kderadiostation
%{_libdir}/libkradiopart.la
%{_libdir}/libkradiopart.so.1
%{_libdir}/libkradiopart.so
%{_libdir}/libkradiopart.so.1.0.0
%{_datadir}/applnk/Multimedia/kderadiostation.desktop
%{_datadir}/apps/kderadiostation
%{_datadir}/config/kderadiostationrc
%{_datadir}/icons/hicolor/32x32/apps/kderadiostation.png
%{_datadir}/locale/*/LC_MESSAGES/kderadiostation.mo

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.5-3
- cleanup of spec file

* Sat Dec 27 2003 Dries Verachtert <dries@ulyssis.org> 0.5-2
- added %post and %postun: /sbin/ldconfig

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.5-1
- first packaging for Fedora Core 1
