# Authority: dag

Summary: A GNOME gnupg interface.
Name: seahorse
Version: 0.7.3
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://seahorse.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.sourceforge.net/pub/sourceforge/seahorse/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gpgme-devel >= 0.3.14
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
Seahorse is a GNOME interface for gnupg.
It uses gpgme as the backend.

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

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper
%{__rm} -f %{buildroot}%{_libdir}/bonobo/*.a \
		%{buildroot}%{_libdir}/bonobo/*.la

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/seahorse/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/bonobo/*.so
%{_libdir}/bonobo/servers/*.server
%{_datadir}/applications/*.desktop
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_datadir}/mime-info/*
%{_datadir}/omf/seahorse/
%{_datadir}/pixmaps/*
%{_datadir}/seahorse/

%changelog
* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Updated to release 0.6.3.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
