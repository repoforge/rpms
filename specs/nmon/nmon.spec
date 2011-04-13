# $Id$
# Authority: dag
# Upstream: Nigel Griffiths <nag$uk,ibm,com>

%define ccopts %nil

### RHEL4 kernel has backported features from >= 2.6.18
%{?el4:%define ccopts -DKERNEL_2_6_18}

Summary: Performance analysis tool
Name: nmon
Version: 14f
Release: 1%{?dist}
License: GPLv3
Group: Applications/System
URL: http://nmon.sourceforge.net/

#Source: http://dl.sf.net/project/nmon/lmon12d.zip
Source0: http://dl.sf.net/sourceforge/nmon/lmon%{version}.c
Source1: http://dl.sf.net/sourceforge/nmon/makefile
Source2: http://dl.sf.net/sourceforge/nmon/Documentation.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86} x86_64 ppc ppc64
BuildRequires: ncurses-devel
BuildRequires: /usr/include/linux/version.h

%description
nmon is designed for performance specialists to use for monitoring and
analyzing performance data.

%prep
%setup -c -T
%{__install} -p -m0644 %{SOURCE0} .
%{__install} -p -m0644 %{SOURCE1} .
%{__install} -p -m0644 %{SOURCE2} .

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

### Remove old log files
/usr/bin/find $NMONDIR -ctime +$KEEPDAYS -daystart -type f | xargs rm -f

### Start the new process
exec /usr/bin/nmon $OPTIONS -m $NMONDIR
EOF

%{__cat} <<EOF >nmon-script.cron
0 0 * * * nobody /usr/bin/nmon-script
EOF

%build
%ifarch ppc ppc64
%{__cc} %{optflags} -D GETUSER -D JFS -D LARGEMEM -D POWER %{ccopts} -lncurses lmon%{version}.c -o nmon
%else
%{__cc} %{optflags} -D GETUSER -D JFS -D LARGEMEM %{ccopts} -lncurses lmon%{version}.c -o nmon
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nmon %{buildroot}%{_bindir}/nmon

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/nmon/
%{__install} -Dp -m0755 nmon-script.sh %{buildroot}%{_bindir}/nmon-script
%{__install} -Dp -m0644 nmon-script.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/nmon-script
%{__install} -Dp -m0644 nmon-script.cron %{buildroot}%{_sysconfdir}/cron.d/nmon-script

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Documentation.txt
%config(noreplace) %{_sysconfdir}/sysconfig/nmon-script
%config %{_sysconfdir}/cron.d/nmon-script
%{_bindir}/nmon
%{_bindir}/nmon-script

%defattr(-, nobody, nobody, 0755)
%{_localstatedir}/log/nmon/

%changelog
* Wed Apr 13 2011 Dag Wieers <dag@wieers.com> - 14f-1
- Updated to release 14f. (Simon Matter)

* Thu Nov 05 2009 Dag Wieers <dag@wieers.com> - 12d-1
- Updated to release 12d.

* Sat Aug 18 2007 Dag Wieers <dag@wieers.com> - 11f-1
- Updated to release 11f.

* Tue Feb 06 2007 Dag Wieers <dag@wieers.com> - 11d-2
- Added nmon-script cronjob to do data collection.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 11d-1
- Initial package. (using DAR)
