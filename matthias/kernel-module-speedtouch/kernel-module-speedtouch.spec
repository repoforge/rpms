# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0

%define _libmoddir /lib/modules

%define rname speedtouch

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/usb
#define modules speedtouch.o
%define modules speedtch.o

Summary: Linux SpeedTouch USB ADSL Modem drivers.
Name: kernel-module-speedtouch
Version: 1.6
Release: 0_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://linux-usb.sourceforge.net/SpeedTouch/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/linux-usb/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: kernel-%{rname}
Provides: kernel-%{rname}
Provides: kernel-modules

%description
Linux SpeedTouch USB ADSL Modem drivers.

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

%package -n kernel-smp-module-speedtouch
Summary: Linux SpeedTouch USB ADSL Modem drivers for SMP.
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Obsoletes: kernel-%{rname}
Provides: kernel-%{rname}
Provides: kernel-modules

%description -n kernel-smp-module-speedtouch
Linux SpeedTouch USB ADSL Modem drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -n %{rname}-%{version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\nArchitecture: %{_target_cpu}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean all \
	KERNELDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} clean all \
	KERNELDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-speedtouch
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun -n kernel-smp-module-speedtouch
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/*

%files -n kernel-smp-module-speedtouch
%defattr(-, root, root, 0755)
%doc COPYING
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/*

%changelog
* Wed Jun 18 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
