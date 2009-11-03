# $Id$
# Authority: dag
# Upstream: <prism54-devel$prism54,org>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# BuildAsRoot: 1

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name prism54
%define real_release 1

%define moduledir /kernel/drivers/net/wireless/prism54
%define modules ksrc/prism54.o

Summary: Linux driver for the 802.11g Prism GT / Prism Duette / Prism Indigo Chipsets
Name: kernel-module-prism54
Version: 1.1
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://prism54.org/

Source: http://prism54.org/pub/linux/stable/tars/2004-03/prism54-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-source >= 2.4.22
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description
Linux driver for the 802.11g Prism GT / Prism Duette / Prism Indigo Chipsets.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-prism54
Summary: Linux SMP driver for the 802.11g Prism GT / Prism Duette / Prism Indigo Chipsets
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description -n kernel-smp-module-prism54
Linux SMP driver for the 802.11g Prism GT / Prism Duette / Prism Indigo Chipsets.

These drivers are build for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

#%package -n prism54-firmware
#Summary: 802.11g Prism GT / Prism Duette / Prism Indigo Chipsets firmware.
#Release: %{real_release}
#Group: System Environment/Base
#
#%description -n prism54-firmware
#802.11g Prism GT / Prism Duette / Prism Indigo Chipsets firmware.

%prep
%setup -n %{real_name}-%{version}

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean modules \
	KVER="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

#### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

#### Make SMP module.
%{__make} %{?_smp_mflags} clean modules \
	KVER="%{kversion}-%{krelease}" \
	CC="${CC:-%{__cc}}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
#### Install firmware
#%{__install} -d -m0755 %{buildroot}%{_libdir}/hotplug/firmware/
#%{__install} -m0644 ksrc/isl3877 ksrc/isl3890 %{buildroot}%{_libdir}/hotplug/firmware/

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-prism54
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-prism54
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-prism54
%defattr(-, root, root, 0755)
%doc README
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

#%files -n prism54-firmware
#%defattr(-, root, root, 0755)
#%doc README
#%dir %{_libdir}/hotplug/
#%dir %{_libdir}/hotplug/firmware/
#%{_libdir}/hotplug/firmware/*

%changelog
* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.0.20040307-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Thu Feb 05 2004 Dag Wieers <dag@wieers.com> - 0.0.20040307-0
- Updated to release 20040307.

* Thu Feb 05 2004 Dag Wieers <dag@wieers.com> - 0.0.20040205-0
- Initial package. (using DAR)
