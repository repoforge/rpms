# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1} 
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: X Window System utility for monitoring system resources
Name: xosview
Version: 1.8.0
Release: 1
License: GPL/BSD
Group: Applications/System
Url: http://xosview.sourceforge.net/

Source: http://dl.sf.net/xosview/xosview-%{version}.tar.gz
Source1: xosview.png
Patch0: xosview-non-i386.patch
Patch2: xosview-ppc.patch
Patch3: xosview-1.8.0-rpath.patch
Patch5: xosview-1.8.0-s390.patch
Patch6: xosview-1.8.0-proc.patch
Patch8: xosview-1.8.0-procstat.patch
Patch9: xosview-1.8.0-strip.patch
Patch10: xosview-1.8.0-gcc33.patch
Patch11: xosview-1.8.0-kernel26.patch
Patch12: xosview-1.8.0-nfs.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
The xosview utility displays a set of bar graphs which show the
current system state, including memory usage, CPU usage, system load,
etc. Xosview runs under the X Window System.

%prep
%setup
%patch0 -p0
%patch2 -p0 -b .ppc
%patch3 -p1
%patch5 -p1 -b .s390
%patch6 -p1 -b .proc
%patch8 -p1 -b .procstat
%patch9 -p1 -b .strip
%patch10 -p1 -b .gcc33
%patch11 -p1 -b .kernel26
%patch12 -p1

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

#%{__cp} -vf %{_datadir}/libtool/config.* config/

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
%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/xosview.png

%{__chmod} 0755 %{buildroot}%{_usr}/X11R6/bin/xosview

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 xosview.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/xosview.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		xosview.desktop
%endif

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
* Sun Oct 10 2004 Dag Wieers <dag@wieers.com> - 1.8.0-1
- Initial package. (using DAR)
