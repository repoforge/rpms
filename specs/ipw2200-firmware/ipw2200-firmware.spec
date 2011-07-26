# $Id$
# Authority: matthias
# Dist: nodist

### EL6 ships with ipw2200-firmware-3.1-4.el6
%{?el6:# Tag: rfx}

%define real_name ipw2200-fw

Summary: Firmware for Intel® PRO/Wireless 2200 network adaptors
Name: ipw2200-firmware
Version: 3.0
Release: 4%{?dist}
License: Distributable
Group: System Environment/Kernel
URL: http://ipw2200.sourceforge.net/firmware.php

# License agreement must be displayed before download (referer protection)
Source0: ipw2200-fw-%{version}.tgz
Source1: ipw2200-fw-2.4.tgz
Source2: ipw2200-fw-2.3.tgz
Source3: ipw2200-fw-2.2.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
This package contains the firmware files required by the ipw2200 driver for
Linux. Usage of the firmware is subject to the terms and conditions contained
in /lib/firmware/LICENSE.ipw2200. Please read it carefully.

%prep
%setup -n %{real_name}-%{version} -a 1 -a 2 -a 3

%build

%install
%{__rm} -rf %{buildroot}
### Terms state that the LICENSE *must* be in the same directory as the firmware
%{__install} -Dp -m0644 LICENSE %{buildroot}/lib/firmware/LICENSE.ipw2200
%{__install} -p -m0644 *.fw %{buildroot}/lib/firmware/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.ipw2200
/lib/firmware/*.fw

%changelog
* Tue Jul 26 2011 Yury V. Zaytsev <yury@shurup.com> - 3.0-4
- RFX'ed on RHEL6.

* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net> 3.0-3
- Move the LICENSE as LICENSE.ipw2200 in the firmware directory to fully
  comply to the Intel redistribution terms and conditions.

* Sun Jun 25 2006 Matthias Saou <http://freshrpms.net> 3.0-2
- Fix inclusion of the 3.0 firmware files.

* Sat Jun 24 2006 Dag Wieers <dag@wieers.com> - 3.0-1
- Updated to release 3.0.

* Mon Jan  2 2006 Matthias Saou <http://freshrpms.net> 2.4-2
- Convert spec file to UTF-8.

* Thu Oct 27 2005 Matthias Saou <http://freshrpms.net> 2.4-1
- Update to 2.4, but keep 2.2 and 2.3 included too.

* Tue May 31 2005 Matthias Saou <http://freshrpms.net> 2.3-2
- Also bundle 2.2 firmware : The recent driver downgrade required this :-/

* Wed May 25 2005 Matthias Saou <http://freshrpms.net> 2.3-1
- Update to 2.3, required by latest FC4 dev and 2.6.12rc.

* Thu Apr 21 2005 Matthias Saou <http://freshrpms.net> 2.2-3
- Remove all symlinks, the only useful location is /lib/firmware now.
- No longer rename all firmware files, recent ipw2200 modules expect the
  default names now (tested w/ FC3 2.6.11 updates and FC4test).

* Thu Feb 17 2005 Matthias Saou <http://freshrpms.net> 2.2-2
- Rename all files from ipw-2.2-* to ipw2200_* as required.

* Wed Feb  9 2005 Matthias Saou <http://freshrpms.net> 2.2-1
- Update to 2.2, required by latest FC kernels.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net> 2.0-1
- Update to 2.0.
- Now put the files in /lib/firmware and symlinks in other dirs.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net> 1.2-1
- Initial RPM release, based on the ipw2100-firmware spec file.

