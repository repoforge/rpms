# $Id$
# Authority: dag

### EL6 ships with ipmitool-1.8.11-6.el6
# ExclusiveDist: el2 el3 el4 el5

### FIXME: Added included sysv scripts.

Summary: Utility for IPMI control
Name: ipmitool
Version: 1.8.8
Release: 1%{?dist}
License: BSD
Group: System Environment/Kernel
URL: http://ipmitool.sourceforge.net/

Source: http://dl.sf.net/ipmitool/ipmitool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ipmitool is a utility for interfacing with devices that support the
Intelligent Platform Management Interface specification. IPMI is an
open standard for machine health, inventory, and remote power control.

ipmitool can communicate with IPMI-enabled devices through either a
kernel driver such as OpenIPMI or over the RMCP LAN protocol defined in
the IPMI specification.  IPMIv2 adds support for encrypted LAN
communications and remote Serial-over-LAN functionality.

It provides commands for reading the Sensor Data Repository (SDR) and
displaying sensor values, displaying the contents of the System Event
Log (SEL), printing Field Replaceable Unit (FRU) information, reading
and setting LAN configuration, and chassis power control.

%prep
%setup

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
    --with-kerneldir
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc %{_mandir}/man1/ipmitool.1*
%doc %{_mandir}/man8/ipmievd.8*
%{_bindir}/ipmitool
%{_sbindir}/ipmievd
%{_datadir}/ipmitool/
%exclude %{_datadir}/doc/ipmitool/

%changelog
* Wed Feb 21 2007 Dag Wieers <dag@wieers.com> - 1.8.8-1
- Initial package. (using DAR)
