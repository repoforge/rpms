# $Id$
# Authority: dag

### EL6 ships with yum-3.2.27-14.el6_0.1
### EL5 ships with yum-3.2.22-26.el5_5.1
# ExclusiveDist: el4

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: RPM installer/updater
Name: yum
Version: 2.4.2
### Do not update release > 1 as we do not want to replace CentOS yum
Release: 0.4%{?dist}
License: GPL
Group: System Environment/Base
Source: http://linux.duke.edu/projects/yum/download/2.4/yum-%{version}.tar.gz

URL: http://linux.duke.edu/yum/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, python
Requires: python, rpm-python, rpm >= 0:4.1.1
Requires: python-sqlite, urlgrabber, python-elementtree
Requires: libxml2-python
Prereq: /sbin/chkconfig, /sbin/service, coreutils

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
obsoletes=1
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add yum

%preun
if [ $1 -eq 0 ]; then
        /sbin/chkconfig --del yum
        /sbin/service yum stop &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL PLUGINS README TODO
%doc %{_mandir}/man5/yum.conf.5*
%doc %{_mandir}/man8/yum-arch.8*
%doc %{_mandir}/man8/yum-shell.8*
%doc %{_mandir}/man8/yum.8*
%config(noreplace) %{_sysconfdir}/yum.conf
%config(noreplace) %{_sysconfdir}/yum.repos.d/
%config(noreplace) %{_sysconfdir}/yum/
%config(noreplace) %{_sysconfdir}/cron.daily/yum.cron
%config(noreplace) %{_sysconfdir}/cron.weekly/yum.cron
%config %{_sysconfdir}/logrotate.d/yum
%config %{_sysconfdir}/rc.d/init.d/yum
%{_bindir}/yum
%{_bindir}/yum-arch
%{_datadir}/yum-cli/
%{python_sitelib}/repomd/
%{python_sitelib}/rpmUtils/
%{python_sitelib}/yum/
%{_localstatedir}/cache/yum/

%changelog
* Fri Jun 16 2006 Dag Wieers <dag@wieers.com> - 2.4.2-0.4
- Cleaned up default yum.conf file. (Steve Glines)

* Tue Feb 21 2006 Dag Wieers <dag@wieers.com> - 2.4.2-0.3
- Removed (CentOS) yumconf from requirements.

* Mon Feb 20 2006 Dag Wieers <dag@wieers.com> - 2.4.2-0
- Imported SPEC file from CentOS 4.

* Wed Feb  8 2006 Johnny Hughes <johnny@centos.org>
- rolled in all CentOS changes (the Apr 10 2005 entry)

* Sun Dec 18 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.4.2

* Wed Nov 30 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.4.1

* Sun Sep  4 2005 Johnny Hughes <johnny@centos.org>
- upgraded CentOS-4 to 2.4.0 (rerolled in the
  below CentOS changes into this version)

* Sun Aug 14 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.4.0

* Fri Aug  5 2005 Seth Vidal <skvidal@phy.duke.edu>
- back to libxml2-python req

* Fri Jul  8 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.3.4

* Tue Jun 14 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.3.3

* Sun Apr 10 2005 Johnny Hughes <johnny@centos.org>
- rolled in CentOS-4 specific changes (require
  centos-yumconf and install yum.conf)

* Wed Apr  6 2005 Seth Vidal <skvidal@phy.duke.edu>
- added python-elementtree dep, remove libxml2 dep

* Mon Apr  4 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.3.2

* Mon Mar 28 2005 Seth Vidal <skvidal@phy.duke.edu>
- add in the /etc/yum/*.yum yum shell files

* Mon Mar  7 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.3.1
- get rid of old obsoletes

* Fri Feb 25 2005 Gijs Hollestelle <gijs@gewis.nl>
- Require python-sqlite

* Fri Feb 25 2005 Seth Vidal <skvidal@phy.duke.edu>
- add yum.cron to weekly to clean packages

* Mon Feb 21 2005 Seth Vidal <skvidal@phy.duke.edu>
- new devel branch - 2.3.0

* Tue Jan 25 2005 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.13

* Sat Nov 27 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.12

* Wed Oct 27 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.11

* Tue Oct 19 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.10

* Mon Oct 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.9 - paper bag release

* Mon Oct 18 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.8

* Wed Oct 13 2004 Seth Vidal <skvidal@phy.duke.edu>
- update to 2.1.7
- re-include yum-arch w/deprecation notice

* Wed Oct  6 2004 Seth Vidal <skvidal@phy.duke.edu>
- mdcaching code and list changes
- 2.1.6

* Mon Oct  4 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.5
- lots of minor bugfixes and corrections

* Tue Sep 28 2004 Seth Vidal <skvidal@phy.duke.edu>
- 2.1.4

* Fri Sep  3 2004 Seth Vidal <skvidal@phy.duke.edu>
- big depsolver update

* Wed Sep  1 2004 Seth Vidal <skvidal@phy.duke.edu>
- more changes

* Tue Aug 31 2004 Seth Vidal <skvidal@phy.duke.edu>
- all new stuff for 2.1.X

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
