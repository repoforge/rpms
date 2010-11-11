# $Id$
# Authority: dag
# Upstream: Noah Levitt <nlevitt$columbia,edu>

### EL6 ships with gucharmap-2.28.2-2.el6
### EL5 ships with gucharmap-1.8.0-1.fc6
# ExclusiveDist: rh6 el2 rh7 rh8 rh9 el3

Summary: Unicode/ISO10646 character map and font viewer
Name: gucharmap
Version: 1.2.0
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://gucharmap.sourceforge.net/

Source: http://ftp.gnome.org/pub/gnome/sources/gucharmap/1.0/gucharmap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.2.0
### Needed to know if we should link gnome-character-map
BuildRequires: gnome-utils

%description
gucharmap is a Unicode/ISO10646 character map and font viewer.

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
%configure \
	--disable-dependency-tracking \
	--disable-gtk-immodules
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Remove gnome-character-map link from buildroot if it is in gnome-utils
[ -e %{_bindir}/gnome-character-map ] && %{__rm} -f %{buildroot}%{_bindir}/gnome-character-map

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_libdir}/gtk-2.0/2.2.0/immodules/*.a \
		%{buildroot}%{_libdir}/gtk-2.0/2.2.0/immodules/*.la

%post
gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
scrollkeeper-update -q || :

%postun
gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING* README TODO
%doc %{_datadir}/gnome/help/gucharmap/
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/gtk-2.0/*/immodules/*.so
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/gucharmap/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/gucharmap/
#exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.0-0.2
- Rebuild for Fedora Core 5.

* Sat Nov 22 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Updated to release 1.0.0.

* Fri Aug 22 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Updated to release 0.9.0.

* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Wed Jun 04 2003 Dag Wieers <dag@wieers.com> - 0.6.1.20030604-0
- Updated to release 0.6.1.20030604.

* Mon May 19 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Tue Mar 25 2003 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Added extra documents.

* Tue Mar 18 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Initial package. (using DAR)
