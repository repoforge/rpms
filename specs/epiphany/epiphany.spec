# $Id$
# Authority: dag
# Upstream: Marco Pesenti Gritti <mpeseng$tin,it>

%define mversion %(rpm -q mozilla-devel --qf '%{RPMTAG_EPOCH}:%{RPMTAG_VERSION}' | tail -1)

Summary: Web browser based on the mozilla rendering engine
Name: epiphany
Version: 1.2.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.gnome.org/projects/epiphany/

Source: http://ftp.gnome.org/pub/GNOME/sources/epiphany/1.2/epiphany-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mozilla-devel = %{mversion}, gtk2-devel, libbonoboui-devel >= 2.1.1
BuildRequires: scrollkeeper, nautilus

Requires: mozilla = %{mversion}
Requires(post): scrollkeeper

%description
Epiphany is a GNOME web browser based on the mozilla rendering engine.
The name meaning: "An intuitive grasp of reality through something (as
an event) usually simple and striking".

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
	--enable-nautilus-view="yes" \
	--enable-compile-warnings="no" \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README TODO
%doc %{_datadir}/gnome/help/epiphany/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop
%{_datadir}/epiphany/
%{_datadir}/omf/epiphany/
%{_datadir}/pixmaps/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/epiphany-1.0/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.5-1.2
- Rebuild for Fedora Core 5.

* Thu May 20 2004 Dag Wieers <dag@wieers.com> - 1.2.5-1
- Updated to release 1.2.5.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.0.7-1
- Rebuild against mozilla-1.6.

* Thu Jan 22 2004 Dag Wieers <dag@wieers.com> - 1.0.7-0
- Updated to release 1.0.7.

* Sat Nov 29 2003 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Rebuild against mozilla-1.5.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Updated to release 1.0.6.

* Thu Nov 06 2003 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Updated to release 1.0.5.

* Tue Oct 28 2003 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Rebuild against mozilla-1.5.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.0.4-0
- Updated to release 1.0.4.

* Thu Oct 16 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Updated to release 1.0.3.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat Oct 04 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Updated to release 1.0.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.9.3-0
- Updated to release 0.9.3.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Tue Jul 15 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Wed Jul 02 2003 Dag Wieers <dag@wieers.com> - 0.7.3-2
- Rebuild against mozilla-1.4.
- And now for real.

* Sun Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.7.3-0
- Updated release to 0.7.3.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated release to 0.7.2.
- Updated release to 0.7.1.

* Sat Jun 07 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated release to 0.7.0.

* Mon May 19 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated release to 0.6.1.

* Mon May 12 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
