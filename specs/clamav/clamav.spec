# $Id$
# Authority: dag
# Upstream: <clamav-devel$lists,sf,net>

### FIXME: Sysv script does not have condrestart option (redo sysv script)
### FIXME: amavisd-new requires clamd to run as user vscan, solution needed
### REMINDER: Look and sync with Petr Kristof's work

%{?el2:%define _without_milter 1}

Summary: Anti-virus software
Name: clamav
Version: 0.86.2
Release: 1
License: GPL
Group: Applications/System
URL: http://www.clamav.net/

Source: http://www.clamav.net/clamav-%{version}.tar.gz
#Source: http://dl.sf.net/clamav/clamav-%{version}.tar.gz
Source1: clamav.init
Source2: clamav-milter.init
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel, zlib-devel, gmp-devel, curl-devel
%{!?_without_milter:BuildRequires: sendmail-devel >= 8.12}
Requires: clamav-db = %{version}-%{release}

### Fedora Extras introduced them differently :(
Obsoletes: libclamav < %{version}-%{release}
Obsoletes: clamav-lib < %{version}-%{release}
Provides: libclamav

%description
Clam AntiVirus is a GPL anti-virus toolkit for UNIX. The main purpose of
this software is the integration with mail servers (attachment scanning).
The package provides a flexible and scalable multi-threaded daemon, a
command line scanner, and a tool for automatic updating via Internet.

The programs are based on a shared library distributed with the Clam
AntiVirus package, which you can use with your own software. Most
importantly, the virus database is kept up to date

%package -n clamd
Summary: The Clam AntiVirus Daemon
Group: System Environment/Daemons
Requires: clamav = %{version}-%{release}

### Fedora Extras introduced them differently :(
Obsoletes: clamav-server <= %{version}-%{release}

%description -n clamd
The Clam AntiVirus Daemon

%package milter
Summary: The Clam AntiVirus sendmail-milter Daemon
Group: Applications/System
Requires: clamd = %{version}-%{release}
Requires: sendmail

%description milter
The Clam AntiVirus sendmail-milter Daemon

%package db
Summary: Virus database for %{name}
Group: Applications/Databases

### Fedora Extras introduced them differently :(
Obsoletes: clamav-update <= %{version}-%{release}
Obsoletes: clamav-data <= %{version}-%{release}

%description db
The actual virus database for %{name}

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: clamav = %{version}-%{release}

### Fedora Extras introduced them differently :(
Obsoletes: libclamav-static-devel <= %{version}-%{release}
Obsoletes: libclamav-devel <= %{version}-%{release}
Provides: libclamav-static-devel, libclamav-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' libtool configure

%{__perl} -pi.orig -e '
		s|\@DBDIR\@|\$(localstatedir)/clamav|g;
		s|\@DBINST\@|\$(localstatedir)/clamav|g;
		s|\@CFGDIR\@|\$(sysconfdir)|g;
		s|\@CFGINST\@|\$(sysconfdir)|g;
		s|^\@INSTALL_CLAMAV_CONF_TRUE\@|\t|g;
	' database/Makefile.in etc/Makefile.in

