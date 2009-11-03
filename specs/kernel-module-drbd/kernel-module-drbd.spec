# $Id$
# Authority: dag
# Upstream: <drbd-devel$lists,sourceforge,net>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define __cc gcc32}

%define _libmoddir /lib/modules
%define _sbindir /sbin

%define real_name drbd
%define real_release 1

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/block
%define modules drbd/drbd.o

Summary: Distributed Redundant Block Device driver
Name: kernel-module-drbd
Version: 0.6.11
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.drbd.org/

Source: http://www.drbd.org/uploads/media/drbd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source

Requires: /boot/vmlinuz-%{kversion}-%{krelease}
Requires: drbd-utils

Obsoletes: kernel-%{real_name}
Provides: kernel-%{real_name}

%description
DRBD is a block device which is designed to build high availability clusters.
This is done by mirroring a whole block device via (a dedicated) network.
You could see it as a network RAID 1.

These drivers are built for kernel %{kversion}-%{krelease}
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n kernel-smp-module-drbd
Summary: Distributed Redundant Block Device driver for SMP
Group: System Environment/Kernel
Release: %{real_release}_%{kversion}_%{krelease}%{?dist}

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp
Requires: drbd-utils

Obsoletes: kernel-%{real_name}
Provides: kernel-%{real_name}

%description -n kernel-smp-module-drbd
DRBD is a block device which is designed to build high availability clusters.
This is done by mirroring a whole block device via (a dedicated) network.
You could see it as a network RAID 1.

These drivers are built for kernel %{kversion}-%{krelease}smp
and architecture %{_target_cpu}.
They might work with newer/older kernels.

%package -n drbd-utils
Summary: Utilities for Distributed Redundant Block Device (DRBD) driver
Release: %{real_release}%{?dist}
Group: System Environment/Base

Obsoletes: %{real_name}

%description -n drbd-utils
DRBD is a block device which is designed to build high availability clusters.
This is done by mirroring a whole block device via (a dedicated) network.
You could see it as a network RAID 1.


%prep
%setup -n %{real_name}-%{version}

### Enable SIGHAND_HACK for RH kernel 2.4.20 and greater
%{?fc1:%{__perl} -pi.orig -e 's|//(#define SIGHAND_HACK)|$1|' drbd_config.h}
%{?rh9:%{__perl} -pi.orig -e 's|//(#define SIGHAND_HACK)|$1|' drbd_config.h}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|usr/share/man|\$(mandir)|g;
		s|var/lib/drbd|\$(localstatedir)/lib/drbd|g;
		s|etc/|\$(sysconfdir)/|g;
		s|sbin/|\$(sbindir)/|g;
	' */Makefile

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
%{__make} %{?_smp_mflags} -C drbd clean all \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"
	KERNVER="%{kversion}-%{krelease}"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}smp" &>/dev/null
cd -

### Make SMP module.
%{__make} %{?_smp_mflags} -C drbd clean all \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	KERNVER="%{kversion}-%{krelease}smp"
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

### Make utilities.
%{__make} %{?_smp_mflags} \
	KDIR="%{_libmoddir}/%{kversion}-%{krelease}/build"

%install
### Install utilities
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/drbd/
%makeinstall \
	KERNVER="%{kversion}-%{krelease}"

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-drbd
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%postun -n kernel-smp-module-drbd
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%post -n drbd-utils
/sbin/chkconfig --add drbd

%preun -n drbd-utils
if [ $1 -eq 0 ]; then
        /sbin/service drbd stop &>/dev/null || :
        /sbin/chkconfig --del drbd
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-drbd
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%files -n drbd-utils
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README scripts/drbd.conf
%doc documentation/*.html documentation/*.sgml documentation/*.txt documentation/HOWTO/*.html
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/ha.d/resource.d/*
%config(noreplace) %{_sysconfdir}/drbd.conf
%config %{_initrddir}/*
%{_sbindir}/*
%{_localstatedir}/lib/drbd/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 0.6.11-1
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Fri Feb 20 2004 Dag Wieers <dag@wieers.com> - 0.6.11-0
- Updated to release 0.6.11.

* Thu Jan 08 2004 Dag Wieers <dag@wieers.com> - 0.6.10-0
- Updated to release 0.6.10.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 0.6.7-0
- Initial package. (using DAR)
