# $Id$
# Authority: dag
# Upstream: Jay Maynard <jmaynard$conmicro,cx>
# Upstream: <hercules-390$yahoogroups,com>

#define date 20041025

Summary: Hercules S/370, ESA/390, and z/Architecture emulator
Name: hercules
Version: 3.02
Release: %{?date:0.%{date}.}1.2%{?dist}
License: QPL
Group: Applications/Emulators
URL: http://www.conmicro.cx/hercules/
Source: http://www.conmicro.cx/hercules/hercules-%{version}%{?date:-cvs}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bison, zlib-devel, bzip2-devel, libgcrypt, gcc-c++
Obsoletes: hercules-docs <= 3.01

%description
Hercules is an emulator for the IBM System/370, ESA/390, and z/Architecture
series of mainframe computers. It is capable of running any IBM operating
system and applications that a real system will run, as long as the hardwre
needed is emulated. Hercules can emulate FBA and CKD DASD, tape, printer,
card reader, card punch, channel-to-channel adapter, LCS Ethernet, and
printer-keyboard, 3270 terminal, and 3287 printer devices.

%prep
%setup -n %{name}-%{version}%{?date:-cvs}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|^(modexecdir) =.*$|$1 = \$(libdir)/hercules|' \
    Makefile.in crypto/Makefile.in

%{__mv} hercules.cnf hercules.cnf.sample
%{__cat} <<EOF >hercules.cnf
# Sample configuration file to run Red Hat Linux or Fedora Core S/390 with the
# the Hercules ESA/390 emulator
#
CPUSERIAL 002623        # CPU serial number
CPUMODEL  3090          # CPU model number: 3090, 7490, 2064
MAINSIZE  256           # Main storage size in megabytes
NUMCPU    1             # Number of CPUs
CNSLPORT  3270          # TCP port number to which consoles connect
#HTTPPORT 8081          # enable a HTTP server on this port
OSTAILOR  LINUX         # OS tailoring
LOADPARM  0120....      # IPL parameter
IODELAY   0             # modern kernels do not need a delay
ARCHMODE  ESA/390       # Architecture mode S/370, ESA/390 or ESAME
TZOFFSET  +0100         # Central Europe
MODPATH   %{_libdir}/hercules

# .-----------------------Device number
# |   .-----------------Device type
# |   |    .---------File name and parameters
# |   |    |
# V   V    V
#---  ---- --------------------
# card reader
000C  3505 kernel.img hercules.prm initrd.img autopad
# card punch
#000D 3525 punch00d.txt ascii
# line printer
#000E 1403 print00e.txt crlf
# local non-SNA 3270 TN3270 client connection
#001F 3270
# CKD direct access storage device
# initialize with: dasdinit -z linux.120 3390-3 lin000
0120  3390 %{_sysconfdir}/hercules/linux.120
# local non-SNA 3270 TN3270 client connection
#0200 3270
#0201 3270
# tape drives
0580  3420 %{_sysconfdir}/hercules/hercules.tdf
#0581 3420 /dev/st0
#0582 3420 ickdsf.ipl
# networking, channel-to-channel adapter
0600  3088 CTCI -n /dev/net/tun -t 1500 192.168.200.3 192.168.200.4
# networking, LCS adaptor
#0700 3088 LCS 192.168.200.4 -n /dev/net/tun -m 01:02:03:04:05:06
EOF

%{__cat} <<EOF >hercules.ins
* Red Hat Linux for S/390 Installation
kernel.img 0x00000000
initrd.img 0x00800000
hercules.prm 0x00010480
EOF

%{__cat} <<'EOF' >hercules.init
#!/bin/sh

###  Startup script for the Hercules S/390 emulator
###  Copyright (C) 2001 Karsten Hopp <karsten@redhat.de>
###  Copyright (C) 2003 Florian La Roche <laroche@redhat.com>

### This is your "hercules network" between your machine running the
### hercules emulator and the Linux guest running in hercules.
HERCNET="192.168.200.0/24"

PATH=/bin:/usr/bin:/sbin:/usr/sbin
export PATH
unset LANG LC_COLLATE

if [ `id -u` != 0 ]; then
    echo "This script requires root permissions."
    exit 1
fi

lsmod | grep -q ipchains && {
    echo "ipchains module is already loaded, cannot setup iptables."
    exit 1
}

### This device must be present for hercules to setup networking.
[ -d /dev/net ] || mkdir -p /dev/net
[ -c /dev/net/tun ] || mknod /dev/net/tun c 10 200

### Load the necessary kernel modules:
modprobe tun ip_tables iptable_filter ip_conntrack ip_conntrack_ftp ip_nat_ftp 2>/dev/null

