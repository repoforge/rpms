# $Id$
# Authority: dag
# Upstream: Axel Kittenberger <axkibe$gmail,com>

Summary: Live syncing (mirroring) daemon
Name: lsyncd
Version: 2.0.2
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://code.google.com/p/lsyncd/

Source: http://lsyncd.googlecode.com/files/lsyncd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lua-devel

Requires: lua
Requires: rsync

%description
Lsyncd(1) watches a local directory trees event monitor interface 
(inotify). It aggregates and combines events for a few seconds and 
then spawns one (or more) process(es) to synchronize the changes. 
By default this is rsync(1). Lsyncd is thus a light-weight live mirror
solution that is comparatively easy to install not requiring new 
filesystems or blockdevices and does not hamper local filesystem 
performance.

%prep
%setup

%build
export LUA_LIBS="-llua -lm"
export LUA_CFLAGS="-I/usr/include/"
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%doc %{_defaultdocdir}/lsyncd/
%doc %{_mandir}/man1/lsyncd.1.gz
%{_bindir}/lsyncd

%changelog
* Tue Feb 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.2-1
- Updated to release 2.0.2 (thanks to Aleksandar Ivanisevic!)

* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
