# $Id$
# Authority: matthias
# Upstream: <proftp-devel@lists.sf.net>

# Distcc: 0

Summary: flexible, stable and highly-configurable FTP Server
Name: proftpd
Version: 1.2.9
Release: 6%{?_with_ldap:_ldap}%{?_with_mysql:_mysql}%{?_with_postgresql:_pgsql}
License: GPL
Group: System Environment/Daemons
URL: http://www.proftpd.org/

Source: ftp://ftp.proftpd.org/distrib/source/proftpd-%{version}.tar.bz2
Source1: proftpd.conf
Source2: proftpd.init
Source3: proftpd-xinetd
Source4: proftpd.logrotate
Source5: welcome.msg
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel, perl, pkgconfig
%{!?_without_tls:BuildRequires: openssl-devel, krb5-devel}
%{?_with_ldap:BuildRequires: openldap-devel}
%{?_with_mysql:BuildRequires: mysql-devel, zlib-devel}
%{?_with_postgresql:BuildRequires: postgresql-devel}
Provides: ftpserver
Conflicts: wu-ftpd, anonftp, vsftpd

Requires: pam >= 0.59, /sbin/service, /sbin/chkconfig, /etc/init.d
%{!?_without_tls:Requires: openssl}
%{?_with_ldap:Requires: openldap}
%{?_with_mysql:Requires: mysql}
%{?_with_postgresql:Requires: postgresql-libs}

%description
ProFTPD is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration. It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package defaults to the standalone behaviour of ProFTPD, but all the
needed scripts to have it run by xinetd instead are included.

Available rpmbuild rebuild options :
--without : tls
--with : ldap mysql postgresql

%prep
%setup

%build
# Workaround for the PostgreSQL include file
%{__perl} -pi.orig -e 's|pgsql/libpq-fe.h|libpq-fe.h|g' contrib/mod_sql_postgres.c

# TLS includes
OPENSSL_INC=""
if OPENSSL_CFLAGS=`pkg-config --cflags openssl`; then
    for i in ${OPENSSL_CFLAGS}; do
        INCPATH=`echo $i | perl -pi -e 's|-I([a-z/]*)|$1|g'`
        test ! -z ${INCPATH} && OPENSSL_INC="${OPENSSL_INC}:${INCPATH}"
    done
fi

%configure \
    --localstatedir=/var/run/%{name} \
    --with-includes=%{_includedir}%{!?_without_tls:${OPENSSL_INC}}%{?_with_mysql::%{_includedir}/mysql} \
    %{?_with_mysql:--with-libraries=%{_libdir}/mysql} \
    %{?_with_postgresql:--with-libraries=%{_libdir}} \
    --with-modules=mod_readme:mod_auth_pam%{?_with_ldap::mod_ldap}%{?_with_mysql::mod_sql:mod_sql_mysql}%{?_with_postgresql::mod_sql:mod_sql_postgres}%{!?_without_tls::mod_tls}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall rundir=%{buildroot}%{_localstatedir}/run/proftpd \
    INSTALL_USER=`id -un` \
    INSTALL_GROUP=`id -gn`
%{__install} -D -m0644 contrib/dist/rpm/ftp.pamd %{buildroot}%{_sysconfdir}/pam.d/ftp
%{__install} -D -m0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/proftpd.conf
%{__install} -D -m0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/rc.d/init.d/proftpd
%{__install} -D -m0640 %{SOURCE3} %{buildroot}%{_sysconfdir}/xinetd.d/xproftpd
%{__install} -D -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/proftpd
%{__install} -D -m0644 %{SOURCE5} %{buildroot}/var/ftp/welcome.msg
mkdir -p %{buildroot}/var/ftp/uploads
mkdir -p %{buildroot}/var/ftp/pub
mkdir -p %{buildroot}/var/log/proftpd
touch %{buildroot}%{_sysconfdir}/ftpusers

%post
if [ $1 = 1 ]; then
    /sbin/chkconfig --add proftpd
    IFS=":"; cat /etc/passwd | \
    while { read username nu nu gid nu nu nu nu; }; do \
        if [ $gid -lt 100 -a "$username" != "ftp" ]; then
            echo $username >> %{_sysconfdir}/ftpusers
        fi
    done
fi

