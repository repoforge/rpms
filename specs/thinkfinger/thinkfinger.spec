# $Id$
# Authority: dag

Summary: Driver for the UPEK/SGS Thomson Microelectronics fingerprint reader
Name: thinkfinger
Version: 0.3
Release: 1
License: GPL
Group: System Environment/Base
URL: http://thinkfinger.sourceforge.net/

Source: http://downloads.sourceforge.net/thinkfinger/thinkfinger-%{version}.tar.gz
Patch0: thinkfinger-0.3-birdir.patch
Patch1: thinkfinger-0.3-acl.patch
Patch2: thinkfinger-0.3-has-device.patch
Patch3: thinkfinger-0.3-hal.patch
Patch5: thinkfinger-refuse-remote-login-thoenig-01.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: doxygen
BuildRequires: libacl-devel
BuildRequires: libusb-devel >= 0.1.11
BuildRequires: pam-devel
Requires: hal

%description
ThinkFinger is a driver for the UPEK/SGS Thomson Microelectronics fingerprint
reader (USB ID 0483:2016). The device is being found either as a standalone USB
device, built into USB keyboards or built into laptops.  The following laptop
vendors are using the device:

- Dell
- IBM/Lenovo
- Toshiba

Toshiba is shipping their laptops either with the UPEK/SGS Thomson
Microelectronics fingerprint reader or with a fingerprint reader built by
AuthenTec. The AuthenTec fingerprint reader is *not* supported by ThinkFinger.

SONY laptops with the UPEK/SGS Thomson Microelectronics fingerprint reader are
not supported.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: libusb-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch1 -p1 -b .acl
%patch2 -p1 -b .has-device
%patch3 -p1 -b .hal
%patch5 -p0 -b .sshdcrash

%{__cat} <<EOF >thinkfinger.modules
#!/bin/bash
/sbin/modprobe uinput &>/dev/null
EOF

%build
%configure \
    --disable-static \
    --enable-console-perms="yes" \
    --with-securedir="/%{_lib}/security"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 thinkfinger.modules %{buildroot}%{_sysconfdir}/sysconfig/modules/thinkfinger.modules

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/pam_thinkfinger/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/tf-tool.1*
%doc %{_mandir}/man8/pam_thinkfinger.8*
%config %{_sysconfdir}/sysconfig/modules/thinkfinger.modules 
%config(noreplace) %{_sysconfdir}/pam_thinkfinger
%config %{_sysconfdir}/security/console.perms.d/*
%{_datadir}/hal/fdi/policy/10osvendor/*
%{_libdir}/libthinkfinger.so.*
/%{_lib}/security/pam_thinkfinger.so
%{_sbindir}/tf-tool
%exclude %{_libdir}/libthinkfinger.la

%files devel
%defattr(-,root,root,-)
%doc docs/autodocs/html/*
%{_includedir}/libthinkfinger.h
%{_libdir}/libthinkfinger.so
%{_libdir}/pkgconfig/libthinkfinger.pc

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (based on fedora)
