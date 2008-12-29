# $Id$
# Authority: dag
# Upstream: Gerd Knorr <kraxel$bytesex,org>

%{?dtag: %{expand: %%define %dtag 1}}

%define _without_libv4l 1

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?el5:%define _with_gl libGL-devel}
%{?el4:%define _with_gl xorg-x11-Mesa-libGL}
%{?el3:%define _with_gl XFree86-Mesa-libGL}
%{?rh9:%define _with_gl XFree86-Mesa-libGL}
%{?rh7:%define _with_gl Glide3-devel}
%{?el2:%define _with_gl Mesa-devel}

%{!?dtag:%define _with_lesstif 1}
%{?el5:%define _with_openmotif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc5:%define _with_openmotif 1}
%{?fc4:%define _with_openmotif 1}
%{?fc3:%define _with_lesstif 1}
%{?el4:%define _with_openmotif 1}
%{?el3:%define _with_openmotif 1}
%{?el2:%define _with_lesstif 1}

%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh7:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}

%define desktop_vendor rpmforge

Summary: Television application for video4linux compliant devices
Name: xawtv
Version: 3.95
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://bytesex.org/xawtv/

Source: http://dl.bytesex.org/releases/xawtv/xawtv-%{version}.tar.gz
Patch0: xawtv-3.95-strip.patch
Patch1: xawtv-3.95-curses-utf8.patch
Patch2: xawtv-3.95-gcc4.patch
Patch3: xawtv-3.95-font.patch
Patch4: xawtv-3.95-region.patch
Patch5: xawtv-3.95-pagesize.patch
Patch6: xawtv-3.95-open.patch
Patch7: xawtv-3.95-man.patch
Patch8: xawtv-3.95-oss.patch
Patch9: xawtv-3.95-scantv.patch
Patch10: xawtv-3.95-fixes.patch
Patch11: xawtv-3.95-no-dga.patch
Patch12: xawtv-3.95-bpl.patch
Patch13: xawtv-3.95-v4l2-old-drop.patch
Patch100: xawtv-3.95-libv4l2.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdv-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: ncurses-devel
BuildRequires: Xaw3d-devel
BuildRequires: zvbi-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}
%{?_with_openmotif:BuildRequires: openmotif-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libFS-devel libXaw-devel libXext-devel libXxf86dga-devel libXv-devel}
%{!?_without_libv4l:BuildRequires: libv4l-devel}
#BuildRequires: libquicktime-devel

%description
Xawtv is a simple xaw-based TV program which uses the bttv driver or
video4linux. Xawtv contains various command-line utilities for
grabbing images and .avi movies, for tuning in to TV stations, etc.
Xawtv also includes a grabber driver for vic.

%prep
%setup
#%{!?_without_modxorg:%patch0 -p1}
%patch0 -p1 -b .strip
%patch1 -p1 -b .curses-utf8
%patch2 -p1 -b .gcc4
#patch3 -p1 -b .font
%patch4 -p1 -b .region
%patch5 -p1 -b .pagesize
%patch6 -p1 -b .open
%patch7 -p1 -b .man
%patch8 -p1 -b .oss
%patch9 -p1 -b .scantv
%patch10 -p1 -b .fixes
%patch11 -p1 -b .no-dga
%patch12 -p1 -b .bpl
%patch13 -p1 -b .v4l2-old-drop 
%{!?_without_libv4l:%patch100 -p1 -b .libv4l}

%{__perl} -pi.orig -e 's| -o root||' Makefile.in

%{__perl} -pi.orig -e 's|# include <FSlib.h>|#include <fonts/FSlib.h>|' console/fs.h

%{__cat} <<EOF >v4l-conf.apps
SESSION=true
USER=root
PROGRAM=%{_sbindir}/v4l-conf
EOF

%{__cat} <<EOF >v4l-conf.pam
#%PAM-1.0
auth		sufficient	pam_rootok.so
auth		required	pam_console.so
account		required	pam_permit.so
session		required	pam_permit.so
session		optional	pam_xauth.so
EOF

%{__cat} <<EOF >xawtv.desktop
[Desktop Entry]
Name=Xawtv Television Viewer
Comment=Watch television on your computer
Icon=gnome-multimedia.png
Exec=xawtv
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

autoconf
autoheader

%build
%configure \
    --disable-motif \
    --disable-quicktime \
    --x-include="%{_includedir}/X11/" \
%{!?_without_modxorg:--x-libraries="%{_libdir}/X11/"}
%{__make} %{?_smp_mflags} verbose="yes"

%install
%{__rm} -rf %{buildroot}
### It fails because %{buildroot}%{_bindir} does not exist. (Fix upstream please)
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__make} install \
    DESTDIR="%{buildroot}" \
    datadir="%{buildroot}%{_datadir}/xawtv" \
    libdir="%{buildroot}%{_libdir}/xawtv" \
    resdir="%{buildroot}%{_datadir}/X11" \
    SUID_ROOT=""

%{__install} -Dp -m0644 v4l-conf.apps %{buildroot}%{_sysconfdir}/security/console.apps/v4l-conf
%{__install} -Dp -m0644 v4l-conf.pam %{buildroot}%{_sysconfdir}/pam.d/v4l-conf

%{__mv} -vf %{buildroot}%{_bindir}/v4l-conf %{buildroot}%{_sbindir}/v4l-conf
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/v4l-conf

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 xawtv.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/xawtv.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        xawtv.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README* TODO contrib/frequencies*
%doc %{_mandir}/man?/*
%doc %{_mandir}/*/man?/*
%config(noreplace) %{_sysconfdir}/pam.d/v4l-conf
%config(noreplace) %{_sysconfdir}/security/console.apps/v4l-conf
%{_bindir}/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/xawtv.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xawtv.desktop}
%{_datadir}/xawtv/
%{_datadir}/X11/app-defaults/Xawtv
%{_libdir}/xawtv/
%{_sbindir}/v4l-conf

%changelog
* Mon Jun 09 2008 Dag Wieers <dag@wieers.com> - 3.95-3
- Rebuild against zvbi-0.2.30.

* Wed Apr 09 2008 Ariel Dembling <arieldembling@gmail.com> 3.95-2
- Fixed compilation errors under CentOS 5.1.

* Thu Mar 29 2007 Dag Wieers <dag@wieers.com> - 3.95-1
- Updated to release 3.95.

* Wed Feb 09 2005 Dag Wieers <dag@wieers.com> - 3.94-2
- Added zvbi-devel build requirement. (Klaus-Peter Schrage)
- Rebuild with zvbi-support.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 3.94-1
- Updated to release 3.94.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 3.92-1
- Updated to release 3.92.

* Sat Apr 11 2004 Dag Wieers <dag@wieers.com> - 3.91-1
- Rebuild against libdv 0.102.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 3.91-0
- Updated to release 3.91.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 3.90-1
- Added desktop file. (Alfredo Milani-Comparetti)

* Tue Oct 21 2003 Dag Wieers <dag@wieers.com> - 3.90-0
- Updated to release 3.90.

* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 3.88-0
- Updated to release 3.88.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 3.86-0
- Updated to release 3.86.

* Sun Jan 05 2003 Dag Wieers <dag@wieers.com> - 3.82-0
- Initial package. (using DAR)
