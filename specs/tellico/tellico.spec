# $Id: $

# Authority: dries
# Upstream: Robby Stephenson <mailto:robby$periapsis,org>
# Screenshot: http://www.periapsis.org/tellico/sshots/main_screen-0.9.png
# ScreenshotURL: http://www.periapsis.org/tellico/sshots.php

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}

Summary: collection manager
Name: tellico
Version: 0.13.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.periapsis.org/tellico/

Source: http://www.periapsis.org/tellico/download/tellico-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, libgcrypt-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, libxslt-devel
BuildRequires: kdelibs-devel, desktop-file-utils, libxml2-devel
BuildRequires: kdemultimedia-devel
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Tellico is a collection manager for KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from Amazon.com. 

%prep
%setup

%build
source  /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source  /etc/profile.d/qt.sh
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/apps/tellico
%{_datadir}/applnk/Applications/tellico.desktop
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/doc/HTML/en/tellico
%{_datadir}/icons/hicolor/*/apps/tellico.png
%{_datadir}/icons/hicolor/*/mimetypes/tellico.png
%{_datadir}/mimelnk/application/x-tellico.desktop

%changelog
* Sun Jul 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.8-1
- Updated to release 0.15.8.

* Mon Apr 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.6-1
- Updated to release 0.13.6.

* Wed Mar 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.5-1
- Updated to release 0.13.5.

* Mon Feb 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.4-1
- Updated to release 0.13.4.

* Sat Jan 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.13.1-2
- kdemultimedia-devel added to the buildrequirements so it picks up 
  kcddb support (Thanks to Vic Gedris)

* Sun Dec 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.13.1-1
- Update to release 0.13.1.

* Sat Dec 04 2004 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Update to release 0.13.

* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
