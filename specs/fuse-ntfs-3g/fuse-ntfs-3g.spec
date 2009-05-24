# $Id$
# Authority: dag

%define _sbindir /sbin

%define real_name ntfs-3g

Summary: Linux NTFS userspace driver 
Name: fuse-ntfs-3g
Version: 2009.4.4
Release: 2
License: GPL
Group: System Environment/Kernel
URL: http://www.ntfs-3g.org/

Source: http://www.ntfs-3g.org/ntfs-3g-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.6.3
Requires: fuse >= 2.6.3

Provides: ntfsprogs-fuse = %{version}-%{release}
Obsoletes: ntfsprogs-fuse <= %{version}-%{release}
Obsoletes: ntfs-3g <= %{version}-%{release}
Provides: ntfs-3g = %{version}-%{release}

%description
The ntfs-3g driver is an open source, GPL licensed, third generation Linux NTFS
driver. It provides full read-write access to NTFS, excluding access to
encrypted files, writing compressed files, changing file ownership, access
right.

Technically it’s based on and a major improvement to the third generation Linux
NTFS driver, ntfsmount. The improvements include functionality, quality and
performance enhancements.

ntfs-3g features are being merged to ntfsmount. In the meanwhile, ntfs-3g is
currently the only free, as in either speech or beer, NTFS driver for Linux
that supports unlimited file creation and deletion.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: ntfs-3g-devel <= %{version}-%{release}
Provides: ntfs-3g-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-ldconfig \
    --disable-static \
    --enable-mount-helper
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Symlink different locations
%{__ln_s} -f %{_bindir}/ntfs-3g %{buildroot}%{_sbindir}/mount.ntfs
%{__ln_s} -f %{_bindir}/ntfs-3g %{buildroot}%{_sbindir}/mount.ntfs-3g
%{__ln_s} -f %{_bindir}/ntfs-3g %{buildroot}%{_bindir}/ntfsmount

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* CREDITS NEWS README
%doc %{_mandir}/man8/mount.ntfs-3g.8*
%doc %{_mandir}/man8/ntfs-3g.8*
%doc %{_mandir}/man8/ntfs-3g.probe.8*
%{_sbindir}/mount.ntfs
%{_sbindir}/mount.ntfs-3g
%{_bindir}/ntfs-3g
%{_bindir}/ntfs-3g.probe
%{_bindir}/ntfsmount
%{_libdir}/libntfs-3g.so.*
%exclude %{_docdir}/ntfs-3g/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so
%{_libdir}/pkgconfig/libntfs-3g.pc
%exclude %{_libdir}/libntfs-3g.la

%changelog
* Thu May 21 2009 Dag Wieers <dag@wieers.com> - 2009.4.4-2
- Added symlink for mount.ntfs so Gnome's Disk Mounter applet doesn't crash.

* Tue May 05 2009 Dag Wieers <dag@wieers.com> - 2009.4.4-1
- Updated to release 2009.4.4.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 2009.2.1-1
- Updated to release 2009.2.1.

* Sat Jan 24 2009 Dag Wieers <dag@wieers.com> - 2009.1.1-1
- Updated to release 2009.1.1.

* Mon Dec 01 2008 Dag Wieers <dag@wieers.com> - 1.5130-1
- Updated to release 1.5130.

* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 1.5012-1
- Updated to release 1.5012.

* Thu Sep 18 2008 Dag Wieers <dag@wieers.com> - 1.2918-1
- Updated to release 1.2918.

* Thu Aug 28 2008 Dag Wieers <dag@wieers.com> - 1.2812-1
- Updated to release 1.2812.

* Mon Jul 14 2008 Dag Wieers <dag@wieers.com> - 1.2712-1
- Updated to release 1.2712.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 1.2531-1
- Updated to release 1.2531.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 1.2506-1
- Updated to release 1.2506.

* Thu Apr 17 2008 Dag Wieers <dag@wieers.com> - 1.2412-1
- Updated to release 1.2412.

* Wed Mar 12 2008 Dag Wieers <dag@wieers.com> - 1.2310-1
- Updated to release 1.2310.

* Sun Feb 17 2008 Dag Wieers <dag@wieers.com> - 1.2216-1
- Updated to release 1.2216.

* Tue Nov 20 2007 Dag Wieers <dag@wieers.com> - 1.1120-1
- Updated to release 1.1120.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.1104-1
- Updated to release 1.1104.

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 1.1030-1
- Updated to release 1.1030.

* Fri Oct 05 2007 Dag Wieers <dag@wieers.com> - 1.1004-1
- Updated to release 1.1004.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 1.913-1
- Updated to release 1.913.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 1.616-1
- Updated to release 1.616.

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 1.417-2
- Symlink mount binaries instead of hardlink (different mountpoints). (Jon Wilson)

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.417-1
- Initial package. (using DAR)
