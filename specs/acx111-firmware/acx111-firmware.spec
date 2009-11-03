# $Id$
# Authority: matthias
# Dist: nodist

Summary: Firmware for Texas Instruments ACX111 network adaptors
Name: acx111-firmware
Version: 1.2.1.34
Release: 1%{?dist}
License: Unknown
Group: System Environment/Kernel
URL: http://acx100.sourceforge.net/wiki/Firmware
Source0: http://acx100.erley.org/acx_fw/acx111_netgear_wg311v2/fw1/FwRad16.bin_%{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Firmware file for Texas Instruments ACX111 based wireless network adaptors,
required by the acx Linux kernel module.


%prep


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/lib/firmware
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}/lib/firmware/tiacx111c16


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
/lib/firmware/tiacx111c16


%changelog
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net> 1.2.1.34-1
- Initial RPM release, based on the ipw2200-firmware spec file.

