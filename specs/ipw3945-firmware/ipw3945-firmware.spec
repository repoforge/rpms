# $Id$
# Authority: matthias
# Dist: nodist

Summary: Firmware for Intel® PRO/Wireless 3945 network adaptors
Name: ipw3945-firmware
Version: 1.13
Release: 1
License: Distributable
Group: System Environment/Kernel
URL: http://bughost.org/ipw3945/
Source0: http://bughost.org/ipw3945/ucode/ipw3945-ucode-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
# Require the binary user space regulatory daemon, so that installing this
# firmware package is enough
Requires: ipw3945d

%description
The file ipw3945.ucode provided in this package is required to be present on
your system in order for the Intel PRO/Wireless 3945ABG Network Connection
Adapater driver for Linux (ipw3945) to be able to operate on your system.


%prep
%setup -n ipw3945-ucode-%{version}


%build


%install
%{__rm} -rf %{buildroot}
%{__install} -D -p -m 0644 ipw3945.ucode %{buildroot}/lib/firmware/ipw3945.ucode


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENSE.ipw3945-ucode README.ipw3945-ucode
/lib/firmware/ipw3945.ucode


%changelog
* Thu Mar 30 2006 Matthias Saou <http://freshrpms.net> 1.13-1
- Initial RPM package, based on ipw2200-firmware.

