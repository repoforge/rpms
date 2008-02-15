# $Id$

# Authority: dries
# Screenshot: http://kasablanca.berlios.de/images/screenshots/sshot031.png

# ExcludeDist: el3 fc1

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Ftp/fxp client
Name: kasablanca
Version: 0.4.0.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kasablanca.berlios.de/

Source: http://download.berlios.de/kasablanca/kasablanca-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: zlib-devel
BuildRequires: kdelibs-devel, gcc-c++
BuildRequires: openssl-devel
BuildRequires: automake, autoconf

%description
Kasablanca is an ftp client, written in c++, using the kde libraries. among
its features are currently encryption (auth tls) support, fxp, site
bookmarks, and queued transfers.

%prep
%setup

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
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
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0.2-1
- Updated to release 0.4.0.2.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.0.1-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Aug 21 2004 Dries Verachtert <dries@ulyssis.org> 0.4.0.1-1
- Update to version 0.4.0.1.

* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> 0.4-1
- Update to version 0.4.

* Mon Mar 22 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- Initial package
