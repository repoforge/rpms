# $Id$
# Authority: dag

%define _without_ntfs 1

Summary: Tool to check and undelete partition
Name: testdisk
Version: 6.4
Release: 1
License: GPL
Group: Applications/System
URL: http://www.cgsecurity.org/wiki/TestDisk

Source: http://www.cgsecurity.org/testdisk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel >= 5.2, e2fsprogs-devel, libjpeg-devel

%description
Tool to check and undelete partition. Works with FAT12, FAT16, FAT32, EXT2,
EXT3, BeFS, CramFS, HFS, JFS, Linux Raid, Linux Swap, LVM, LVM2, NSS,
ReiserFS, UFS, XFS

%prep
%setup

%build
%configure \
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
* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 6.4-1
- Initial package. (using DAR)
