# $Id$
# Authority: dag
# Upstream: <syslinux$zytor,com>

# Rationale: If you need syslinux, you'd appreciate the latest, trust me.

##BuildAsRoot: 1

Summary: Kernel bootloader for FAT or ISO9660 filesystems or PXE networks
Name: syslinux
Version: 2.13
Release: 1
License: GPL
Group: Applications/System
URL: http://syslinux.zytor.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/syslinux-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Autoreq: 0
ExclusiveArch: i386 x86_64
BuildRequires: nasm, perl, netpbm-progs
Requires: mtools

%description
Syslinux is a simple kernel loader. It normally loads the kernel (and an
optional initrd image) from a FAT filesystem. It can also be used as a
PXE bootloader during network boots (PXELINUX), or for booting from
ISO 9660 CD-ROMs (ISOLINUX).

%prep
%setup

%build
%{__make} clean
%{__make} %{?_smp_mflags} installer
%{__make} -C sample tidy

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/syslinux/ \
			%{buildroot}%{_includedir}
%makeinstall install-lib \
	INSTALLROOT="%{buildroot}" \
	BINDIR="%{_bindir}" \
	LIBDIR="%{_libdir}" \
	INCDIR="%{_includedir}"
%{__install} -m0755 mkdiskimage sys2ansi.pl keytab-lilo.pl %{buildroot}%{_libdir}/syslinux/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING NEWS README TODO *.doc memdisk/memdisk.doc sample/
%{_bindir}/*
%{_libdir}/syslinux/
%{_libdir}/libsyslinux*
%{_includedir}/syslinux.h

%changelog
* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 2.13-1
- Updated to release 2.13.

* Mon Oct 11 2004 Dag Wieers <dag@wieers.com> - 2.11-2
- Re-added libsyslinux.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 2.11-1
- Updated to release 2.11.

* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 2.09-1
- Updated to release 2.09.

* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 2.08-0
- Updated to release 2.08.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 2.07-0.pre5
- Updated to release 2.07-pre5.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 2.06-0
- Initial package. (using DAR)
