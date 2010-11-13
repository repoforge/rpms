# $Id$
# Authority: dag

### EL6 ships with e2fsprogs-1.41.12-3.el6
### EL5 ships with e2fsprogs-1.39-23.el5_5.1
### EL4 ships with e2fsprogs-1.35-12.24.el4
### EL3 ships with e2fsprogs-1.32-15.4
### EL2 ships with e2fsprogs-1.26-1.73
# ExclusiveDist: rh7
# Tag: rft

%define	_root_sbindir	/sbin
%define	_root_libdir	/%{_lib}

Summary: Utilities for managing the second extended (ext2) filesystem
Name: e2fsprogs
Version: 1.34
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://e2fsprogs.sourceforge.net/

Source:  http://dl.sf.net/e2fsprogs/e2fsprogs-%{version}.tar.gz
Patch2: e2fsprogs-1.27-nostrip.patch
Patch4: e2fsprogs-1.32-mainframe.patch
Patch5: e2fsprogs-1.32-s390.patch
Patch6: e2fsprogs-1.32-nosync.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Prereq: /sbin/ldconfig

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in second
extended (ext2) filesystems. E2fsprogs contains e2fsck (used to
repair filesystem inconsistencies after an unclean shutdown), mke2fs
(used to initialize a partition to contain an empty ext2 filesystem),
debugfs (used to examine the internal structure of a filesystem, to
manually repair a corrupted filesystem, or to create test cases for
e2fsck), tune2fs (used to modify filesystem parameters), and most of
the other core ext2fs filesystem utilities.

You should install the e2fsprogs package if you need to manage the
performance of an ext2 filesystem.

%package devel
Summary: Ext2 filesystem-specific static libraries and headers
Group: Development/Libraries
Requires: e2fsprogs = %{version}
Prereq: /sbin/install-info

%description devel
E2fsprogs-devel contains the libraries and header files needed to
develop second extended (ext2) filesystem-specific programs.

You should install e2fsprogs-devel if you want to develop ext2
filesystem-specific programs. If you install e2fsprogs-devel, you'll
also want to install e2fsprogs.

