# $Id$
# Authority: matthias
### Skip this package for dag's repo
# Tag: rft


# Which distro to make the default configuration for
%{?!dist:%{expand: %%define distro fd}}
%{?fc3:%{expand: %%define distro fd}}
%{?fc2:%{expand: %%define distro fd}}
%{?fc1:%{expand: %%define distro fd}}
%{?rh9:%{expand: %%define distro rh}}
%{?rh8:%{expand: %%define distro rh}}
%{?rh7:%{expand: %%define distro rh}}
%{?yd3:%{expand: %%define distro yd}}

# Defined as YYYYMMDD if this is a snapshot build
#define date 20040416

# Python name and version, use "--define 'python python2'"
%{!?python: %{expand: %%define python python}}
%define pyminver 2.2

Summary: YellowDog Updater Modified, an rpm package management utility
Name: yum
Version: 2.0.7
Release: 3%{?date:.%{date}}%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.linux.duke.edu/projects/yum/
Source: http://linux.duke.edu/projects/yum/download/%{?date:daily/}2.0/%{name}-%{?date}%{!?date:%{version}}.tar.gz
Source11: yum-fd.conf
Source12: yum-yd.conf
Source13: yum-rh.conf
Source50: RPM-GPG-KEY-redhat
Source51: RPM-GPG-KEY-yellowdog
Source52: RPM-GPG-KEY-freshrpms
Source53: RPM-GPG-KEY-fedora
Requires(post): /sbin/chkconfig, /sbin/service, rpm
Requires(preun): /sbin/chkconfig, /sbin/service
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
%setup -n %{name}%{!?date:-%{version}}


%build
# Replace interpreter's name if it's not "python"
if [ "%{python}" != "python" ]; then
    find . -type f | \
        xargs %{__perl} -pi -e 's|/usr/bin/python|/usr/bin/%{python}|g'
    export PYTHON="%{python}"
fi
# Change the defaut debug level of the cron entry
%{__perl} -pi -e 's|-d 0|-d 1|g' etc/yum.cron
%configure
%{__make}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%find_lang %{name}
%{__install} -p -m0644 %{_sourcedir}/yum-%{distro}.conf %{buildroot}/etc/yum.conf
%{__cp} -ap %{SOURCE50} %{SOURCE51} %{SOURCE52} %{SOURCE53} .


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/chkconfig --add yum
/sbin/service yum condrestart >/dev/null 2>&1 || :
%if %{distro} == yd
# Import Yellow Dog gpg key if needed
rpm -q gpg-pubkey-aeb6b9c4-3cf4089e >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-yellowdog
%elseif %{distro} == rh
# Import Red Hat gpg key if needed
rpm -q gpg-pubkey-db42a60e-37ea5438 >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-redhat
%elseif %{distro} == fd
# Import Fedora gpg key if needed
rpm -q gpg-pubkey-4f2a6fd2-3f9d9d3b >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-fedora
%endif
# Import Freshrpms.net gpg key if needed
rpm -q gpg-pubkey-e42d547b-3960bdf1 >/dev/null 2>&1 || \
    rpm --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-freshrpms
# We don't want a possible error to leave the previous package installed
exit 0

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del yum
    /sbin/service yum stop >/dev/null 2>&1 || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%doc RPM-GPG-KEY-freshrpms
%if %{distro} == yd
%doc RPM-GPG-KEY-yellowdog
#%pubkey RPM-GPG-KEY-yellowdog
#%pubkey RPM-GPG-KEY-freshrpms
%elseif %{distro} == rh
%doc RPM-GPG-KEY-redhat
%{?rh9%pubkey RPM-GPG-KEY-freshrpms}
%{?rh9:%pubkey RPM-GPG-KEY-redhat}
%elseif %{distro} == fd
%doc RPM-GPG-KEY-fedora
%{?fc2:%pubkey RPM-GPG-KEY-freshrpms}
%{?fc1:%pubkey RPM-GPG-KEY-freshrpms}
%{?fc2:%pubkey RPM-GPG-KEY-fedora}
%{?fc1:%pubkey RPM-GPG-KEY-fedora}
%endif
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
* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-3
- Fix gpgcheck in yum.conf.
- Import the Fedora key on Fedora Core.
- Updated the source's URL.
- Renamed the public key files to be consistent with the Red Hat naming.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-2
- Increased the release to take precedence over the default FC2 yum package.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 2.0.7-0
- Update to 2.0.7 at last.

* Fri Apr 30 2004 Matthias Saou <http://freshrpms.net/> 2.0.6-1.20040416
- Update to 20040416 snapshot.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 2.0.6-1
- Update to 2.0.6.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1.20040303
- Update to today's snapshot.

* Mon Feb 23 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1.20040229
- Update to today's snapshot.

* Sun Feb  1 2004 Matthias Saou <http://freshrpms.net/> 2.0.5-1
- Update to 2.0.5.

* Wed Jan  7 2004 Matthias Saou <http://freshrpms.net/> 2.0.4-3.20040103
- Update to the latest daily.
- Removed the rawhide configuration.
- Made fd the default instead of rh.
- Build as noarch as python files are .py instead of .pyc previously.

* Thu Dec 11 2003 Matthias Saou <http://freshrpms.net/> 2.0.4-2.20031205
- Update to the latest daily.

* Thu Oct 30 2003 Matthias Saou <http://freshrpms.net/> 2.0.4-2
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
