# $Id$
# Authority: matthias

# Dist: nodist

Summary: Firmware for Intel® PRO/Wireless 2100 network adaptors
Name: ipw2100-firmware
Version: 1.1
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://ipw2100.sourceforge.net/firmware.php
Source0: http://cache-www.intel.com/cd/00/00/09/63/96377_96377.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
This package contains the firmware files required by the ipw-2100 driver for
Linux. Usage of the firmware is subject to the terms contained in :
%{_defaultdocdir}/%{name}-%{version}/LICENSE. Please read it carefully.


%prep
%setup -c


%build


%install
%{__rm} -rf %{buildroot}
# Install all firmware files
%{__mkdir_p} %{buildroot}%{_sysconfdir}/firmware \
             %{buildroot}%{_libdir}/hotplug/firmware
%{__install} -m 0644 *.fw %{buildroot}%{_sysconfdir}/firmware/
# Symlink all of them for hotplug loading to work
for file in *.fw; do
    %{__ln_s} %{_sysconfdir}/firmware/${file} \
        %{buildroot}%{_libdir}/hotplug/firmware/
done


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_sysconfdir}/firmware/*.fw
%{_libdir}/hotplug/firmware/*.fw


%changelog
* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net> 1.1-1
- Cosmetic spec file changes.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to firmware version 1.1.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Change description to explicitly point to the LICENSE file.

* Sat May  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

