# $Id$
# Authority: dag
# Upstream: <bluez-devel$lists,sourceforge,net>

# ExclusiveDist: rh6 el2 rh7 rh8 rh9 el3 fc1


%{?el3:%define _without_dbus 1}
%{?rh9:%define _without_dbus 1}
%{?rh8:%define _without_dbus 1}
%{?rh7:%define _without_dbus 1}
%{?el2:%define _without_dbus 1}
%{?rh6:%define _without_dbus 1}

%define _bindir /bin
%define _sbindir /sbin

Summary: Bluetooth utilities
Name: bluez-utils
Version: 2.10
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://bluez.sourceforge.net/

Source: http://bluez.sf.net/download/bluez-utils-%{version}.tar.gz
Patch3: bluez-utils-2.9-pie.patch
Patch10: bluez-utils-2.9-conf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExcludeArch: s390 s390x
BuildRequires: bluez-libs-devel >= 2.0, flex
%{!?_without_dbus:BuildRequires: dbus-devel}

Obsoletes: bluez-pan <= %{version}-%{release}
Obsoletes: bluez-sdp <= %{version}-%{release}

%description
Bluetooth utilities (bluez-utils):

hcitool, hciattach, hciconfig, hcid
l2ping, start scripts (Red Hat),
pcmcia configuration files

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package cups
Summary: CUPS printer backend for Bluetooth printers
Group: System Environment/Daemons
Requires: bluez-libs >= %{version}
Requires: cups

%description cups
This package contains the CUPS backend

%prep
%setup

### Patch2: bluez-utils-2.2-pcmciaerr.patch perl oneliner
%{__perl} -pi.pcmciaerr -e 's|^(  bind "serial_cs") class "bluetooth"$|$1|' pcmcia/bluetooth.conf

%patch3 -p1 -b .pie
%patch10 -b .conf

### FIXME: mandir is defined as /usr/share/man
%{__perl} -pi.mandir -e 's|^(mandir) = .*$|$1 = \$(datadir)/man|' rfcomm/Makefile.am tools/Makefile.am

%{__cat} <<'EOF' >bluetooth.sysv
#!/bin/sh
#
# bluetooth    Bluetooth subsystem starting and stopping
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: 2345 25 90
# description: Bluetooth subsystem

source %{_initrddir}/functions

[ -x %{_sbindir}/hcid ] || exit 1

### Default variables
HCID_ENABLE=true
SDPD_ENABLE=true
HIDD_ENABLE=true
HID2HCI_ENABLE=true
RFCOMM_ENABLE=true
PAND_ENABLE=false
DUND_ENABLE=false

HCID_CONFIG="%{_sysconfdir}/bluetooth/hcid.conf"
RFCOMM_CONFIG="%{_sysconfdir}/bluetooth/rfcomm.conf"

HIDD_OPTIONS=""
DUND_OPTIONS="--listen --persist"
PAND_OPTIONS="--listen --role NAP"

SYSCONFIG="%{_sysconfdir}/sysconfig/bluetooth"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="bluetooth"
desc="Bluetooth"

start() {

	if [ "$HCID_ENABLE" == "true" ]; then
		prog="hcid"
        	echo -n $"Starting $desc ($prog): "
		daemon $prog -f $HCID_CONFIG
		echo
	fi

	if [ "$SDPD_ENABLE" == "true" ]; then
		prog="sdpd"
        	echo -n $"Starting $desc ($prog): "
		daemon $prog
		echo
	fi

	if [ "$HIDD_ENABLE" == "true" ]; then
		desc="Bluetooth Human Interface Device Daemon"
		prog="hidd"
        	echo -n $"Starting $desc ($prog): "
		daemon $prog --server $HIDD_OPTIONS
		echo
	fi

	if [ "$HID2HCI_ENABLE" == "true" ]; then
		desc="Bluetooth"
		prog="hid2hci"
		echo -n $"Starting $desc ($prog): "
		daemon $prog --tohci
		echo
	fi

	if [ "$RFCOMM_ENABLE" == "true" ]; then
		prog="rfcomm"
		echo -n $"Starting $desc ($prog): "
		daemon $prog -f $RFCOMM_CONFIG bind all
		echo
	fi

	if [ "$DUND_ENABLE" == "true" ]; then
		desc="Bluetooth Dial-Up-Networking Daemon"
		prog="dund"
		echo -n $"Starting $desc ($prog): "
		daemon $prog $DUND_OPTIONS
		echo
	fi

	if [ "$PAND_ENABLE" == "true" ]; then
		desc="Bluetooth Personal Area Networking Daemon"
		prog="pand"
		echo -n $"Starting $desc ($prog): "
		daemon $prog $PAND_OPTIONS
		echo
	fi

	prog="bluetooth"
	touch %{_localstatedir}/lock/subsys/$prog
	return 0
}

stop() {
	for prog in pand dund; do
		pidofproc $prog &>/dev/null || continue
		echo -n $"Shutting down $desc ($prog): "
		killproc $prog
		echo
	done

	prog="rfcomm"
	echo -n $"Shutting down $desc ($prog): "
	$prog release all
	killproc $prog
	echo

	for prog in hidd sdpd hcid; do
		pidofproc $prog &>/dev/null || continue
		echo -n $"Shutting down $desc ($prog): "
		killproc $prog
		echo
	done

	prog="bluetooth"
	rm -f %{_localstatedir}/lock/subsys/$prog
	return 0
}

restart() {
	stop
	start
}

case "$1" in
  start)
	start
        ;;
  stop)
	stop
        ;;
  restart|reload)
	restart
	;;
  condrestart)
        [ -e %{_localstatedir}/lock/subsys/$prog ] && restart
        RETVAL=$?
        ;;
  status)
        status hcid
        status sdpd
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|condrestart|status}"
        RETVAL=1
esac

exit $RETVAL
EOF

%build
%configure \
	--enable-cups \
%{!?_without_dbus:--enable-dbus} \
	--enable-hid2hci \
	--enable-pcmcia
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 bluetooth.sysv %{buildroot}%{_initrddir}/bluetooth
%{__install} -Dp -m0644 scripts/bluetooth.default %{buildroot}%{_sysconfdir}/sysconfig/bluetooth
%{__install} -Dp -m0755 cups/bluetooth %{buildroot}%{_libdir}/cups/backend/bluetooth


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
%config(noreplace) %{_sysconfdir}/sysconfig/bluetooth
%config %{_initrddir}/bluetooth
%config %{_sysconfdir}/pcmcia/bluetooth.conf
%config %{_sysconfdir}/pcmcia/bluetooth
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sysconfdir}/default/bluetooth
%exclude %{_sysconfdir}/init.d/bluetooth

%files cups
%defattr(-, root, root, 0755)
%{_libdir}/cups/backend/bluetooth

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 30 2006 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to new release 2.10.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 2.9-1
- Updated to new release 2.9.
- Reworked sysv script.

* Wed Feb 04 2004 Dag Wieers <dag@wieers.com> - 2.4-1
- Fixed location from sysv script.
- Initial package. (using DAR)
