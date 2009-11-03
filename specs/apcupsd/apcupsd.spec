# $Id$
# Authority: dag
# Upstream: Kern Sibbald <kern$sibbald,com>
# Upstream: <apcupsd-users$lists,sourceforge,net>

%define _sbindir /sbin

Summary: APC UPS power control daemon
Name: apcupsd
Version: 3.14.3
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.apcupsd.com/

Source: http://dl.sf.net/apcupsd/apcupsd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glibc-devel, gd-devel, net-snmp-devel
Requires: perl

%description
Apcupsd can be used for controlling most APC UPSes. During a power failure,
apcupsd will inform the users about the power failure and that a shutdown
may occur. If power is not restored, a system shutdown will follow when the
battery is exausted, a timeout (seconds) expires, or the battery runtime
expires based on internal APC calculations determined by power consumption
rates. If the power is restored before one of the above shutdown conditions
is met, apcupsd will inform users about this fact.

Some features depend on what UPS model you have (simple or smart).

%prep
%setup

### Add a default apcupsd.conf for Apache.
%{__cat} <<EOF >apcupsd.httpd
ScriptAlias /apcupsd/ %{_localstatedir}/www/apcupsd/
<Directory %{_localstatedir}/www/apcupsd/>
        DirectoryIndex upsstats.cgi
        Options ExecCGI
        order deny,allow
        deny from all
        allow from 127.0.0.1
</Directory>
EOF

%{__cat} <<EOF >apcupsd.logrotate
%{_localstatedir}/log/apcupsd.events {
        missingok
        copytruncate
        notifempty
}
EOF

%build
%configure \
	--sysconfdir="%{_sysconfdir}/apcupsd" \
	--with-cgi-bin="%{_localstatedir}/www/apcupsd" \
	--enable-apcsmart \
	--enable-cgi \
	--enable-dumb \
	--enable-master-slave \
	--enable-net \
	--enable-pthreads \
	--enable-snmp \
	--enable-usb
%{__make} %{?_smp_mflags}
%{__make} -C examples hid-ups

%install
%{__rm} -rf %{buildroot}

### FIXME: 'make install' doesn't create sysv-dir and bails out.
%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 examples/hid-ups %{buildroot}%{_sysconfdir}/apcupsd/hid-ups
%{__install} -Dp -m0755 examples/make-hiddev %{buildroot}%{_sysconfdir}/apcupsd/make-hiddev
%{__install} -Dp -m0644 apcupsd.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/apcupsd.conf
%{__install} -Dp -m0644 apcupsd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/apcupsd

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add apcupsd

if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
        if ! grep -q "Include .*/apcupsd.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
                echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/apcupsd.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#               /sbin/service httpd restart
        fi
fi

%preun
if [ $1 -eq 0 ]; then
        /sbin/service apcuspd stop &>/dev/null || :
        /sbin/chkconfig --del apcupsd
fi

%postun
/sbin/service apcupsd condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING doc/* examples/ INSTALL
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/apcupsd/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/apcupsd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/apcupsd
%config %{_initrddir}/*
%{_sbindir}/*
%{_localstatedir}/www/apcupsd/
%exclude %{_initrddir}/halt*
%{_datadir}/hal/fdi/policy/20thirdparty/80-apcupsd-ups-policy.fdi

%changelog
* Sun Mar  2 2008 Dries Verachtert <dries@ulyssis.org> - 3.14.3-1
- Updated to release 3.14.3.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.10.18-1.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 3.10.18-1
- Updated to new release 3.10.18.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 3.10.13-2
- Added --enable-snmp configure option. (Bobby Kuo)

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 3.10.13-1
- Updated to new release 3.10.13.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 3.10.12-1
- Added apcupsd.logrotate. (Derek Werthmuller)
- Updated to new release 3.10.12.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 3.10.11-1
- Added apcupsd.conf. (Andrew Newman)
- Fixed unsuccessful 'make install'.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 3.10.11-0
- Initial package. (using DAR)
