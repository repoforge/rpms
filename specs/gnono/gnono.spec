# $Id$
# Authority: dag
# Upstream: Derrick J. Houy <djhouy$paw,za,org>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: UNO card game
Name: gnono
Version: 0.0.3
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.paw.co.za/projects/gnono/

Source: ftp://ftp.paw.co.za/pub/PAW/sources/gnono-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-libs-devel, autoconf, automake
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
An interesting card game, like UNO.

%prep
%setup

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >gnono.desktop.in
[Desktop Entry]
Name=Gnono
Comment=UNO alike card game
Exec=gnono
Icon=gnono.png
Type=Application
Terminal=false
Encoding=UTF-8
Categories=GNOME;Application;Game;CardGame;
EOF

%build
%configure \
	--without-debug
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/gnono-icon.png %{buildroot}%{_datadir}/pixmaps/gnono.png

%if %{?!_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net --delete-original \
		--add-category X-Red-Hat-Base               \
		--dir %{buildroot}%{_datadir}/applications  \
		%{buildroot}%{_datadir}/gnome/apps/Games/gnono.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/pixmaps/gnono.png
%{_datadir}/pixmaps/gnono/
%exclude %{_prefix}/doc/
%{!?_without_freedesktop:%{_datadir}/applications/net-gnono.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/gnono.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1.2
- Rebuild for Fedora Core 5.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Add improved desktop file.

* Fri Jan 07 2003 Dag Wieers <dag@wieers.com> - 0.0.3-0
- Initial package. (using DAR)
