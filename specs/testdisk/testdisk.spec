# $Id$
# Authority: dag

### Problem when building testdisk 0.6.9 with EWF 20080501
#define _without_ewf 1

### Build doesn't use libcarvpath, due to errors with libcarvpath 1.0.0
%define _without_libcarvpath 1

%{?el5:%define _without_libuuid 1}

%{?el4:%define _without_libcarvpath 1}
%{?el4:%define _without_libuuid 1}

%{?el3:%define _without_libcarvpath 1}
%{?el3:%define _without_libuuid 1}

%{?el2:%define _without_libcarvpath 1}
%{?el2:%define _without_libuuid 1}
%{?el2:%define _without_ntfs 1}

Summary: Tools to check and undelete partition or recover deleted files
Name: testdisk
Version: 6.11.3
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.cgsecurity.org/wiki/TestDisk

Source: http://www.cgsecurity.org/testdisk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel
BuildRequires: libjpeg-devel
BuildRequires: ncurses-devel >= 5.2
%{!?_without_ewf:BuildRequires: libewf-devel}
%{!?_without_libcarvpath:BuildRequires: libcarvpath-devel}
%{!?_without_libuuid:BuildRequires: libuuid-devel}
%{!?_without_ntfs:BuildRequires: ntfsprogs-devel}

%description
The testdisk package contains the testdisk tool. This tool can check and
undelete partition information. It works with FAT12, FAT16, FAT32, EXT2,
EXT3, BeFS, CramFS, HFS, JFS, Linux Raid, Linux Swap, LVM, LVM2, NSS,
ReiserFS, UFS, XFS.

It also includes the photorec tool. This tool allows to recover deleted
files from filesystems.

%prep
%setup

%build
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE"
%configure \
    --program-prefix="%{?_program_prefix}" \
%{?_without_ewf:--without-ewf} \
%{?_without_ntfs:--without-ntfs}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS doc/
%doc %{_mandir}/man1/photorec.1*
%doc %{_mandir}/man1/testdisk.1*
%{_sbindir}/photorec
%{_sbindir}/testdisk

%changelog
* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 6.11.3-2
- Rebuilt against libewf-20100226.

* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 6.11.3-1
- Updated to release 6.11.3.

* Mon Apr 20 2009 Dag Wieers <dag@wieers.com> - 6.11-1
- Updated to release 6.11.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 6.10-1
- Updated to release 6.10.

* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 6.9-2
- Built with ntfs support.

* Thu Feb 14 2008 Dag Wieers <dag@wieers.com> - 6.9-1
- Updated to release 6.9.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 6.8-1
- Updated to release 6.8.

* Wed Jun 27 2007 Dag Wieers <dag@wieers.com> - 6.7-1
- Updated to release 6.7.

* Sun Feb 18 2007 Dag Wieers <dag@wieers.com> - 6.6-1
- Updated to release 6.6.

* Wed Nov 08 2006 Dag Wieers <dag@wieers.com> - 6.5-1
- Updated to release 6.5.

* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 6.4-1
- Initial package. (using DAR)
