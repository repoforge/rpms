# $Id$
# Authority: shuff
# Upstream: <developers$prosody,im>

Summary: Lightweight XMPP server in Lua
Name: prosody
Version: 0.8.2
Release: 1%{?dist}
License: MIT
Group: Applications/Communications
URL: http://prosody.im/

Source: http://prosody.im/downloads/source/prosody-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: libidn-devel
BuildRequires: lua
# BuildRequires: luadbi
# BuildRequires: luaevent-prosody
BuildRequires: luaexpat
BuildRequires: luafilesystem
# BuildRequires: luasec
BuildRequires: luasocket
# BuildRequires: luazlib-brimworks
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: rpm-macros-rpmforge
Requires: lua
Requires: luaexpat
Requires: luafilesystem
Requires: luasocket
Requires(post): /usr/sbin/groupadd
Requires(post): /usr/sbin/useradd
Requires(preun): /usr/sbin/groupdel
Requires(preun): /usr/sbin/userdel

%description
Prosody is a modern flexible communications server for Jabber/XMPP written in
Lua. It aims to be easy to set up and configure, and light on resources. For
developers it aims to be easy to extend and give a flexible system on which to
rapidly develop added functionality, or prototype new protocols. 

%prep
%setup

%build
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_sharedstatedir}/prosody \
    --with-lua-lib=%{_libdir} \
    --require-config
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
if [ $1 -eq 1 ]; then
    /usr/sbin/groupadd -r prosody
    /usr/sbin/useradd -r -d %{_sharedstatedir}/prosody -g prosody -s /bin/false prosody
    exit 0
fi

%preun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel prosody
    /usr/sbin/groupdel prosody
    exit 0
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING DEPENDS HACKERS INSTALL README TODO doc/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_usr}/lib/prosody/
%{_sharedstatedir}/*
%config(noreplace) %{_sysconfdir}/prosody.cfg.lua
%dir %{_sysconfdir}/certs/
%{_sysconfdir}/certs/Makefile
%config(noreplace) %{_sysconfdir}/certs/localhost*
%config(noreplace) %{_sysconfdir}/certs/openssl.cnf


%changelog
* Tue Jun 28 2011 Steve Huff <shuff@vecna.org> - 0.8.2-1
- Initial package.