%{__perl} -pi.orig -e '
		s|^(Example)|#$1|;
		s|^#(LogFile) .+$|$1 %{_localstatedir}/log/clamav/clamd.log|;
		s|^#(LogFileMaxSize) .*|$1 0|;
		s|^#(LogTime)|$1|;
		s|^#(LogSyslog)|$1|;
		s|^#(PidFile) .+$|$1 %{_localstatedir}/run/clamav/clamd.pid|;
		s|^#(TemporaryDirectory) .+$|$1 %{_localstatedir}/tmp|;
		s|^#(DatabaseDirectory) .+$|$1 %{_localstatedir}/clamav|;
		s|^(LocalSocket) .+$|#$1 %{_localstatedir}/run/clamav/clamd.sock|;
		s|^#(FixStaleSocket)|$1|;
		s|^#(TCPSocket) .+$|$1 3310|;
		s|^#(TCPAddr) .+$|$1 127.0.0.1|;
		s|^#(MaxConnectionQueueLength) .+$|$1 30|;
		s|^#(StreamSaveToDisk)|$1|;
		s|^#(MaxThreads ) .+$|$1 50|;
		s|^#(ReadTimeout) .+$|$1 300|;
		s|^#(User) .+$|$1 clamav|;
		s|^#(AllowSupplementaryGroups)|$1|;
		s|^#(DetectBrokenExecutables)|$1|;
		s|^#(ArchiveMaxCompressionRatio) .+|$1 300|;
		s|^#(ArchiveBlockEncrypted)|$1|;
		s|^#(ArchiveBlockMax)|$1|;
		s|^#(ScanMail)|$1|;
	' etc/clamd.conf

%{__perl} -pi.orig -e '
		s|^(Example)|#$1|;
		s|^#(DatabaseDirectory) .+$|$1 %{_localstatedir}/clamav|;
		s|^#(UpdateLogFile) .+$|$1 %{_localstatedir}/log/clamav/freshclam.log|;
		s|^#(PidFile) .+$|$1 %{_localstatedir}/run/clamav/freshclam.pid|;
		s|^#(DatabaseOwner) .+$|$1 clamav|;
		s|^(Checks) .+$|$1 24|;
		s|^#(NotifyClamd) .+$|$1 %{_sysconfdir}/clamd.conf|;
	' etc/freshclam.conf

%{__cat} <<EOF >clamd.logrotate
%{_localstatedir}/log/clamav/clamd.log {
	missingok
	notifempty
	create 644 clamav clamav
	postrotate
		killall -HUP clamd 2>/dev/null || :
	endscript
}
EOF

%{__cat} <<EOF >freshclam.logrotate
%{_localstatedir}/log/clamav/freshclam.log {
	missingok
	notifempty
	create 644 clamav clamav
}
EOF

%{__cat} <<'EOF' >freshclam.cron
#!/bin/sh

### A simple update script for the clamav virus database.
### This could as well be replaced by a SysV script.

### fix log file if needed
LOG_FILE="%{_localstatedir}/log/clamav/freshclam.log"
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    chmod 644 "$LOG_FILE"
    chown clamav.clamav "$LOG_FILE"
fi

%{_bindir}/freshclam \
    --quiet \
    --datadir="%{_localstatedir}/clamav" \
    --log="$LOG_FILE" \
    --log-verbose \
    --daemon-notify="%{_sysconfdir}/clamd.conf"
EOF

%{__cat} <<EOF >clamav-milter.sysconfig
### Simple config file for clamav-milter, you should
### read the documentation and tweak it as you wish.

CLAMAV_FLAGS="
	--config-file=%{_sysconfdir}/clamd.conf
	--max-children=10
	--force-scan
	--quiet
	--dont-log-clean
	--noreject
	-obl local:%{_localstatedir}/clamav/clmilter.socket
"
EOF

%build
%configure  \
	--program-prefix="%{?_program_prefix}" \
%{!?_without_milter:--enable-milter} \
	--enable-id-check \
	--with-libcurl \
	--enable-dns \
	--disable-clamav \
	--with-user="clamav" \
	--with-group="clamav" \
	--with-dbdir="%{_localstatedir}/clamav" \
	--disable-zlib-vcheck
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/clamd
%{__install} -Dp -m0755 freshclam.cron %{buildroot}%{_sysconfdir}/cron.daily/freshclam
%{__install} -Dp -m0644 freshclam.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/freshclam
%{__install} -Dp -m0644 clamd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/clamav

%if %{!?_without_milter:1}0
%{__install} -Dp -m0755 %{SOURCE2} %{buildroot}%{_initrddir}/clamav-milter
%{__install} -Dp -m0644 clamav-milter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/clamav-milter
%else
%{__rm} %{buildroot}%{_mandir}/man8/clamav-milter.8*
%endif

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/clamav/
touch %{buildroot}%{_localstatedir}/log/clamav/freshclam.log
touch %{buildroot}%{_localstatedir}/log/clamav/clamd.log

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/clamav/

