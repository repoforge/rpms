# $Id$

# Authority: dag
# Upstream: <ndiswrapper-general@lists.sourceforge.net>

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsUser: 0

%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define rname ndiswrapper
%define rrelease 1

%define moduledir /kernel/drivers/net/ndiswrapper
%define modules ndiswrapper.o

Summary: Linux NDIS wrapper drivers.
Name: kernel-module-ndiswrapper
Version: 0.5
Release: %{rrelease}_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://ndiswrapper.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ndiswrapper/ndiswrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: ndiswrapper-utils

Provides: kernel-modules

%description
Linux NDIS wrapper drivers.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n ndiswrapper-utils
Summary: NDIS wrapper utilities.
Release: %{rrelease}
License: GPL
Group: System Environment/Base

Obsoletes: ndiswrapper
Provides: ndiswrapper

%description -n ndiswrapper-utils
NDIS wrapper utilities.

%prep
%setup -n %{rname}-%{version}

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
cd driver
%{__make} %{?_smp_mflags} \
	KSRC="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	KVERS="24"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Make utilities.
%{__make} %{?_smp_mflags} -C utils \
	CFLAGS="%{optflags}"

%install
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 utils/loadndisdriver %{buildroot}%{_bindir}

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n ndiswrapper-utils
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README
%{_bindir}/*

%changelog
* Mon Mar 08 2004 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Initial package. (using DAR)
