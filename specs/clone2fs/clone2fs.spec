# $Id$
# Authority: dag

%define _sbindir /sbin

Summary: Tool to clone ext2/ext3 filesystems
Name: clone2fs
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.mr511.de/software/

Source: http://www.mr511.de/software/clone2fs-%{version}.tar.gz
Patch1: clone2fs-1.2.0-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel

%description
clone2fs is a utility to clone an ext2/ext3 filesystem.

Unlike dd, clone2fs does not copy the whole volume but only blocks that are
actually in use. Therefore, it is usually faster. It's also faster than
dump/restore, tar or similar backup software because it accesses the source
and destination volumes sequentially most of the time.

Note that clone2fs allows you to clone a mounted file system without warning,
even if it's writable. In the latter case, you have to run e2fsck on the
resulting image in order to make it consistent. Since copying takes a while,
changes made while clone2fs is working may or may not appear in the clone. If
you need an exact clone, umount the source file system, or remount it in
read-only mode.

%prep
%setup
%patch1

%build
%{__make} %{?_smp_mflags} CC="%{__cc}" OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README
%{_sbindir}/clone2fs

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
