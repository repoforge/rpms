# $Id$
# Authority: dag


### EL4 and older has too old gnutls :-/
%{?el4:%define _without_crypto 1}
%{?el3:%define _without_crypto 1}
%{?rh9:%define _without_crypto 1}
%{?rh7:%define _without_crypto 1}
%{?el2:%define _without_crypto 1}

%{?rh7:%define _without_gnomevfs 1}
%{?el2:%define _without_gnomevfs 1}
%{?rh6:%define _without_gnomevfs 1}

Summary: NTFS filesystem libraries and utilities
Name: ntfsprogs
Version: 1.13.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://linux-ntfs.sourceforge.net/

Source: http://dl.sf.net/linux-ntfs/ntfsprogs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{!?_without_crypto:BuildRequires: libgcrypt-devel, gnutls >= 1.2.8}
%{!?_without_gnomevfs:BuildRequires: glib2-devel, gnome-vfs2-devel}

%description
The Linux-NTFS project aims to bring full support for the NTFS filesystem
to the Linux operating system. Linux-NTFS currently consists of a static
library and utilities such as mkntfs, ntfscat, ntfsls, ntfsresize, and
ntfsundelete (for a full list of included utilities see man 8 ntfsprogs).

%package -n gnome-vfs2-ntfs
Summary: NTFS GNOME virtual filesystem module
Group: System Environment/Base
Requires: %{name} = %{version}-%{release}

%description -n gnome-vfs2-ntfs
This package contains the NTFS GNOME virtual filesystem (VFS) module which
allows GNOME VFS clients to seamlessly utilize the NTFS library.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --disable-fuse-module \
    --disable-static \
%{!?_without_crypto:--enable-crypto} \
%{!?_without_gnomevfs:--enable-gnome-vfs}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la
%{__rm} -f %{buildroot}%{_libdir}/gnome-vfs-2.0/modules/*.{a,la,so.*}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README TODO*
%doc %{_mandir}/man8/mkfs.ntfs.8*
%doc %{_mandir}/man8/mkntfs.8*
%doc %{_mandir}/man8/ntfs*.8*
%{_bindir}/ntfscat
%{_bindir}/ntfscluster
%{_bindir}/ntfscmp
%{_bindir}/ntfsfix
%{_bindir}/ntfsinfo
%{_bindir}/ntfsls
%{_libdir}/libntfs.so.*
%{_sbindir}/mkntfs
%{_sbindir}/ntfsclone
%{_sbindir}/ntfscp
%{_sbindir}/ntfslabel
%{_sbindir}/ntfsresize
%{_sbindir}/ntfsundelete
/sbin/mkfs.ntfs

%if %{!?_without_gnomevfs:1}0
%files -n gnome-vfs2-ntfs
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/libntfs-gnomevfs.8*
%config %{_sysconfdir}/gnome-vfs-2.0/modules/libntfs.conf
%{_libdir}/gnome-vfs-2.0/modules/*.so
%endif

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.txt doc/attribute_definitions doc/CodingStyle doc/template.c doc/template.h doc/tunable_settings
%{_includedir}/ntfs/
%{_libdir}/libntfs.so

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 1.13.1-1
- Updated to release 1.13.1.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 1.9.4-1
- Updated to release 1.9.4.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 1.9.0-1
- Updated to release 1.9.0.

* Mon Mar 01 2004 Dag Wieers <dag@wieers.com> - 1.8.5-0
- Updated to release 1.8.5.

* Fri Feb 13 2004 Dag Wieers <dag@wieers.com> - 1.8.4-0
- Initial package. (using DAR)
