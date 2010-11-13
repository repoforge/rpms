# $Id$
# Authority: dag

### EL6 ships with yum-3.2.27-14.el6_0.1
### EL5 ships with yum-3.2.22-26.el5_5.1
# ExclusiveDist: el2 rh7

Summary: RPM installer/updater
Name: yum
Version: 1.0.3
### Do not update release > 1 as we do not want to replace CentOS yum
Release: 0.1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.dulug.duke.edu/yum/

Source: http://linux.duke.edu/projects/yum/download/1.0/yum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: rpm-python python >= 1.5.2
Requires: rpm-python >= 4.0.4 python >= 1.5.2  rpm >= 4.0.4
Prereq: /sbin/chkconfig, /sbin/service

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

%prep
%setup

### Clean up default yum configuration file
%{__cat} <<EOF >etc/yum.conf
[main]
cachedir=/var/cache/yum
debuglevel=2
logfile=/var/log/yum.log
pkgpolicy=newest
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add yum
/sbin/service yum condrestart &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del yum
	/sbin/service yum stop &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man5/yum.conf.5*
%doc %{_mandir}/man8/yum-arch.8*
%doc %{_mandir}/man8/yum.8*
%config(noreplace) %{_sysconfdir}/yum.conf
%config(noreplace) %{_sysconfdir}/cron.daily/yum.cron
%config %{_sysconfdir}/init.d/yum
%config %{_sysconfdir}/logrotate.d/yum
%{_bindir}/yum
%{_bindir}/yum-arch
%{_datadir}/yum/
%{_localstatedir}/cache/yum/

%changelog
* Fri Jun 16 2006 Dag Wieers <dag@wieers.com> - 1.0.3-0.1
- Cleaned up default yum.conf file. (Steve Glines)

* Mon Feb 20 2006 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Imported SPEC file from CentOS 2.

* Sat Feb 28 2004 John Newbigin <jn@it.swin.edu.au>
- Final version for CentOS-2

* Tue Dec 30 2003 John Newbigin <jn@it.swin.edu.au>
- CentOS-2

* Mon Sep  8 2003 Seth Vidal <skvidal@phy.duke.edu>
- brown paper-bag 1.0.3

* Mon Sep  8 2003 Seth Vidal <skvidal@phy.duke.edu>
- ver to 1.0.2

* Mon May 19 2003 Seth Vidal <skvidal@phy.duke.edu>
- ver to 1.0.1

* Mon Apr 28 2003 Seth Vidal <skvidal@phy.duke.edu>
- fix up for changes and fhs compliance

* Tue Mar 11 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump ver to 1.0
- fix conf file
- for rhl 7.3

* Sun Dec 22 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped to ver 0.9.4
- split spec file for rhl 7x vs 8

* Sun Oct 20 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped ver to 0.9.3

* Mon Aug 26 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped ver to 0.9.2

* Thu Jul 11 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped ver to 0.9.1

* Thu Jul 11 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped ver  to 0.9.0

* Thu Jul 11 2002 Seth Vidal <skvidal@phy.duke.edu>
- added rpm require

* Sun Jun 30 2002 Seth Vidal <skvidal@phy.duke.edu>
- 0.8.9

* Fri Jun 14 2002 Seth Vidal <skvidal@phy.duke.edu>
- 0.8.7

* Thu Jun 13 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped to 0.8.5

* Thu Jun 13 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped to 0.8.4

* Sun Jun  9 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped to 0.8.2
* Thu Jun  6 2002 Seth Vidal <skvidal@phy.duke.edu>
- First packaging
