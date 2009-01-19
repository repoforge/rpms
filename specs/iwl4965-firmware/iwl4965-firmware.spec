# $Id$
# Authority: Fabian
# Dist: nodist

%define real_name iwlwifi-4965-ucode

Summary: Firmware for IntelÂ® Wireless WiFi Link 4965AGN network adapter
Name: iwl4965-firmware
Version: 228.57.1.21
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-4965-ucode-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch: noarch

%description
This package provides the firmware required for running an Intel
Wireless WiFi Link 4965AGN adapter with the Linux kernel iwl4965 driver.

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 iwlwifi-4965-1.ucode %{buildroot}/lib/firmware/iwlwifi-4965-1.ucode
%{__install} -p -m0644 LICENSE.iwlwifi-4965-ucode %{buildroot}/lib/firmware/LICENSE.iwlwifi-4965-ucode
%{__install} -p -m0644 README.iwlwifi-4965-ucode %{buildroot}/lib/firmware/README.iwlwifi-4965-ucode

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.iwlwifi-4965-ucode
%doc /lib/firmware/README.iwlwifi-4965-ucode
/lib/firmware/iwlwifi-4965-1.ucode

%changelog
* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 228.57.1.21-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 228.57.1.21-1
- Initial RPM package based on 228.57.1.21 iwlwifi 4965 firmware.
