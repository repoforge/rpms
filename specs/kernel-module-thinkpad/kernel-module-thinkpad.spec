# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0

%define _libmoddir /lib/modules

%define rname thinkpad

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/thinkpad
%define modules smapi.o superio.o rtcmosram.o thinkpadpm.o thinkpad.o

Summary: IBM ThinkPad kernel modules.
Name: kernel-module-thinkpad
Version: 4.8
Release: 0_%{kversion}_%{krelease}
License: GPL
Group: System Environment/Kernel
URL: http://tpctl.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://download.sourceforge.net/tpctl/%{rname}_%{version}.tar.gz
Source1: %{rname}-README.modules.conf
Patch0: thinkpad-4.8-rpm.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: kernel-source
Requires: /boot/vmlinuz-%{kversion}-%{krelease}

Obsoletes: thinkpad, kernel-thinkpad
Provides: thinkpad, kernel-thinkpad
Provides: kernel-modules

%description
IBM ThinkPad kernel modules.

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

%prep
%setup -n %{rname}-%{version}
%patch0

%{__ln_s} -f 2.4/drivers/ .
%{__ln_s} -f 2.4/include/ .

%{__perl} -pi.orig -e '
		s|^(DIR_MOD_VER):=.*$|$1:=\$(DIR_MOD)/%{kversion}-%{krelease}/kernel/drivers|;
		s|^(CFLAGS):=(.*)$|$1:=$2 \$(RPM_OPT_FLAGS)|;
	' Makefile */Makefile

%build
### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
%{__make} %{?_smp_mflags} clean all \
	KSRC="%{_libmoddir}/%{kversion}-%{krelease}/build"

%install
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Install UP module.
%{__make} install_modules

%{__install} -d -m0755 %{buildroot}/dev \
			%{buildroot}%{_mandir}/man4
touch %{buildroot}/dev/thinkpad
%{__install} -m0644 %{SOURCE1} .
%{__install} -m0644 man/*.4 %{buildroot}%{_mandir}/man4/

### FIXME: A manual page should not be part of a kernel module package, added to documentation.
%{__rm} -rf %{buildroot}%{_mandir}

%post
if [ "$1" -ne 0 ]; then
	groupadd -r thinkpad
	if [ ! -e /dev/thinkpad ]; then
		mknod -m0664 /dev/thinkpad c 10 170
	fi
	chown root:thinkpad /dev/thinkpad
fi
/sbin/depmod -ae %{kversion}-%{krelease} || :

%postun
groupdel thinkpad
/sbin/depmod -ae %{kversion}-%{krelease} || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* SUPPORTED-MODELS TECHNOTES man/
#%doc %{_mandir}/man4/*
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
%ghost /dev/thinkpad

%changelog
* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 4.8-0
- Updated to release 4.8.

* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 4.3-3
- Moved manpage to documentation directory.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 4.3-1
- Updated to release 4.3.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 4.0-0
- Initial package. (using DAR)
