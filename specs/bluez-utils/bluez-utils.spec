# $Id$

# Authority: dag

### FIXME: configure has problems finding flex output using soapbox on RHEL3
# Soapbox: 0

%define _bindir /bin
%define _sbindir /sbin

Summary: Bluetooth utilities.
Name: bluez-utils
Version: 2.4
Release: 1
License: GPL
Group: Applications/System
URL: http://bluez.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://bluez.sf.net/download/bluez-utils-%{version}.tar.gz
Patch2: bluez-utils-2.2-pcmciaerr.patch
Patch5: bluez-utils-2.3-bluepin-gtk2.patch
Patch6: bluez-utils-2.5-pinwait.patch
Patch7: bluez-utils-2.3-tmpfile.patch
Patch8: bluez-utils-2.5-dbus.patch
Patch10: bluez-utils-2.3-conf.patch
Patch11: bluez-utils-2.3-status.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


ExcludeArch: s390 s390x
BuildRequires: bluez-libs-devel >= 2.0
BuildRequires: flex, autoconf, automake14
%{?rhfc1:BuildRequires: dbus-devel}

%description
Bluetooth utilities (bluez-utils):

hcitool, hciattach, hciconfig, hcid
l2ping, start scripts (Red Hat), 
pcmcia configuration files

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%prep
%setup

### Patch2: bluez-utils-2.2-pcmciaerr.patch perl oneliner
%{__perl} -pi.pcmciaerr -e 's|^(  bind "serial_cs") class "bluetooth"$|$1|' pcmcia/bluetooth.conf

%patch5 -p1 -b .bluepin
%patch6 -b .pinwait

### patch7: bluez-utils-2.3-tmpfile.patch perl oneliner
%{__perl} -pi.tmpfile -e 's|^(    /sbin/hciattach \$DEVICE \$MANFID) > /tmp/pcmcia$|$1|' pcmcia/bluetooth

%patch8 -p1 -b .dbus

%patch10 -p1 -b .conf
%patch11 -p1 -b .status

### FIXME: mandir is defined as /usr/usr/share/man
%{__perl} -pi.mandir -e 's|^(mandir) = .*$|$1 = \$(datadir)/man|' rfcomm/Makefile.am tools/Makefile.am

%build
aclocal-1.4; automake-1.4; autoconf
%configure \
	--enable-pcmcia \
%{?rhfc1:--enable-dbus}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%post
/sbin/chkconfig --add bluetooth

%preun
if [ $1 -eq 0 ]; then
        /sbin/service bluetooth stop &>/dev/null || :
	/sbin/chkconfig --del bluetooth
fi

%postun
/sbin/service bluetooth condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/bluetooth/
%config %{_initrddir}/*
%config %{_sysconfdir}/pcmcia/bluetooth.conf
%config %{_sysconfdir}/pcmcia/bluetooth
%{_bindir}/*
%{_sbindir}/*

%changelog
* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.4-1
- Fixed location from sysv script.
- Initial package. (using DAR)
