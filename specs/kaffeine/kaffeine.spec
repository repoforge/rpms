# $Id$
# Authority: dries

# Screenshot: http://kaffeine.sourceforge.net/pics/05/kaffeine05-1.png
# ScreenshotURL: http://kaffeine.sourceforge.net/screenshots.html

##ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Media player based on xine-lib
Name: kaffeine
Version: 0.7.1
Release: 1.2
License: GPL
Group: Applications/Multimedia
URL: http://kaffeine.sourceforge.net

Source: http://dl.sf.net/kaffeine/kaffeine-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, desktop-file-utils, gettext, gcc-c++
%{?el4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
BuildRequires: xine-lib-devel >= 1.0.0

%description
Kaffeine is a simple and easy to use media player based on the xine-lib and
full integrated in KDE3. It supports drag and drop and provides an editable
playlist, a Konqueror plugin, a Mozilla plugin, OSD, and much more.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
source /etc/profile.d/qt.sh
%configure --without-gstreamer LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
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
%doc AUTHORS ChangeLog COPYING CREDITS README TODO
%doc %{_mandir}/man?/*
%doc %{_mandir}/de/man?/*
%{_bindir}/kaffeine
%{_libdir}/libkmediapart.so.*
%{_libdir}/libkmediapart.la
%{_libdir}/kde3/libkaffeinepart.so
%{_libdir}/kde3/libkaffeinepart.la
%{_datadir}/services/kaffeine_part.desktop
%{_datadir}/apps/konqueror/servicemenus/kaffeine*.desktop
%{_datadir}/apps/profiles/kaffeine.profile.xml
%{_datadir}/apps/kaffeine/
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/applications/kde/kaffeine.desktop
%doc %{_datadir}/doc/HTML/*/kaffeine
%{_datadir}/icons/*/*/*/*.png

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/kaffeine_export.h
%{_includedir}/kaffeine/
%{_libdir}/libkmediapart.so
%{_libdir}/kde3/libkaffeinepart.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1.2
- Rebuild for Fedora Core 5.

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 0.7-1
- Update to 0.7, which doesn't build on FC4 it seems.
- Remove unnecessary build requirements.

* Sun Mar 20 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-2
- Added a devel subpackage so it can update and can be updated by
  the kaffeine package of kde-redhat.

* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.

