# $Id$
# Authority: rudolf
# Upstream: <clamav-devel$lists,sf,net>

Summary: Anti-virus software
Name: clamav
Version: 0.75.1
Release: 1
License: GPL
Group: Applications/System
URL: http://www.clamav.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://dl.sf.net/clamav/clamav-%{version}.tar.gz
Source1: clamav.init
Source2: clamav-milter.init
Patch0: clamav-0.67-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel, zlib-devel, gmp-devel
BuildRequires: sendmail-devel >= 8.12
Requires: clamav-db = %{version}-%{release}
Obsoletes: libclamav <= %{version}-%{release}
Obsoletes: clamav-lib <= %{version}-%{release}
Provides: libclamav

%description 
Clam Antivirus is a powerful anti-virus scanner for Unix. It
supports AMaViS, compressed files, uses the virus database from
OpenAntivirus.org, and includes a program for auto-updating.

%package -n clamd
Summary: The Clam AntiVirus Daemon
Group: System Environment/Daemons
Requires: clamav = %{version}-%{release}
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
Obsoletes: clamav-update <= %{version}-%{release}
Obsoletes: clamav-data <= %{version}-%{release}

%description db
The actual virus database for %{name}

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: clamav = %{version}-%{release}
Obsoletes: libclamav-static-devel <= %{version}-%{release}
Obsoletes: libclamav-devel <= %{version}-%{release}
Provides: libclamav-static-devel, libclamav-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0

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
		s|^#(ReadTimeout) .+$|$1 300|;
		s|^#(User) .+$|$1 clamav|;
		s|^#(AllowSupplementaryGroups)|$1|;
		s|^#(ScanMail)|$1|;
		s|^#(ArchiveBlockEncrypted)|$1|;
	' etc/clamav.conf

%{__perl} -pi.orig -e '
		s|^#(DatabaseDirectory) .+$|$1 %{_localstatedir}/clamav|;
		s|^#(UpdateLogFile) .+$|$1 %{_localstatedir}/log/clamav/freshclam.log|;
		s|^#(DatabaseOwner) .+$|$1 clamav|;
		s|^(Checks) .+$|$1 24|;
		s|^#(NotifyClamd) .+$|$1 %{_sysconfdir}/clamav.conf|;
	' etc/freshclam.conf

%{__cat} <<EOF >clamav.logrotate
%{_localstatedir}/log/clamav/clamav.log {
	create 644 clamav clamav
	monthly
	compress
}
EOF

%{__cat} <<EOF >freshclam.logrotate
%{_localstatedir}/log/clamav/freshclam.log {
	create 644 clamav clamav
	monthly
	compress
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
    --daemon-notify="%{_sysconfdir}/clamav.conf"
EOF

%{__cat} <<EOF >clamav-milter.sysconfig
### Simple config file for clamav-milter, you should
### read the documentation and tweak it as you wish.

CLAMAV_FLAGS="
	--config-file=%{_sysconfdir}/clamav.conf
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
	--enable-milter \
	--enable-id-check \
	--disable-clamav \
	--with-user="clamav" \
	--with-group="clamav" \
	--with-dbdir="%{_localstatedir}/clamav"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/clamd
%{__install} -D -m0755 %{SOURCE2} %{buildroot}%{_initrddir}/clamav-milter
%{__install} -D -m0644 clamav-milter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/clamav-milter
%{__install} -D -m0755 freshclam.cron %{buildroot}%{_sysconfdir}/cron.daily/freshclam
%{__install} -D -m0644 freshclam.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/freshclam
%{__install} -D -m0644 clamav.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/clamav

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/clamav/
touch %{buildroot}/var/log/clamav/freshclam.log
touch %{buildroot}/var/log/clamav/clamav.log

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
%doc docs/DMS/Debian_Mail_server.html docs/clamdoc.*
%doc docs/html/ docs/clamd_supervised/
%doc docs/French/ docs/Japanese/ docs/Polish/ docs/Portugese/
%doc docs/Spanish/ docs/Turkish/ etc/freshclam.conf
%doc %{_mandir}/man1/sigtool.1*
%doc %{_mandir}/man1/clamscan.1*
%doc %{_mandir}/man1/freshclam.1*
%doc %{_mandir}/man5/freshclam.conf.5*
%config(noreplace) %{_sysconfdir}/freshclam.conf
%{_bindir}/clamscan
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_libdir}/*.so.*

%files -n clamd
%defattr(-, root, root, 0755)
%doc contrib/clamdwatch/ etc/clamav.conf
%doc %{_mandir}/man1/clamdscan.1*
%doc %{_mandir}/man5/clamav.conf.5*
%doc %{_mandir}/man8/clamd.8*
%config(noreplace) %{_sysconfdir}/clamav.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/clamav
%config %{_initrddir}/clamd
%{_sbindir}/clamd
%{_bindir}/clamdscan

%defattr(0644, clamav, clamav, 0755)
%{_localstatedir}/run/clamav/
%{_localstatedir}/clamav/
%{_localstatedir}/log/clamav/clamav.log

%files milter
%defattr(-, root, root, 0755)
%doc clamav-milter/INSTALL
%doc %{_mandir}/man8/clamav-milter.8*
%config(noreplace) %{_sysconfdir}/sysconfig/clamav-milter
%config %{_initrddir}/clamav-milter
%{_sbindir}/clamav-milter

%files db
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/cron.daily/freshclam
%config(noreplace) %{_sysconfdir}/logrotate.d/freshclam

%defattr(0644, clamav, clamav, 0755)
%config(noreplace) %{_localstatedir}/clamav/
%{_localstatedir}/log/clamav/freshclam.log

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/clamav-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libclamav.pc

%changelog
* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.75.1-1
- Added obsoletes for fedora.us.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 0.75.1-1
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
