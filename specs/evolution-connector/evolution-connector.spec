# ExcludeDist: el4

%define plibdir %(pkg-config evolution-shell --variable=privlibdir 2>/dev/null)

Summary: Evolution Connector for Microsoft(tm) Exchange server.
Name: evolution-connector
Version: 1.4.7.2
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.novell.com/products/connector/

Source: http://ftp.gnome.org/pub/GNOME/sources/ximian-connector/1.4/ximian-connector-%{version}.tar.bz2
Patch0: evolution-connector-dynamic-ldap.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: evolution-devel >= 1.4.5
BuildRequires: openldap-devel, gettext, perl-XML-Parser
Requires: evolution >= 1.4.5
Obsoletes: ximian-connector <= %{version}
Provides: ximian-connector = %{version}-%{release}

%description
With the Connector for Microsoft Exchange installed, Evolution functions as
an Exchange client, enabling users to become full participants in company-wide
group scheduling and other collaborative tasks. Linux and Solaris users can
access public folders, Global Address Lists, email, calendar, task lists,
and group scheduling information.

%prep
%setup -n ximian-connector-%{version}
%patch0 -p1

%build
%configure \
	--with-openldap \
	--with-static-ldap="no"
%{__make} %{?_smp_mflags} \
	LDFLAGS="-rpath %{plibdir}"

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang ximian-connector-1.4
find docs -type f -name "Makefile*" -exec rm -f {} \;

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/apps_evolution_exchange.schemas &>/dev/null || :

%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/apps_evolution_exchange.schemas &>/dev/null || :

%files -f ximian-connector-1.4.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS docs/*
%{_sysconfdir}/gconf/schemas/apps_evolution_exchange.schemas
%{_bindir}/ximian-connector-setup
%exclude %{_libdir}/evolution/*/camel-providers/libcamelexchange.*a
%{_libdir}/evolution/*/camel-providers/libcamelexchange.*
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/evolution/*/evolution-exchange-storage
%{_datadir}/evolution/*/*/*.png
%{_datadir}/ximian-connector/

%changelog
* Fri Aug 27 2004 Dag Wieers <dag@wieers.com> - 1.4.7.2-1
- Initial package. (using DAR)
