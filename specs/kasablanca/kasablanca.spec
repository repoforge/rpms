# $Id$

# Authority: dries
# Screenshot: http://kasablanca.berlios.de/images/screenshots/sshot031.png

# ExcludeDist: el3 fc1

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Ftp/fxp client
Name: kasablanca
Version: 0.4.0.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kasablanca.berlios.de/

Source: http://download.berlios.de/kasablanca/kasablanca-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc-c++
BuildRequires: qt-devel, openssl-devel
BuildRequires: automake, autoconf
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Kasablanca is an ftp client, written in c++, using the kde libraries. among
its features are currently encryption (auth tls) support, fxp, site 
bookmarks, and queued transfers.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/applnk/Utilities/kasablanca.desktop
%{_datadir}/apps/kasablanca
%{_datadir}/doc/HTML/en/kasablanca
%{_datadir}/icons/*/*/apps/kasablanca.png
%{_datadir}/config.kcfg/kbconfig.kcfg

%changelog
* Sat Aug 21 2004 Dries Verachtert <dries@ulyssis.org> 0.4.0.1-1
- Update to version 0.4.0.1.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> 0.4-1
- Update to version 0.4.

* Mon Mar 22 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- Initial package
