# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Distcc: 0
# BuildAsRoot: 1

%{?dtag: %{expand: %%define %dtag 1}}

### FIXME: IBM openafs-1.2.9-rh9.0.5 and openafs-kernel-1.2.9-rh9.0.5 conflict with these packages.

### FIXME: Quick fix, real solution still undetermined
%define _unpackaged_files_terminate_build 0

%ifarch i386 i586 i686 athlon
%define sysname i386_linux24
%endif
%ifarch alpha
%define sysname alpha_linux24
%endif
%ifarch ia64
%define sysname ia64_linux24
%endif
%ifarch ppc ppc64
%define sysname ppc_linux24
%endif
%ifarch s390
%define sysname s390_linux24
%endif

Summary: OpenAFS distributed filesystem
Name: openafs
Version: 1.2.10
Release: 0%{?dist}
License: IBM Public License
Group: System Environment/Daemons
URL: http://www.openafs.org/

Source0: http://www.openafs.org/dl/openafs/%{version}/openafs-%{version}-src.tar.bz2
### http://grand.central.org/dl/cellservdb/CellServDB
Source5: openafs-CellServDB
Source6: openafs-afsmodname
Patch0: openafs-1.2.9-rc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf, automake
#BuildRequires: kernel-source %{!?rh62:, pam-devel}
Requires: kernel-module-openafs = %{version}

%description
The AFS distributed filesystem.  AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides common files shared across all the various
OpenAFS packages but are not necessarily tied to a client or server.

%package client
Summary: OpenAFS Filesystem Client
Group: System Environment/Daemons
Requires: binutils, openafs = %{version}-%{release}

%description client
This package provides basic client support to mount and manipulate
AFS.

%package server
Summary: OpenAFS Filesystem Server
Group: System Environment/Daemons
Requires: openafs = %{version}-%{release}

%description server
This package provides basic server support to host files in an AFS
Cell.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

#%package compat
#Summary: OpenAFS client compatibility symlinks
#Group: Networking/Filesystems
#Requires: openafs = %{version}-%{release}, openafs-client = %{version}-%{release}
#Obsoletes: openafs-client-compat
#
#%description compat
#This package provides compatibility symlinks in /usr/afsws.  It is
#completely optional, and is only necessary to support legacy
#applications and scripts that hard-code the location of AFS client
#programs.

%prep
%setup
%patch0 -p0 -b .rc

touch SuidCells
echo "openafs.org" > ThisCell
echo "/afs:/usr/vice/cache:100000" > cacheinfo

%build
%{__aclocal} -I src/cf
%{__autoconf}
%{__autoconf} configure-libafs.in > configure-libafs
chmod +x configure-libafs
%{__autoheader}

./configure \
	--with-afs-sysname="%{sysname}" \
	--enable-redhat-buildsys \
	--enable-transarc-paths

#	--with-linux-kernel-headers="/lib/modules/%{kversion}-%{krelease}/build/include" \
#	--enable-bitmap-later \
#	--enable-bos-restricted-mode \
#	--enable-fast-restart \

### Build the user-space AFS stuff and the libafs tree
%{__make} %{?_smp_mflags} dest_nolibafs only_libafs_tree

%install
%{__rm} -rf %{buildroot}
%makeinstall
#%{__install} -d -m0755 %{buildroot}%{_sbindir} \
#			%{buildroot}%{_sysconfdir}/sysconfig \
#			%{buildroot}%{_sysconfdir}/openafs \
#			%{buildroot}%{_initrddir} \
#			%{buildroot}/lib/security \
#			%{buildroot}%{_prefix}/afs/logs \
#			%{buildroot}%{_prefix}/vice/etc
#%{__install} -d -m0700 %{buildroot}%{_prefix}/vice/cache

### Copy files from dest to the appropriate places in BuildRoot
#%{__cp} -av %{sysname}/dest/bin/* %{buildroot}%{_bindir}
#%{__cp} -av %{sysname}/dest/include/* %{buildroot}%{_includedir}
#%{__cp} -av %{sysname}/dest/lib/* %{buildroot}%{_libdir}
#%{__cp} -av %{sysname}/dest/etc/* %{buildroot}%{_sbindir}
#%{__cp} -av %{sysname}/dest/root.server/usr/afs/bin/* %{buildroot}%{_prefix}/afs/
#%{__cp} -av %{sysname}/dest/root.client/usr/vice/etc/afsd/* %{buildroot}%{_prefix}/vice/etc/
#%{__cp} -av %{sysname}/dest/root.client/usr/vice/etc/modload/* %{buildroot}%{_prefix}/vice/etc/

### Link kpasswd to kapasswd
#%{__ln_s} -f kpasswd %{buildroot}%{_bindir}/kapasswd

### Copy root.client config files
%{__install} -Dp -m0755 %{sysname}/dest/root.client/usr/vice/etc/afs.conf %{buildroot}%{_sysconfdir}/sysconfig/afs
%{__install} -Dp -m0755 %{sysname}/dest/root.client/usr/vice/etc/afs.rc %{buildroot}%{_initrddir}/afs

### Copy PAM modules
#%{__install} -p -m0755 %{sysname}/dest/lib/pam* %{buildroot}/lib/security/
#%{__ln_s} -f pam_afs.so.1 %{buildroot}/lib/security/pam_afs.so
#%{__ln_s} -f pam_afs.krb.so.1 %{buildroot}/lib/security/pam_afs.krb.so

