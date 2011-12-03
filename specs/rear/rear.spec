# $Id$
# Authority: dag

# ExcludeDist: el2 el3

Summary: Relax and Recover (Rear) is a Linux Disaster Recovery framework
Name: rear
Version: 1.12.0
Release: 1%{?dist}
License: GPLv3
Group: Applications/Archiving
URL: http://rear.sourceforge.net/

Source: http://dl.sf.net/project/rear/rear/1.12/%{version}/rear-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: binutils
Requires: ethtool
#Requires: genisomimage
Requires: gzip
Requires: iproute
Requires: iputils
Requires: mingetty
Requires: mkisofs
Requires: parted
Requires: portmap
#Requires: redhat-lsb
#Requires: rpcbind
Requires: syslinux
Requires: tar
Requires: util-linux

%description
Relax and Recover (abbreviated rear) is a highly modular disaster recovery
framework for GNU/Linux based systems, but can be easily extended to other
UNIX alike systems. The disaster recovery information (and maybe the backups)
can be stored via the network, local on hard disks or USB devices, DVD/CD-R,
tape, etc. The result is also a bootable image that is capable of booting via
PXE, DVD/CD and USB media.

Relax and Recover integrates with other backup software and provides integrated
bare metal disaster recovery abilities to the compatible backup software.

%prep
%setup

%{__install} -d -m0755 etc/cron.d/
%{__cat} <<'EOF' >etc/cron.d/rear
#30 0 1 * * root %{_sbindir}/rear mkrescue
#30 1 * * * root %{_sbindir}/rear checklayout || %{_sbindir}/rear mkrescue
EOF

%{__install} -d -m0755 etc/udev/rules.d/
%{__cat} <<'EOF' >etc/udev/rules.d/62-rear-usb.rules
#ACTION=="add", SUBSYSTEM=="block", ENV{ID_FS_LABEL}=="REAR-000", RUN+="%{_sbindir}/rear udev"
EOF

%{__cat} <<'EOF' >etc/rear/os.conf
OS_VENDOR=RedHatEnterpriseServer
OS_VERSION=%{?rhel}
EOF

%{__perl} -pi -e '
        s|^CONFIG_DIR=.*|CONFIG_DIR="%{_sysconfdir}/rear"|;
        s|^SHARE_DIR=.*|SHARE_DIR="%{_datadir}/rear"|;
        s|^VAR_DIR=.*|VAR_DIR="%{_localstatedir}/lib/rear"|;
    ' usr/sbin/rear

%{__perl} -pi -e '
        s|/etc|%{_sysconfdir}|g;
        s|/usr/sbin|%{_sbindir}|g;
        s|/usr/share|%{_datadir}|g;
        s|/usr/share/doc/packages|%{_docdir}|g;
    ' doc/rear.8

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/rear/

%{__install} -d -m0755 %{buildroot}%{_datadir}/rear/
%{__cp} -av usr/share/rear/* %{buildroot}%{_datadir}/rear/

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/
%{__cp} -av etc/. %{buildroot}%{_sysconfdir}/

%{__install} -Dp -m0755 usr/sbin/rear %{buildroot}%{_sbindir}/rear
%{__install} -Dp -m0644 usr/share/rear/doc/rear.8 %{buildroot}%{_mandir}/man8/rear.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc usr/share/rear/COPYING usr/share/rear/README usr/share/rear/TODO
%doc usr/share/rear/doc/*
%doc %{_mandir}/man8/rear.8*
%config(noreplace) %{_sysconfdir}/cron.d/rear
%config(noreplace) %{_sysconfdir}/rear/
%config(noreplace) %{_sysconfdir}/udev/rules.d/62-rear-usb.rules
%{_datadir}/rear/
%{_localstatedir}/lib/rear/
%{_sbindir}/rear
%exclude %{_datadir}/rear/doc/

%changelog
* Thu Nov 24 2011 Dag Wieers <dag@wieers.com> - 1.12.0-1
- Updated to release 1.12.0.

* Fri Dec 10 2010 Dag Wieers <dag@wieers.com> - 1.7.26-1
- Updated to release 1.7.26.

* Mon Aug 30 2010 Dag Wieers <dag@wieers.com> - 1.7.25-2
- Do not exclude %%{_datadir}/rear/doc/ as it is used by the mkrpm workflow.

* Tue Jun 22 2010 Dag Wieers <dag@wieers.com> - 1.7.25-1
- Updated to release 1.7.25.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.7.24-1
- Updated to release 1.7.24.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.7.23-1
- Initial package. (using DAR)
