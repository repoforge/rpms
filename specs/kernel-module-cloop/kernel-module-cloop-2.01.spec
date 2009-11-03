# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1


%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name cloop
%define real_version 2.01-1
%define real_release 0

%define moduledir /kernel/drivers/block
%define modules cloop.o

Summary: Linux driver for compressed loop devices
Name: kernel-module-cloop
Version: 2.01
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://developer.linuxtag.net/knoppix/sources/

Source: http://developer.linuxtag.net/knoppix/sources/cloop_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: cloop-utils

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description
cloop is a filesystem-independent, transparently decompressed,
read-only block devices.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-cloop
Summary: Compressed loop device driver for SMP
Group: System Environment/Kernel
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: cloop-utils

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description -n kernel-smp-module-cloop
cloop is a filesystem-independent, transparently decompressed,
read-only block devices.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n cloop-utils
Summary: Utilities for compressed loop device driver
Release: %{real_release}%{?dist}
Group: System Environment/Base

%description -n cloop-utils
cloop is a filesystem-independent, transparently decompressed,
read-only block devices.

%prep
%setup -n %{real_name}-%{version}

### Build for specific Red Hat kernel
%{__perl} -pi.orig -e 's|^(CFLAGS:=)|$1-DREDHAT_KERNEL |' Makefile

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{real_version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_DIR="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} clean all \
	KERNEL_DIR="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Install utilities.
%{__install} -Dp -m0755 create_compressed_fs %{buildroot}%{_bindir}/create_compressed_fs
%{__install} -Dp -m0755 extract_compressed_fs %{buildroot}%{_bindir}/extract_compressed_fs
%{__install} -d -m0755 %{buildroot}/dev/
mknod %{buildroot}/dev/cloop b 240 0
for i in 0 1 2 3 4 5 6 7 8 9; do
	mknod %{buildroot}/dev/cloop$i b 240 $i
done

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-cloop
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-cloop
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
/dev/cloop*

%files -n kernel-smp-module-cloop
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/
/dev/cloop*

%files -n cloop-utils
%defattr(-, root, root, 0755)
%doc CHANGELOG README
%{_bindir}/*

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 2.01-0
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)
- Updated to release 2.01.

* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 2.00-0
- Updated to release 2.00.

* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 1.02-0
- Initial package. (using DAR)
