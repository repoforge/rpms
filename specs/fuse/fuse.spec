# $Id$
# Authority: dag

### RHEL 5.4 ships with fuse 2.7.4-8.el5
# ExclusiveDist: el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_udev 1}

Summary: File System in Userspace (FUSE) utilities
Name: fuse
Version: 2.7.4
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://fuse.sourceforge.net/

Source: http://dl.sourceforge.net/sourceforge/fuse/fuse-%{version}.tar.gz
Patch: fuse-udev_rules.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires(pre): %{_sbindir}/groupadd
%{!?_without_udev:Requires(post): /sbin/MAKEDEV}
Requires(postun): %{_sbindir}/groupdel
Provides: fuse-libs = %{version}-%{release}
Obsoletes: fuse-libs <= %{version}-%{release}
provides: libfuse = %{version}-%{release}
Obsoletes: libfuse <= %{version}-%{release}

%description
With FUSE it is possible to implement a fully functional filesystem in a 
userspace program. This package contains the FUSE userspace tools to 
mount a FUSE filesystem.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
License: LGPL
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%{__perl} -pi.orig -e '
        s|chown root|echo chown root|;
        s|mknod|echo mknod|;
    ' util/Makefile.in
%patch0 -b .patch0

%{__cat} <<EOF >README.security
This fuse package for security reasons only allows members of the group "fuse"
to (u)mount fuse filesystems. If you for example want to allow the user "foo" 
to mount fuse filesystems you have to add him to the fuse group by running

    # /usr/sbin/usermod -a -G fuse foo

Or use tools like "system-config-users" to add user "foo" to the fuse group.

Note that the user has to re-login after he was added to the group.


If you do not want to add all users to the fuse group you can also run

    # chmod 4755 /usr/bin/fusermount

to allow everyone to mount fuse filesystems. You have to re-run that command
after each fuse update.
EOF

%{__cat} <<EOF >fuse-makedev.d-fuse
c 660 root     fuse      10 229  1   1 fuse
EOF

%{__cat} <<EOF >fuse-udev.nodes
fuse
EOF

%{__ln_s} ../lib util/lib

%build
### Kernel module is part of dkms-fuse
%configure \
    --disable-static \
    --disable-kernel-module 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{!?_without_udev:1}0
%{__install} -Dp -m0644 fuse-udev.nodes %{buildroot}%{_sysconfdir}/udev/makedev.d/99-fuse.nodes
%{__install} -Dp -m0644 fuse-makedev.d-fuse %{buildroot}%{_sysconfdir}/makedev.d/z-fuse
%else
mkdir -p %{buildroot}/dev/
touch %{buildroot}/dev/fuse
%endif

### 4755 -> 0755 to enable stripping
%{__chmod} 0755 %{buildroot}%{_bindir}/fusermount

%clean
%{__rm} -rf %{buildroot}

%pre 
if [ $1 -eq 1 ]; then
    %{_sbindir}/groupadd -r fuse &>/dev/null || :
fi

%post
%if %{!?_without_udev:1}0
/sbin/MAKEDEV fuse
%else
mknod -m0600 /dev/fuse c 10 229
chown root:fuse /dev/fuse
%endif
/sbin/ldconfig

%postun 
if [ $1 -eq 0 ]; then
    %{_sbindir}/groupdel fuse || :
fi
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYING.LIB FAQ Filesystems NEWS README README.NFS README.security
%config %{_sysconfdir}/init.d/fuse
%if %{!?_without_udev:1}0
%dir %{_sysconfdir}/udev/
%dir %{_sysconfdir}/udev/rules.d/
%config %{_sysconfdir}/udev/rules.d/99-fuse.rules
%dir %{_sysconfdir}/makedev.d/
%{_sysconfdir}/makedev.d/z-fuse
%dir %{_sysconfdir}/udev/
%dir %{_sysconfdir}/udev/makedev.d/
%{_sysconfdir}/udev/makedev.d/99-fuse.nodes
%else
%ghost /dev/fuse
%exclude %{_sysconfdir}/udev/rules.d/99-fuse.rules
%endif
/sbin/mount.fuse
%{_bindir}/ulockmgr_server
%{_libdir}/libfuse.so.*
%{_libdir}/libulockmgr.so.*

%defattr(4754, root, fuse, 0755)
%{_bindir}/fusermount

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_includedir}/fuse/
%{_includedir}/fuse.h
%{_includedir}/ulockmgr.h
%{_libdir}/libfuse.so
%{_libdir}/libulockmgr.so
%{_libdir}/pkgconfig/fuse.pc
%exclude %{_libdir}/libfuse.la
%exclude %{_libdir}/libulockmgr.la

%changelog
* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 2.7.4-1
- Updated to release 2.7.4.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 2.7.3-1
- Updated to release 2.7.3.

* Thu Feb 07 2008 Dag Wieers <dag@wieers.com> - 2.7.2-1
- Updated to release 2.7.2.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.7.0-2
- Added compatibility Provides and Obsoletes for ATrpms.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Updated to release 2.7.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 2.6.5-1
- Updated to release 2.6.5.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 2.6.3-1
- Initial package. (using DAR)
