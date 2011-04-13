# $Id$
# Authority: dag

Summary: Tool to undelete files from MsDos/Windows disks (FAT filesystems)
Name: mundelete
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Aapplications/File
URL: http://sourceforge.net/projects/mundelete

Source: http://dl.sf.net/project/mundelete/mundelete/mundelete-%{version}/mundelete.tar.gz
Patch: mundelete-1.0-newgcc-alt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mundelete is a program to undelete files from MsDos/Windows disks. It
supports FAT12/FAT16/FAT32 and vfat extensions. It works under Unix
systems.

WARNING!!! Carefully read man page before usage and select the working
directory if possible. Otherwise the storage can be filled with old waste
and file system may be corrupted.

%prep
%setup -n %{name}
%patch -p1

%build
%{__rm} -rf {mundelete,bin/*}
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin/mundelete %{buildroot}/%{_bindir}/mundelete
%{__install} -Dp -m0644 man/mundelete.1 %{buildroot}/%{_mandir}/man1/mundelete.1

%files
%doc README
%doc %{_mandir}/man1/mundelete.1*
%{_bindir}/mundelete

%changelog
* Tue Feb 15 2011 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
