# $Id$

# Authority: newrpms
# Upstream: Justin David Smith <justins@chaos2.org>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A clone of the classic DOS game, "Scorched Earth".
Name: xscorch
Version: 0.1.15
Release: 0
License: GPL
Group: Amusements/Games
URL: http://chaos2.org/xscorch/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://chaos2.org/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel >= 1.2

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The basic
goal is to annihilate enemy tanks using overpowered guns :). Basically,
you buy weapons, you target the enemy by adjusting the angle of your
turret and firing power, and you hope to destroy their tank before they
destroy yours.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 img/xscorch-icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Scorched Earth
Comment=%{summary}
Icon=xscorch.xpm
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
EOF

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Games/
	%{__install} -m0644 gnome-%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Games/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category Game                        \
		--dir %{buildroot}%{_datadir}/applications \
		gnome-%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/xscorch/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Games/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 1.91-1
- Added .desktop file.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 1.91-0
- Initial package. (using DAR)
