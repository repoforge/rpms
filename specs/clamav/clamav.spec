# $Id$
# Authority: newrpms
# Upstream: <clamav-devel@lists.sourceforge.net>

%define rversion 0.67-1
%define milter 1
%{?rhel3:%undefine milter}

Summary: Anti-virus utility for Unix.
Name: clamav
Version: 0.67.1
Release: 1
License: GPL
Group: Applications/System
URL: http://clamav.sf.net/

Source0: http://dl.sf.net/clamav/clamav-%{rversion}.tar.gz
Source1: http://dl.sf.net/clamav/clamav-%{rversion}.tar.gz.sig
Source2: clamav.init
Source3: clamav-milter.init
Patch0: clamav-0.67-config.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: bzip2-devel, zlib-devel
%{?milter:BuildRequires: sendmail-devel >= 8.12}
Requires: clamav-db = %{version}-%{release}
Obsoletes: libclamav = 0.54	
Provides: libclamav

%description 
Clam Antivirus is a powerful anti-virus scanner for Unix. It
supports AMaViS, compressed files, uses the virus database from
OpenAntivirus.org, and includes a program for auto-updating.

%package -n clamd
Summary: The Clam AntiVirus Daemon
Group: System Environment/Daemons
Requires: clamav = %{version}-%{release}

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

%description db
The actual virus database for %{name}

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: clamav = %{version}-%{release}
Obsoletes: libclamav-static-devel = 0.54 
Obsoletes: libclamav-devel = 0.54
Provides: libclamav-static-devel, libclamav-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{rversion}
%patch0

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

/usr/bin/freshclam \
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
	--max-children=2
	-obl local:%{_localstatedir}/clamav/clmilter.socket
"
EOF

%build
%configure  \
	--program-prefix="%{?_program_prefix}" \
%{?milter:--enable-milter} \
	--disable-clamav \
	--with-user="clamav" \
	--with-group="clamav" \
	--with-dbdir="%{_localstatedir}/clamav"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__make} install \
	DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/sysconfig/ \
			%{buildroot}%{_sysconfdir}/cron.daily/ \
			%{buildroot}%{_sysconfdir}/logrotate.d/ \
			%{buildroot}%{_localstatedir}/log/clamav/ \
			%{buildroot}%{_localstatedir}/run/clamav/

%{__install} -m0755 %{SOURCE2} %{buildroot}%{_initrddir}/clamd

%{?milter:%{__install} -m0755 %{SOURCE3} %{buildroot}%{_initrddir}/clamav-milter}
%{?milter:%{__install} -m0644 clamav-milter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/clamav-milter}

%{__install} -m0755 freshclam.cron %{buildroot}%{_sysconfdir}/cron.daily/freshclam
%{__install} -m0644 freshclam.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/freshclam
%{__install} -m0644 clamav.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/clamav
touch %{buildroot}/var/log/clamav/freshclam.log
touch %{buildroot}/var/log/clamav/clamav.log

### huh? a bug?
%{__install} -m0644 etc/clamav.conf %{buildroot}%{_sysconfdir}/clamav.conf

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
%{!?milter:	%{buildroot}%{_mandir}/man8/clamav-milter.8*}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%pre -n clamd
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || :

%post -n clamd
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add clamd
elif [ -f /var/lock/subsys/clamd ]; then 
	service clamd restart > /dev/null 2>/dev/null || :
fi

%preun -n clamd
if [ $1 -eq 0 ]; then
	service clamd stop > /dev/null 2>/dev/null || :
	/sbin/chkconfig --del clamd
fi

%post milter
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add clamav-milter
elif [ -f /var/lock/subsys/clamav-milter ]; then
	service clamav-milter restart &>/dev/null || :
fi
                                                                               
%preun milter
if [ $1 -eq 0 ]; then
	service clamav-milter stop &>/dev/null || :
	/sbin/chkconfig --del clamav-milter
fi

%pre db
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || : 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog FAQ INSTALL NEWS README TODO test/
%doc docs/DMS/Debian_Mail_server.html docs/clamdoc.*
%doc docs/html/ docs/clamd_supervised/
%doc docs/French/ docs/Japanese/ docs/Polish/ docs/Portugese/
%doc docs/Spanish/ docs/Turkish/
%doc %{_mandir}/man1/sigtool.1*
%doc %{_mandir}/man1/clamscan.1*
%doc %{_mandir}/man1/freshclam.1*
%config(noreplace) %{_sysconfdir}/freshclam.conf
%{_bindir}/clamscan
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_libdir}/*.so.*

%files -n clamd
%defattr(-, root, root, 0755)
%doc contrib/clamdwatch/ contrib/trashscan/
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

%if %{?milter:1}%{!?milter:0}
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
%config(noreplace) %{_localstatedir}/clamav/
%{_localstatedir}/log/clamav/freshclam.log

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
#%exclude %{_libdir}/*.la

%changelog
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
