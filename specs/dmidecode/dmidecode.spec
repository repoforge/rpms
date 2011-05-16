# $Id$
# Authority: dag

### Includes all tools except dmidecode which ships with kernel-utils on RHEL2, RHEL3 and RHEL4
%{?el4:%define _without_dmidecode 1}
%{?el3:%define _without_dmidecode 1}
%{?el2:%define _without_dmidecode 1}

### EL5+ includes biosdecode, ownership and vpddecode inside dmidecode package
### EL6 ships with dmidecode-2.10-1.30.1.el6
### EL5 ships with dmidecode-2.10-3.el5
%{!?_without_dmidecode:# Tag: rfx}

Summary: Tool to analyse BIOS DMI data
Name: dmidecode
Epoch: 1
Version: 2.11
Release: 0.1%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://www.nongnu.org/dmidecode/

Source: http://download.savannah.gnu.org/releases/dmidecode/dmidecode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86} x86_64
### kernel-utils includes dmidecode on RHEL2, RHEL3 and RHEL4
%{?_without_dmidecode:Requires: kernel-utils}

%description
dmidecode reports information about x86 & ia64 hardware as described in the
system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number,
BIOS version, asset tag as well as a lot of other details of varying
level of interest and reliability depending on the manufacturer.

This will often include usage status for the CPU sockets, expansion
slots (e.g. AGP, PCI, ISA) and memory module slots, and the list of
I/O ports (e.g. serial, parallel, USB).

This package does not include dmidecode, which ships with the kernel-utils
package.

%prep
%setup

%build
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install-bin install-man DESTDIR="%{buildroot}" prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG LICENSE README
%doc %{_mandir}/man8/biosdecode.8*
%doc %{_mandir}/man8/dmidecode.8*
%doc %{_mandir}/man8/ownership.8*
%doc %{_mandir}/man8/vpddecode.8*
%{_sbindir}/biosdecode
%{_sbindir}/ownership
%{_sbindir}/vpddecode
%{?_without_dmidecode:%exclude %{_sbindir}/dmidecode}
%{!?_without_dmidecode:%{_sbindir}/dmidecode}

%changelog
* Mon May 16 2011 Dag Wieers <dag@wieers.com> - 1:2.11-0.1
- Updated to release 2.11.

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 1:2.10-0.1
- Updated to release 2.10.

* Fri Sep 19 2008 Dag Wieers <dag@wieers.com> - 1:2.7-1
- Initial package. (using DAR)
