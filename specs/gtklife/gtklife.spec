# $Id$
# Authority: dag
# Upstream: Suzanne Britton <gtklife$ironphoenix,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?el2:%define _without_gtk2 1}

%define desktop_vendor rpmforge

Summary: Conway's game of life.
Name: gtklife
Version: 5.1
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://ironphoenix.org/tril/gtklife/

Source: http://ironphoenix.org/tril/gtklife/gtklife-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
GtkLife is a fast and user-friendly implementation of Conway's Life program.
It is something comparable to the venerable XLife in speed, but with a more
modern and featureful GUI. It is not tied to any particular desktop
environment.

%prep
%setup

%{__cat} <<EOF >gtklife.desktop
[Desktop Entry]
Name=Conway's Game Of Life
Comment=Create patterns and see them evolve
Icon=gtklife.png
Exec=gtklife
Terminal=false
Encoding=UTF-8
Type=Application
Categories=GNOME;Application;Game;
EOF

%build
%configure \
%{!?_without_gtk2:--with-gtk2}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 icon_48x48.png %{buildroot}%{_datadir}/pixmaps/gtklife.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 gtklife.desktop %{buildroot}%{_datadir}/gnome/apps/Games/gtklife.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gtklife.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README doc/*
%{_bindir}/gtklife
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/gtklife.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gtklife.desktop}
%{_datadir}/gtklife/
%{_datadir}/pixmaps/gtklife.png
%exclude %{_prefix}/doc/gtklife/

%changelog
* Sat Sep 16 2006 Dag Wieers <dag@wieers.com> - 5.1-2
- Use configure and --with-gtk2 if applicable.

* Fri Sep 15 2006 Dag Wieers <dag@wieers.com> - 5.1-1
- Updated to release 5.1.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 5.0-1
- Updated to release 5.0.

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 4.2-1
- Updated to release 4.2.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 4.1-1
- Updated to release 4.1.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 4.0-1
- Updated to release 4.0.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 2.0-2
- Small cosmetic changes.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
