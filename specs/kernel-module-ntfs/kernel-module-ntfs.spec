# $Id$
# Authority: dag

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ntfs
%define real_release 1

%define moduledir /kernel/fs/ntfs
%define modules ntfs.o

Summary: Linux driver for NTFS filesystem
Name: kernel-module-ntfs
Version: %{kversion}
Release: %{real_release}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://linux-ntfs.sf.net/info/redhat.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: kernel-ntfs
Provides: kernel-ntfs
Provides: kernel-modules

%description
Linux driver for NTFS filesystem.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ntfs
Release: %{real_release}_%{kversion}_%{krelease}
Summary: Linux SMP driver for NTFS filesystem
License: GPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules

%description -n kernel-smp-module-ntfs
Linux SMP driver for NTFS filesystem.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -cT

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
cd %{_usrsrc}/linux-%{kversion}-%{krelease}/fs/ntfs/
%{__make} ntfs.o \
	TOPDIR="%{_usrsrc}/linux-%{kversion}-%{krelease}" \
	CFLAGS="-Wall -pipe -O3 -fomit-frame-pointer -D__KERNEL__ -DMODULE -DEXPORT_SYMTAB -DMODVERSIONS -I%{_libmoddir}/%{kversion}-%{krelease}/build/include -include %{_libmoddir}/%{kversion}-%{krelease}/build/include/linux/modversions.h"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}/fs/ntfs/
%{__make} ntfs.o \
	TOPDIR="%{_usrsrc}/linux-%{kversion}-%{krelease}" \
	CFLAGS="-Wall -pipe -O3 -fomit-frame-pointer -D__KERNEL__ -DMODULE -DEXPORT_SYMTAB -DMODVERSIONS -I%{_libmoddir}/%{kversion}-%{krelease}/build/include -include %{_libmoddir}/%{kversion}-%{krelease}/build/include/linux/modversions.h"
#TEST	CFLAGS="-D__KERNEL__ -I%{_usrsrc}/linux-%{kversion}-%{krelease}/include -Wall -Wstrict-prototypes -Wno-trigraphs -O2 -fomit-frame-pointer -fno-strict-aliasing -fno-common -pipe -mpreferred-stack-boundary=2 -march=%{_arch} -DMODULE -DMODVERSIONS -include %{_usrsrc}/linux-%{kversion}-%{krelease}/include/linux/modversions.h -nostdinc -iwithprefix include"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
cd -

%install
### Install utilities.

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-ntfs
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-ntfs
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ntfs
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com>
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
