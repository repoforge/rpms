# Authority: dag
# Upstream: Nicola Fragale <nicolafragale@libero.it>

Summary: Address book application.
Name: rubrica
Version: 1.0.10
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://digilander.iol.it/nfragale/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://digilander.libero.it/nfragale/download/rubrica/rubrica-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libgnomeui-devel >= 2.0, libxslt-devel >= 1.0, libmcrypt-devel

%description
An address book for GNOME. 

%prep
%setup

%build
#{__autoconf}
#{__automake}
%configure \
	--disable-install-schemas \
	--enable-nls
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/rubrica/

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
%doc AUTHORS ChangeLog COPYING CREDITS NEWS README TODO doc/examples.rub
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/rubrica/
%{_datadir}/pixmaps/rubrica/
%{_datadir}/applications/*.desktop

%changelog
* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 1.0.10-0
- Updated to release 1.0.10.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Updated to release 1.0.5.

* Sun May 25 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat May 10 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
