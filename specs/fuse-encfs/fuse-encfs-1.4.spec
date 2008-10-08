# $Id$
# Authority: dag

%define real_name encfs

Summary: Encrypted pass-thru filesystem in userspace
Name: fuse-encfs
Version: 1.4.1
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.arg0.net/encfs

#Source: http://www.arg0.net/encfs-1.4.1.tgz
Source: http://encfs.googlecode.com/files/encfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel
BuildRequires: fuse-devel >= 2.2
BuildRequires: openssl-devel
BuildRequires: rlog-devel >= 1.3
BuildRequires: rlog-devel < 1.4
Requires: fuse >= 2.2

Obsoletes: encfs <= %{name}-%{version}
Provides: encfs = %{name}-%{version}

%description
EncFS implements an encrypted filesystem in userspace using FUSE. FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace. EncFS encrypts all data and filenames in the filesystem and
passes access through to the underlying filesystem. Similar to CFS except that
it does not use NFS. 

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-static \
    --disable-valgrind
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/encfs.1*
%doc %{_mandir}/man1/encfsctl.1*
%{_bindir}/encfs
%{_bindir}/encfsctl
%{_bindir}/encfssh
%{_libdir}/libencfs.so*
%exclude %{_libdir}/libencfs.la

%changelog
* Sun Jan 13 2008 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Tue Jan 08 2008 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