### Populate /usr/vice/etc
#%{__install} -p -m0644 cacheinfo SuidCells ThisCell %{buildroot}%{_prefix}/vice/etc/
#%{__install} -p -m0644 %{SOURCE5} %{buildroot}%{_prefix}/vice/etc/CellServDB
#%{__install} -p -m0755 %{SOURCE6} %{buildroot}%{_prefix}/vice/etc/afsmodname

### Install DOCUMENTATION
### Build the DOC directory
#%{__install} -d -m0755 %{buildroot}%{_docdir}/openafs-%{version}
#tar cf - -C doc LICENSE html pdf | tar xf - -C %{buildroot}%{_docdir}/openafs-%{version}/
##install -m0644 %{buildroot}%{_docdir}/openafs-%{version}
##install -m0644 %{buildroot}%{_docdir}/openafs-%{version}

### Create filelist
#grep -v "^#" <<EOF >openafs-file-list
#/usr/bin/afsmonitor
#/usr/bin/bos
#/usr/bin/fs
#/usr/bin/kapasswd
#/usr/bin/kpasswd
#/usr/bin/klog
#/usr/bin/klog.krb
#/usr/bin/pagsh
#/usr/bin/pagsh.krb
#/usr/bin/pts
#/usr/bin/scout
#/usr/bin/sys
#/usr/bin/tokens
#/usr/bin/tokens.krb
#/usr/bin/translate_et
#/usr/bin/udebug
#/usr/bin/unlog
#/usr/sbin/backup
#/usr/sbin/butc
#/usr/sbin/fms
#/usr/sbin/fstrace
#/usr/sbin/kas
#/usr/sbin/read_tape
#/usr/sbin/restorevol
#/usr/sbin/rxdebug
#/usr/sbin/uss
#/usr/sbin/vos
#EOF

### Install compatiblity links
#for pair in bin:bin etc:sbin; do
#	olddir="${pair/:*}"
#	newdir="${pair/*:}"
#
#	%{__install} -d -m0755 %{buildroot}%{_prefix}/afsws/$olddir
#	for f in $(cat openafs-file-list); do
#		if echo "$f" | grep -q "/$newdir/"; then
#			fb="$(basename $f)"
#			%{__ln_s} -f %{_prefix}/$newdir/$fb %{buildroot}%{_prefix}/afsws/$olddir/$fb
#		fi
#	done
#done

%clean
%{__rm} -rf %{buildroot}

#%pre compat
#if [ -e %{_prefix}/afsws ]; then
#        %{__rm} -rf %{_prefix}/afsws
#fi

%post
/sbin/chkconfig --add afs

%post client
### If this is inside the package, live updates will fail.
if [ ! -d /afs ]; then
	%{__install} -d -m0700 -o0 -g0 /afs
fi

#echo
#echo The AFS cache is configured for 100 MB. Edit the
#echo %{_prefix}/vice/etc/cacheinfo file to change this before
#echo running AFS for the first time. You should also
#echo set your home cell in %{_prefix}/vice/etc/ThisCell.
#echo
#echo Also, you may want to edit /etc/pam.d/login and
#echo possibly others there to get an AFS token on login.
#echo Put the line:
#echo
#echo    auth	   sufficient   /lib/security/pam_afs.so try_first_pass ignore_root
#echo
#echo before the one for pwdb.
#echo

%post server
if [ -f %{_sysconfdir}/sysconfig/afs ] ; then
	srv="$(grep ^AFS_SERVER %{_sysconfdir}/sysconfig/afs | sed 's/^AFS_SERVER[\s]*=[\s]*//')"
	if [ "$srv" == "on" ] ; then
		exit 0
	fi
fi

#echo
#echo Be sure to edit /etc/sysconfig/afs and turn AFS_SERVER on
#echo

%preun
if [ $1 -eq 0 ] ; then
        /sbin/service afs stop
        /sbin/chkconfig --del afs
	[ -d /afs ] && rmdir /afs
fi

### file lists
%files -f openafs-file-list
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/sysconfig/afs
%config %{_initrddir}/afs

%files client
%defattr(-, root, root, 0755)
%dir %{_prefix}/vice
%dir %{_prefix}/vice/cache
%config %{_prefix}/vice/etc/
%{_bindir}/cmdebug
%{_bindir}/up
/lib/security/pam_afs.krb.so.1
/lib/security/pam_afs.krb.so
/lib/security/pam_afs.so.1
/lib/security/pam_afs.so

%files server
%defattr(-, root, root, 0755)
%{_prefix}/afs/
%{_sbindir}/prdb_check
%{_sbindir}/vldb_check
%{_sbindir}/vldb_convert

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/rxgen
%{_includedir}/afs/
%{_includedir}/*.h
%{_includedir}/rx/
%{_libdir}/afs/
%{_libdir}/*.a

#%files compat
#%defattr(-, root, root, 0755)
#%{_prefix}/afsws/
#%{_bindir}/kpasswd
#%{_bindir}/kpwvalid

%changelog
* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 1.2.10-0
- Updated to release 1.2.10.

* Wed May 21 2003 Dag Wieers <dag@wieers.com> - 1.2.9-0
- Initial package. (using DAR)
