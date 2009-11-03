# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Application to read out information from the Belgian electronic ID card
%define real_name Belgian_Identity_Card_Run-time
Name: eid-belgium
Version: 2.5.9
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://eid.belgium.be/

### Since it needs a specific referer, download it from http://www.belgium.be/zip/eid_datacapture_nl.html
Source: http://www.belgium.be/zip/Belgian_Identity_Card_Run-time%{version}.tar.bz2
Patch0: eid-belgium-2.5.9-openscreader.patch
Patch1: eid-belgium-2.5.9-reader-pcsc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### SCons doesn't build when eid-belgium is already installed
BuildConflicts: eid-belgium
BuildRequires: scons, wxGTK-devel >= 2.4, openssl-devel >= 0.9.7, pcsc-lite-devel >= 1.2.9
BuildRequires: qt-devel >= 3.3.3, java-sdk
#BuildRequires: java-sdk-1.4.2
Provides: belpic = %{version}-%{release}
Obsoletes: belpic <= %{version}-%{release}
Provides: beid = %{version}-%{release}
Obsoletes: beid <= %{version}-%{release}

%description
This application allows the user to read out any information from a
Belgian electronic ID card, by using libbeid and libbeidlibopensc to
read the data from the card and parse it. Both identity information and
information about the stored cryptographic keys can be read in a
user-friendly manner, and can easily be printed out or stored for later
reviewal.

The application verifies the signature of the identity information,
checks whether it was signed by a government-issued key, and optionally
checks the certificate against the government's Certificate Revocation List
(CRL) and/or by using the Online Certificate Status Protocol (OCSP) against
the government's servers.

%prep
%setup -n beid-%{version}

%patch0 -p0
%patch1 -p0

%{__cat} <<EOF >beidcrld.sysconfig
OPTIONS=""
EOF

%{__cat} <<'EOF' >beidcrld.sysv
#!/bin/bash
#
# Init file for the Belgian electronic ID card CRL daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 90 10
# description: Belgian electronic ID card CRL daemon
#
# processname: beidcrld
# config: %{_sysconfdir}/sysconfig/beidcrld

source %{_initrddir}/functions

[ -x %{_bindir}/beidcrld ] || exit 1

### Default variables
SYSCONFIG="/etc/sysconfig/beidcrld"
OPTIONS=""

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="beidcrld"
desc="Belgian eID CRL daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog $OPTIONS
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	killproc $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

restart() {
	stop
	start
}

reload() {
	echo -n $"Reloading $desc ($prog): "
	killproc $prog -HUP
	RETVAL=$?
	echo
	return $RETVAL
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	restart
	;;
  reload)
	reload
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/$prog ] && restart
	RETVAL=$?
	;;
  status)
	status $prog
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%{__cat} <<EOF >beidpcscd.sysconfig
OPTIONS=""
EOF

%{__cat} <<'EOF' >beidpcscd.sysv
#!/bin/bash
#
# Init file for the Belgian electronic ID card PCSC daemon
#
# Written by Dag Wieers <dag@wieers.com>
#
# chkconfig: - 90 10
# description: Belgian electronic ID card PCSC daemon
#
# processname: beidpcscd
# config: %{_sysconfdir}/sysconfig/beidpcscd

source %{_initrddir}/functions

[ -x %{_bindir}/beidpcscd ] || exit 1

### Default variables
SYSCONFIG="/etc/sysconfig/beidpcscd"
OPTIONS=""

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

RETVAL=0
prog="beidpcscd"
desc="Belgian eID PCSC daemon"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog $OPTIONS
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	killproc $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

restart() {
	stop
	start
}

reload() {
	echo -n $"Reloading $desc ($prog): "
	killproc $prog -HUP
	RETVAL=$?
	echo
	return $RETVAL
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	restart
	;;
  reload)
	reload
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/$prog ] && restart
	RETVAL=$?
	;;
  status)
	status $prog
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

### Fixing the references to /usr/local in some files
%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{buildroot}%{_sysconfdir}|g' \
	SConstruct
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{buildroot}%{_libdir}|g' \
	src/newpkcs11/SConscript
%{__perl} -pi.orig -e 's|/etc/init.d\b|%{buildroot}%{_initrddir}|g' \
	src/beidservicecrl/SConscript \
	"src/Belpic PCSC Service/SConscript"

%{__perl} -pi.orig -e 's|/usr/local/etc\b|%{_sysconfdir}|g' \
	src/beidcommon/config.cpp \
	src/newpkcs11/config.h
