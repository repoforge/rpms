# $Id$

# Authority: dag

Summary: Bluetooth firmware loader
Name: bluez-bluefw
Version: 1.0
Release: 0
License: GPL
Group: Applications/System
URL: http://bluez.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bluez.sf.net/download/bluez-bluefw-%{version}.tar.gz
Source1: pcmcia-includes.tar.gz
Patch0: bluez-bluefw-0.9-path.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


ExcludeArch: s390 s390x
BuildRequires: glibc-devel >= 2.2.4

%description
Bluetooth firmware loader.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%prep
%setup
%{__tar} -xvzf %{SOURCE1}
%patch0 -p1

%build
%configure \
	--with-kernel="$(pwd)"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	fwdir="%{buildroot}%{_sysconfdir}/bluetooth/firmware" \
	usbdir="%{buildroot}%{_sysconfdir}/hotplug/usb"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%config %{_sysconfdir}/bluetooth/firmware/*
%config %{_sysconfdir}/hotplug/usb/*
%{_sbindir}/bluefw

%changelog
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
