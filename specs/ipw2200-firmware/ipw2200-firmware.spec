# $Id$
# Authority: matthias
# Dist: nodist

Summary: Firmware for Intel® PRO/Wireless 2200 network adaptors
Name: ipw2200-firmware
Version: 2.0
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://ipw2200.sourceforge.net/firmware.php
# License agreement must be displayed before download (referer protection)
Source: ipw2200-fw-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
This package contains the firmware files required by the ipw-2200 driver for
Linux. Usage of the firmware is subject to the terms contained in :
%{_defaultdocdir}/%{name}-%{version}/LICENSE. Please read it carefully.


%prep
%setup -c


%build


%install
%{__rm} -rf %{buildroot}
# Install all firmware files
%{__mkdir_p} %{buildroot}/lib/firmware \
             %{buildroot}%{_sysconfdir}/firmware \
             %{buildroot}%{_libdir}/hotplug/firmware
%{__install} -m 0644 *.fw %{buildroot}/lib/firmware/
# Symlink all of them for new and old hotplug loading to work
for file in *.fw; do
    %{__ln_s} /lib/firmware/${file} \
        %{buildroot}%{_sysconfdir}/firmware/
    %{__ln_s} /lib/firmware/${file} \
        %{buildroot}%{_libdir}/hotplug/firmware/
done


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE
/lib/firmware/*.fw
%{_sysconfdir}/firmware/*.fw
%{_libdir}/hotplug/firmware/*.fw


%changelog
* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net> 2.0-1
- Update to 2.0.
- Now put the files in /lib/firmware and symlinks in other dirs.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net> 1.2-1
- Initial RPM release, based on the ipw2100-firmware spec file.

