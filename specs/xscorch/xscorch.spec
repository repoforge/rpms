# $Id$
# Authority: newrpms
# Upstream: Justin David Smith <justins$chaos2,org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Clone of the classic DOS game, "Scorched Earth"
Name: xscorch
Version: 0.2.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://chaos2.org/xscorch/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://chaos2.org/xscorch/xscorch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The basic
goal is to annihilate enemy tanks using overpowered guns :). Basically,
you buy weapons, you target the enemy by adjusting the angle of your
turret and firing power, and you hope to destroy their tank before they
destroy yours.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
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
%{__install} -D -m0644 img/xscorch-icon.xpm %{buildroot}%{_datadir}/pixmaps/xscorch.xpm

%if %{dfi}
	%{__install} -D -m0644 xscorch.desktop %{buildroot}%{_datadir}/gnome/apps/Games/xscorch.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/xscorch/
%{_datadir}/pixmaps/*.xpm
%if %{dfi}
        %{_datadir}/gnome/apps/Games/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.1.15-1
- Added .desktop file.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 0.1.15-0
- Initial package. (using DAR)
