# $Id$
# Authority: ned
# Dist: nodist

%define real_name iwlwifi-5000-ucode

Summary: Firmware for IntelÂ® Wireless WiFi Link 5000AGN series network adapters
Name: iwl5000-firmware
Version: 8.24.2.12
Release: 1
License: Redistributable, no modification permitted
Group: System Environment/Kernel
URL: http://intellinuxwireless.org/

Source0: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-%{version}.tar.gz
Source1: http://intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-ucode-5.4.A.11.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__install} -Dp -m0644 iwlwifi-5000-2.ucode %{buildroot}/lib/firmware/iwlwifi-5000-2.ucode

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE* README*
/lib/firmware/iwlwifi-5000-1.ucode
/lib/firmware/iwlwifi-5000-2.ucode

%changelog
* Wed May 27 2009 Dag Wieers <dag@wieers.com> - 8.24.2.12-1
- Updated to release 8.24.2.12.

* Sat Jan 24 2009 Dag Wieers <dag@wieers.com> - 5.4.A.11-2
- Moved the LICENSE and README to %%{_docdir}.

* Thu Jan 15 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 5.4.A.11-1
- Cosmetic changes for RPMforge integration.

* Fri Jan 02 2009 Philip J Perry <ned at unixmail.co.uk> - 5.4.A.11-1
- Initial RPM package based on 5.4.A.11 iwlwifi 5000 firmware.

