# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

# Tag: test

Summary: The boot loader for Linux and other operating systems
Name: lilo
Version: 22.5.9
Release: 1
License: MIT
Group: System Environment/Base
URL: http://home.san.rr.com/johninsd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://home.san.rr.com/johninsd/pub/linux/lilo/lilo-%{version}.tar.gz
Source2: keytab-lilo.c
#Patch3: lilo-21.4.4-graphical.patch
#Patch4: lilo-0.21-enableflame.patch
#Patch5: lilo-0.21-broken.patch
#Patch6: lilo-21.4.4-sa5300.patch
#Patch7: lilo-21.4.4-boot.patch
#Patch8: lilo-21.4.4-i2o.patch
#Patch9: lilo-21.4.4-unsafe.patch
#Patch10: lilo-21.4.4-2DAC960.patch
#Patch100: lilo-21.4.4-lvm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Exclusivearch: i386

BuildRequires: tetex-latex, fileutils, tetex-dvips
%{!?fc1:BuildRequires: dev86}
Requires: mkinitrd >= 3.4.7
Prereq: /sbin/grubby

%description
LILO (LInux LOader) is a basic system program which boots your Linux
system.  LILO loads the Linux kernel from a floppy or a hard drive,
boots the kernel and passes control of the system to the kernel.  LILO
can also boot other operating systems.

%prep
%setup
#%patch3 -p1 -b .graphical
##%patch4 -p1 -b .enableflame
## work around broken kernel headers
#%patch5 -p1 -b .broken
#%patch6 -p1 -b .sa5300
#%patch7 -p1 -b .boot
#%patch8 -p1 -b .i2o
#%patch9 -p1 -b .unsafe
#%patch10 -p1 -b .DAC960
#%patch100 -b .lvm
%{__perl} -pi.orig -e 's|^(#define LILO_H)|$1\n#include <asm/page.h>|' lilo.h

%build
%{__make} %{?_smp_mflags} \
	AS86="echo" \
	LD86="echo" || :
${CC:-gcc} %{optflags} -o keytab-lilo %{SOURCE2}
%{__make} -C doc || :
dvips doc/user.dvi -o doc/User_Guide.ps
dvips doc/tech.dvi -o doc/Technical_Guide.ps
%{__rm} -f doc/*.aux doc/*.log doc/*.toc

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_mandir}
%makeinstall \
	ROOT="%{buildroot}" \
	MAN_DIR="%{_mandir}" \
	AS86="echo" \
	LD86="echo" || :
#%{__mv} -f %{buildroot}%{_sbindir} %{buildroot}%{_bindir}
%{__install} -D -m0755 keytab-lilo %{buildroot}%{_bindir}/keytab-lilo

# remove unpackaged file from the buildroot
#%{__rm} -f %{buildroot}%{_bindir}/keytab-lilo.pl

%post
if [ -f /etc/lilo.conf ]; then
    if [ "$(/sbin/grubby --bootloader-probe | grep -q lilo)" ]; then
        /sbin/lilo > /dev/null
    fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING INCOMPAT QuickInst README doc/
%doc %{_mandir}/man?/*
%{_bindir}/*
/boot/*
/sbin/*

%changelog
* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 21.5.9-1
- Updated to release 21.5.9.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 21.4.4-0
- Added LVM /boot patch.
- Reverted to release 21.4.4.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 22.5-0
- Initial package. (using DAR)
