# $Id$
# Authority: dag

### EL6 ships with yum-3.2.27-14.el6_0.1
### EL5 ships with yum-3.2.22-26.el5_5.1
# ExclusiveDist: rh9 el3

Summary: RPM installer/updater
Name: yum
Version: 2.0.8
### Do not update release > 1 as we do not want to replace CentOS yum
Release: 0.1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.dulug.duke.edu/yum/

Source: http://linux.duke.edu/projects/yum/download/2.0/yum-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, python
Requires: python, rpm-python, rpm >= 0:4.1.1, libxml2-python
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
distroverpkg=redhat-release
tolerant=1
exactarch=1
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%find_lang %{name}

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

%files -f %{name}.lang
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
* Fri Jun 16 2006 Dag Wieers <dag@wieers.com> - 2.0.8-0.1
- Cleaned up default yum.conf file. (Steve Glines)

* Mon Feb 20 2006 Dag Wieers <dag@wieers.com> - 2.0.8-0
- Imported SPEC file from CentOS 3.

* Wed Jan 05 2005 Lance Davis <lance@centos.org>
- keep copy of conf file if symlink

* Sun Dec 19 2004 Lance Davis <lance@centos.org>
- modified yum.conf for centos-3.4

* Tue Sep 14 2004 Seth Vidal <skvidal@phy.duke.edu>
- fixes for yum.conf to be picked up

* Wed Feb 18 2004 Lance Davis <lance@caosity.org>
- adjusted for centos

* Thu Feb  5 2004 Pasi Pirhonen <upi@iki.fi>
- replace yum.conf w/ symlink to file in tao-yumconf
- augment gpgcheck error message w/ Tao-specific info

* Sat Jan 31 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.0.5


* Sun Oct 19 2003 Seth Vidal <skvidal@phy.duke.edu>
- 2.0.4

* Mon Sep  8 2003 Seth Vidal <skvidal@phy.duke.edu>
- brown paper-bag 2.0.3

* Sun Sep  7 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump to 2.0.2

* Fri Aug 15 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump to 2.0.1

* Sun Jul 13 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump to 2.0

* Sat Jul 12 2003 Seth Vidal <skvidal@phy.duke.edu>
- made yum.cron config(noreplace)

* Sat Jun  7 2003 Seth Vidal <skvidal@phy.duke.edu>
- add stubs to spec file for rebuilding easily with custom yum.conf and
- yum.cron files

* Sat May 31 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump to 1.98

* Mon Apr 21 2003 Seth Vidal <skvidal@phy.duke.edu>
- bump to 1.97

* Wed Apr 16 2003 Seth Vidal <skvidal@phy.duke.edu>
- moved to fhs compliance
- ver to 1.96

* Mon Apr  7 2003 Seth Vidal <skvidal@phy.duke.edu>
- updated for 1.95 betaish release
- remove /sbin legacy
- no longer starts up by default
- do the find_lang thing

* Sun Dec 22 2002 Seth Vidal <skvidal@phy.duke.edu>
- bumped ver to 0.9.4
- new spec file for rhl 8.0

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
