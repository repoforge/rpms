# $Id$
# Authority: dag
# Upstream: Thomas Hood <jdthood$yahoo,co,uk>

# ExcludeDist: fc2 fc3

# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0
# BuildAsRoot: 1

%define _libmoddir /lib/modules

%define real_name thinkpad

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /kernel/drivers/thinkpad
%define modules rtcmosram.o smapi.o superio.o thinkpad.o thinkpadpm.o

Summary: IBM ThinkPad kernel modules
Name: kernel-module-thinkpad
Version: 5.0
Release: 0_%{kversion}_%{krelease}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://tpctl.sourceforge.net/

Source0: http://dl.sf.net/tpctl/thinkpad_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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
%setup -n %{real_name}-%{version}

### FIXME: Remove chown/chgrp from Makefile. (Please fix upstream)
%{__perl} -pi.orig -e '
		s| -o 0 -g 0 | |;
		s|^(DIR_MOD):=(.+)$|$1:=\$(RPM_BUILD_ROOT)$2|;
		s|^(DIR_MOD_VER):=.*$|$1:=\$(DIR_MOD)/%{kversion}-%{krelease}/kernel/drivers|;
		s|^(CFLAGS):=(.*)$|$1:=$2 \$(RPM_OPT_FLAGS)|;
	' Makefile */*/Makefile

%{__cat} <<EOF >README.modules.conf
To enable the thinkpad kernel modules, place the following to your
/etc/modules.conf:

alias char-major-10-170 thinkpad
EOF

#%{__ln_s} -f 2.4/drivers/ .
#%{__ln_s} -f 2.4/include/ .

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
	KSRC="%{_libmoddir}/%{kversion}-%{krelease}/build"
cd 2.4/drivers/
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -p -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}

%install
%{__install} -d -m0755 %{buildroot}/dev \
			%{buildroot}%{_mandir}/man4
touch %{buildroot}/dev/thinkpad
%{__install} -p -m0644 man/*.4 %{buildroot}%{_mandir}/man4/

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
%doc AUTHORS ChangeLog COPYING man/ README* SUPPORTED-MODELS TECHNOTES
#%doc %{_mandir}/man4/*
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/
%ghost /dev/thinkpad

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 5.0-0
- Updated to release 5.0.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 4.8-0
- Updated to release 4.8.

* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 4.3-3
- Moved manpage to documentation directory.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 4.3-1
- Updated to release 4.3.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 4.0-0
- Initial package. (using DAR)
