# $Id$
# Authority: dag
# Upstream: <bluez-devel$lists,sf,net>

# ExclusiveDist: rh6 el2 rh7 rh8 rh9 fc1

%define _sbindir /sbin

Summary: Bluetooth firmware loader
Name: bluez-bluefw
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://bluez.sourceforge.net/

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Changed %%{_sbindir} to /sbin. (Soós Péter, RHbz #120881)

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