### Enable IP forwarding, you can permanently change this in in
### /etc/sysctl.conf with "net.ipv4.ip_forward = 1".
echo "1" >/proc/sys/net/ipv4/ip_forward

### Masquerade the hercules network.
iptables -t nat -A POSTROUTING -s ${HERCNET} -j MASQUERADE
iptables -A FORWARD -i eth0 -o tun0 -m state --state ESTABLISHED,RELATED -j ACCEPT

### Start hercules itself.
cd %{_sysconfdir}/hercules
LD_ASSUME_KERNEL=2.4.1
export LD_ASSUME_KERNEL
hercules
EOF

%{__cat} <<EOF >hercules.prm
root=/dev/ram0 ro ip=off ramdisk_size=40000
EOF

%{__cat} <<EOF >hercules.tdf
@TDF
tape0 FIXED RECSIZE 1024
kernel.img FIXED RECSIZE 1024
hercules.prm FIXED RECSIZE 1024
initrd.img FIXED RECSIZE 1024
EOT
EOF

%build
%configure \
    --enable-shared \
    --enable-dependency-tracking \
    --enable-optimization="%{optflags}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}
%{__install} -Dp -m0755 hercules.init %{buildroot}%{_sysconfdir}/hercules/hercules.init
%{__install} -Dp -m0644 hercules.cnf %{buildroot}%{_sysconfdir}/hercules/hercules.cnf
%{__install} -Dp -m0644 hercules.ins %{buildroot}%{_sysconfdir}/hercules/hercules.ins
%{__install} -Dp -m0644 hercules.prm %{buildroot}%{_sysconfdir}/hercules/hercules.prm
%{__install} -Dp -m0644 hercules.tdf %{buildroot}%{_sysconfdir}/hercules/hercules.tdf

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc CHANGES README* RELEASE* hercules.cnf.sample html/ util/
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/hercules/
%config(noreplace) %{_sysconfdir}/hercules/*
%{_bindir}/*
%{_datadir}/hercules/
%{_libdir}/hercules/
%{_libdir}/libherc.so
%{_libdir}/libhercs.so
%exclude %{_libdir}/libherc.la
%exclude %{_libdir}/libhercs.la
%exclude %{_libdir}/hercules/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-%{?date:0.%{date}.}1.2
- Rebuild for Fedora Core 5.

* Tue Jan 25 2005 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 3.02-0.20041025.1
- Update to today's CVS snapshot.

* Thu Jul 29 2004 Matthias Saou <http://freshrpms.net/> 3.01-2.20040729
- Update to CVS version.
- Merge the docs back into the main package.

* Sat Jul 17 2004 Matthias Saou <http://freshrpms.net/> 3.01-2
- Updated config's ctc entry to the new syntax.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.
- Added default configuration from Florian La Roche.

* Fri Oct 3 2003 Jay Maynard <jmaynard@conmicro.cx>
Updates for version 3.00: lots of libraries and executable changes.

* Thu Feb 6 2003 Jay Maynard <jmaynard@conmicro.cx>
Fixed permissions again. Thanks to John Summerfield for finding
my screwup and pointing it out.

* Sun Feb 2 2003 Jay Maynard <jmaynard@conmicro.cx>
Updates for 2.17: new files, RPM 4 updates to build specifications (thanks
to Florian La Roche), fixed default attributes (thanks again to John
Summerfield, and this time it'll stick!), and RPM 4 updates to file header
(thanks to Frank Meurer).

* Wed Jul 3 2002 Jay Maynard <jmaynard@conmicro.cx>
Added Alpha build kludge to bypass setresuid test in configure.

* Sat May 4 2002 Jay Maynard <jmaynard@conmicro.cx>
Removed enable-setuid-hercifc option (thanks again to John Summerfield).

* Fri Apr 19 2002 Jay Maynard <jmaynard@conmicro.cx>
Added new HTTP server files for 2.16.

* Thu Dec 20 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed build process to include configure step.

* Sun May 7 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed executables for Hercules 2.12; set default attributes (thanks to
John Summerfield).

* Sun Feb 3 2001 Jay Maynard <jmaynard@conmicro.cx>
Changed executables for Hercules 2.10.

* Sun Oct 8 2000 Jay Maynard <jmaynard@conmicro.cx>
Added multi-architecture build processing.

* Sun Jul 4 2000 Jay Maynard <jmaynard@conmicro.cx>
Added BuildRoot (thanks to David Barth).

* Sun Jun 18 2000 Jay Maynard <jmaynard@conmicro.cx>
Created RPM.
