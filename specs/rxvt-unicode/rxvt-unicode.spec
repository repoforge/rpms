# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

%define desktop_vendor rpmforge

Summary: Unicode version of rxvt
Name: rxvt-unicode
Version: 9.06
Release: 1
License: GPL
Group: User Interface/X
URL: http://software.schmorp.de/

Source: http://dist.schmorp.de/rxvt-unicode/Attic/rxvt-unicode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, libX11-devel, libXt-devel, libXft-devel, libXpm-devel, libXrender-devel}
%{!?_without_fontconfig:BuildRequires: fontconfig-devel}
BuildRequires: freetype-devel
BuildRequires: glib2-devel
BuildRequires: perl
BuildRequires: /usr/bin/tic

%description
rxvt-unicode is a clone of the well known terminal emulator rxvt, modified to
store text in Unicode (either UCS-2 or UCS-4) and to use locale-correct input
and output. It also supports mixing multiple fonts at the same time, including
Xft fonts.

%prep
%setup

%{__cat} <<EOF >rxvt-unicode.desktop
[Desktop Entry]
Name=RXVT Terminal (unicode)
Comment=Use the command line
Exec=urxvt
Terminal=false
Type=Application
Encoding=UTF-8
Icon=gnome-term-linux.png
Categories=GNOME;Application;System;TerminalEmulator;
EOF

%build
%configure \
    --enable-24bit \
    --enable-combining \
    --enable-fading \
    --enable-font-styles \
    --enable-frills \
    --enable-half-shadow \
    --enable-iso14755 \
    --enable-keepscrolling \
    --enable-lastlog \
    --enable-linespace \
    --enable-menubar \
    --enable-mousewheel \
    --enable-next-scroll \
    --enable-plain-scroll \
    --enable-pointer-blank \
    --enable-resources \
    --enable-rxvt-scroll \
    --enable-selectionscrolling \
    --enable-slipwheeling \
    --enable-smart-resize \
    --enable-tinting \
    --enable-transparency \
    --enable-utmp \
    --enable-wtmp \
    --enable-xft \
    --enable-xgetdefault \
    --enable-xterm-scroll \
    --enable-xpm-background \
    --enable-xim \
    --with-codesets="all" \
    --with-save-lines="2000" \
    --with-xpm-includes="%{_includedir}/X11" \
    --with-xpm-library="%{_libdir}"
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

desktop-file-install --vendor=%{desktop_vendor} \
    --dir=%{buildroot}%{_datadir}/applications  \
    rxvt-unicode.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README.FAQ doc/changes.txt doc/README.xvt doc/etc/
%doc %{_mandir}/man1/urxvt.1*
%doc %{_mandir}/man1/urxvtc.1*
%doc %{_mandir}/man1/urxvtd.1*
%doc %{_mandir}/man3/urxvtperl.3*
%doc %{_mandir}/man7/urxvt.7*
%{_bindir}/urxvt
%{_bindir}/urxvtc
%{_bindir}/urxvtd
%{_datadir}/applications/%{desktop_vendor}-rxvt-unicode.desktop
%{_libdir}/urxvt/

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 9.06-1
- Updated to release 9.06.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 9.05-1
- Updated to release 9.05.

* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 9.01-1
- Updated to release 9.01.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 9.0-1
- Updated to release 9.0.

* Sun Nov 25 2007 Dag Wieers <dag@wieers.com> - 8.7-1
- Updated to release 8.7.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 8.6-1
- Updated to release 8.6.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 8.4-2
- Define %%{desktop_vendor}.

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 8.4-1
- Initial package. (using DAR)
