# Authority: dag

# Upstream: Marco Pesenti Gritti <mpeseng@tin.it>
#
### Doesn't compile with Soapbox because of the scrollkeeper bug
# Soapbox: 0

Summary: A GNOME web browser based on the mozilla rendering engine.
Name: epiphany
Version: 0.8.2
Release: 0
Group: Applications/Internet
License: GPL
URL: http://epiphany.mozdev.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://downloads.mozdev.org/epiphany/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: mozilla-devel >= 1.3, gtk2-devel, libbonoboui-devel >= 2.1.1
BuildRequires: epiphany-devel, scrollkeeper

Requires(post): scrollkeeper

%description
Epiphany is a GNOME web browser based on the mozilla rendering engine.
The name meaning: "An intuitive grasp of reality through something (as
an event) usually simple and striking"

%prep
%setup

%build
%configure \
	--enable-nautilus-view="yes" \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### FIXME: Don't know why anyone would want these header-files.
%{__rm} -rf %{buildroot}%{_includedir}

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

%changelog
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
