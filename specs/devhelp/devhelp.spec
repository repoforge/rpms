# $Id$
# Authority: dag
# Upstream: Mikael Hallendal <micke$imendio,com>

Summary: API document browser
Name: devhelp
Version: 0.9.1
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.imendio.com/projects/devhelp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/devhelp/0.9/devhelp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.3.1, libgnomeui-devel >= 2.2, gnome-vfs2-devel >= 2.2
BuildRequires: gtkhtml2-devel >= 2.0.0, intltool

%description
devhelp is an API document browser for GNOME.

%prep
%setup

%build
intltoolize
%configure \
	--disable-schemas-install \
	--with-html-widget="gtkhtml2"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/devhelp.schemas
%{_bindir}/devhelp*
%{_datadir}/applications/*.desktop
%{_datadir}/devhelp/
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_includedir}/devhelp-1.0/
%exclude %{_libdir}/libdevhelp-1.a
%exclude %{_libdir}/libdevhelp-1.la
%{_libdir}/libdevhelp-1.so.0.0.0
%{_libdir}/pkgconfig/libdevhelp-1.0.pc

%changelog
* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Updated to release 0.8.1.

* Sun Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Updated to release 0.7.

* Sun Apr 27 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
