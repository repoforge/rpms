# $Id$
# Authority: dag

### EL2 ships with rxvt-2.7.8-4
%{?el2:# Tag: rfx}

%define desktop_vendor rpmforge

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Color VT102 terminal emulator for the X Window System
Name: rxvt
Version: 2.7.10
Release: 2%{?dist}
Epoch: 18
License: GPL
Group: User Interface/X
URL: http://www.rxvt.org/

Source: http://dl.sf.net/rxvt/rxvt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: libtool
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: xorg-x11-proto-devel, libXt-devel, libXpm-devel}

Requires: utempter

%description
Rxvt is a color VT102 terminal emulator for the X Window System. Rxvt
is intended to be an xterm replacement for users who don't need the
more esoteric features of xterm, like Tektronix 4014 emulation,
session logging and toolkit style configurability. Since it does not
support those features, rxvt uses much less swap space than xterm
uses. This is a significant advantage on a machine which is serving a
large number of X sessions.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >rxvt.desktop
[Desktop Entry]
Name=RXVT Terminal
Comment=Use the command line
Exec=rxvt
Icon=gnome-term-linux.png
Type=Application
Terminal=false
Encoding=UTF-8
Categories=GNOME;Application;System;TerminalEmulator;
EOF

%build
%configure \
%{!?_without_modxorg:--x-includes="%{_includedir}"} \
%{!?_without_modxorg:--x-libraries="%{_libdir}"} \
%{?_without_modxorg:--x-libraries="%{_prefix}/X11R6/%{_lib}"} \
    --enable-256-color \
    --enable-everything \
    --enable-languages \
    --enable-shared \
    --enable-smart-resize \
    --enable-ttygid \
    --enable-xgetdefault \
    --with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall mandir="%{buildroot}%{_mandir}/man1"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --add-category X-Red-Hat-Base               \
    --dir %{buildroot}%{_datadir}/applications  \
    rxvt.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.txt doc/BUGS doc/FAQ doc/README* doc/TODO
%doc doc/menu/ doc/rxvt* doc/xterm.seq
%doc %{_mandir}/man1/rclock.1*
%doc %{_mandir}/man1/rxvt.1*
%{_bindir}/rclock
%{_bindir}/rxvt
%{_bindir}/rxvt-2.7.10
%{_datadir}/applications/%{desktop_vendor}-rxvt.desktop
%{_libdir}/librxvt.so.*
%exclude %{_libdir}/*.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rxvtlib.h
%{_libdir}/librxvt.a
%{_libdir}/librxvt.so

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 2.7.10-2
- Fix build for modxorg.

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 2.7.10-1
- Addded improved desktop file.

* Sun Oct 11 2003 Dag Wieers <dag@wieers.com> - 2.7.10-0
- Initial package. (using DAR)
