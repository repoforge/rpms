# $Id$
# Authority: dag
# Upstream: Billy Biggs <vektor$dumbterm,net>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: High quality TV viewer
Name: tvtime
Version: 0.9.12
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://tvtime.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tvtime/tvtime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: freetype-devel >= 2.0, zlib-devel, libpng-devel, XFree86-libs
BuildRequires: SDL-devel, gcc-c++
#BuildRequires: libstdc++-devel

%description
tvtime is a high quality television application for use with video
capture cards.  tvtime processes the input from a capture card and
displays it on a computer monitor or projector.  Unlike other television
applications, tvtime focuses on high visual quality making it ideal for
videophiles.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{!?_without_freedesktop:1}0
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{buildroot}%{_datadir}/applications/net-tvtime.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* data/COPYING* docs/html/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/tvtime/
%{_bindir}/tvtime-command
%{_bindir}/tvtime-configure
%{_bindir}/tvtime-scanner
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/tvtime.png
%{_datadir}/pixmaps/*
%{_datadir}/tvtime/
%defattr(4775, root, root, 0755)
%{_bindir}/tvtime

%changelog
* Thu Jul 08 2004 Dag Wieers <dag@wieers.com> - 0.9.12-1
- Cosmetic changes.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 0.9.12-0
- Updated to release 0.9.12.

* Thu Nov 13 2003 Dag Wieers <dag@wieers.com> - 0.9.11-0
- Updated to release 0.9.11.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Updated to release 0.9.10.

* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.9.8.5-0
- Initial package. (using DAR)
