# $Id$
# Authority: dag
# Upstream: Massimiliano Ghilardi <max$Linuz,sns,it>

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}


### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Textmode windowing environment
Name: twin
Version: 0.5.1
Release: 0
License: GPL
Group: Applications/System
URL: http://linuz.sns.it/~max/twin/

Source: http://dl.sf.net/twin/twin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf, ncurses-devel, automake, gtk+-devel
BuildRequires: libtermcap-devel
%{?fc4:BuildRequires: libtool-ltdl-devel}
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Twin is a windowing environment with mouse support, window manager,
terminal emulator and networked clients, all inside a text display.

It supports a variety of displays:
* plain text terminals (any termcap/ncurses compatible terminal,
  Linux console, twin's own terminal emulator);
* X11, where it can be used as a multi-window xterm;
* itself (you can display a twin on another twin);
* twdisplay, a general network-transparent display client, used
  to attach/detach more displays on-the-fly.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/twin/{BUGS,COPYING*,INSTALL,README*,*.lsm,*.txt}
%{__rm} -rf %{buildroot}%{_datadir}/twin/docs/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog.txt COPYING* README* twin-current.lsm
%doc docs/*.txt docs/Compatibility docs/FAQ docs/Philosophy docs/Tutorial
%doc TODOS/TODO TODOS/twin-thoughts
%doc %{_mandir}/man?/*
%config %{_libdir}/twin/
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/TT/
%{_libdir}/*.so.*
%{_datadir}/twin/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/TT/
%{_includedir}/Tutf/
%{_includedir}/Tw/

%changelog
* Sun Sep 07 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sun Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.4.6-0
- Updated to release 0.4.6.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.4.5-0
- Initial package. (using DAR)
