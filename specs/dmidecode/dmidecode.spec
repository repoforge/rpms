# $Id$
# Authority: dag
# Rationale: Includes all tools except dmidecode which ships with kernel-utils

### RHEL5 includes biosdecode, ownership and vpddecode inside dmidecode package
# ExclusiveDist: el2 rh7 rh9 el3 el4

Summary: Tool to analyse BIOS DMI data
Name: dmidecode
Version: 2.7
Release: 0.1
License: GPLv2+
Group: System Environment/Base
URL: http://www.nongnu.org/dmidecode/

Source: http://download.savannah.gnu.org/releases/dmidecode/dmidecode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
### kernel-utils includes dmidecode
Requires: kernel-utils

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
%exclude %{_sbindir}/dmidecode

%changelog
* Fri Sep 19 2008 Dag Wieers <dag@wieers.com> - 1:2.7-1
- Initial package. (using DAR)
