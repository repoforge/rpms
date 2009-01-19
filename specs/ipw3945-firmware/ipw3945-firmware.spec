# $Id$
# Authority: matthias
# Dist: nodist

%define real_name ipw3945-ucode

Summary: Firmware for Intel® PRO/Wireless 3945 network adaptors
Name: ipw3945-firmware
Version: 1.14.2
Release: 2
License: Distributable
Group: System Environment/Kernel
URL: http://bughost.org/ipw3945/

Source0: http://bughost.org/ipw3945/ucode/ipw3945-ucode-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: dos2unix
### Require the binary user space regulatory daemon, so that installing this
### firmware package is enough
Requires: ipw3945d

%description
The file ipw3945.ucode provided in this package is required to be present on
your system in order for the Intel PRO/Wireless 3945ABG Network Connection
Adapater driver for Linux (ipw3945) to be able to operate on your system.

%prep
%setup -n %{real_name}-%{version}
dos2unix LICENSE.ipw3945-ucode README.ipw3945-ucode

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 ipw3945.ucode %{buildroot}/lib/firmware/ipw3945.ucode
%{__install} -Dp -m0644 LICENSE.ipw3945-ucode %{buildroot}/lib/firmware/LICENSE.ipw3945-ucode
%{__install} -Dp -m0644 README.ipw3945-ucode %{buildroot}/lib/firmware/README.ipw3945-ucode

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc /lib/firmware/LICENSE.ipw3945-ucode
%doc /lib/firmware/README.ipw3945-ucode
/lib/firmware/ipw3945.ucode

%changelog
* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 1.14.2-2
- Bring firmware package in to line with others wrt. license.

* Thu Mar 30 2006 Matthias Saou <http://freshrpms.net> 1.14.2-1
- Update to 1.14.2.
- Remove suffix from LICENSE and README files.
- Fix end of line encoding of LICENSE and README files with dos2unix.

* Thu Mar 30 2006 Matthias Saou <http://freshrpms.net> 1.13-1
- Initial RPM package, based on ipw2200-firmware.
