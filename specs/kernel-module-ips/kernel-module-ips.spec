# $Id$
# Authority: dag

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Soapbox: 0
# Distcc: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name ips
%define real_version 611
%define real_release 1

%define moduledir /kernel/drivers/misc/ips
%define modules ips.o

Summary: Linux IBM PCI ServeRAID drivers
Name: kernel-module-ips
Version: 6.11
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www-3.ibm.com/pc/support/site.wss/MIGR-39729.html

Source: ips-%{real_version}.tgz
Source1: ips-Makefile
Source2: ips-kernel-ver.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Provides: kernel-modules

%description
Linux IBM PCI ServeRAID drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ips
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
Summary: Linux IBM PCI ServeRAID drivers for SMP
License: GPL
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Provides: kernel-modules

%description -n kernel-smp-module-ips
Linux IBM PCI ServeRAID drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%prep
%setup -c -n %{real_name}-%{real_version}
%{__install} -p -m0644 %{SOURCE1} Makefile
%{__install} -p -m0644 %{SOURCE2} kernel-ver.c

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
%{__make} clean all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} clean all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-ips
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-ips
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.ips README
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ips
%defattr(-, root, root, 0755)
%doc Changelog.ips README
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 6.11-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 6.11-0
- Initial package. (using DAR)
