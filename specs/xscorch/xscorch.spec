# $Id$
# Authority: rudolf
# Upstream: Justin David Smith <justins$chaos2,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Clone of the classic DOS game, "Scorched Earth"
Name: xscorch
Version: 0.2.0
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://xscorch.org/

Source: http://xscorch.org/releases/xscorch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2
BuildRequires: gcc-c++
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The basic
goal is to annihilate enemy tanks using overpowered guns :). Basically,
you buy weapons, you target the enemy by adjusting the angle of your
turret and firing power, and you hope to destroy their tank before they
destroy yours.

%prep
%setup

%{__cat} <<EOF >xscorch.desktop
[Desktop Entry]
Name=Scorched Earth
Comment=Destroy the enemy tanks before they destroy you
Icon=xscorch.xpm
Exec=xscorch
Terminal=false
Type=Application
Categories=Application;Game;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 img/xscorch-icon.xpm %{buildroot}%{_datadir}/pixmaps/xscorch.xpm

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 xscorch.desktop %{buildroot}%{_datadir}/gnome/apps/Games/xscorch.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xscorch.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/xscorch.6*
%{_bindir}/xscorch*
%{_datadir}/xscorch/
%{_datadir}/pixmaps/xscorch.xpm
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/xscorch.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xscorch.desktop}

%changelog
* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.2.0-2
- Samll fix in desktop entry.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.1.15-1
- Added .desktop file.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 0.1.15-0
- Initial package. (using DAR)
