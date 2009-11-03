# $Id$
# Authority: dag
# Upstream: Nigel Griffiths <nag$uk,ibm,com>

Summary: Performance analysis tool
Name: nmon
Version: 11f
Release: 1%{?dist}
License: Proprietary
Group: Applications/System
URL: http://www-128.ibm.com/developerworks/aix/library/au-analyze_aix/
#URL: http://www-941.haw.ibm.com/collaboration/wiki/display/WikiPtype/nmon

#Source0: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_x86_%{version}.zip?version=1
Source0: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon_x86_%{version}.zip?version=1
#Source1: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_power_%{version}.zip?version=2
Source1: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon_power_rhel4.zip?version=1
#Source2: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon4linux_x86_64_b.zip?version=1
Source2: http://www-941.haw.ibm.com/collaboration/wiki/download/attachments/437/nmon_x86_64_rhel4.zip?version=1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64 ppc ppc64

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -c -a1 -a2

%{__cat} <<EOF >nmon-script.sysconfig
### The directory to store the nmon data files
NMONDIR="/var/log/nmon"

### Default options for nmon
OPTIONS="-f -t"

### Number of days to keep nmon data files
KEEPDAYS="31"
EOF

%{__cat} <<'EOF' >nmon-script.sh
#!/bin/bash

### Please make modifications to the options and path in /etc/sysconfig/nmon-script

### Default variables
SYSCONFIG="/etc/sysconfig/nmon-script"
NMONDIR="/var/log/nmon"
OPTIONS="-f -t"
KEEPDAYS="31"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

### Kill the old process(es)
/usr/bin/pkill -x -f "/usr/bin/nmon $OPTIONS -m $NMONDIR"

### Start the new process
/usr/bin/nmon $OPTIONS -m $NMONDIR

### Remove old log files
/usr/bin/find $NMONDIR  -ctime +$KEEPDAYS -daystart -type f | xargs rm -f
EOF

%{__cat} <<EOF >nmon-script.cron
0 0 * * * nobody /usr/bin/nmon-script
EOF

%build

%install
%{__rm} -rf %{buildroot}
%ifarch i386
%{?el5:%{__install} -Dp -m0755 nmon_x86_rhel4 %{buildroot}%{_bindir}/nmon}
%{?fc6:%{__install} -Dp -m0755 nmon_x86_fedora5 %{buildroot}%{_bindir}/nmon}
%{?fc5:%{__install} -Dp -m0755 nmon_x86_fedora5 %{buildroot}%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_rhel4 %{buildroot}%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_x86_rhel3 %{buildroot}%{_bindir}/nmon}
%{?rh9:%{__install} -Dp -m0755 nmon_x86_rhel3 %{buildroot}%{_bindir}/nmon}
%{?rh7:%{__install} -Dp -m0755 nmon_x86_rhel2 %{buildroot}%{_bindir}/nmon}
%{?el2:%{__install} -Dp -m0755 nmon_x86_rhel2 %{buildroot}%{_bindir}/nmon}
%endif
%ifarch x86_64
%{?el5:%{__install} -Dp -m0755 nmon_x86_64_rhel4 %{buildroot}%{_bindir}/nmon}
%{?fc6:%{__install} -Dp -m0755 nmon_x86_64_fedora6 %{buildroot}%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_x86_64_rhel4 %{buildroot}%{_bindir}/nmon}
%endif
%ifarch ppc ppc64
%{?el5:%{__install} -Dp -m0755 nmon_power_rhel4 %{buildroot}%{_bindir}/nmon}
%{?el4:%{__install} -Dp -m0755 nmon_power_rhel4 %{buildroot}%{_bindir}/nmon}
%{?el3:%{__install} -Dp -m0755 nmon_power_rhel3 %{buildroot}%{_bindir}/nmon}
%endif

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/nmon/
%{__install} -Dp -m0755 nmon-script.sh %{buildroot}%{_bindir}/nmon-script
%{__install} -Dp -m0644 nmon-script.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/nmon-script
%{__install} -Dp -m0644 nmon-script.cron %{buildroot}%{_sysconfdir}/cron.d/nmon-script

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/sysconfig/nmon-script
%config %{_sysconfdir}/cron.d/nmon-script
%{_bindir}/nmon
%{_bindir}/nmon-script

%defattr(-, nobody, nobody, 0755)
%{_localstatedir}/log/nmon/

%changelog
* Sat Aug 18 2007 Dag Wieers <dag@wieers.com> - 11f-1
- Updated to release 11f.

* Tue Feb 06 2007 Dag Wieers <dag@wieers.com> - 11d-2
- Added nmon-script cronjob to do data collection.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 11d-1
- Initial package. (using DAR)
