# $Id$

# Authority: dries

Summary: rpm build system
Name: pydar2
Version: 0.041
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://dries.ulyssis.org/rpm/pydar2/

BuildArch: noarch
Source: http://dries.ulyssis.org/rpm/pydar2/pydar2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-log4py, rpm-build

%description
Pydar2 is a distributed build system for rpm packages. It allows you to
build spec files from multiple spec repositories (spec files in svn, cvs, ..)
for multiple distribution/architectures on multiple computers with one
central queue. It's possible to automatically queue new builds and you can
alter most of the behaviour with scripts.

Pydar2 is not yet finished. It can be used but it's far from userfriendly.
The slave-buildserver uses sudo and the network communication between the
programs is not encrypted, so i suggest you only use it on a private network
with only users which you trust.

%package master
Summary: pydar2 master server
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: spectool

%package client
Summary: pydar2 client
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%package slave
Summary: pydar2 slave
Group: Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: yum, sudo

%package dries
Summary: scripts which generate dries.ulyssis.org/rpm
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description master
The master build server keeps the central queue of commands (spec files
which have to be build), a checkout of all the spec repositories and
information about users, slave build machines and targets.

%description client
The client program allows you to add new commands to the queue.

%description slave
The slave build server gets commands from the master and builds rpm
packages.

Warning: the slave build server currently uses sudo for certain commands.

%description dries
This package contains some scripts which are rpmforge/dries specific and
which can be used to customize pydar2 so it builds rpmforge packages.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/howto.txt
%{_datadir}/pydar2/pydar
%dir %{_sysconfdir}/pydar2


%files master
%defattr(-, root, pydar2master, 0740)
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/master.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/specrepositories.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/targets.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/accounts.conf
%config(noreplace) %{_sysconfdir}/pydar2/rpmforgeacceptcommandconfig/excluded
%config(noreplace) %{_sysconfdir}/pydar2/rpmforgeacceptcommandconfig/excludedauthoritytags
%config(noreplace) %{_sysconfdir}/pydar2/rpmforgeacceptcommandconfig/temporarilyexcluded
%defattr(-, pydar2master, pydar2master, 0700)
%dir %{_var}/lib/pydar2/specrepos
%defattr(-, pydar2master, pydar2master, 0755)
%dir %{_var}/lib/pydar2/masterwebroot
%defattr(-, root, root, 0755)
%dir %{_var}/lib/pydar2
%{_datadir}/pydar2/sql
%dir %{_datadir}/pydar2/scripts
%{_datadir}/pydar2/pydar-buildserver-master.py
%{_datadir}/pydar2/pydar-master-autoqueue.py
%{_datadir}/pydar2/pydar-master-update.py
%{_datadir}/pydar2/pydar-master-movecommandresults.py
%{_datadir}/pydar2/pydar-master-targetupdate.py
%{_datadir}/pydar2/log4py.conf
%{_bindir}/pydar-buildserver-master
%{_bindir}/pydar-master-autoqueue
%{_bindir}/pydar-master-movecommandresults
%{_bindir}/pydar-master-update
%{_bindir}/pydar-master-targetupdate

%files dries
%defattr(-, root, root, 0755)
%{_datadir}/pydar2/dries
%{_datadir}/pydar2/scripts/*.py

%files slave
%defattr(-, root, pydar2slave, 0740)
%config(noreplace) %{_sysconfdir}/pydar2/slave.conf
%dir %{_sysconfdir}/pydar2/yum
%config(noreplace) %{_sysconfdir}/pydar2/yum/*.conf
%defattr(-, pydar2slave, pydar2slave, 0740)
%dir %{_var}/lib/pydar2/slavedataroot
%dir %{_var}/lib/pydar2/roots
%dir %{_var}/lib/pydar2/yum
%defattr(-, root, root, 0755)
%{_datadir}/pydar2/pydar-buildserver-slave.py
%{_bindir}/pydar-buildserver-slave

%files client
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/pydar2/client.conf
%{_datadir}/pydar2/pydar-remote.py
%{_bindir}/pydar-remote

%pre
/usr/sbin/groupadd pydar2master || :
/usr/sbin/groupadd pydar2slave || :
/usr/sbin/useradd -M -g pydar2master pydar2master || :
/usr/sbin/useradd -M -g pydar2slave pydar2slave || :

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.041-1.2
- Rebuild for Fedora Core 5.

* Fri Jul 22 2005 Dries Verachtert <dries@ulyssis.org> 0.033-1
- Update to release 0.033.

* Mon Jun 27 2005 Dries Verachtert <dries@ulyssis.org> 0.026-1
- Update to release 0.026.

* Tue Jun 14 2005 Dries Verachtert <dries@ulyssis.org> 0.023-1
- Update to release 0.023.

* Fri Jun 10 2005 Dries Verachtert <dries@ulyssis.org> 0.022-1
- Update, bash scripts in /usr/bin added.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> 0.021-1
- Update, most of the functionality seems to work.

* Wed May 25 2005 Dries Verachtert <dries@ulyssis.org> 0.011-1
- Update

* Sat May 14 2005 Dries Verachtert <dries@ulyssis.org> 0.007-1
- Update

* Tue May 9 2004 Dries Verachtert <dries@ulyssis.org> 0.004-1
- this version actually works with different buildmachines

* Tue Apr 28 2004 Dries Verachtert <dries@ulyssis.org> 0.002-1
- update

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
