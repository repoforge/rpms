# $Id$

# Authority: dag

%define rversion 2.08

Summary: Simple kernel loader which boots from a FAT filesystem.
Name: syslinux
Version: 2.08
Release: 0
License: GPL
Group: Applications/System
URL: http://syslinux.zytor.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{rversion}.tar.bz2
#Patch: syslinux-2.04-x86_64.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#Autoreq: 0
ExclusiveArch: i386 x86_64
BuildRequires: nasm, perl, netpbm-progs
Requires: mtools

%description
Syslinux is a simple kernel loader. It normally loads the kernel (and an 
optional initrd image) from a FAT filesystem. It can also be used as a
PXE bootloader during network boots.

%prep
%setup -n %{name}-%{rversion}
#patch0 -p1 -b .x86_64

%build
%{__make} clean
%{__make} %{?_smp_mflags} installer

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/syslinux/ \
			%{buildroot}%{_includedir}
%makeinstall install-lib \
	BINDIR="%{buildroot}%{_bindir}" \
	LIBDIR="%{buildroot}%{_libdir}" \
	INCDIR="%{buildroot}%{_includedir}"
%{__install} -m0755 mkdiskimage sys2ansi.pl keytab-lilo.pl %{buildroot}%{_libdir}/syslinux/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libsyslinux* \
		%{buildroot}%{_includedir}/syslinux.h

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING NEWS README TODO *.doc memdisk/memdisk.doc sample/sample.*
%{_bindir}/*
%{_libdir}/syslinux/

%changelog
* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 2.08-0
- Updated to release 2.08.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 2.07-0.pre5
- Updated to release 2.07-pre5.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 2.06-0
- Initial package. (using DAR)
