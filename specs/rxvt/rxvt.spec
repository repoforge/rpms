# $Id$
# Authority: dag

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Color VT102 terminal emulator for the X Window System
Name: rxvt
Version: 2.7.10
Release: 1
Epoch: 18
License: GPL
Group: User Interface/Desktops
URL: http://www.rxvt.org/

Source: http://dl.sf.net/rxvt/rxvt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
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
Name=Rxvt Terminal
Comment=Small and fast X terminal application
Exec=rxvt
Icon=gnome-term-linux.png
Type=Application
Terminal=false
Encoding=UTF-8
Categories=GNOME;Application;System;TerminalEmulator;
EOF

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	--enable-256-color \
	--enable-everything \
	--enable-greek \
	--enable-languages \
	--enable-shared \
	--enable-smart-resize \
	--enable-ttygid \
	--enable-xgetdefault \
	--with-x
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	mandir="%{buildroot}%{_mandir}/man1"

%if %{?!_without_freedesktop:1}0
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		rxvt.desktop
%else
        %{__install} -D -m0644 rxvt.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/rxvt.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/BUGS doc/FAQ doc/README* doc/TODO doc/*.txt doc/*.html
%doc doc/menu/ doc/rxvt* doc/xterm.seq
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la
%{!?_without_freedesktop:%{_datadir}/applications/net-rxvt.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Utilities/rxvt.desktop}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 2.7.10-1
- Addded improved desktop file.

* Sun Oct 11 2003 Dag Wieers <dag@wieers.com> - 2.7.10-0
- Initial package. (using DAR)
