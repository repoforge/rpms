# $Id$
# Authority: dag
# Upstream: Josua Dietze <usb_admin@draisberghof.de>

### Only build for distributions that have usb_modeswitch
# ExcludeDist: el2 el3 el4

%define real_name usb-modeswitch-data

Summary: USB Modeswitch gets 4G cards in operational mode 
Name: usb_modeswitch-data
Version: 20120120
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://www.draisberghof.de/usb_modeswitch/

Source0: http://www.draisberghof.de/usb_modeswitch/%{real_name}-%{version}.tar.bz2
Source1: http://www.draisberghof.de/usb_modeswitch/device_reference.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: tcl
Requires: udev
Requires: usb_modeswitch >= 1.1.2

%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-devices and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to function.

%prep
%setup -n %{real_name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 40-usb_modeswitch.rules %{buildroot}/lib/udev/rules.d/40-usb_modeswitch.rules
%{__install} -p -m 644 %{SOURCE1} .

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}
%{__cp} -av usb_modeswitch.d/ %{buildroot}%{_sysconfdir}/

%clean
%{__rm} -rf %{buildroot}

%post
%{?el6:/sbin/udevadm control --reload-rules}
%{?el5:/sbin/udevcontrol reload_rules}

%postun
%{?el6:/sbin/udevadm control --reload-rules}
%{?el5:/sbin/udevcontrol reload_rules}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README device_reference.txt
%config %{_sysconfdir}/usb_modeswitch.d/
/lib/udev/rules.d/40-usb_modeswitch.rules

%changelog
* Sat Apr 8 2012 Igor Velkov <mozdiav@iav.lv> - 20120120
- Updated to the latest version.

* Sat Dec 11 2010 Dag Wieers <dag@wieers.com> - 20101202-1
- Initial package. (using DAR)
