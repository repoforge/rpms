# $Id$

# Authority: dries

Summary: Programs and libs needed for manipulating reiserfs partitions
Name: progsreiserfs
Version: 0.3.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.namesys.com

Source: ftp://ftp.namesys.com/pub/libreiserfs/progsreiserfs-0.3.0.4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a library for reiserfs filesystem access and manipulation.
The primary goal is to develop the nice, full functionality library
wich might be linked against any projects which needed reiserfs filesystem
access. There are GNU Parted, GNU GRUB, Yaboot, Partimage, EVMS, etc.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
export LDFLAGS=-L`pwd`/libdal/.libs
%configure --enable-static=yes --enable-shared=yes
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%package devel
Summary: Progsreiserfs development files
Group: Development/Libraries
Requires: progsreiserfs = %{version}-%{release}

%description devel
Development files of progsreiserfs.

%package conflict
Summary: The files conflicting with the package reiserfs-utils
Group: Applications/System
Requires: progsreiserfs = %{version}-%{release}

%description conflict
This subpackage contains the files which are conflicting with the files of
the package reiserfs-utils.

%files
%defattr(-, root, root, 0755)
%{_libdir}/libdal-0.3.so.0.0.0
%{_libdir}/libdal-0.3.so.0
%{_libdir}/libreiserfs-0.3.so.0.0.0
%{_libdir}/libreiserfs-0.3.so.0
%{_sbindir}/cpfs.reiserfs
%{_sbindir}/resizefs.reiserfs
%{_sbindir}/tunefs.reiserfs
%{_datadir}/aclocal/progsreiserfs.m4
%{_mandir}/man8/cpfs.reiserfs.8.gz
%{_mandir}/man8/mkfs.reiserfs.8.gz
%{_mandir}/man8/reiserfs.8.gz
%{_mandir}/man8/resizefs.reiserfs.8.gz
%{_mandir}/man8/tunefs.reiserfs.8.gz

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/dal
%{_includedir}/reiserfs
%{_libdir}/libdal.so
%{_libdir}/libdal.a
%{_libdir}/libdal.la
%{_libdir}/libreiserfs.a
%{_libdir}/libreiserfs.la
%{_libdir}/libreiserfs.so

%files conflict
%defattr(-, root, root, 0755)
%{_sbindir}/fsck.reiserfs
%{_sbindir}/mkfs.reiserfs

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0.4-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 3 2004 Dries Verachtert 0.3.0.4-1
- first packaging for Fedora Core 1
