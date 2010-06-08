# $Id$
# Authority: dag

Summary: Relax and Recover (ReaR) is a Linux Disaster Recovery framework
Name: rear
Version: 1.7.24
Release: 1%{?dist}
License: GPLv2
Group: Applications/Archiving
URL: http://rear.sourceforge.net/

Source: http://dl.sf.net/rear/rear-%{version}.tar.gz
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
Requires: portmap
Requires: redhat-lsb
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

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/rear/
%{__cp} -av etc/rear/* %{buildroot}%{_sysconfdir}/rear/

%{__install} -Dp -m0755 usr/sbin/rear %{buildroot}%{_sbindir}/rear
%{__install} -Dp -m0644 doc/rear.8 %{buildroot}%{_mandir}/man8/rear.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README doc/*
%doc %{_mandir}/man8/rear.8*
%config(noreplace) %{_sysconfdir}/rear/
%{_datadir}/rear/
%{_localstatedir}/lib/rear/
%{_sbindir}/rear
%exclude %{_datadir}/rear/doc/

%changelog
* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.7.24-1
- Updated to release 1.7.24.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.7.23-1
- Initial package. (using DAR)
