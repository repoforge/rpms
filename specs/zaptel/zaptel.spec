# $id: zaptel.spec,v 1.2 2003/11/17 12:31:10 dude Exp $

# For pre-versions
%define prever RC1

# "uname -r" output of the kernel to build for, the running one
# if none was specified with "--define 'kernel <uname -r>'"
%{!?kernel: %{expand: %%define kernel %(uname -r)}}
 
%define kversion %(echo %{kernel} | sed -e s/smp// -)
%define krelver  %(echo %{kversion} | tr -s '-' '_')
%if %(echo %{kernel} | grep -c smp)
        %{expand:%%define ksmp -smp}
%endif

Summary: Zaptel telephony interface support
Name: zaptel
Version: 1.0
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: System Environment/Libraries
URL: http://www.asterisk.org/
Source0: ftp://ftp.asterisk.org/pub/telephony/zaptel/zaptel-%{version}%{?prever:-%{prever}}.tar.gz
Source1: zaptel-makedev.d.txt
Patch: zaptel-1.0-RC1-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: newt, kernel-module-zaptel
BuildRequires: newt-devel, kernel-source = %{kversion}, MAKEDEV

%description
This package contains the libraries, device entries, startup scripts and tools
needed to use Digium telephony hardware. This includes the pseudo TDM
interfaces.

You will also need to install a kernel modules package matching your current
kernel for everything to work, and edit /etc/modules.conf.


%package -n kernel%{?ksmp}-module-zaptel
Summary: Kernel modules for the Zaptel devices.
Release: %{release}_%{krelver}
Group: System Environment/Kernel
Requires: kernel%{?ksmp} = %{kversion}, /sbin/depmod
Provides: kernel-modules
%{?ksmp:Provides: kernel-module-zaptel = %{version}-%{release}_%{krelver}}

%description -n kernel%{?ksmp}-module-zaptel
This package contains the zaptel kernel modules for the Linux kernel package :
%{kversion} (%{_target_cpu}%{?ksmp:, SMP}).


%prep
%setup -n zaptel-%{version}%{?prever:-%{prever}}
%patch -p1 -b .makefile


%build
# Replace kernel version with the correct one
#perl -pi -e 's|`uname -r`|%{kernel}|g' Makefile
#perl -pi -e 's|/usr/src/linux-2.4/|/usr/src/linux-%{kversion}/|g' Makefile
# Get the ztdummy module compiled too
%{__perl} -pi -e 's|# ztdummy.o|ztdummy.o|g' Makefile
export CFLAGS="%{optflags}"
export KFLAGS="%{optflags} -D__BOOT_KERNEL_H_ -D__MODULE_KERNEL_%{_target_cpu}=1 %{?ksmp:-D__BOOT_KERNEL_SMP=1} %{!?ksmp:-D__BOOT_KERNEL_UP=1}"
%{__make} %{?_smp_mflags} KVERSION=%{kversion}


%install
%{__rm} -rf %{buildroot}
%{__make} install KVERSION=%{kversion} INSTALL_PREFIX=%{buildroot}

# Install and generate all the device stuff
%{__install} -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/makedev.d/zaptel
 
# Create entry list
/dev/MAKEDEV \
    -c %{buildroot}%{_sysconfdir}/makedev.d \
    -d %{buildroot}/dev -M zaptel | sed 's|%{buildroot}||g' > device.list

# Install the init script and sysconfig file
%{__install} -m 0644 -D zaptel.sysconfig \
    %{buildroot}%{_sysconfdir}/sysconfig/zaptel
%{__install} -m 0755 -D zaptel.init \
    %{buildroot}%{_initrddir}/zaptel

# Move kernel modules in the "kernel" subdirectory, also get smp right
%{__mkdir_p} %{buildroot}/lib/modules/%{kernel}/kernel
%{__mv} %{buildroot}/lib/modules/%{kversion}/misc \
        %{buildroot}/lib/modules/%{kernel}/kernel/

# Move the modules config file back in order to put it in docs instead
%{__mv} %{buildroot}%{_sysconfdir}/modules.conf.zaptel .


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post -n kernel%{?ksmp}-module-zaptel
/sbin/depmod -a -F /boot/System.map-%{kernel} %{kernel} >/dev/null 2>&1 || :
                                                                                
%postun -n kernel%{?ksmp}-module-zaptel
/sbin/depmod -a -F /boot/System.map-%{kernel} %{kernel} >/dev/null 2>&1 || :


%files -f device.list
%defattr(-, root, root, 0755)
%doc ChangeLog README.fxsusb modules.conf.zaptel
%doc ifcfg-hdlc0 ifup-hdlc zaptel.conf.sample
%config(noreplace) %{_sysconfdir}/sysconfig/zaptel
%config(noreplace) %{_sysconfdir}/zaptel.conf
%{_sysconfdir}/makedev.d/zaptel
%{_initrddir}/zaptel
/usr/sbin/ztcfg
/usr/sbin/zttool
%{_includedir}/*.h
%{_includedir}/linux/*.h
%{_libdir}/*.so*

%files -n kernel%{?ksmp}-module-zaptel
%defattr(-, root, root, 0755)
/lib/modules/%{kernel}/kernel/misc/*


%changelog
* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.RC1.1
- Update to 1.0-RC1.
- Major Makefile patch updates, spec updates to match.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/>
- Uncomment the ztdummy module to have it built.

* Wed Nov  5 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

