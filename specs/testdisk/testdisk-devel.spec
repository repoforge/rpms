# $Id$
# Authority: dag

# Tag: test

%{?rh7:%define _without_ewf 1}
%{?rh7:%define _without_ntfs 1}

%{?el2:%define _without_ntfs 1}

Summary: Tools to check and undelete partition or recover deleted files
Name: testdisk
%define real_version 6.10-WIP
Version: 6.10
Release: 0.wip20080522
License: GPL
Group: Applications/System
URL: http://www.cgsecurity.org/wiki/TestDisk

Source: http://www.cgsecurity.org/testdisk-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel
BuildRequires: libjpeg-devel
BuildRequires: ncurses-devel >= 5.2
%{!?_without_ewf:BuildRequires: libewf-devel}
%{!?_without_ntfs:BuildRequires: ntfsprogs-devel}

%description
The testdisk package contains the testdisk tool. This tool can check and
undelete partition information. It works with FAT12, FAT16, FAT32, EXT2,
EXT3, BeFS, CramFS, HFS, JFS, Linux Raid, Linux Swap, LVM, LVM2, NSS,
ReiserFS, UFS, XFS.

It also includes the photorec tool. This tool allows to recover deleted
files from filesystems.

%prep
%setup -n %{name}-%{real_version}

%build
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
%exclude %{_docdir}/%{name}-%{real_version}

%changelog
* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 6.10-0.wip20080522
- Updated to release 6.10-WIP.
- Built with ewf and ntfs support.

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
