# $Id$
# Authority: dag

%define usbdropdir %(pkg-config libpcsclite --variable="usbdropdir" 2>/dev/null)

Summary: Generic USB CCID smart card reader driver
%define real_name ccid
Name: pcsc-lite-ccid
Version: 1.2.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://pcsclite.alioth.debian.org/ccid.html

### Source is a fixed address per file, substituting version doesn't work.
Source: http://alioth.debian.org/download.php/1867/ccid-1.2.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libusb-devel >= 0.1.7, pcsc-lite-devel >= 1.3.3
Requires: libusb >= 0.1.7, pcsc-lite >= 1.3.3
Requires: initscripts

Provides: pcsc-ifd-handler
Provides: ccid = %{version}-%{release}
Obsoletes: ccid <= %{version}-%{release}

%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-dependency-tracking \
	--disable-static \
	--enable-twinserial
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

#%{__install} -Dp -m0644 %{buildroot}%{_sysconfdir}/reader.conf %{buildroot}%{_sysconfdir}/reader.conf.d/gempctwin.conf
%{__mv} -f %{buildroot}%{_sysconfdir}/reader.conf GemPCTwin.reader.conf

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
	%{_initrddir}/pcscd try-restart &>/dev/null || :
fi

%postun
%{_initrddir}/pcscd try-restart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README GemPCTwin.reader.conf
%{usbdropdir}/ifd-ccid.bundle/
%{usbdropdir}/serial/

%changelog
* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
