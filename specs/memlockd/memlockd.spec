# $Id$
# Authority: dag
# Upstream: Russell Coker <russell$coker,com,au>

### FIXME: Add sysv scripts for RHEL

Summary: Daemon to lock files into memory
Name: memlockd
Version: 0.05
Release: 1%{?dist}
License: GPL
Group: Applications/
URL: http://www.coker.com.au/memlockd/

#Source: http://www.coker.com.au/memlockd/memlockd_%{version}.tar.gz
Source: http://ftp.de.debian.org/debian/pool/main/m/memlockd/memlockd_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Memlockd is a daemon that locks files into memory. Then if a machine starts
paging heavily the chance of being able to login successfully is significantly
increased.

The default configuration will lock all the files needed for login to a Debian
GNU/Linux system via the console or via ssh.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 memlockd %{buildroot}%{_sbindir}/memlockd
%{__install} -Dp -m0644 memlockd.8 %{buildroot}%{_mandir}/man8/memlockd.8
%{__install} -Dp -m0644 memlockd.cfg %{buildroot}%{_sysconfdir}/memlockd.cfg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changes.txt memlockd.cfg
%doc %{_mandir}/man8/memlockd.8*
%config %{_sysconfdir}/memlockd.cfg
%{_sbindir}/memlockd

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