%preun
if [ $1 = 0 ]; then
    /sbin/service proftpd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del proftpd
    /sbin/service xinetd reload >/dev/null 2>&1 || :
    if [ -d /var/run/proftpd ]; then
        rm -rf /var/run/proftpd/*
    fi
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service proftpd condrestart >/dev/null 2>&1
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS ChangeLog NEWS README* doc/* sample-configurations/
%dir %{_localstatedir}/run/proftpd
%config(noreplace) %{_sysconfdir}/proftpd.conf
%config(noreplace) %{_sysconfdir}/xinetd.d/xproftpd
%config %{_sysconfdir}/ftpusers
%config %{_sysconfdir}/pam.d/ftp
%config %{_sysconfdir}/logrotate.d/proftpd
%{_sysconfdir}/rc.d/init.d/proftpd
%{_mandir}/*/*
%{_bindir}/*
%{_sbindir}/*
%dir /var/ftp/
%dir /var/ftp/pub/
%config(noreplace) /var/ftp/welcome.msg

%defattr(0750, root, root, 0755)
%dir /var/log/proftpd/

%defattr(0331, ftp, ftp, 0755)
%dir /var/ftp/uploads/

%changelog
* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 1.2.9-6.fr
- Pass /var/run/proftpd as localstatedir to configure to fix pid and
  scoreboard file problems.

* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-4.fr
- Fixed the MySQL include path, thanks to Jim Richardson.
- Renamed the postgres conditional build to postgresql.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-3.fr
- Renamed the xinetd service to xproftpd to avoid conflict.
- Only HUP the standalone proftpd through logrotate if it's running.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-2.fr
- Rebuild for Fedora Core 1.
- Modified the init script to make it i18n aware.

* Fri Oct 31 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-1.fr
- Update to 1.2.9.

* Wed Sep 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.8p to fix secutiry vulnerability.
- Fix the TLS build option at last, enable it by default.

* Mon Aug  4 2003 Matthias Saou <http://freshrpms.net/>
- Minor fixes in included README files.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.8.
- Remove the renamed linuxprivs module.
- Added TLS module build option.

* Fri Dec 13 2002 Matthias Saou <http://freshrpms.net/>
- Fix change for ScoreboardFile in the default conf, thanks to Sven Hoexter.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.7.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Tue Sep 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.6.
- Fixed typo in the config for "AllowForeignAddress" thanks to Michel Kraus.
- Removed obsolete user install patch.
- Added "modular" ldap, mysql and postgresql support.

* Mon Jun 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.5.
- Changed the welcome.msg to config so that it doesn't get replaced.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Tue Oct 23 2001 Matthias Saou <http://freshrpms.net/>
- Changed the default config file : Where the pid file is stored, addedd
  an upload authorization in anon server, and separate anon logfiles.
- Updated welcome.msg to something nicer.

* Fri Oct 19 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.4, since 1.2.3 had a nasty umask bug.

* Sat Aug 18 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.2 final.
- Changed the default config file a lot.

* Wed Apr 25 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.2rc2.

* Mon Apr  1 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.2rc1.

* Tue Mar 20 2001 Matthias Saou <http://freshrpms.net/>
- Added a DenyFilter to prevent a recently discovered DOS attack.
  This is only useful for fresh installs since the config file is not
  overwritten.

* Fri Mar  2 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.1.
- New init script (added condrestart).

* Tue Feb 27 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.0 final.

* Tue Feb  6 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.0rc3 (at last a new version!)
- Modified the spec file to support transparent upgrades

* Wed Nov  8 2000 Matthias Saou <http://freshrpms.net/>
- Upgraded to the latest CVS to fix the "no PORT command" bug
- Fixed the ftpuser creation script
- Modified the default config file to easily change to an anonymous
  server

* Sun Oct 15 2000 Matthias Saou <http://freshrpms.net/>
  [proftpd-1.2.0rc2-2]
- Updated the spec file and build process for RedHat 7.0
- Added xinetd support
- Added logrotate.d support

* Fri Jul 28 2000 Matthias Saou <http://freshrpms.net/>
  [proftpd-1.2.0rc2-1]
- Upgraded to 1.2.0rc2

- Upgraded to 1.2.0rc1
* Sat Jul 22 2000 Matthias Saou <http://freshrpms.net/>
  [proftpd-1.2.0rc1-1]
- Upgraded to 1.2.0rc1
- Re-did the whole spec file (it's hopefully cleaner now)
- Made a patch to be able to build the RPM as an other user than root
- Added default pam support (but without /etc/shells check)
- Rewrote the rc.d script (mostly exit levels and ftpshut stuff)
- Modified the default configuration file to not display a version number
- Changed the package to standalone in one single RPM easily changeable
  to inetd (for not-so-newbie users)
- Fixed the ftpusers generating shell script (missing "nu"s for me...)
- Removed mod_ratio (usually used with databases modules anyway)
- Removed the prefix (relocations a rarely used on non-X packages)
- Gzipped the man pages

* Thu Oct 03 1999 O.Elliyasa <osman@Cable.EU.org>
- Multi package creation.
  Created core, standalone, inetd (&doc) package creations.
  Added startup script for init.d
  Need to make the "standalone & inetd" packages being created as "noarch"
- Added URL.
- Added prefix to make the package relocatable.

* Wed Sep 08 1999 O.Elliyasa <osman@Cable.EU.org>
- Corrected inetd.conf line addition/change logic.

* Sat Jul 24 1999 MacGyver <macgyver@tos.net>
- Initial import of spec.

