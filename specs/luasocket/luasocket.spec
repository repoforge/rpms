# $Id$
# Authority: shuff
# Upstream: Diego Nehab <diego$impa,br>

%define luaversion %(echo `pkg-config --variable=V lua`)
%define lualibdir %{_libdir}/lua/%{luaversion}
%define luadatadir %{_datadir}/lua/%{luaversion}

Summary: Network socket extension for Lua
Name: luasocket
Version: 2.0.2
Release: 1%{?dist}
License: MIT
Group: Applications/Development
URL: http://w3.impa.br/~diego/software/luasocket/

Source: http://luaforge.net/frs/download.php/2664/luasocket-2.0.2.tar.gz
Patch0: luasocket-2.0.2_destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: lua-devel >= 5.1
BuildRequires: make
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: lua >= 5.1

%description
LuaSocket is a Lua extension library that is composed by two parts: a C core
that provides support for the TCP and UDP transport layers, and a set of Lua
modules that add support for functionality commonly needed by applications that
deal with the Internet.

The core support has been implemented so that it is both efficient and simple
to use. It is available to any Lua application once it has been properly
initialized by the interpreter in use. The code has been tested and runs well
on several Windows and Unix platforms.

Among the support modules, the most commonly used implement the SMTP (sending
e-mails), HTTP (WWW access) and FTP (uploading and downloading files) client
protocols. These provide a very natural and generic interface to the
functionality defined by each protocol. In addition, you will find that the
MIME (common encodings), URL (anything you could possible want to do with one)
and LTN12 (filters, sinks, sources and pumps) modules can be very handy. 

%prep
%setup
%patch0

# fix the makefile
%{__perl} -pi -e "s|^INSTALL_TOP_SHARE=.*$|INSTALL_TOP_SHARE=%{luadatadir}|;" config
%{__perl} -pi -e "s|^INSTALL_TOP_LIB=.*$|INSTALL_TOP_LIB=%{lualibdir}|;" config

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
%doc LICENSE NEW README doc/ samples/
%{lualibdir}/*
%{luadatadir}/*

%changelog
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 2.0.2-1
- Initial package.
