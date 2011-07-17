# $Id$
# Authority: shuff
# Upstream: Kepler Project <info$keplerproject,org>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

Summary: LDAP client library for Lua
Name: lualdap
Version: 1.1.0
Release: 1%{?dist}
License: MIT
Group: Applications/Development
URL: http://www.keplerproject.org/lualdap/

Source: http://luaforge.net/frs/download.php/2998/lualdap-%{version}.tar.gz
Patch0: lualdap-1.1.0_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: openldap-devel
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1

%description
LuaLDAP is a simple interface from Lua to an LDAP client, in fact it is a bind
to OpenLDAP or to ADSI. It enables a Lua program to:

* Connect to an LDAP server;
* Execute any operation (search, add, compare, delete, modify and rename);
* Retrieve entries and references of the search result.

%prep
%setup
%patch0

# fix the makefile
%{__perl} -pi -e "s|^LUA_LIBDIR=.*$|LUA_LIBDIR=%{lualibdir}|;" config
%{__perl} -pi -e "s|^LUA_INC=.*$|LUA_INC=%{_includedir}|;" config
%{__perl} -pi -e "s|^OPENLDAP_INC=.*$|OPENLDAP_INC=%{_includedir}|;" config
%{__perl} -pi -e "s|^LUA_VERSION_NUM=.*$|LUA_VERSION_NUM=510|;" config

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README doc/us/*
%{lualibdir}/*

%changelog
* Sun Jul 17 2011 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.
