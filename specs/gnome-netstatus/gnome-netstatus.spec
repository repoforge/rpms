# Authority: dag
# Upstream: Mark McLoughlin <mark@skynet.ie>

Summary: Network interface status applet.
Name: gnome-netstatus
Version: 0.16
Release: 0
License: GPL
Group: Applications/Internet
URL: http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-netstatus/%{version}/gnome-netstatus-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
gnome-netstatus is a network interface status applet.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gnome-netstatus/
%{_datadir}/icons/gnome-netstatus/
%{_datadir}/pixmaps/*

%changelog
* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> -  0.16-0
- Updated to release 0.16.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> -  0.14-0
- Updated to release 0.14.

* Thu Jan 15 2004 Dag Wieers <dag@wieers.com> -  0.13-0
- Updated to release 0.13.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> -  0.12-0
- Updated to release 0.12.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> -  0.11-0
- Updated to release 0.11.

* Thu Jun 12 2003 Dag Wieers <dag@wieers.com> -  0.10-0
- Updated to release 0.10.

* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> -  0.9-0
- Initial package. (using DAR)
