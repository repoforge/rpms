# $Id$
# Authority: dag
# Upstream: Axel Kittenberger <axkibe$gmail,com>

Summary: Live syncing (mirroring) daemon
Name: lsyncd
Version: 2.0.2
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://code.google.com/p/lsyncd/

Source0: http://lsyncd.googlecode.com/files/lsyncd-%{version}.tar.gz
Source1: %{name}.init
Source2: %{name}.sysconfig

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lua-devel

Requires: /sbin/chkconfig
Requires: /sbin/service
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

%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop &>/dev/null || :
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%doc %{_defaultdocdir}/lsyncd/
%doc %{_mandir}/man1/lsyncd.1.gz
%{_bindir}/lsyncd
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Tue Mar 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.2-2
- Added an init script (thanks to Aleksandar Ivanisevic!)

* Tue Feb 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.0.2-1
- Updated to release 2.0.2 (thanks to Aleksandar Ivanisevic!)

* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