%post
/sbin/ldconfig 2>/dev/null

ZONES="/usr/share/zoneinfo/zone.tab"
CONFIG="/etc/sysconfig/clock"

if [ -r "$CONFIG" -a -r "$ZONES" ]; then
	source "$CONFIG"
	export CODE="$(grep -E "\b$ZONE\b" "$ZONES" | head -1 | cut -f1 | tr [A-Z] [a-z])"
fi

if [ -z "$CODE" ]; then
	export CODE="local"
fi

%{__perl} -pi -e '
		s|^(DatabaseMirror) database\.clamav\.net$|$1 db.$ENV{"CODE"}.clamav.net\n$1 db.local.clamav.net|;
		s|^(DatabaseMirror) db\.\.clamav\.net$|$1 db.$ENV{"CODE"}.clamav.net\n$1 db.local.clamav.net|;
	' %{_sysconfdir}/freshclam.conf{,.rpmnew} &>/dev/null || :

%postun
/sbin/ldconfig 2>/dev/null

%pre -n clamd
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || :

%post -n clamd
/sbin/chkconfig --add clamd

%preun -n clamd
if [ $1 -eq 0 ]; then
	/sbin/service clamd stop &>/dev/null || :
	/sbin/chkconfig --del clamd
fi

%postun -n clamd
/sbin/service clamd condrestart &>/dev/null || :

%post milter
/sbin/chkconfig --add clamav-milter

%preun milter
if [ $1 -eq 0 ]; then
	/sbin/service clamav-milter stop &>/dev/null || :
	/sbin/chkconfig --del clamav-milter
fi

%postun milter
/sbin/service clamav-milter condrestart &>/dev/null || :

