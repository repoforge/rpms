# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

%define rname WindowMaker

Summary: A fast, feature rich Window manager.
Name: windowmaker
Version: 0.80.2
Release: 4
License: GPL
Group: User Interface/Desktops
URL: http://www.windowmaker.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://windowmaker.org/pub/source/release/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: XFree86-devel, libpng-devel, libjpeg-devel, libungif-devel 
BuildRequires: libtiff-devel, zlib-devel, gettext

Provides: %{rname}, %{rname}-libs, windowmanager
Obsoletes: %{rname}, %{rname}-libs

%description
Window Maker is an X11 window manager designed to give additional
integration support to the GNUstep Desktop Environment. In every way
possible, it reproduces the elegant look and feel of the NeXTSTEP[tm]
GUI. It is fast, feature rich, easy to configure, and easy to use. In
addition, Window Maker works with GNOME and KDE, making it one of the
most useful and universal window managers available.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{rname}-%{version}

%{__cat} <<EOF >windowmaker.xsession
#!/bin/sh
exec /etc/X11/xdm/Xsession wmaker
EOF

%build
export LINGUAS="$(cd po; echo *.po | sed -e 's|zh_TW.Big5.po||g; s|.po||g')"
%configure \
	--with-appspath="%{_libdir}/GNUstep" \
	--with-nlsdir="%{_datadir}/locale" \
	--enable-gnome \
	--enable-kde \
	--enable-modelock \
	--enable-openlook \
	--enable-usermenu
%{__make} %{?_smp_mflags}

### FIXME: Replace fixed /usr/lib by $(libdir). (Please fix upstream)
%{__perl} -pi.orig -e 's|/usr/lib/|\$(libdir)/|g' WPrefs.app/Makefile

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	NLSDIR="%{buildroot}%{_datadir}/locale"
%find_lang %{rname}
%find_lang WPrefs
%find_lang WINGs
%{__cat} WINGs.lang WPrefs.lang >> %{rname}.lang

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/
%{__install} -m0755 windowmaker.xsession "%{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Window Maker"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGFORM BUGS ChangeLog COPYING* FAQ* NEWS README* TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/X11/gdm/Sessions/*
%config %{_sysconfdir}/WindowMaker/
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/GNUstep/
%{_datadir}/WindowMaker/
%{_datadir}/WINGs/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 0.80.2-4
- Fixed the location of WPrefs from /etc/WindowMaker/WMState. (Hasan)

* Mon May 12 2003 Dag Wieers <dag@wieers.com> - 0.80.2-3
- Added "Window Maker" GDM Xsession entry. (Bert de Bruijn)

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 0.80.2-1
- Provide 'windowmanager'.
- Initial package. (using DAR)
