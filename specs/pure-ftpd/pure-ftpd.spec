# $Id$
# Authority: dag


%{?el4:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_ldap 1}
%{?el2:%define _without_pgsql 1}
%{?el2:%define _without_selinux 1}
%{?el2:%define _without_tls 1}

Summary: Lightweight, fast and secure FTP server
Name: pure-ftpd
Version: 1.0.36
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.pureftpd.org/

Source0: http://download.pureftpd.org/pub/pure-ftpd/releases/pure-ftpd-%{version}.tar.bz2
Source1: pure-ftpd.init
Source6: pure-ftpd.README.SELinux
Source7: pure-ftpd.pureftpd.te
Patch0: pure-ftpd-1.0.27-config.patch
Patch1: pure-ftpd-paminclude.patch
Provides: ftpserver
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libcap-devel
BuildRequires: pam-devel
BuildRequires: perl
BuildRequires: python
%{!?_without_ldap:BuildRequires: openldap-devel}
%{!?_without_mysql:BuildRequires: mysql-devel}
%{!?_without_pgsql:BuildRequires: postgresql-devel}
%{!?_without_selinux:BuildRequires: checkpolicy, selinux-policy-devel}
%{!?_without_tls:BuildRequires: openssl-devel}
Requires: chkconfig
Requires: initscripts
Requires: logrotate
Requires: usermode

%description
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.
Rebuild switches:
--without extauth  disable external authentication
--without ldap     disable ldap support
--without mysql    disable mysql support
--without pgsql    disable postgresql support
--without tls      disable SSL/TLS

%package selinux
Summary: SELinux support for Pure-FTPD
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}
Requires: policycoreutils
Requires: initscripts

%description selinux
This package adds SELinux enforcement to Pure-FTPD. Install it if you want
Pure-FTPd to be protected in the same way other FTP servers are in Fedora
(e.g. VSFTPd and ProFTPd)

%prep
%setup
%patch0 -p0 -b .config
%patch1 -p0 -b .paminclude

%{__cat} <<EOF >pure-ftpd.logrotate
/var/log/pureftpd.log {
    weekly
    notifempty
    missingok
}
EOF

%{__cat} <<EOF >pure-ftpd.xinetd
# default: off
# description: pure-ftpd server, xinetd version. \
# Don't run the standalone version if you run \
# this and remember do set "Daemonize" to "no" \
# in /etc/pure-ftpd/pure-ftpd.conf
service ftp
{
	disable	= yes
	socket_type		= stream
	wait			= no
	user			= root
	server			= /usr/sbin/pure-config.pl
	server_args		= /etc/pure-ftpd/pure-ftpd.conf
	log_on_success		+= DURATION USERID
	log_on_failure		+= USERID
	nice			= 10
}
EOF

%{__cat} <<EOF >pure-ftpwho.pam
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       required     pam_localuser.so
account    required     pam_permit.so
EOF

%{__cat} <<EOF >pure-ftpwho.consoleapps
USER=root
PROGRAM=%{_sbindir}/pure-ftpwho
GUI=no
EOF

%{__install} -Dp -m0644 %{SOURCE6} README.SELinux
%{__install} -Dp -m0644 %{SOURCE7} selinux/pureftpd.te
%{__cat} <<EOF >selinux/pureftpd.fc
%{_sbindir}/pure-ftpd    system_u:object_r:ftpd_exec_t:s0
%{_localstatedir}/log/pureftpd.log    system_u:object_r:xferlog_t:s0
EOF
touch selinux/pureftpd.if

%build
%configure \
    --sysconfdir="%{_sysconfdir}/pure-ftpd" \
    --without-bonjour \
    --with-altlog \
    --with-capabilities \
    --with-cookie \
    --with-diraliases \
%{!?_without_extauth:--with-extauth} \
    --with-ftpwho \
    --with-largefile \
%{!?_without_ldap:--with-ldap} \
%{!?_without_mysql:--with-mysql} \
    --with-pam \
    --with-paranoidmsg \
    --with-peruserlimits \
%{!?_without_pgsql:--with-pgsql} \
    --with-privsep \
    --with-puredb \
    --with-quotas \
    --with-ratios \
    --with-rfc2640 \
    --with-sendfile \
    --with-throttling \
%{!?_without_tls:--with-tls --with-certfile="%{_sysconfdir}/pki/pure-ftpd/pure-ftpd.pem"} \
    --with-uploadscript \
    --with-virtualchroot \
    --with-virtualhosts \
    --with-welcomemsg
%{__make} %{?_smp_mflags}

%{!?_without_selinux:%{__make} -C selinux -f %{_datadir}/selinux/devel/Makefile}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 configuration-file/pure-config.pl %{buildroot}%{_sbindir}/pure-config.pl
%{__install} -Dp -m0644 configuration-file/pure-ftpd.conf %{buildroot}%{_sysconfdir}/pure-ftpd/pure-ftpd.conf
%{__install} -Dp -m0755 configuration-file/pure-config.py %{buildroot}%{_sbindir}/pure-config.py
%{__install} -Dp -m0644 pureftpd-ldap.conf %{buildroot}%{_sysconfdir}/pure-ftpd/pureftpd-ldap.conf
%{__install} -Dp -m0644 pureftpd-mysql.conf %{buildroot}%{_sysconfdir}/pure-ftpd/pureftpd-mysql.conf
%{__install} -Dp -m0644 pureftpd-pgsql.conf %{buildroot}%{_sysconfdir}/pure-ftpd/pureftpd-pgsql.conf

