# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname mpi350

%define moduledir /kernel/drivers/net/wireless/mpi350
%define modules mpi350.o

%define rrelease 1

Summary: Linux MPI350 (Aironet 350) mini PCI drivers.
Name: kernel-module-mpi350
Version: 2.0
Release: %{rrelease}_%{kversion}_%{krelease}
License: MPL
Group: System Environment/Kernel
URL: http://www.cisco.com/warp/public/102/wlan/linux.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: Linux-ACU-Driver-v%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: aironet-utils

Provides: kernel-modules

%description
Linux MPI350 (Aironet 350) mini PCI drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-mpi350
Release: %{rrelease}_%{kversion}_%{krelease}
Summary: Linux MPI350 (Aironet 350) mini PCI drivers.
License: MPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: aironet-utils

Provides: kernel-modules

%description -n kernel-smp-module-mpi350
Linux MPI350 (Aironet 350) mini PCI drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n aironet-utils
Summary: Aironet Cisco utilities.
Release: %{rrelease}
License: Proprietary
Group: System Environment/Base

Obsoletes: Cisco-LEAP, aironet-utilities
Provides: Cisco-LEAP

%description -n aironet-utils
Aironet Cisco utilities.

%prep
%setup -c %{name}-%{version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
cd driver/
%{__cc} -MD -O2 -Wall -Wstrict-prototypes -D__KERNEL__ -DMODULE -pipe -I%{_libmoddir}/%{kversion}-%{krelease}/build/include -c mpi350.c
#%{__cc} -MD -O2 -Wall -Wstrict-prototypes -D__KERNEL__ -DMODULE -pipe -I%{_libmoddir}/%{kversion}-%{krelease}/build/include -c airo.c
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make SMP module.
cd driver/
%{__cc} -MD -O2 -Wall -Wstrict-prototypes -D__KERNEL__ -DMODULE -pipe -I%{_libmoddir}/%{kversion}-%{krelease}/build/include  -c mpi350.c
#%{__cc} -MD -O2 -Wall -Wstrict-prototypes -D__KERNEL__ -DMODULE -pipe -I%{_libmoddir}/%{kversion}-%{krelease}/build/include  -c airo.c
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sysconfdir} \
			%{buildroot}/opt/cisco/
%{__install} -m0755 utilities/acu utilities/bcard utilities/leapset utilities/leapscript utilities/leaplogin %{buildroot}%{_bindir}
%{__install} -m0644 ACU.PRFS %{buildroot}/opt/cisco/
%{__install} -m0644 ethX.cfg %{buildroot}%{_sysconfdir}/eth2.cfg
%{__tar} -xvzf helpml.tar.gz -C %{buildroot}/opt/cisco/

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-mpi350
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-mpi350
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-mpi350
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n aironet-utils
%defattr(-, root, root, 0755)
%doc config.350 readme.txt ethX.cfg
%{_sysconfdir}/*
%{_bindir}/*
/opt/cisco/

%changelog
* Thu Jul 24 2003 Dag Wieers <dag@wieers.com> - 2.0-1
- Remove airo module, please use the one supplied by the kernel.
- Renamed aironet-utilities to aironet-utils.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 2.0-0
- Initial package. (using DAR)
