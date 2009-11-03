# $Id$
# Authority: dag


# Tag: test

Summary: The boot loader for Linux and other operating systems
Name: lilo
Version: 22.8
Release: 1%{?dist}
License: MIT
Group: System Environment/Base
URL: http://home.san.rr.com/johninsd/

Source: http://home.san.rr.com/johninsd/pub/linux/lilo/lilo-%{version}.src.tar.gz
Source2: keytab-lilo.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Exclusivearch: i386 x86_64

BuildRequires: tetex-latex, tetex-dvips, fileutils, dosfstools
BuildRequires: dev86 >= 0.16.10
Requires: mkinitrd >= 3.4.7
Prereq: /sbin/grubby

%description
LILO (LInux LOader) is a basic system program which boots your Linux
system.  LILO loads the Linux kernel from a floppy or a hard drive,
boots the kernel and passes control of the system to the kernel.  LILO
can also boot other operating systems.

%prep
%setup

%build
%{__make} %{?_smp_mflags} all
${CC:-gcc} %{optflags} -o keytab-lilo %{SOURCE2}
%{__make} -C doc || :
dvips doc/user.dvi -o doc/User_Guide.ps
dvips doc/tech.dvi -o doc/Technical_Guide.ps
%{__rm} -f doc/*.aux doc/*.log doc/*.toc

%install
%{__rm} -rf %{buildroot}
%{__make} install ROOT="%{buildroot}" \
	MAN_DIR="%{_mandir}"
%{__mv} -v %{buildroot}/sbin %{buildroot}%{_bindir}
%{__install} -Dp -m0755 keytab-lilo %{buildroot}%{_bindir}/keytab-lilo

%post
if [ -f /etc/lilo.conf ]; then
    if /sbin/grubby --bootloader-probe | grep -q lilo; then
        /sbin/lilo > /dev/null
    fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING INCOMPAT QuickInst README doc/
%doc %{_mandir}/man5/lilo.conf.5*
%doc %{_mandir}/man8/lilo.8*
%doc %{_mandir}/man8/mkrescue.8*
%{_bindir}/keytab-lilo
%{_bindir}/lilo
%{_bindir}/mkrescue
/boot/diag1.img
/boot/diag2.img
%exclude %{_sbindir}/keytab-lilo.pl

%changelog
* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 22.8-1
- Updated to release 22.8.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 22.7-1
- Updated to release 22.7.

* Thu Nov 18 2004 Dag Wieers <dag@wieers.com> - 22.6.1-1
- Updated to release 22.6.1.

* Fri Sep 03 2004 Dag Wieers <dag@wieers.com> - 22.6-1
- Updated to release 22.6.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 22.5.9-1
- Updated to release 22.5.9.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 21.4.4-0
- Added LVM /boot patch.
- Reverted to release 21.4.4.

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 22.5-0
- Initial package. (using DAR)
