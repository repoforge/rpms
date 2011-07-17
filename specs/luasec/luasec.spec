# $Id$
# Authority: shuff
# Upstream: Bruno Silverste <bruno.silvestre$gmail,com>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

Summary: TLS/SSL support for Lua
Name: luasec
Version: 0.4.1
Release: 1%{?dist}
License: MIT
Group: Applications/Development
URL: http://www.inf.puc-rio.br/~brunoos/luasec/

Source: http://www.inf.puc-rio.br/~brunoos/luasec/download/luasec-%{version}.tar.gz
Patch0: luasec-0.4.1_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: luasocket
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1
Requires: luasocket

%description
LuaSec is a binding for OpenSSL library to provide TLS/SSL communication. It
takes an already established TCP connection and creates a secure session
between the peers.

%prep
%setup
%patch0

# fix the makefile
%{__perl} -pi -e "s|^LUAPATH=.*$|LUAPATH=%{luadatadir}|;" Makefile
%{__perl} -pi -e "s|^LUACPATH=.*$|LUACPATH=%{lualibdir}|;" Makefile

%build
%{__make} %{?_smp_mflags} linux

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG INSTALL LICENSE samples/
%{lualibdir}/*
%{luadatadir}/*

%changelog
* Thu Jul 14 2011 Steve Huff <shuff@vecna.org> - 0.4.1-1
- Initial package.
