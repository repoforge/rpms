# $Id$
# Authority: dag
# Upstream: <syslinux$zytor,com>

# Rationale: If you need syslinux, you'd appreciate the latest, trust me.
### EL6 ships with syslinux-3.86-1.1.el6
### EL5 ships with syslinux-3.11-4
### EL4 ships with syslinux-2.11-1
### EL3 ships with syslinux-2.06-0.3E
### EL2 ships with syslinux-2.00-1EL
# Tag: rfx

%define _sbindir /sbin

Summary: Kernel bootloader for FAT or ISO9660 filesystems or PXE networks
Name: syslinux
Version: 5.00
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://syslinux.zytor.com/

Source: http://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86} x86_64
BuildRequires: nasm
BuildRequires: netpbm-progs
BuildRequires: perl
BuildRequires: upx
Requires: mtools

Obsoletes: syslinux-devel <= %{version}-%{release}
Provides: syslinux-devel = %{version}-%{release}

%description
SYSLINUX is a suite of bootloaders, currently supporting DOS FAT
filesystems, Linux ext2/ext3 filesystems (EXTLINUX), PXE network boots
(PXELINUX), or ISO 9660 CD-ROMs (ISOLINUX).  It also includes a tool,
MEMDISK, which loads legacy operating systems from these media.

%prep
%setup

%build
%{__make} CC="%{__cc}" clean
%{__make} spotless
%{__make}
%{__make} CC="%{__cc}" installer

%install
%{__rm} -rf %{buildroot}
%{__make} install-all \
    INSTALLROOT="%{buildroot}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}" \
    SBINDIR="%{_sbindir}"
#    INCDIR="%{_includedir}" \
#    LIBDIR="%{_prefix}/lib" \

### Clean up buildroot
%{__rm} -rf %{buildroot}/tftpboot/

### Clean up docroot
%{__make} -C sample tidy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README doc/* sample/
%doc %{_mandir}/man1/extlinux.1*
%doc %{_mandir}/man1/gethostip.1*
%doc %{_mandir}/man1/lss16toppm.1*
%doc %{_mandir}/man1/ppmtolss16.1*
%doc %{_mandir}/man1/syslinux.1*
%doc %{_mandir}/man1/syslinux2ansi.1*
%{_bindir}/gethostip
%{_bindir}/isohybrid
%{_bindir}/isohybrid.pl
%{_bindir}/keytab-lilo
%{_bindir}/lss16toppm
%{_bindir}/md5pass
%{_bindir}/memdiskfind
%{_bindir}/mkdiskimage
%{_bindir}/ppmtolss16
%{_bindir}/pxelinux-options
%{_bindir}/sha1pass
%{_bindir}/syslinux
%{_bindir}/syslinux2ansi
%{_datadir}/syslinux/
%{_sbindir}/extlinux
/boot/extlinux/

%changelog
* Thu Dec 06 2012 Dag Wieers <dag@wieers.com> - 5.00-1
- Updated to release 5.00.

* Tue Nov 20 2012 Dag Wieers <dag@wieers.com> - 4.06-1
- Updated to release 4.06.

* Sat Dec 10 2011 Dag Wieers <dag@wieers.com> - 4.05-1
- Updated to release 4.05.

* Tue Apr 19 2011 Dag Wieers <dag@wieers.com> - 4.04-1
- Updated to release 4.04.

* Sun Oct 24 2010 Dag Wieers <dag@wieers.com> - 4.03-1
- Updated to release 4.03.

* Thu Jul 22 2010 Dag Wieers <dag@wieers.com> - 4.02-1
- Updated to release 4.02.

* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 4.01-1
- Updated to release 4.01.

* Tue Jun 29 2010 Dag Wieers <dag@wieers.com> - 4.00-1
- Updated to release 4.00.

* Sat Apr 03 2010 Dag Wieers <dag@wieers.com> - 3.86-1
- Updated to release 3.86.

* Mon Feb 22 2010 Dag Wieers <dag@wieers.com> - 3.85-1
- Updated to release 3.85.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 3.84-1
- Updated to release 3.84.

* Fri Oct 09 2009 Dag Wieers <dag@wieers.com> - 3.83-1
- Updated to release 3.83.

* Tue Jun 09 2009 Dag Wieers <dag@wieers.com> - 3.82-1
- Updated to release 3.82.

* Sat May 30 2009 Dag Wieers <dag@wieers.com> - 3.81-1
- Updated to release 3.81.

* Wed May 06 2009 Dag Wieers <dag@wieers.com> - 3.80-1
- Updated to release 3.80.

* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 3.75-1
- Updated to release 3.75.

* Fri Apr 10 2009 Dag Wieers <dag@wieers.com> - 3.74-1
- Updated to release 3.74.

* Mon Jan 26 2009 Dag Wieers <dag@wieers.com> - 3.73-1
- Updated to release 3.73.

* Sun Sep 28 2008 Dag Wieers <dag@wieers.com> - 3.72-2
- Fixed Patch1.

* Fri Sep 26 2008 Dag Wieers <dag@wieers.com> - 3.72-1
- Updated to release 3.72.

* Fri Aug 01 2008 Dag Wieers <dag@wieers.com> - 3.71-1
- Updated to release 3.71.

* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 3.70-1
- Updated to release 3.70.

* Sat Apr 12 2008 Dag Wieers <dag@wieers.com> - 3.63-1
- Updated to release 3.63.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 3.62-1
- Updated to release 3.62.

* Mon Feb 04 2008 Dag Wieers <dag@wieers.com> - 3.61-1
- Updated to release 3.61.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 3.60-1
- Updated to release 3.60.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 3.55-1
- Updated to release 3.55.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 3.53-1
- Updated to release 3.53.

* Wed Sep 26 2007 Dag Wieers <dag@wieers.com> - 3.52-1
- Updated to release 3.52.

* Sat Sep 08 2007 Dag Wieers <dag@wieers.com> - 3.51-2
- Fixed the location of syslinux on x86_64. (Matt Hyclak)

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 3.51-1
- Updated to release 3.51.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 3.50-1
- Updated to release 3.50.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 3.35-1
- Updated to release 3.35.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 3.31-1
- Updated to release 3.31.

* Sun Aug 27 2006 Dag Wieers <dag@wieers.com> - 3.20-1
- Updated to release 3.20.

* Sun Sep 04 2005 Dag Wieers <dag@wieers.com> - 3.11-1
- Updated to release 3.11.

* Fri Aug 26 2005 Dag Wieers <dag@wieers.com> - 3.10-1
- Updated to release 3.10.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.09-1
- Updated to release 3.09.

* Thu May 19 2005 Dag Wieers <dag@wieers.com> - 3.08-1
- Updated to release 3.08.

* Sun Jan 16 2005 Dag Wieers <dag@wieers.com> - 3.07-1
- Updated to release 3.07.

* Mon Jan 10 2005 Dag Wieers <dag@wieers.com> - 3.06-1
- Updated to release 3.06.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Mon Jan 03 2005 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

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
