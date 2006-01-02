# $Id$
# Authority: matthias
# Dist: nodist

Summary: Firmware for Intel® PRO/Wireless 2100 network adaptors
Name: ipw2100-firmware
Version: 1.3
Release: 2
License: Distributable
Group: System Environment/Kernel
URL: http://ipw2100.sourceforge.net/firmware.php
# License agreement must be displayed before download (referer protection)
Source: ipw2100-fw-%{version}.tgz
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
%{__mkdir_p} %{buildroot}/lib/firmware
%{__install} -p -m 0644 *.fw %{buildroot}/lib/firmware/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE
/lib/firmware/*.fw


%changelog
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

