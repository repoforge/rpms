# $Id$
# Authority: ned
# Dist: nodist

%define real_name iwlwifi-3945-ucode

Summary: Firmware for Intel Wireless 3945 network adapter
Name: iwl3945-firmware
Version: 15.28.1.8
Release: 2
License: Redistributable, no modification permitted
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source0: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-%{version}.tgz
Source1: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-3945-ucode-2.14.4.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch: noarch

%description
This package provides the firmware required for running an Intel
Wireless 3945 adapter with the Linux kernel iwl3945 driver.

%prep
%setup -c %{real_name} -a 1

### Copy the latest LICENSE and README
%{__cp} -av %{real_name}-%{version}/{LICENSE,README}* .

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}/lib/firmware/
%{__install} -Dp -m0644 */*.ucode %{buildroot}/lib/firmware/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* README*
/lib/firmware/iwlwifi-3945*.ucode

%changelog
* Sat Jan 24 2009 Dag Wieers <dag@wieers.com> - 15.28.1.8-2
- Added 2.14.4 firmware.

* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 15.28.1.8-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 15.28.1.8-1
- Initial RPM package based on 15.28.1.8 iwlwifi 3945 firmware.
