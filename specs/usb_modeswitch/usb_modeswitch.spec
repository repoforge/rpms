# $Id$
# Authority: dag

%define real_name usb-modeswitch

Summary: USB Modeswitch gets 4G cards in operational mode
Name: usb_modeswitch
Version: 1.2.3
Release: 1%{?dist}
Group: Applications/System
License: GPLv2+
URL: http://www.draisberghof.de/usb_modeswitch/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://www.draisberghof.de/usb_modeswitch/usb-modeswitch-%{version}.tar.bz2
Source1: http://www.draisberghof.de/usb_modeswitch/device_reference.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libusb-devel
Requires: usb_modeswitch-data

%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-devices and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 usb_modeswitch %{buildroot}%{_sbindir}/usb_modeswitch
%{__install} -Dp -m0644 usb_modeswitch.conf %{buildroot}%{_sysconfdir}/usb_modeswitch.conf
%{__install} -Dp -m0644 usb_modeswitch.1 %{buildroot}%{_mandir}/man1/usb_modeswitch.1
%{__install} -Dp -m0755 usb_modeswitch.tcl %{buildroot}/lib/udev/usb_modeswitch

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/usb_modeswitch.1*
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%{_sbindir}/usb_modeswitch
/lib/udev/usb_modeswitch

%changelog
* Sat Dec 11 2010 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Initial package. (using DAR)
