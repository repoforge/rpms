# $Id$
# Authority: matthias
# Dist: nodist

### EL6 ships with ipw2100-firmware-1.3-11.el6

%define real_name ipw2100-fw

Summary: Firmware for Intel® PRO/Wireless 2100 network adaptors
Name: ipw2100-firmware
Version: 1.3
Release: 3%{?dist}
License: Distributable
Group: System Environment/Kernel
URL: http://ipw2100.sourceforge.net/firmware.php

### License agreement must be displayed before download (referer protection)
Source: ipw2100-fw-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
This package contains the firmware files required by the Intel® PRO/Wireless
2100 (ipw2100) driver for Linux.

IMPORTANT NOTICE : This package is covered by the Intel® license found in the
/lib/firmware/LICENSE.ipw2100 file. Usage of this package requires agreeing
to the terms of the Intel® license.

%prep
%setup -c %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
### Terms state that the LICENSE *must* be in the same directory as the firmware
%{__install} -Dp -m0644 LICENSE %{buildroot}/lib/firmware/LICENSE.ipw2100
%{__install} -p -m0644 *.fw %{buildroot}/lib/firmware/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.ipw2100
/lib/firmware/*.fw

%changelog
* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net> 1.3-3
- Move the LICENSE as LICENSE.ipw2100 in the firmware directory to fully
  comply to the Intel redistribution terms and conditions.

* Mon Jan  2 2006 Matthias Saou <http://freshrpms.net> 1.3-2
- Convert spec file to UTF-8.
- Remove all symlinks to keep only /lib/firmware like in ipw2200-firmware.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net> 1.3-1
- Now put the files in /lib/firmware and symlinks in other dirs.

* Tue Sep 28 2004 Matthias Saou <http://freshrpms.net> 1.3-1
- Update to 1.3.

* Wed Aug 25 2004 Matthias Saou <http://freshrpms.net> 1.2-1
- Update to 1.2.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net> 1.1-1
- Cosmetic spec file changes.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to firmware version 1.1.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Change description to explicitly point to the LICENSE file.

* Sat May  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

