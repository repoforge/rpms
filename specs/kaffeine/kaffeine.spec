# $Id: $
# Authority: dries
# Screenshot: http://kaffeine.sourceforge.net/pics/05/kaffeine05-1.png
# ScreenshotURL: http://kaffeine.sourceforge.net/screenshots.html

Summary: Media player based on xine-lib
Name: kaffeine
Version: 0.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kaffeine.sourceforge.net

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kaffeine/kaffeine-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
BuildRequires: xine-lib-devel

%description
Kaffeine is a simple and easy to use media player based on the xine-lib and
full integrated in KDE3. It supports drag and drop and provides an editable
playlist, a Konqueror plugin, a Mozilla plugin, OSD, and much more. 

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL README TODO
%doc %{_mandir}/man?/*
%doc %{_mandir}/de/man?/*
%{_bindir}/kaffeine
%{_includedir}/kaffeine
%{_libdir}/libkmediapart.*
%{_libdir}/kde3/libkaffeinepart.*
%{_datadir}/services/kaffeine_part.desktop
%{_datadir}/apps/konqueror/servicemenus/kaffeine*.desktop
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/apps/kaffeine
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/applnk/Multimedia/kaffeine.desktop
%doc %{_datadir}/doc/HTML/*/kaffeine
%{_datadir}/icons/*/*/*/*.png

%changelog
* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
