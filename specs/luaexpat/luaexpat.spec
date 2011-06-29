# $Id$
# Authority: shuff
# Upstream: Kepler Project <info$keplerproject,org>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

%define lualibopts %(echo `pkg-config --libs lua`)

%define real_version 1.1

Summary: Expat extension for Lua
Name: luaexpat
Version: 1.1.0
Release: 1%{?dist}
License: MIT
Group: Applications/Development
URL: http://mathewwild.co.uk/projects/luaexpat/

Source: http://luaforge.net/frs/download.php/2469/luaexpat-1.1.tar.gz
Patch0: luaexpat-1.1.0_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: expat-devel >= 2.0.0
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1

%description
LuaExpat is a SAX XML parser based on the Expat library.

%prep
%setup -n %{name}-%{real_version}
%patch0

# fix the makefile
%{__perl} -pi -e "s|^PREFIX =.*$|PREFIX = %{_prefix}|;" config
%{__perl} -pi -e "s|^LUA_DIR=.*$|LUA_DIR= %{luadatadir}|;" config
%{__perl} -pi -e "s|^LUA_LIBDIR=.*$|LUA_LIBDIR= %{lualibdir}|;" config
%{__perl} -pi -e "s|^LUA_INC=.*$|LUA_INC= %{_includedir}|;" config
%{__perl} -pi -e "s|^EXPAT_INC=.*$|EXPAT_INC= %{_includedir}|;" config
%{__perl} -pi -e "s|^LUA_VERSION_NUM=.*$|LUA_VERSION_NUM= 501|;" config
%{__perl} -pi -e "s|^COMPAT_DIR=.*$|COMPAT_DIR= %{_includedir}|;" config
%{__perl} -pi -e "s|^LIB_OPTION=.*$|LIB_OPTION= %{lualibopts} -shared|;" config

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"

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
%{luadatadir}/*

%changelog
* Wed Jun 29 2011 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.
