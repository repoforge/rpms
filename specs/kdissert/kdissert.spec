# $Id$
# Authority: dag
# Upstream: <tnagy256$yahoo,fr>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Mindmapping tool for creating texts
Name: kdissert
Version: 0.2.5
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://freehackers.org/~tnagy/kdissert/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://freehackers.org/~tnagy/kdissert/kdissert-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel 

%description
Kdissert is a mind-mapping tool for helping students to create texts
like dissertations, reports and thesis

%prep
%setup

%{__cat} <<EOF >kdissert.desktop
[Desktop Entry]
Name=KDissert Mind-mapping Tool
Comment=Helps to create structured text documents
Exec=kdissert
Icon=kdissert.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Office;TextEditor;
StartupNotify=true
EOF

%build
source "/etc/profile.d/qt.sh"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%makeinstall
%find_lang %{name}

%{__install} -D -m0644 src/hi128-app-kdissert.png %{buildroot}%{_datadir}/pixmaps/kdissert.png

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 kdissert.desktop %{buildroot}%{_datadir}/applications/kdissert.desktop
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/gxine.desktop}

%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde                  \
		--dir %{buildroot}%{_datadir}/applications \
		--add-category X-Red-Hat-Base              \
		kdissert.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%doc %{_docdir}/HTML/en/kdissert/
%{_bindir}/kdissert
%exclude %{_libdir}/libkdiss*.la
%{_datadir}/applications/kde/kdissert.desktop
%{_datadir}/applnk/Utilities/kdissert.desktop
%{_datadir}/apps/kdissert/
%{_datadir}/config.kcfg/kdissert.kcfg
%{_datadir}/icons/crystalsvg/*/actions/kdissert_*.png
%{_datadir}/icons/hicolor/*/apps/kdissert.png
%{_datadir}/mimelnk/application/x-kdissert.desktop
%{_datadir}/pixmaps/kdissert.png
%{_libdir}/libkdiss*.so
%{!?_without_freedesktop:%{_datadir}/applications/kde-kdissert.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/kdissert.desktop}

%changelog
* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 0.2.5-1
- Initial package. (using DAR)
