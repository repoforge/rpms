# $Id$
# Authority: dag

%define real_name cryptofs

Summary: FUSE-based user-space encrypted filesystem
Name: fuse-cryptofs
Version: 0.6.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://reboot.animeirc.de/cryptofs/

Source: http://reboot.animeirc.de/cryptofs/cryptofs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel >= 2.2, libgcrypt-devel, pinentry, glib2-devel >= 2.6
Requires: fuse >= 2.2

Obsoletes: cryptofs <= %{name}-%{version}
Provides: cryptofs = %{name}-%{version}

%description
CryptoFS will use a normal directory to store files encrypted. The mountpoint
will contain the decrypted files. Every file stored in this mountpoint will be
written encrypted (data and filename) to the directory that was mounted. If you
unmount the directory the encrypted data can only be access by mounting the
directory with the correct key again. Like other FUSE/LUFS filesystems it does
not need root access or any complicated setup like creating a filesystem on a
encrypted disk using the loop device.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-static \
	--disable-lufs
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README cryptofs.conf
%{_bindir}/cryptofs

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Initial package. (using DAR)