%{__install} -Dp -m0644 man/pure-ftpd.8 %{buildroot}%{_mandir}/man8/pure-ftpd.8
%{__install} -Dp -m0644 man/pure-ftpwho.8 %{buildroot}%{_mandir}/man8/pure-ftpwho.8
%{__install} -Dp -m0644 man/pure-mrtginfo.8 %{buildroot}%{_mandir}/man8/pure-mrtginfo.8
%{__install} -Dp -m0644 man/pure-uploadscript.8 %{buildroot}%{_mandir}/man8/pure-uploadscript.8
%{__install} -Dp -m0644 man/pure-pw.8 %{buildroot}%{_mandir}/man8/pure-pw.8
%{__install} -Dp -m0644 man/pure-pwconvert.8 %{buildroot}%{_mandir}/man8/pure-pwconvert.8
%{__install} -Dp -m0644 man/pure-statsdecode.8 %{buildroot}%{_mandir}/man8/pure-statsdecode.8
%{__install} -Dp -m0644 man/pure-quotacheck.8 %{buildroot}%{_mandir}/man8/pure-quotacheck.8
%{__install} -Dp -m0644 man/pure-authd.8 %{buildroot}%{_mandir}/man8/pure-authd.8

%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/pure-ftpd
%{__install} -Dp -m0644 pam/pure-ftpd %{buildroot}%{_sysconfdir}/pam.d/pure-ftpd
%{__install} -Dp -m0644 pure-ftpd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/pure-ftpd
%{__install} -Dp -m0644 pure-ftpd.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/pure-ftpd
%{__install} -Dp -m0644 pure-ftpwho.pam %{buildroot}%{_sysconfdir}/pam.d/pure-ftpwho
%{__install} -Dp -m0644 pure-ftpwho.consoleapps %{buildroot}%{_sysconfdir}/security/console.apps/pure-ftpwho
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/pure-ftpwho

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/ftp/
%{!?_without_tls:%{__install} -d -m0700 %{buildroot}%{_sysconfdir}/pki/pure-ftpd/}
%{!?_without_selinux:%{__install} -Dp -m0644 selinux/pureftpd.pp %{buildroot}%{_datadir}/selinux/packages/pure-ftpd/pureftpd.pp}

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -le 1 ]; then
    /sbin/chkconfig --add pure-ftpd
fi
if [ -d %{_sysconfdir}/pki/pure-ftpd/ -a ! -f %{_sysconfdir}/pki/pure-ftpd/pure-ftpd.pem ]; then
    %{_sysconfdir}/pki/tls/certs/make-dummy-cert %{_sysconfdir}/pki/pure-ftpd/pure-ftpd.pem
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service pure-ftpd stop &>/dev/null || :
    /sbin/chkconfig --del pure-ftpd
fi

%postun
if [ $1 -gt 0 ]; then
    /sbin/service pure-ftpd condrestart &>/dev/null || :
fi

%post selinux
if [ $1 -le 1 ]; then
    semodule -i %{_datadir}/selinux/packages/pure-ftpd/pureftpd.pp 2>/dev/null || :
    fixfiles -R pure-ftpd restore
    /sbin/service pure-ftpd condrestart &>/dev/null || :
fi

%preun selinux
if [ $1 -eq 0 ]; then
    semodule -r pureftpd 2>/dev/null || :
    fixfiles -R pure-ftpd restore
    /sbin/service pure-ftpd condrestart &>/dev/null
fi

%postun selinux
if [ $1 -gt 0 ]; then
    semodule -i %{_datadir}/selinux/packages/pure-ftpd/pureftpd.pp 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CONTACT FAQ HISTORY NEWS README* THANKS
%doc contrib/pure-vpopauth.pl pureftpd.schema contrib/pure-stat.pl
%doc %{_mandir}/man8/pure-*.8*
%config %{_initrddir}/pure-ftpd
%config(noreplace) %{_sysconfdir}/logrotate.d/pure-ftpd
%config(noreplace) %{_sysconfdir}/pam.d/pure-ftpd
%config(noreplace) %{_sysconfdir}/pure-ftpd/
%config(noreplace) %{_sysconfdir}/xinetd.d/pure-ftpd
%config %{_sysconfdir}/pam.d/pure-ftpwho
%config %{_sysconfdir}/security/console.apps/pure-ftpwho
%{!?_without_tls:%{_sysconfdir}/pki/pure-ftpd/}
%{_bindir}/pure-*
%dir %{_localstatedir}/ftp/
%{_sbindir}/pure-*

%if %{!?_without_selinux:1}0
%files selinux
%defattr(-, root, root, 0755)
%doc README.SELinux
%{_datadir}/selinux/packages/pure-ftpd/pureftpd.pp
%endif

%changelog
* Thu Aug 30 2012 Denis Fateyev <denis@fateyev.com> - 1.0.36-1
- Updated to release 1.0.36

* Mon Oct 06 2008 Dag Wieers <dag@wieers.com> - 1.0.21-1
- Updated to release 1.0.21. (rebased on Fedora)

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 1.0.16-0
- Updated to release 1.0.16.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.0.14-1
- Added sysv scripts with chkconfig.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 1.0.14-0
- Initial package. (using DAR)
