# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define _with_smp %(test -f /usr/src/linux-%{kernel}/configs/kernel-%{kversion}-%{_target_cpu}-smp.config && echo 1 || echo 0)

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ntfs

%define moduledir /kernel/fs/ntfs
%define modules ntfs.o

Summary: Linux driver for NTFS filesystem
Name: kernel-module-ntfs
Version: 0.0
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://linux-ntfs.sourceforge.net/info/redhat.html

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-source

%description
Linux driver for NTFS filesystem.


%package -n kernel-module-ntfs-%{kernel}
Summary: Linux SMP driver for NTFS filesystem
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}
Requires: kernel = %{kernel}

Provides: kernel-module-ntfs = %{version}-%{release}
Provides: kernel-modules

%description -n kernel-module-ntfs-%{kernel}
Linux driver for NTFS filesystem.

These drivers are built for kernel %{kernel}
and architecture %{_target_cpu}.
They might work with newer/older kernels.


%package -n kernel-smp-module-ntfs-%{kernel}
Summary: Linux SMP driver for NTFS filesystem
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kernel}smp
Requires: kernel-smp = %{kernel}smp

Provides: kernel-module-ntfs = %{version}-%{release}
Provides: kernel-modules

%description -n kernel-smp-module-ntfs-%{kernel}
Linux SMP driver for NTFS filesystem.

These drivers are built for kernel %{kernel}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -cT

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kernel}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/\(i.86\|athlon\)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
	&>/dev/null
cd -

### Make UP module.
cd %{_usrsrc}/linux-%{kernel}/fs/ntfs/
%{__make} ntfs.o \
	TOPDIR="%{_usrsrc}/linux-%{kernel}" \
	CFLAGS="-Wall -pipe -O3 -fomit-frame-pointer -D__KERNEL__ -DMODULE -DEXPORT_SYMTAB -DMODVERSIONS -I%{_libmoddir}/%{kernel}/build/include -include %{_libmoddir}/%{kernel}/build/include/linux/modversions.h"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}%{moduledir}
cd -

%if %{_with_smp}
### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kernel}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep \
	EXTRAVERSION="-%{krelease}smp" \
	ARCH="$(echo %{_target_cpu} | sed -e 's/\(i.86\|athlon\)/i386/' -e 's|sun4u|sparc64|' -e 's|arm.*|arm|' -e 's|sa110|arm|')" \
	&>/dev/null
cd -

### Make SMP module.
cd %{_usrsrc}/linux-%{kernel}/fs/ntfs/
%{__make} ntfs.o \
	TOPDIR="%{_usrsrc}/linux-%{kernel}" \
	CFLAGS="-Wall -pipe -O3 -fomit-frame-pointer -D__KERNEL__ -DMODULE -DEXPORT_SYMTAB -DMODVERSIONS -I%{_libmoddir}/%{kernel}/build/include -include %{_libmoddir}/%{kernel}/build/include/linux/modversions.h"
#TEST	CFLAGS="-D__KERNEL__ -I%{_usrsrc}/linux-%{kversion}-%{krelease}/include -Wall -Wstrict-prototypes -Wno-trigraphs -O2 -fomit-frame-pointer -fno-strict-aliasing -fno-common -pipe -mpreferred-stack-boundary=2 -march=%{_arch} -DMODULE -DMODVERSIONS -include %{_usrsrc}/linux-%{kversion}-%{krelease}/include/linux/modversions.h -nostdinc -iwithprefix include"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}/
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kernel}smp%{moduledir}
cd -
%endif

%install
### Install utilities.

%post -n kernel-module-ntfs-%{kernel}
/sbin/depmod -ae %{kernel} || :

%postun -n kernel-module-ntfs-%{kernel}
/sbin/depmod -ae %{kernel} || :

%post -n kernel-smp-module-ntfs-%{kernel}
/sbin/depmod -ae %{kernel}smp || :

%postun -n kernel-smp-module-ntfs-%{kernel}
/sbin/depmod -ae %{kernel}smp || :

%clean
%{__rm} -rf %{buildroot}

%files -n kernel-module-ntfs-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%if %{_with_smp}
%files -n kernel-smp-module-ntfs-%{kernel}
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/
%endif

%changelog
* Sat Jun 26 2004 Dag Wieers <dag@wieers.com> - 0.0-1
- Moved to new standard naming scheme.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.0-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 0.0-1
- Initial package. (using DAR)
