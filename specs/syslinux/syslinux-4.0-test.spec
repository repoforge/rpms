# $Id$
# Authority: dag
# Upstream: <syslinux$zytor,com>

# Rationale: If you need syslinux, you'd appreciate the latest, trust me.
# Tag: test

%define _sbindir /sbin

Summary: Kernel bootloader for FAT or ISO9660 filesystems or PXE networks
Name: syslinux
Version: 4.00
%define real_version 4.00-pre47
Release: 0.pre47%{?dist}
License: GPL
Group: Applications/System
URL: http://syslinux.zytor.com/

Source: http://www.kernel.org/pub/linux/utils/boot/syslinux/Testing/syslinux-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
BuildRequires: nasm
BuildRequires: netpbm-progs
BuildRequires: perl
Requires: mtools

Obsoletes: syslinux-devel <= %{version}-%{release}
Provides: syslinux-devel = %{version}-%{release}

%description
SYSLINUX is a suite of bootloaders, currently supporting DOS FAT
filesystems, Linux ext2/ext3 filesystems (EXTLINUX), PXE network boots
(PXELINUX), or ISO 9660 CD-ROMs (ISOLINUX).  It also includes a tool,
MEMDISK, which loads legacy operating systems from these media.

%prep
%setup -n %{name}-%{real_version}

%build
%{__make} clean
%{__make} %{?_smp_mflags} installer

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
* Sun May 30 2010 Dag Wieers <dag@wieers.com> - 4.00-0.pre47
- Updated to release 4.00-pre47.

* Mon May 17 2010 Dag Wieers <dag@wieers.com> - 4.00-0.pre45
- Updated to release 4.00-pre45.

* Thu May 13 2010 Dag Wieers <dag@wieers.com> - 4.00-0.pre43
- Updated to release 4.00-pre43.

* Sat May 01 2010 Dag Wieers <dag@wieers.com> - 4.00-0.pre40
- Updated to release 4.00-pre40.

* Sat Apr 03 2010 Dag Wieers <dag@wieers.com> - 4.00-0.pre38
- Updated to release 4.00-pre38.

* Wed Mar 31 2010 Dag Wieers <dag@wieers.com> - 3.86-0.pre2
- Updated to release 3.86-pre2.

* Thu Feb 18 2010 Dag Wieers <dag@wieers.com> - 3.85-0.pre13
- Updated to release 3.85-pre13.

* Thu Feb 04 2010 Dag Wieers <dag@wieers.com> - 3.85-0.pre5
- Updated to release 3.85-pre5.

* Mon Sep 28 2009 Dag Wieers <dag@wieers.com> - 3.83-0.pre11
- Updated to release 3.83-pre11.

* Sun Sep 06 2009 Dag Wieers <dag@wieers.com> - 3.83-0.pre10
- Updated to release 3.83-pre10.

* Sat Aug 01 2009 Dag Wieers <dag@wieers.com> - 3.83-0.pre5
- Updated to release 3.83-pre5.

* Tue Jun 09 2009 Dag Wieers <dag@wieers.com> - 3.82-0.pre5
- Updated to release 3.82-pre5.

* Tue May 26 2009 Dag Wieers <dag@wieers.com> - 3.81-0.pre13
- Updated to release 3.81-pre13.

* Mon May 25 2009 Dag Wieers <dag@wieers.com> - 3.81-0.pre10
- Updated to release 3.81-pre10.

* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 3.81-0.pre9
- Updated to release 3.81-pre9.

* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 3.81-0.pre7
- Updated to release 3.81-pre7.

* Tue May 19 2009 Dag Wieers <dag@wieers.com> - 3.81-0.pre6
- Updated to release 3.81-pre6.

* Sun May 03 2009 Dag Wieers <dag@wieers.com> - 3.80-0.pre7
- Updated to release 3.80-pre7.

* Fri May 01 2009 Dag Wieers <dag@wieers.com> - 3.80-0.pre5
- Updated to release 3.80-pre5.

* Thu Apr 30 2009 Dag Wieers <dag@wieers.com> - 3.80-0.pre4
- Updated to release 3.80-pre4.

* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 3.75-0.pre4
- Updated to release 3.75-pre4.

* Wed Apr 15 2009 Dag Wieers <dag@wieers.com> - 3.75-0.pre2
- Updated to release 3.75-pre2.

* Thu Apr 09 2009 Dag Wieers <dag@wieers.com> - 3.74-0.pre21
- Updated to release 3.74-pre21.

* Tue Apr 07 2009 Dag Wieers <dag@wieers.com> - 3.74-0.pre19
- Updated to release 3.74-pre19.

* Wed Jan 07 2009 Dag Wieers <dag@wieers.com> - 3.73-0.pre7
- Updated to release 3.73-pre7

* Sun Nov 23 2008 Dag Wieers <dag@wieers.com> - 3.73-0.pre6
- Updated to release 3.73-pre6.

* Thu Oct 16 2008 Dag Wieers <dag@wieers.com> - 3.73-0.pre4
- Updated to release 3.73-pre4.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 3.73-0.pre3
- Updated to release 3.73-pre3.

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
