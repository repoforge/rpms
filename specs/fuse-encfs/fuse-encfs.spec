# $Id$
# Authority: dag

%define real_name encfs

Summary: Encrypted pass-thru filesystem in userspace
Name: fuse-encfs
Version: 1.3.2
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://arg0.net/wiki/encfs/

Source: http://arg0.net/vgough/download/encfs-%{version}-1.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, fuse-devel >= 2.2, rlog-devel >= 1.3
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
	--disable-static
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
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/libencfs.so*

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
