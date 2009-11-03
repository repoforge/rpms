# $Id$
# Authority: matthias
# Dist: nodist

Summary: Firmware for Texas Instruments ACX100 network adaptors
Name: acx100-firmware
Version: 1.9.8.b
Release: 1%{?dist}
License: Unknown
Group: System Environment/Kernel
URL: http://acx100.sourceforge.net/wiki/Firmware
Source0: http://acx100.erley.org/acx_fw/acx100_dlink_dwl520+/fw1/WLANGEN.BIN_%{version}
Source1: http://acx100.erley.org/acx_fw/acx100usb_dlink_dwl120+/fw1/ACX100_USB.bin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Firmware files for Texas Instruments ACX100 based wireless network adaptors,
required by the acx Linux kernel module. You might need to add some card
specific radio firmware files in addition to this packages. Please see :
http://acx100.erley.org/acx_fw/acx1xx.htm


%prep


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/lib/firmware
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}/lib/firmware/tiacx100
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}/lib/firmware/tiacx100usb


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
/lib/firmware/tiacx100
/lib/firmware/tiacx100usb


%changelog
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net> 1.2.1.34-1
- Initial RPM release, based on the ipw2200-firmware spec file.

