# $Id$

# Authority: dag

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsUser: 0

%define _libmoddir /lib/modules

%define rname ltmodem
%define rversion 8.26a9
%define rrelease 1

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/char/ltmodem
%define modules lt_modem.o lt_serial.o

Summary: Linux Linmodem drivers
Name: kernel-module-ltmodem
Version: 8.26
Release: %{rrelease}.a9_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://ltmodem.heby.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.physcip.uni-stuttgart.de/heby/ltmodem-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: kernel-source, pciutils
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description
Linux Linmodem drivers.

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

%package -n kernel-smp-module-ltmodem
Summary: Linux Linmodem drivers
Group: System Environment/Kernel

Requires: /boot/vmlinuz-%{kversion}-%{krelease}smp

Obsoletes: %{rname}, kernel-%{rname}
Provides: %{rname}, kernel-%{rname}
Provides: kernel-modules

%description -n kernel-smp-module-ltmodem
Linux Linmodem drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp.
They might work with newer/older kernels.

%prep
%setup -n %{rname}-%{rversion}
%{__tar} -xvzf source.tar.gz

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{rversion}\nKernel version: %{kversion}-%{krelease}\nArchitecture: %{_target_cpu}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean &>/dev/null
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep EXTRAVERSION="-%{krelease}" &>/dev/null
cd -

### Make UP module.
cd source
%configure \
	--with-force="yes" \
	--with-kernel="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__make} %{?_smp_mflags} all
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
cd source
%configure \
	--with-force="yes" \
	--with-kernel="%{_libmoddir}/%{kversion}-%{krelease}/build"
%{__make} %{?_smp_mflags} all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
cd source
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/devfs/conf.d/
%{__install} -m0644 debian/etc_devfs_conf.d_ltmodem %{buildroot}%{_sysconfdir}/devfs/conf.d/ltmodem

%post
/sbin/depmod -ae %{kversion}-%{krelease} || :
if [ -e /dev/.devfsd ]; then
        if [ -x /usr/sbin/update-devfsd ]; then
                /usr/sbin/update-devfsd
        fi
else
	if [ ! -e /dev/ttyLT0 ]; then
		mknod -m660 /dev/ttyLT0 c 62 64
		chown root:uucp /dev/ttyLT0
		if [ ! -e /dev/modem ]; then
			ln -s /dev/ttyLT0 /dev/modem
		fi
	fi
fi

%postun
/sbin/depmod -ae %{kversion}-%{krelease} || :

%post -n kernel-smp-module-ltmodem
/sbin/depmod -ae %{kversion}-%{krelease}smp || :
if [ -e /dev/.devfsd ]; then
        if [ -x /usr/sbin/update-devfsd ]; then
                /usr/sbin/update-devfsd
        fi
else
	if [ ! -e /dev/ttyLT0 ]; then
		mknod -m660 /dev/ttyLT0 c 62 64
		chown root:uucp /dev/ttyLT0
		if [ ! -e /dev/modem ]; then
			ln -s /dev/ttyLT0 /dev/modem
		fi
	fi
fi

%postun -n kernel-smp-module-ltmodem
/sbin/depmod -ae %{kversion}-%{krelease}smp || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc DOCs/ source/1ST-READ source/CHANGELOG source/UPDATES-BUGS utils/
%{_sysconfdir}/devfs/conf.d/ltmodem
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-ltmodem
%defattr(-, root, root, 0755)
%doc DOCs/ source/1ST-READ source/CHANGELOG source/UPDATES-BUGS utils/
%{_sysconfdir}/devfs/conf.d/ltmodem
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Thu Mar 11 2004 Dag Wieers <dag@wieers.com> - 8.26-1.a9
- Fixed the longstanding smp kernel bug. (Bert de Bruijn)

* Wed Mar 12 2003 Dag Wieers <dag@wieers.com> - 8.26-0.a9
- Initial package. (using DAR)
