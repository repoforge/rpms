# $Id$
# Authority: matthias

# ExclusiveDist: el2 rh7 yd2 yd3

# Which distro to make the default configuration for, defaults to 'rh'
%{?_with_yd: %{expand: %%define distro yd}}
%{!?distro: %{expand: %%define distro rh}}

# Which release version and arch
%{!?distrover: %{expand: %%define distrover 7.3}}
%{!?distroarch: %{expand: %%define distroarch i386}}

# Defined as YYYYMMDD if this is a snapshot build
#define date 20030702

# Still needed with some old releases
%define __libtoolize :

Summary: YellowDog Updater Modified, an rpm package management utility
Name: yum
Version: 1.0.3
Release: 3%{?date:.%{date}}.%{distro}%{?dist}
License: GPL
Group: System Environment/Base
Source: http://www.dulug.duke.edu/yum/download/1.0/%{name}-%{?date}%{!?date:%{version}}.tar.gz
Source11: yum-rh.conf
Source12: yum-yd.conf
Source50: RPM-GPG-KEY-redhat
Source51: RPM-GPG-KEY-yellowdog
Source52: RPM-GPG-KEY-freshrpms
URL: http://www.linux.duke.edu/projects/yum/
Requires(pre): /sbin/chkconfig, /sbin/service
Requires(post): /sbin/chkconfig, /sbin/service
Requires: rpm >= 4.0, python >= 1.5.2, rpm-python
Requires: gnupg
Conflicts: rpm >= 4.1.1
BuildRequires: rpm-python, python >= 1.5.2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

Available rpmbuild rebuild options :
--with : rh (default) yd rawhide

%prep
%setup -n %{name}%{!?date:-%{version}}

%build
# Change the defaut debug level of the cron entry
perl -pi -e 's|-d 0|-d 1|g' etc/yum.cron
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%{__install} -p -m0644 %{_sourcedir}/yum-%{distro}.conf \
    %{buildroot}%{_sysconfdir}/yum.conf
perl -pi -e 's/\$releasever/%{distrover}/g' %{buildroot}%{_sysconfdir}/yum.conf
perl -pi -e 's/\$basearch/%{distroarch}/g' %{buildroot}%{_sysconfdir}/yum.conf
cp -a %{_sourcedir}/RPM-GPG-KEY* .

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add yum
/sbin/service yum condrestart >/dev/null 2>&1 || :
%ifnarch ppc
# Import Red Hat gpg key
gpg --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-redhat >/dev/null 2>&1
%else
# Import Yellow Dog gpg key
gpg --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-yellowdog >/dev/null 2>&1
%endif
# Import Freshrpms.net gpg key
gpg --import %{_docdir}/%{name}-%{version}/RPM-GPG-KEY-freshrpms >/dev/null 2>&1

%preun
if [ $1 -eq 0 ]; then
        /sbin/chkconfig --del yum
        /sbin/service yum stop >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README RPM-GPG-KEY-* TODO
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
* Thu Oct 16 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the configuration file as release variables don't seem supported.

* Thu Oct  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3 at last.
- Synch with the 2.0 spec.
- Added automatic gpg key import.
- Import RH key for all archs except ppc where YD one is imported instead.

* Fri Jul  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 20030702 1.0.1 snapshot.

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