%prep
%setup -q
%patch2 -p1
#%patch4 -p1 -b .lr
%patch5 -p1
%patch6 -p1
chmod 644 po/*.po

%build
%configure --enable-elf-shlibs --enable-nls
make
make -C po

%install
%{__rm} -rf %{buildroot}
export PATH=/sbin:$PATH

make install install-libs DESTDIR="$RPM_BUILD_ROOT" \
	root_sbindir=%{_root_sbindir} root_libdir=%{_root_libdir}
make install -C po DESTDIR="$RPM_BUILD_ROOT"

%find_lang %{name}

cd ${RPM_BUILD_ROOT}%{_libdir}
ln -sf %{_root_libdir}/libcom_err.so.2 libcom_err.so
ln -sf %{_root_libdir}/libe2p.so.2 libe2p.so
ln -sf %{_root_libdir}/libext2fs.so.2 libext2fs.so
ln -sf %{_root_libdir}/libss.so.2 libss.so
ln -sf %{_root_libdir}/libuuid.so.1 libuuid.so

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%post devel
if [ -x /sbin/install-info ]; then
    /sbin/install-info %{_infodir}/libext2fs.info.gz %{_infodir}/dir
fi
exit 0

%postun devel
if [ $1 = 0 ]; then
   /sbin/install-info --delete %{_infodir}/libext2fs.info.gz %{_infodir}/dir
fi
exit 0

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README RELEASE-NOTES

%{_root_sbindir}/badblocks
%{_root_sbindir}/blkid
%{_root_sbindir}/debugfs
%{_root_sbindir}/dumpe2fs
%{_root_sbindir}/e2fsck
%{_root_sbindir}/e2image
%{_root_sbindir}/e2label
%{_root_sbindir}/findfs
%{_root_sbindir}/fsck
%{_root_sbindir}/fsck.ext2
%{_root_sbindir}/fsck.ext3
%{_root_sbindir}/logsave
%{_root_sbindir}/mke2fs
%{_root_sbindir}/mkfs.ext2
%{_root_sbindir}/mkfs.ext3
%{_root_sbindir}/resize2fs
%{_root_sbindir}/tune2fs
%{_sbindir}/mklost+found

%{_root_libdir}/libblkid.so.*
%{_root_libdir}/libcom_err.so.*
%{_root_libdir}/libe2p.so.*
%{_root_libdir}/libext2fs.so.*
%{_root_libdir}/libss.so.*
%{_root_libdir}/libuuid.so.*
%{_root_libdir}/evms/libe2fsim.1.2.1.so

%{_bindir}/chattr
%{_bindir}/lsattr
%{_bindir}/uuidgen
%{_mandir}/man1/chattr.1*
%{_mandir}/man1/lsattr.1*
%{_mandir}/man1/uuidgen.1*

%{_mandir}/man3/libuuid.3*
%{_mandir}/man3/uuid_clear.3*
%{_mandir}/man3/uuid_compare.3*
%{_mandir}/man3/uuid_copy.3*
%{_mandir}/man3/uuid_generate.3*
%{_mandir}/man3/uuid_generate_random.3*
%{_mandir}/man3/uuid_generate_time.3*
%{_mandir}/man3/uuid_is_null.3*
%{_mandir}/man3/uuid_parse.3*
%{_mandir}/man3/uuid_time.3*
%{_mandir}/man3/uuid_unparse.3*

%{_mandir}/man8/badblocks.8*
%{_mandir}/man8/blkid.8*
%{_mandir}/man8/debugfs.8*
%{_mandir}/man8/dumpe2fs.8*
%{_mandir}/man8/e2fsck.8*
%{_mandir}/man8/findfs.8*
%{_mandir}/man8/fsck.ext2.8*
%{_mandir}/man8/fsck.ext3.8*
%{_mandir}/man8/e2image.8*
%{_mandir}/man8/e2label.8*
%{_mandir}/man8/fsck.8*
%{_mandir}/man8/logsave.8*
%{_mandir}/man8/mke2fs.8*
%{_mandir}/man8/mkfs.ext2.8*
%{_mandir}/man8/mkfs.ext3.8*
%{_mandir}/man8/mklost+found.8*
%{_mandir}/man8/resize2fs.8*
%{_mandir}/man8/tune2fs.8*

%files devel
%defattr(-, root, root, 0755)
%{_infodir}/libext2fs.info*
%{_bindir}/compile_et
%{_bindir}/mk_cmds

%{_libdir}/libblkid.a
%{_libdir}/libcom_err.a
%{_libdir}/libcom_err.so
%{_libdir}/libe2p.a
%{_libdir}/libe2p.so
%{_libdir}/libext2fs.a
%{_libdir}/libext2fs.so
%{_libdir}/libss.a
%{_libdir}/libss.so
%{_libdir}/libuuid.a
%{_libdir}/libuuid.so

%{_datadir}/et
%{_datadir}/ss
%{_includedir}/blkid
%{_includedir}/e2p
%{_includedir}/et
%{_includedir}/ext2fs
%{_includedir}/ss
%{_includedir}/uuid
%{_mandir}/man1/compile_et.1*
%{_mandir}/man1/mk_cmds.1*
%{_mandir}/man3/com_err.3*
%{_mandir}/man3/libblkid.3*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.34-1.2
- Rebuild for Fedora Core 5.

* Fri Aug 01 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.34
- do not strip some more apps, should probably just change $(STRIP)...

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 08 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.33
- enable translations

* Fri Apr 18 2003 Jeremy Katz <katzj@redhat.com> 1.32-11
- fix error message, do block size checking on s390 only

* Thu Apr 17 2003 Jeremy Katz <katzj@redhat.com> 1.32-10
- check the return code of BLKSSZGET ioctl() to avoid breaking with files

* Tue Apr 15 2003 Phil Knirsch <pknirsch@redhat.com> 1.32-9
- Improved dasd blocksize patch to make it more generic and work correctly.

* Thu Mar 27 2003 Phil Knirsch <pknirsch@redhat.com> 1.32-8
- Removed sync call from e2fsck target. Not needed anymore.

* Wed Mar 26 2003 Phil Knirsch <pknirsch@redhat.com> 1.32-7
- Fixed problem with mke2fs and default blocksize small partitions on dasd
- Disabled Florians patch for now as it's a little incomplete. :-)

* Sun Feb 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add an ugly patch to read full lines of input during e2fsck for /dev/console

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 14 2003 Bill Nottingham <notting@redhat.com> 1.32-2
- do *not* create htree filesystems by default

* Mon Nov 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.32

* Fri Nov 01 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.30, leave out already integrated patches
- clean up spec file
- also package some missing files

* Tue Sep 24 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.29, adapt patches to current source

* Sat Aug 10 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add missing man-pages to filelist

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jun 21 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add HTree version of e2fsprogs, disable s390 patch
- add e2fsprogs-dir_index.patch

* Mon Jun 17 2002 Karsten Hopp <karsten@redhat.de>
- set default blocksize for mke2fs on S/390 and zSeries to 4096

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr 09 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix further bug in man-page #62995

* Thu Apr 04 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix man-pages

* Thu Mar 21 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.27
- patch5 should not be needed anymore

* Fri Mar 08 2002 Elliot Lee <sopwith@redhat.com>
- Make link for mkfs.ext3 (patch5)
- Add man pages for {mkfs,fsck}.{ext2,ext3}

* Tue Feb 19 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.26

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Nov 04 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.25
- patch for BLKGETSIZE64 is not needed anymore
- adapt autoconf-2.50 patch

* Thu Nov  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.23-5
- Make the C++ patch work even with g++ 3.1

* Mon Oct 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.23-4
- Fix headers of libext2fs - it wasn't possible to include them from
  C++ code (using private as a variable name isn't a good idea)
- Fix build with autoconf 2.5x

* Mon Sep 17 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add e2image to filelist

* Wed Aug 29 2001 Bill Nottingham <notting@redhat.com>
- disable BLKGETSIZE64 ioctl support for now

* Sun Aug 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.23. This was requested to support the "auto" fstype
  to ease ext2 <-> ext3 conversions.

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add some more man-pages, patch by <Martin.Wilck@fujitsu-siemens.com>

* Tue Jun 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- make sure "configure" is writable

* Mon Jun 25 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.22

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.21

* Mon Jun 11 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add endian patch from sct@redhat.com  #44104

* Tue May 29 2001 Than Ngo <than@redhat.com>
- update to 1.20
- add Url

* Tue May 15 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- make sure ldconfig doesn't have any input and scripts end
  with "exit 0"

* Tue May 15 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to e2fsprogs-1.20-WIP-0514.tar.gz

* Sun Apr 15 2001 Alan Eldridge <alane@geeksrus.net>
- Added 16K buffer for reading /proc/partitions in
  get_label_by_device.c to correct problems with LABEL= in fsck
  caused by not reading /proc/partitions in a single read() call;
  if somebody has a "partitions" > 16K, it may still fail ...
* Fri Apr 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add further IDE and SCSI disks to a hardcoded list in fsck #34190

* Tue Feb 27 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- require the main rpm from the devel rpm

* Thu Feb 22 2001 Helge Deller <hdeller@redhat.de>
- fix fsck -A bug (#21242)

* Mon Feb 12 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix bug with 16 byte long labels #27071

* Mon Sep 11 2000 Jeff Johnson <jbj@redhat.com>
- build for Red Hat 7.1.

* Tue Aug  8 2000 Jeff Johnson <jbj@redhat.com>
- merge LABEL patch.
- update to 1.19.

* Tue Jul 25 2000 Erik Troan <ewt@redhat.com>
- fixed LABEL handling

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 26 2000 Matt Wilson <msw@redhat.com>
- added resize2fs from the WIP snapshot

* Thu Jun 15 2000 Matt Wilson <msw@redhat.com>
- patched to build against linux 2.4 headers

* Mon Jun  5 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Fri Apr 28 2000 Bill Nottingham <notting@redhat.com>
- fix for ia64

* Sat Feb  5 2000 Bill Nottingham <notting@redhat.com>
- add install-info scripts

* Thu Feb 03 2000 Elliot Lee <sopwith@redhat.com>
- Fix bug #8585 (Y2K problems in debugfs)

* Wed Feb 02 2000 Jakub Jelinek <jakub@redhat.com>
- allow multiline errors in et, so that other programs
  can use compile_et (from Kerberos)

* Thu Jan 13 2000 Jeff Johnson <jbj@redhat.com>
- build 1.18 for 6.2.

* Tue Oct 26 1999 Bill Nottingham <notting@redhat.com>
- update to 1.17

* Mon Oct 25 1999 Bill Nottingham <notting@redhat.com>
- update to 1.16

* Thu Oct 21 1999 Bill Nottingham <notting@redhat.com>
- add patch to fix SIGUSR1 kills.

* Mon Oct 04 1999 Cristian Gafton <gafton@redhat.com>
- rebuild against new glibc in the sparc tree

* Thu Sep 23 1999 Jakub Jelinek <jakub@redhat.com>
- update mke2fs man page so that it reflects changes in mke2fs
  netweem 1.14 and 1.15

* Thu Aug  5 1999 Bill Nottingham <notting@redhat.com>
- fix lsattr on alpha

* Thu Jul 29 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.15.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- fix fsck segfault

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.14
- use %configure to generate config.sub on arm

* Thu Jan 14 1999 Jeff Johnson <jbj@redhat.com>
- fix /usr/bin/compile_et and doco for com_err.h (#673)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- build with prefix=/usr
- add arm patch

* Mon Dec 28 1998 Jeff Johnson  <jbj@redhat.com>
- update to 1.13.

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Mon Jul 13 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.12.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- include <asm/types.h> to match kernel types in utils

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- fixed broken llseek() prototype

* Wed Aug 20 1997 Erik Troan <ewt@redhat.com>
- added patch to prototype llseek

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
