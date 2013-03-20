# $Id$
# Authority: dag

### EL6 ships with ccid-1.3.9-3.el6
### EL5 ships with ccid-1.3.8-1.el5
# Tag: rfx
## ExclusiveDist: el2 el3 el4

%define usbdropdir %(pkg-config libpcsclite --variable="usbdropdir" 2>/dev/null)
%define real_name ccid

Summary: Generic USB CCID smart card reader driver
Name: pcsc-lite-ccid
Version: 1.3.10
Release: 1%{?dist}
License: LGPLv2+ and GPLv2+
Group: System Environment/Libraries
URL: http://pcsclite.alioth.debian.org/ccid.html

### Source is a fixed address per file, substituting version doesn't work.
Source: http://alioth.debian.org/download.php/2924/ccid-%{version}.tar.bz2
Patch0: ccid-1.3.10-dectel.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libusb-devel >= 0.1.7
BuildRequires: pcsc-lite-devel >= 1.3.3
Requires: initscripts
Requires: libusb >= 0.1.7
Requires: pcsc-lite >= 1.3.3

Provides: pcsc-ifd-handler
Provides: ccid = %{version}-%{release}
Obsoletes: ccid <= %{version}-%{release}

%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0

%build
%configure --enable-twinserial
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mv} %{buildroot}/usr/share/doc/ccid/README_Kobil_mIDentity_switch.txt .
%{__cp} -av src/openct/LICENSE LICENSE.openct
%{__install} -Dp -m0644 src/pcscd_ccid.rules %{buildroot}%{_sysconfdir}/udev/rules.d/85-pcscd_ccid.rules
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/reader.conf.d/
%{__mv} %{buildroot}%{_sysconfdir}/reader.conf %{buildroot}%{_sysconfdir}/reader.conf.d/libccidtwin

%clean
%{__rm} -rf %{buildroot}

%post
if /sbin/service pcscd status &>/dev/null; then
    /usr/sbin/pcscd -H &>/dev/null || :
fi

%postun
if /sbin/service pcscd status &>/dev/null; then
    /usr/sbin/pcscd -H &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENSE.openct README README_Kobil_mIDentity_switch.txt
%doc %{_mandir}/man1/RSA_SecurID_getpasswd.1*
%doc %{_mandir}/man8/Kobil_mIDentity_switch.8*
%dir %{_sysconfdir}/reader.conf.d/
%config(noreplace) %{_sysconfdir}/reader.conf.d/libccidtwin
%dir %{_sysconfdir}/udev/rules.d/
%config %{_sysconfdir}/udev/rules.d/85-pcscd_ccid.rules
%{_bindir}/RSA_SecurID_getpasswd
%{_sbindir}/Kobil_mIDentity_switch
%{usbdropdir}/ifd-ccid.bundle/
%{usbdropdir}/serial/

%changelog
* Thu Feb 24 2011 Dag Wieers <dag@wieers.com> - 1.3.10-1
- Updated to release 1.3.10.

* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
