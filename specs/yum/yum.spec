# $Id: yum.spec,v 1.2 2004/03/01 14:07:36 thias Exp $

# Which distro to make the default configuration for, defaults to 'rh'
%{?_with_yellowdog: %{expand: %%define distro yd}}
%{?_with_redhat: %{expand: %%define distro rh}}
%{!?distro: %{expand: %%define distro fd}}

# Defined as YYYYMMDD if this is a snapshot build
%define date 20040303

# Python name and version, use "--define 'python python2'"
%{!?python: %{expand: %%define python python}}
%define pyminver 2.2

Summary: YellowDog Updater Modified, an rpm package management utility
Name: yum
Version: 2.0.5
Release: 1%{?date:.%{date}}.%{distro}.fr
License: GPL
Group: System Environment/Base
URL: http://www.linux.duke.edu/projects/yum/
Source: http://www.dulug.duke.edu/yum/download/%{?date:daily/}2.0/%{name}-%{?date}%{!?date:%{version}}.tar.gz
Source11: yum-fd.conf
Source12: yum-yd.conf
Source13: yum-rh.conf
Source50: RPM-GPG-KEY.redhat
Source51: RPM-GPG-KEY.yellowdog
Source52: RPM-GPG-KEY.freshrpms
Requires(pre): /sbin/chkconfig, /sbin/service
Requires(post): /sbin/chkconfig, /sbin/service
Requires: rpm >= 4.1.1, %{python} >= %{pyminver}, rpm-python, libxml2-python
Requires: gnupg
BuildRequires: rpm-python, %{python} >= %{pyminver}, gettext
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded 
automatically prompting the user as necessary.

Available rpmbuild rebuild options :
--with : fedora (default) yellowdog redhat

%prep
%setup -q -n %{name}%{!?date:-%{version}}

%build
# Replace interpreter's name if it's not "python"
if [ "%{python}" != "python" ]; then
    find . -type f | \
        xargs perl -pi -e 's|/usr/bin/python|/usr/bin/%{python}|g'
    export PYTHON="%{python}"
fi
# Change the defaut debug level of the cron entry
perl -pi -e 's|-d 0|-d 1|g' etc/yum.cron
%configure 
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}
install -m 644 %{_sourcedir}/yum-%{distro}.conf %{buildroot}/etc/yum.conf
cp -a %{_sourcedir}/RPM-GPG-KEY* .

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add yum
/sbin/service yum condrestart >/dev/null 2>&1 || :
%ifarch ppc
# Import Yellow Dog gpg key if needed
rpm -q gpg-pubkey-aeb6b9c4-3cf4089e >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY.yellowdog
%else
# Import Red Hat gpg key if needed
rpm -q gpg-pubkey-db42a60e-37ea5438 >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY.redhat
%endif
# Import Freshrpms.net gpg key if needed
rpm -q gpg-pubkey-e42d547b-3960bdf1 >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY.freshrpms

%preun
if [ $1 -eq 0 ]; then
        /sbin/chkconfig --del yum
        /sbin/service yum stop >/dev/null 2>&1 || :
fi

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING TODO
%ifarch ppc
%doc RPM-GPG-KEY.yellowdog
%pubkey RPM-GPG-KEY.yellowdog
%else
%doc RPM-GPG-KEY.redhat
%pubkey RPM-GPG-KEY.redhat
%endif
%doc RPM-GPG-KEY.freshrpms
%pubkey RPM-GPG-KEY.freshrpms
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/cron.daily/%{name}.cron
%config %{_sysconfdir}/init.d/%{name}
%config %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-arch
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_localstatedir}/cache/%{name}

%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1.20040303.fr
- Update to today's snapshot.

* Mon Feb 23 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1.20040229.fr
- Update to today's snapshot.

* Sun Feb  1 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1.fr
- Update to 2.0.5.

* Wed Jan  7 2004 Matthias Saou <http://freshrpms.net/> 2.0.4-3.20040103.fr
- Update to the latest daily.
- Removed the rawhide configuration.
- Made fd the default instead of rh.
- Build as noarch as python files are .py instead of .pyc previously.

* Thu Dec 11 2003 Matthias Saou <http://freshrpms.net/> 2.0.4-2.20031205.fr
- Update to the latest daily.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 2.0.4-2.fr
- Added Fedora Linux support.
- Added gettext build dep.

* Tue Oct 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.4.

* Thu Oct  2 2003 Matthias Saou <http://freshrpms.net/>
- Added Yellow Dog Linux RPM-GPG-KEY file.
- Import RH key for all archs except ppc where YD one is imported instead.
- Added %%pubkey to tag gpg keys as such.

* Thu Sep 18 2003 Matthias Saou <http://freshrpms.net/>
- Updated the rawhide config.
- Added ruffpack (but disabled) to the yd config.
- Added automatic import of Red Hat and Freshrpms gpg keys if not present.

* Tue Sep  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.3.

* Mon Sep  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.2.

* Thu Aug 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 20030828.

* Mon Aug 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.1.

* Sun Aug 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to the latest snapshot - 20030810.

* Sat Aug  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to the latest snapshot - 20030809.

* Thu Aug  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to the latest snapshot - 20030807.
- Change the cron entry to debug level 1 in order for root to get mail.
- Simplified the default config based on the latest upstream one.

* Thu Jul 17 2003 Matthias Saou <http://freshrpms.net/>
- Added support for Red Hat Linux 7.x's "python2".

* Mon Jul 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0 final.

* Mon Jul  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.98 20030710.

* Mon Jul  7 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's daily release.

* Mon Jun 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.98.
- Added Red Hat Linux Rawhide config file.

* Sun May  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.97 for Red Hat Linux 9 and Yellow Dog Linux 3.0 at last.
- Added libxml2-python dep.

* Fri Mar 14 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Change configuration files to point to freshrpms.net yum repository.

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
