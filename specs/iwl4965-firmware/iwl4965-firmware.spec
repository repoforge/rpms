# $Id$
# Authority: ned
# Dist: nodist

### EL6 ships with iwl4965-firmware-228.61.2.24-2.1.el6

%define real_name iwlwifi-4965-ucode

Summary: Firmware for Intel Wireless WiFi Link 4965AGN network adapter
Name: iwl4965-firmware
Version: 228.57.2.23
Release: 1%{?dist}
License: Redistributable, no modification permitted
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source0: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-%{version}.tgz
Source1: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-228.57.1.21.tgz
Source2: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-4.44.17.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch: noarch

%description
This package provides the firmware required for running an Intel
Wireless WiFi Link 4965AGN adapter with the Linux kernel iwl4965/iwlagn driver.

%prep
%setup -c %{real_name} -a 1 -a 2

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
/lib/firmware/iwlwifi-4965*.ucode

%changelog
* Thu Jan 22 2009 Philip J Perry <ned at unixmail.co.uk> - 228.57.2.23-1
- Add firmware v2 228.57.2.23 required for (el-5.3) iwlagn driver.
- keep firmware v1 228.57.1.21 required for (el-5.2) iwl4965 driver.
- Bundle firmware v 4.44.17 required for older driver revisions.

* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 228.57.1.21-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 228.57.1.21-1
- Initial RPM package based on 228.57.1.21 iwlwifi 4965 firmware.
