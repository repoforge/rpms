# $Id$
# Authority: matthias

Summary: Port scan detection and active defense
Name: portsentry
Version: 1.1
Release: 11%{?dist}
License: Freely Distributable
Group: Applications/System
URL: http://www.psionic.com/products/portsentry.html
Source0: http://dl.sf.net/sentrytools/%{name}-%{version}.tar.gz
Source1: portsentry.init
Source2: portsentry.modes
Source3: portsentry.cron
Patch: portsentry-1.1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: sentry

%description
PortSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and reliable
host based intrusion detection software to the Internet community. More
information can be obtained from http://www.psionic.com.

PortSentry has a number of options to detect port scans, the purpose of this
is to give an admin a heads up that their host is being probed. There are
similar programs that do this already (klaxon, etc.) We have added a little
twist to the whole idea (auto-blocking), plus extensive support for
stealth scan detection.

PortSentry has four "stealth" scan detection modes. Method one uses a
pre-defined list of ports to watch over. If someone pokes at them
it activates. The second method is what is called "inverse" port binding,
where every port under a range is watched *except* for those that the
system has bound for network daemons when the PortSentry starts or ones that
you've manually excluded. This is a very sensitive way for looking for
port probes, but also the most prone to false alarms.

%prep
%setup
%patch -p1 -b .freshrpms

%build
%{__make} %{?_smp_mflags} linux

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}/var/portsentry
%{__make} install

%{__install} -Dp -m 700 %{SOURCE1} %{buildroot}/etc/init.d/portsentry
%{__install} -Dp -m 600 %{SOURCE2} %{buildroot}/etc/portsentry/portsentry.modes
%{__install} -Dp -m 600 %{SOURCE3} %{buildroot}/etc/cron.d/portsentry

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add portsentry

%preun
if [ $1 -eq 0 ]; then
  /sbin/service portsentry stop > /dev/null 2>&1
  /sbin/chkconfig --del portsentry
fi

%postun
if [ $1 -ge 1 ]; then
  /sbin/service portsentry condrestart > /dev/null 2>&1
fi

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE README*
%config /etc/init.d/portsentry
%config /etc/cron.d/portsentry
%dir /etc/portsentry
%config(noreplace) /etc/portsentry/portsentry.conf
%config(noreplace) /etc/portsentry/portsentry.ignore
%config(noreplace) /etc/portsentry/portsentry.modes
%attr(700, root, root) %dir /var/portsentry
/usr/sbin/portsentry

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1-11.fr
- Rebuild for Fedora Core 1.
- Updated the init script for automatic i18n support.

* Wed Sep 17 2003 Matthias Saou <http://freshrpms.net/>
- Changed automatic restart to be every 20min instead of 6h.
- Exclude 135 TCP because of Blaster (too many blocked NATed addresses).

* Fri May  9 2003 Matthias Saou <http://freshrpms.net/>
- One year without changes :-)
- Rebuilt for Red Hat Linux 9.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Thu Dec  6 2001 Matthias Saou <http://freshrpms.net/>
- Restart portsentry upon iptables/ipchains flush to not let the
  previously blocked hosts to what they want!
- Now default to iptables and not ipchains.

* Wed Oct 31 2001 Matthias Saou <http://freshrpms.net/>
- Removed the mail sent every 6 hours about the flush on success.

* Wed Oct 17 2001 Matthias Saou <http://freshrpms.net/>
- Fixed the emailing example KILL_RUN_CMD I had added.

* Fri Sep 18 2001 Matthias Saou <http://freshrpms.net/>
- Fixed the init script to update correctly the ignore file on non
  english systems.

* Sat Aug 18 2001 Matthias Saou <http://freshrpms.net/>
- Added UDP port 123 to the advanced exclude, since ntp queries were
  getting the ntp server blocked!

* Fri Aug  3 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.1.
- Spec file cleanup, merged both patches to the new version.
- New updated initscript, now excludes default gateways and nameservers.
- Added a cron entry to flush added iptables/ipchains entries.

* Thu Nov  9 2000 Matthias Saou <http://freshrpms.net/>
- added some exclude tcp & udp ports in "a" modes
- changed the default mode to "atcp" & "audp" with a portsentry.modes
  file

* Tue Sep 5 2000 Tim Powers <timp@redhat.com>
- fixed initscript so that it doesn't overwrite the portsentry.ignore file,
  just appends to it (in a roundabout way)
- patched default behavior of config file *not* to automagically start
  blocking tcp and udp
- the above were tested by Henri J. Schlereth" <henris@bga.com>, and don't
  forget he reported the problem to me too :)

* Thu Aug 10 2000 Tim Powers <timp@redhat.com>
- fixed the initscript so that it actually starts both or all modes of
  scanning
- noreplace for config files

* Thu Aug 10 2000 Tim Powers <timp@redhat.com>
- fixed perms on /var/portsentry
- added initscript with many suggestions from Henri J. Schlereth
  <henris@bga.com>, it's real nice :)
- added post, preun and postun sections since we now have an initscript

* Wed Aug 9 2000 Tim Powers <timp@redhat.com>
- FHSified the package. Was putting stuff in the horrible location of
  /usr/psionic, which is not FHS compliant. Fixed.

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu May 18 2000 Tim Powers <timp@redhat.com>
- update to 1.0

* Tue Nov 23 1999 Tim Powers <timp@redhat.com>
- updated to 0.99.1

* Tue Jul 20 1999 Tim Powers <timp@redhat.com>
- yet another name change and version update to 0.98
- made neccessary changes to everything so it would build

* Wed May 05 1999 Bill Nottingham <notting@redhat.com>
- build for powertools-6.0, rename to portsentry

* Fri Oct 2  1998 Michael Maher <minke@redhat.com>
- built package
