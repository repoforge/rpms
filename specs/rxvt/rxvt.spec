# $Id$
# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: color VT102 terminal emulator for the X Window System
Name: rxvt
Version: 2.7.10
Release: 0
Epoch: 4
License: GPL
Group: User Interface/Desktops
URL: http://www.rxvt.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/rxvt/rxvt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool
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

%{__cat} <<EOF >rxvt.desktop
[Desktop Entry]
Name=Rxvt Terminal
Comment=Small and fast X terminal application
Exec=rxvt
Icon=rterm.xpm
Type=Application
Terminal=false
Categories=GNOME;Application;System;Utility;TerminalEmulator;
StartupNotify=true
EOF

%build
#%{__autoconf} -l autoconf autoconf/configure.in > configure 
#chmod +x configure
#%{__cp} -f /usr/share/libtool/config.* autoconf

%configure \
	--prefix="%{_prefix}/X11R6" \
	--exec-prefix="%{_prefix}/X11R6" \
	--mandir="%{_prefix}/X11R6/man/man1" \
	--enable-shared \
	--enable-languages \
	--enable-greek \
	--enable-ttygid \
	--enable-mousewheel \
	--with-x \
	--with-xpm-includes="%{_includedir}/include/X11" \
	--with-xpm-library="%{_prefix}/X11R6/lib" \
	--with-xpm \
	--enable-utmp \
	--enable-wtmp \
	--disable-frills \
	--enable-xgetdefault \
	--enable-smart-resize \
	--enable-256-color
#	--with-term="rxvt" \
#	--disable-xgetdefault \

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir} \
			%{buildroot}%{_prefix}/X11R6/man/man1/ \
			%{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/ \
			%{buildroot}%{_prefix}/X11R6/lib/X11/{ja,ko,zh_CN,zh_TW}/{app-defaults,rxvt}/
%makeinstall \
	bindir="%{buildroot}%{_prefix}/X11R6/bin" \
	mandir="%{buildroot}%{_prefix}/X11R6/man/man1"

%{__install} -d -m0755 %{buildroot}%{_docdir}/rxvt-%{version}/menu/
%{__install} -m0644 doc/menu/* %{buildroot}%{_docdir}/rxvt-%{version}/menu/

%if %{dfi}
        %{__install} -D -m0644 rxvt.desktop %{buildroot}%{_datadir}/gnome/apps/Utilities/rxvt.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		rxvt.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/BUGS doc/FAQ doc/README.* doc/TODO doc/changes.txt doc/menu/ doc/rxvt* doc/xterm.seq
%doc %{_prefix}/X11R6/man/man?/*
%{_prefix}/X11R6/bin/*
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la
%if %{dfi}
        %{_datadir}/gnome/apps/Utilities/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h


%changelog
* Sun Oct 11 2003 Dag Wieers <dag@wieers.com> - 2.7.10-0
- Initial package. (using DAR)
