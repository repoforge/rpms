# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

### xfsprogs abuses libexecdir
%{expand: %%define _libexecdir %{_libdir}}
%{expand: %%define _libdir /%{_lib}}
%{expand: %%define _bindir %{_sbindir}}
%{expand: %%define _sbindir /sbin}

Summary: Utilities for managing the XFS filesystem
Name: xfsprogs
Version: 2.6.13
Release: 3%{?dist}
License: GPL
Group: System Environment/Base
URL: http://oss.sgi.com/projects/xfs/

Source: ftp://oss.sgi.com/projects/xfs/download/cmd_tars/xfsprogs-%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, libtool, gettext
BuildRequires: readline-devel, libtermcap-devel
BuildRequires: /usr/include/uuid/uuid.h
Provides: xfs-cmds = %{version}-%{release}
Obsoletes: xfs-cmds <= %{version}
Conflicts: xfsdump < 2.0.0

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

Refer to the documentation at http://oss.sgi.com/projects/xfs/
for complete details.  This implementation is on-disk compatible
with the IRIX version of XFS.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export tagname=CC
%configure \
	--enable-shared="yes" \
	--enable-gettext="yes" \
	--enable-readline="yes" \
	--enable-editline="no" \
	--enable-shared-uuid="yes"
%{__make} %{?_sm_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install install-dev \
	DIST_ROOT="%{buildroot}"

### nuke .la files, etc
#rm -f $RPM_BUILD_ROOT/%{_lib}/*.la $RPM_BUILD_ROOT/{_lib}/*.a $RPM_BUILD_ROOT%{_lib}/*.so

### fix up symlink to be correct
%{__ln_s} -f ../../%{_lib}/libhandle.so.1 %{buildroot}%{_libdir}/libhandle.so

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>dev/null || :

%postun
/sbin/ldconfig 2>dev/null || :

%files
%defattr(-, root, root, 0755)
%doc doc/CHANGES doc/COPYING doc/CREDITS doc/PORTING README doc/README.LVM doc/README.quota
%doc %{_mandir}/man5/*
%doc %{_mandir}/man8/*
%{_bindir}/*
%{_sbindir}/fsck.xfs
%{_sbindir}/mkfs.xfs
%{_sbindir}/xfs_repair
%{_libdir}/*.so.*
%exclude %{_docdir}/xfsprogs/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{_includedir}/disk/
%{_includedir}/xfs/
%{_libdir}/*.a
#exclude %{_libdir}/*.la
%{_libdir}/*.so
%exclude %{_libexecdir}/*.a
%exclude %{_libexecdir}/*.la

%changelog
* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 2.6.13-3
- Imported from RH CVS.

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> - 2.6.13-3
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  5 2004 Jeremy Katz <katzj@redhat.com> - 2.6.13-1
- update to 2.6.13 per request of upstream
- fixes mount by label of xfs on former raid partition (#122043)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan  8 2004 Jeremy Katz <katzj@redhat.com> 2.6.0-2
- add defattr (reported by Matthias)

* Tue Dec 23 2003 Elliot Lee <sopwith@redhat.com> 2.6.0-3
- Fix tyops in dependencies

* Mon Dec 22 2003 Jeremy Katz <katzj@redhat.com> 2.6.0-1
- build for Fedora Core
- switch to more explicit file lists, nuke .la files

* Tue Dec 16 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.6.0
- Update to 2.6.0.

* Sat Sep 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Sync with XFS 1.3.0.
- Update to 2.5.6.

* Thu Apr 10 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.3.9-0_2.90at
- Rebuilt for Red Hat 9.

