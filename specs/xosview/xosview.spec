# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

%define desktop_vendor rpmforge

Summary: X Window System utility for monitoring system resources
Name: xosview
Version: 1.8.2
Release: 1.2
License: GPL/BSD
Group: Applications/System
URL: http://xosview.sourceforge.net/

Source: http://dl.sf.net/xosview/xosview-%{version}.tar.gz
Source1: xosview.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

%prep
%setup

%{__cat} <<EOF >xosview.desktop
[Desktop Entry]
Name=Xosview OS Monitor
Comment=Display resources in real-time
Exec=xosview
Terminal=false
Type=Application
Icon=xosview.png
Categories=Application;System;
Encoding=UTF-8
EOF

#%{__cp} -fpv %{_datadir}/libtool/config.* config/

%build
%configure \
	--disable-linux-memstat
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_prefix}/X11R6/bin/ \
			%{buildroot}%{_prefix}/X11R6/man/man1/ \
			%{buildroot}%{_prefix}/X11R6/lib/X11/app-defaults/
%makeinstall \
	PREFIX_TO_USE="%{buildroot}%{_prefix}/X11R6"
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xosview.png

%{__chmod} 0755 %{buildroot}%{_usr}/X11R6/bin/xosview

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 xosview.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/xosview.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xosview.desktop
%endif

### FIXME: Binary does not get stripped by brp-strip (RPM bug?)
strip %{buildroot}%{_prefix}/X11R6/bin/xosview

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING* README README.linux TODO
%doc %{_prefix}/X11R6/man/man1/xosview.1*
%{_prefix}/X11R6/bin/xosview
%{_prefix}/X11R6/lib/X11/app-defaults/XOsview
%{_datadir}/icons/xosview.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/xosview.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xosview.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.2-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 1.8.2-1
- Updated to release 1.8.2.

* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 1.8.0-1
- Initial package. (using DAR)
