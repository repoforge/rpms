# $Id$
# Authority: dag
# Upstream: <tuukkat$ee,oulu,fi>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define real_name qc-usb
%define real_release 1

%define moduledir /kernel/drivers/usb/qc-usb
%define modules quickcam.o

Summary: Linux QuickCam USB Drivers
Name: kernel-module-qc-usb
Version: 0.5.1
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.ee.oulu.fi/~tuukkat/quickcam/quickcam.html

Source: http://www.ee.oulu.fi/~tuukkat/quickcam/qc-usb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: qcset

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description
Linux QuickCam USB drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-qc-usb
Summary: Linux QuickCam USB Drivers for SMP kernels
Group: System Environment/Kernel
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: qcset

Obsoletes: %{real_name}, kernel-%{real_name}
Provides: %{real_name}, kernel-%{real_name}
Provides: kernel-modules

%description -n kernel-smp-module-qc-usb
Linux QuickCam USB drivers for SMP kernels.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n qcset
Summary: Linux QuickCam USB utilities
Release: %{real_release}%{?dist}
Group: System Environment/Base

%description -n qcset
Utility to configure the QuickCam USB settings.

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
%{__make} %{?_smp_mflags} clean all \
	MODULE_DIR="%{_libmoddir}/%{kversion}-%{krelease}"
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
	MODULE_DIR="%{_libmoddir}/%{kversion}-%{krelease}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
### Install utilities.
%{__install} -Dp -m0755 qcset %{buildroot}%{_bindir}/qcset

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-qc-usb
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-qc-usb
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-qc-usb
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n qcset
%defattr(-, root, root, 0755)
%doc APPLICATIONS COPYING FAQ README README.qce TODO qcweb-info.txt
%{_bindir}/qcset

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Sep 17 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- User contributed package. (Bert de Bruijn)

* Tue Sep 16 2003 Bert de Bruijn <bert@debruijn.be> - 0.5.1-0
- Initial package.
