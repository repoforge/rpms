# $Id$
# Authority: dag
# Upstream: Michael K, Johnson <ttywatch$danlj,org>

Summary: Log output of arbitrarily many devices
Name: ttywatch
Version: 0.14
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.danlj.org/mkj/ttywatch/

Source: http://www.danlj.org/mkj/ttywatch/ttywatch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: lockdev-devel, /usr/bin/install, pkgconfig, glib2-devel
Requires: /sbin/chkconfig

%description
ttywatch was originally designed to log serial console output from
lots of Linux machines on a single monitor machine.  It handles
log rotation correctly and can be configured both in a configuration
file and on the command line -- and you can mix-and-match at your
convenience.  It can be set up to allow users to interact via the
network with any of the ports being logged.  It can also log output
in arbitrary ways via modules, which can be built with the
ttywatch-devel package.

%prep
%setup

%build
%{__make} %{_smp_mflags} \
	OPTFLAGS="%{optflags} -I/usr/include"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	TOPDIR="%{buildroot}"

%post
/sbin/chkconfig --add ttywatch

%preun
if [ $1 -eq 0 ]; then
	/sbin/service ttywatch stop &>/dev/null || :
	/sbin/chkconfig --del ttywatch
fi

%postun
/sbin/service ttywatch condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING TODO
%doc %{_mandir}/man8/ttywatch.8*
%config %{_initrddir}/ttywatch
%config(noreplace) %{_sysconfdir}/ttywatch.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/ttywatch
%{_sbindir}/ttywatch
%{_includedir}/ttywatch.h

%defattr(-, root, root, 0700)
%dir %{_localstatedir}/log/ttywatch/

%changelog
* Sun Dec 26 2004 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Tue Mar 30 2004 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