%{__perl} -pi.orig -e 's|/usr/local/lib\b|%{_libdir}|g' \
	src/newpkcs11/etc/Belgian_eID_PKCS11_java.cfg \
	src/newpkcs11/etc/beid-pkcs11-register.html
%{__perl} -pi.orig -e 's|/usr/local/bin/beidgui.png\b|%{_datadir}/icons/beidgui.png|g' \
	src/eidviewer/beidgui.desktop
%{__perl} -pi.orig -e 's|/usr/local/bin\b|%{_bindir}|g' \
	src/beidservicecrl/belgium.be-beidcrld \
	"src/Belpic PCSC Service/belgium.be-beidpcscd" \
	src/eidviewer/beidgui.desktop
%{__perl} -pi.orig -e 's|/usr/local/share\b|%{_datadir}|g' \
	src/eidviewer/beidgui.conf

%build
export CFLAGS="%{optflags}"
export JAVA_HOME="$(readlink /etc/alternatives/java_sdk)"
source "/etc/profile.d/qt.sh"
scons configure prefix="%{_prefix}"
scons prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_libdir}
source "/etc/profile.d/qt.sh"
scons install --cache-disable prefix="%{buildroot}%{_prefix}" libdir="%{buildroot}%{_libdir}"

%{__install} -Dp -m0755 beidcrld.sysv %{buildroot}%{_initrddir}/beidcrld
%{__install} -Dp -m0755 beidpcscd.sysv %{buildroot}%{_initrddir}/beidpcscd
%{__install} -Dp -m0644 beidcrld.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/beidcrld
%{__install} -Dp -m0644 beidpcscd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/beidpcscd

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--add-category Utility                     \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_bindir}/beidgui.desktop

%{__install} -d -m0755 %{buildroot}%{_datadir}/icons/
%{__mv} -vf %{buildroot}%{_bindir}/beidgui.png %{buildroot}%{_datadir}/icons/beidgui.png

### Fix library symlinks
for lib in $(ls %{buildroot}%{_libdir}/libbeid*.so.?.?.?); do
	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?}
done

### Fix locale files
for file in $(ls %{buildroot}%{_datadir}/locale/beidgui_*.mo); do
	lang="${file%.mo}"
	lang="${lang#%{buildroot}%{_datadir}/locale/beidgui_}"
	%{__mkdir} -p %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
	%{__mv} -f $file %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/beidgui.mo
done
%find_lang beidgui

%post
/sbin/ldconfig
/sbin/chkconfig --add beidcrld
/sbin/chkconfig --add beidpcscd
update-desktop-database %{_datadir}/applications &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service beidcrld stop &>/dev/null || :
        /sbin/chkconfig --del beidcrld
        /sbin/service beidpcscd stop &>/dev/null || :
        /sbin/chkconfig --del beidpcscd
fi

%postun
/sbin/ldconfig
/sbin/service beidcrld condrestart &>/dev/null || :
/sbin/service beidpcscd condrestart &>/dev/null || :
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f beidgui.lang
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL README VERSION doc/*.rtf doc/*.doc
%doc %{_mandir}/man1/beid-pkcs11-tool.1*
%doc %{_mandir}/man1/beid-tool.1*
%config(noreplace) %{_sysconfdir}/beidbase.conf
%config(noreplace) %{_sysconfdir}/beidgui.conf
%config(noreplace) %{_sysconfdir}/sysconfig/beidcrld
%config(noreplace) %{_sysconfdir}/sysconfig/beidpcscd
%config %{_initrddir}/beidcrld
%config %{_initrddir}/beidpcscd
%exclude %{_initrddir}/belgium.be-beidcrld
%exclude %{_initrddir}/belgium.be-beidpcscd
%{_bindir}/beid-pkcs11-tool
%{_bindir}/beid-tool
%{_bindir}/beidcrld
%{_bindir}/beidpcscd
%{_bindir}/beidgui
%{_datadir}/applications/%{desktop_vendor}-beidgui.desktop
%{_datadir}/beid/
%exclude %{_datadir}/beid/eID-toolkit_licensingtermsconditions*.rtf
%exclude %{_datadir}/beid/DeveloperGuide.doc
%{_datadir}/icons/beidgui.png
%{_includedir}/beid/
%{_libdir}/libbeid*.so*
%{_libdir}/pkcs11/

%changelog
* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 2.5.9-2
- Added patch to build against pcsc-lite 1.4. (Daniel De Baerdemaeker)

* Fri Feb 09 2007 Dag Wieers <dag@wieers.com> - 2.5.9-1
- Initial package. (using DAR)