%pre db
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || : 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FAQ INSTALL NEWS README TODO test/
%doc docs/*.pdf etc/freshclam.conf
%doc %{_mandir}/man1/sigtool.1*
%doc %{_mandir}/man1/clamscan.1*
%doc %{_mandir}/man1/freshclam.1*
%doc %{_mandir}/man5/freshclam.conf.5*
%config(noreplace) %{_sysconfdir}/freshclam.conf
%{_bindir}/clamscan
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_libdir}/libclamav.so.*

%files -n clamd
%defattr(-, root, root, 0755)
%doc contrib/clamdwatch/ etc/clamd.conf
%doc %{_mandir}/man1/clamdscan.1*
%doc %{_mandir}/man5/clamd.conf.5*
%doc %{_mandir}/man8/clamd.8*
%config(noreplace) %{_sysconfdir}/clamd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/clamav
%config %{_initrddir}/clamd
%{_sbindir}/clamd
%{_bindir}/clamdscan

%defattr(0644, clamav, clamav, 0755)
%{_localstatedir}/run/clamav/
%dir %{_localstatedir}/clamav/
%exclude %{_localstatedir}/clamav/*
%dir %{_localstatedir}/log/clamav/
%ghost %{_localstatedir}/log/clamav/clamd.log

%if %{!?_without_milter:1}0
%files milter
%defattr(-, root, root, 0755)
%doc clamav-milter/INSTALL
%doc %{_mandir}/man8/clamav-milter.8*
%config(noreplace) %{_sysconfdir}/sysconfig/clamav-milter
%config %{_initrddir}/clamav-milter
%{_sbindir}/clamav-milter
%endif

%files db
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/cron.daily/freshclam
%config(noreplace) %{_sysconfdir}/logrotate.d/freshclam

%defattr(0644, clamav, clamav, 0755)
%config(noreplace) %verify(user group mode) %{_localstatedir}/clamav/
%dir %{_localstatedir}/log/clamav/
%ghost %{_localstatedir}/log/clamav/freshclam.log

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/clamav-config
%{_includedir}/clamav.h
%{_libdir}/libclamav.a
%exclude %{_libdir}/libclamav.la
%{_libdir}/libclamav.so
%{_libdir}/pkgconfig/libclamav.pc

%changelog
* Mon Jul 25 2005 Dag Wieers <dag@wieers.com> - 0.86.2-1
- Updated to release 0.86.2.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.86.1-1
- Updated to release 0.86.1.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.85.1-1
- Updated to release 0.85.1.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.84-1
- Updated to release 0.84.

* Mon Feb 14 2005 Dag Wieers <dag@wieers.com> - 0.83-1
- Updated to release 0.83.

* Thu Feb 10 2005 Dag Wieers <dag@wieers.com> - 0.82-2
- Fix for false positive on RIFF files. (Roger Jochem)

* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 0.82-1
- Updated to release 0.82.

* Thu Jan 27 2005 Dag Wieers <dag@wieers.com> - 0.81-1
- Improved logrotate scripts. (Filippo Grassilli)
- Updated to release 0.81.

* Wed Dec 01 2004 Dag Wieers <dag@wieers.com> - 0.80-2
- Added %dir /var/clamav/log. (Adam Bowns)
- Changed logrotate script to use clamd.log. (Stuart Schneider)
- Added curl dependency. (Petr Kristof)
- Synchronized some options from Petr. (Petr Kristof)
- Fixed another clamav.conf reference. (Michael Best)

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 0.80-1
- Updated package description. (Arvin Troels)
- Incorporated fixes from Jima. (Jima)
- Config clamav.conf renamed to clamd.conf.
- Removed obsolete patch.
- Added macros for building without milter.
- Updated to release 0.80.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.75.1-1
- Added obsoletes for fedora.us.
- Updated to release 0.75.1.

* Mon Jul 26 2004 Dag Wieers <dag@wieers.com> - 0.75-2
- Fixed a problem where $CODE was empty.

* Fri Jul 23 2004 Dag Wieers <dag@wieers.com> - 0.75-1
- Updated to release 0.75.

* Wed Jun 30 2004 Dag Wieers <dag@wieers.com> - 0.74-1
- Updated to release 0.74.

* Tue Jun 15 2004 Dag Wieers <dag@wieers.com> - 0.73-1
- Updated to release 0.73.

* Thu Jun 03 2004 Dag Wieers <dag@wieers.com> - 0.72-1
- Updated to release 0.72.

* Thu May 20 2004 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.70-2
- Fixed the installation check for conf files. (Richard Soderberg)
- Changed the init-order of the sysv scripts. (Will McCutcheon)
- Changes to the default configuration files.

* Sat Mar 17 2004 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.68-1
- Updated to release 0.68.

* Fri Mar 12 2004 Dag Wieers <dag@wieers.com> - 0.67.1-1
- Updated to release 0.67-1.
- Added clamdwatch and trashcan to clamd.

* Mon Mar 08 2004 Dag Wieers <dag@wieers.com> - 0.67-1
- Personalized SPEC file.

* Mon Aug 22 2003 Matthias Saou/Che
- Added "--without milter" build option. (Matthias Saou)
- Fixed freshclam cron (Matthias Saou)
- Built the new package. (Che)

* Tue Jun 24 2003 Che
- clamav-milter introduced.
- a few more smaller fixes.

* Sun Jun 22 2003 Che
- version upgrade

* Mon Jun 16 2003 Che
- rh9 build
- various fixes
- got rid of rpm-helper prereq

* Fri Mar 24 2003 Che
- some cleanups and fixes
- new patch added

* Fri Nov 22 2002 Che
- fixed a config patch issue

* Fri Nov 22 2002 Che
- version upgrade and some fixes

* Sat Nov 02 2002 Che
- version upgrade

* Wed Oct 24 2002 Che
- some important changes for lsb compliance

* Wed Oct 23 2002 Che
- initial rpm release
