# $Id$
# Authority: dag

Summary: Mindi creates emergency boot disks/CDs using your kernel, tools and modules
Name: mindi
Version: 2.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://www.mondorescue.org/
Source: ftp://ftp.mondorescue.org/src/mindi-%{version}.tar.gz

# Not yet possible as busybox is a binary that should go alongside
# BuildArch:	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: bzip2 >= 0.9, mkisofs, ncurses, binutils, gawk, dosfstools, mindi-busybox, parted, perl, mtools, which, grep >= 2.5

# Not on all systems
#Conflicts: bonnie++

%description
Mindi takes your kernel, modules, tools and libraries, and puts them on N
bootable disks (or 1 bootable CD image). You may then boot from the disks/CD
and do system maintenance - e.g. format partitions, backup/restore data,
verify packages, etc.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
export DONT_RELINK="1"
export HEAD="%{buildroot}"
export PREFIX="%{_prefix}"
export CONFDIR="%{_sysconfdir}"
export MANDIR="%{_mandir}"
#export DOCDIR="%{_docdir}"
export LIBDIR="%{_libdir}"
export CACHEDIR="%{_localstatedir}/cache/mindi"
export PKGBUILDMINDI="true"

sh -x install.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README* svn.log TODO
%doc %{_mandir}/man8/mindi.8*
%config(noreplace) %{_sysconfdir}/mindi/
%{_libdir}/mindi/
%{_localstatedir}/cache/mindi/
%{_sbindir}/mindi
%{_sbindir}/mindi-bkphw
%{_sbindir}/parted2fdisk
%{_sbindir}/parted2fdisk.pl

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Initial package. (using DAR)
