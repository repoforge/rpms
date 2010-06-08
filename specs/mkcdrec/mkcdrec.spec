# $Id$
# Authority: dag

%define _optdir %{_localstatedir}/opt/mkcdrec
%define _boot_arch x86

Summary: Make CD-ROM Recovery (mkCDrec) disaster recovery tool-set
Name: mkcdrec
Version: 1.0.0
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Archiving
URL: http://mkcdrec.ota.be/

Source: http://dl.sf.net/project/mkcdrec/mkcdrec/v1.0/mkcdrec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 2.96
Requires: ash
Requires: cdrecord
Requires: fileutils
Requires: kernel >= 2.0.0
Requires: mkisofs
Requires: rsync
Requires: tar
Requires: util-linux >= 2.11
%if %{_boot_arch}==ia64
Requires: chkconfig mtools
Requires: parted >= 1.6
%endif
%if %{_boot_arch}==x86_64
Requires: syslinux
%endif
%if %{_boot_arch}==x86
BuildRequires: syslinux >= 1.60
Requires: coreutils syslinux
%endif

%description
mkCDrec (Make CDROM Recovery) makes a bootable (El Torito) disaster recovery
image, including backups of the Linux system to one or more CD-ROM(s)
(multi-volume sets). Otherwise, the backups can be stored on another disk,
NFS disk, or (remote) tape. After a disk crash or system intrusion, the system
can be booted from the CD-ROM and one can restore the complete system as 
it was. It also features disk cloning, which allows one to restore a disk
to another disk (the destination disk does not have to be of the same size,
as it calculates the partition layout itself). Currently, ext2, ext3, minix, 
msdos, fat, vfat, reiserfs, xfs and jfs filesystems are supported.
One Button Disaster Recovery (OBDR) is also supported as recovery method.

%prep
%setup -n %{name}

%build
%{__make} -f Makefile.%{_boot_arch} build

%install
%{__rm} -rf %{buildroot}
find . -name CVS -exec rm -Rfv {} \;

%{__install} -Dp -m0755 busybox*/busybox %{buildroot}%{_optdir}/busybox/busybox
%{__install} -Dp -m0755 busybox*/busybox.links %{buildroot}%{_optdir}/busybox/busybox.links
%{__install} -Dp -m0755 busybox*/applets/install.sh %{buildroot}%{_optdir}/busybox/applets/install.sh

%{__install} -Dp -m0755 cutstream*/cutstream %{buildroot}%{_optdir}/bin/cutstream
%{__install} -Dp -m0755 pastestream*/pastestream %{buildroot}%{_optdir}/bin/pastestream
%{__install} -Dp -m0755 mediacheck/checkisomd5 %{buildroot}%{_optdir}/bin/checkisomd5
%{__install} -Dp -m0755 mediacheck/implantisomd5 %{buildroot}%{_optdir}/bin/implantisomd5

%{__install} -Dp -m0755 contributions/mkcdrec %{buildroot}%{_optdir}/contributions/mkcdrec
%{__install} -p -m0755 contributions/*.sh %{buildroot}%{_optdir}/contributions/

%{__install} -d -m0755 %{buildroot}%{_optdir}/scripts/messages/
%{__install} -p -m0644 scripts/messages/* %{buildroot}%{_optdir}/scripts/messages/

find modules/ scripts/ -type f -exec %{__install} -Dp -m0755 {} %{buildroot}%{_optdir}/{} \;

#%{__install} -d -m0755 %{buildroot}%{_optdir}/modules/
#%{__install} -Dp -m0755 modules/* %{buildroot}%{_optdir}/modules/

find etc/ usr/ -type f -exec %{__install} -Dp -m0644 {} %{buildroot}%{_optdir}/{} \;

find . -type f -maxdepth 1 -exec %{__install} -Dp -m0755 {} %{buildroot}%{_optdir}/{} \;

%{__install} -Dp -m0644 doc/autorun.inf %{buildroot}%{_optdir}/doc/autorun.inf
%{__install} -Dp -m0644 doc/README %{buildroot}%{_optdir}/doc/README
%{__install} -Dp -m0644 doc/CD-Rom.ico %{buildroot}%{_optdir}/doc/CD-Rom.ico

%{__install} -Dp -m0644 doc/mkcdrec.8 %{buildroot}%{_mandir}/man8/mkcdrec.8

%{__install} -Dp -m0750 contributions/mkcdrec %{buildroot}%{_sbindir}/mkcdrec

%{__rm} -f %{buildroot}%{_optdir}/.cvsignore
%{__rm} -f %{buildroot}%{_optdir}/COPYING
%{__rm} -f %{buildroot}%{_optdir}/Changelog
%{__rm} -f %{buildroot}%{_optdir}/README

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc Changelog COPYING README
%doc %{_optdir}/doc/
%doc %{_mandir}/man8/mkcdrec.8*
%config(noreplace) %{_optdir}/Config.sh
%{_optdir}/VERSION
%{_optdir}/.config.bb
%{_optdir}/busybox
%{_optdir}/bin/
%{_optdir}/contributions/
%{_optdir}/scripts/
%{_optdir}/modules/
%{_optdir}/etc/
%{_optdir}/usr/
%{_optdir}/linuxrc
%{_optdir}/linuxrc_find_and_prep_root
%{_optdir}/linuxrc_post
%{_optdir}/linuxrc_pre
%{_optdir}/Makefile
%{_optdir}/Makefile.new-powermac
%{_optdir}/Makefile.x86
%{_optdir}/Makefile.sparc
%{_optdir}/Makefile.ia64
%{_optdir}/Makefile.x86_64
%{_sbindir}/mkcdrec

%changelog
* Mon May 31 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
