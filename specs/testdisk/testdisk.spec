# $Id$
# Authority: dag

%define _without_ntfs 1

Summary: Tools to check and undelete partition or recover deleted files
Name: testdisk
Version: 6.6
Release: 1
License: GPL
Group: Applications/System
URL: http://www.cgsecurity.org/wiki/TestDisk

Source: http://www.cgsecurity.org/testdisk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 5.2, e2fsprogs-devel, libjpeg-devel

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
%configure \
	--program-prefix="%{?_program_prefix}" \
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
* Sun Feb 18 2007 Dag Wieers <dag@wieers.com> - 6.6-1
- Updated to release 6.6.

* Wed Nov 08 2006 Dag Wieers <dag@wieers.com> - 6.5-1
- Updated to release 6.5.

* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 6.4-1
- Initial package. (using DAR)
