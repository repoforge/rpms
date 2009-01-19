# $Id$
# Authority: Fabian
# Dist: nodist

%define real_name iwlwifi-5000-ucode

Summary: Firmware for IntelÂ® Wireless WiFi Link 5000AGN series network adapters
Name: iwl5000-firmware
Version: 5.4.A.11
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch: noarch

%description
This package provides the firmware required for running Intel Wireless
WiFi Link 5000AGN series adapters with the Linux kernel iwlagn driver.

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 iwlwifi-5000-1.ucode %{buildroot}/lib/firmware/iwlwifi-5000-1.ucode
%{__install} -p -m0644 LICENSE.iwlwifi-5000-ucode %{buildroot}/lib/firmware/LICENSE.iwlwifi-5000-ucode
%{__install} -p -m0644 README.iwlwifi-5000-ucode %{buildroot}/lib/firmware/README.iwlwifi-5000-ucode

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.iwlwifi-5000-ucode
%doc /lib/firmware/README.iwlwifi-5000-ucode
/lib/firmware/iwlwifi-5000-1.ucode

%changelog
* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 5.4.A.11-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 5.4.A.11-1
- Initial RPM package based on 5.4.A.11 iwlwifi 5000 firmware.

