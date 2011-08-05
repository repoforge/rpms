# $Id$
# Authority: shuff
# Upstream: Kepler Project <info$keplerproject,org>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

%define lualibopts %(echo `pkg-config --libs lua`)

Summary: Filesystem management extension for Lua
Name: luafilesystem
Version: 1.5.0
Release: 2%{?dist}
License: MIT
Group: Applications/Development
URL: http://keplerproject.github.com/luafilesystem/

Source: https://github.com/downloads/keplerproject/luafilesystem/luafilesystem-%{version}.tar.gz
Patch0: luafilesystem-1.5.0_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: perl
BuildRequires: pkgconfig
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1

%description
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory
structure and file attributes.

%prep
%setup
%patch0

# fix the makefile
%{__perl} -pi -e "s|^PREFIX =.*$|PREFIX = %{_prefix}|;" config
%{__perl} -pi -e "s|^LUA_LIBDIR=.*$|LUA_LIBDIR= %{lualibdir}|;" config
%{__perl} -pi -e "s|^LUA_INC=.*$|LUA_INC= %{_includedir}|;" config
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

%changelog
* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 1.5.0-2
- Captured missing pkgconfig dependency.

* Wed Jun 29 2011 Steve Huff <shuff@vecna.org> - 1.1.0-1
- Initial package.
