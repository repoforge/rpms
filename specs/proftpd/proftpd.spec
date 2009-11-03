# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_acl 1}
%{?el2:%define _without_acl 1}
%{?el2:%define _without_postgresql 1}

Summary: Flexible, stable and highly-configurable FTP server
Name: proftpd
Version: 1.3.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.proftpd.org/

Source0: ftp://ftp.proftpd.org/distrib/source/proftpd-%{version}.tar.bz2
Source1: proftpd.conf
Source2: proftpd.init
Source3: proftpd-xinetd
Source4: proftpd.logrotate
Source5: welcome.msg
Source6: proftpd.pam
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel, ncurses-devel, pkgconfig
BuildRequires: openssl-devel, krb5-devel
BuildRequires: openldap-devel, mysql-devel, zlib-devel
%{!?_without_acl:BuildRequires: libacl-devel}
%{!?_without_postgresql:BuildRequires: postgresql-devel}
Requires: pam >= 0.59
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service
Provides: ftpserver

%description
ProFTPD is an enhanced FTP server with a focus toward simplicity, security,
and ease of configuration. It features a very Apache-like configuration
syntax, and a highly customizable server infrastructure, including support for
multiple 'virtual' FTP servers, anonymous FTP, and permission-based directory
visibility.

This package defaults to the standalone behaviour of ProFTPD, but all the
needed scripts to have it run by xinetd instead are included.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package ldap
Summary: Module to add LDAP support to the ProFTPD FTP server
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description ldap
Module to add LDAP support to the ProFTPD FTP server.

%package mysql
Summary: Module to add MySQL support to the ProFTPD FTP server
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description mysql
Module to add MySQL support to the ProFTPD FTP server.

%package postgresql
Summary: Module to add PostgreSQL support to the ProFTPD FTP server
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description postgresql
Module to add PostgreSQL support to the ProFTPD FTP server.

%prep
%setup

# Disable stripping in order to get useful debuginfo packages
%{__perl} -pi -e 's|"-s"|""|g' configure

%build
if pkg-config openssl; then
    export CFLAGS="%{optflags} $(pkg-config --cflags openssl)"
    export LDFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"
fi
%configure \
    --libexecdir="%{_libexecdir}/proftpd" \
    --localstatedir="%{_var}/run" \
    --enable-ctrls \
    --enable-dso \
%{!?_without_acl:--enable-facl} \
    --enable-ipv6 \
    --enable-openssl \
    --with-includes="%{_includedir}/mysql" \
    --with-libraries="%{_libdir}/mysql" \
    --with-modules="mod_readme:mod_auth_pam:mod_tls" \
    --with-shared="mod_ldap:mod_sql:mod_sql_mysql:%{!?_without_postgresql:mod_sql_postgres:}mod_quotatab:mod_quotatab_file:mod_quotatab_ldap:mod_quotatab_sql"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    rundir="%{_var}/run/proftpd" \
    INSTALL_USER=`id -un` \
    INSTALL_GROUP=`id -gn`
%{__install} -D -p -m 0640 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/proftpd.conf
%{__install} -D -p -m 0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/proftpd
%{__install} -D -p -m 0640 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/xinetd.d/xproftpd
%{__install} -D -p -m 0644 %{SOURCE4} \
    %{buildroot}%{_sysconfdir}/logrotate.d/proftpd
%{__install} -D -p -m 0644 %{SOURCE5} %{buildroot}/var/ftp/welcome.msg
%{__install} -D -p -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/proftpd
%{__mkdir_p} %{buildroot}/var/ftp/uploads
%{__mkdir_p} %{buildroot}/var/ftp/pub
%{__mkdir_p} %{buildroot}/var/log/proftpd
touch %{buildroot}%{_sysconfdir}/ftpusers

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add proftpd
    IFS=":"; cat /etc/passwd | \
    while { read username nu nu gid nu nu nu nu; }; do \
        if [ $gid -lt 100 -a "$username" != "ftp" ]; then
            echo $username >> %{_sysconfdir}/ftpusers
        fi
    done
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service proftpd stop &>/dev/null || :
    /sbin/chkconfig --del proftpd
    /sbin/service xinetd reload &>/dev/null || :
    if [ -d %{_var}/run/proftpd ]; then
        rm -rf %{_var}/run/proftpd/*
    fi
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service proftpd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS ChangeLog NEWS README* doc/* sample-configurations/
%dir %{_localstatedir}/run/proftpd/
%config(noreplace) %{_sysconfdir}/proftpd.conf
%config(noreplace) %{_sysconfdir}/xinetd.d/xproftpd
%config %{_sysconfdir}/ftpusers
%config(noreplace) %{_sysconfdir}/pam.d/proftpd
%config(noreplace) %{_sysconfdir}/logrotate.d/proftpd
%{_sysconfdir}/rc.d/init.d/proftpd
%{_mandir}/man?/*
%{_bindir}/*
%dir %{_libexecdir}/proftpd/
%{_libexecdir}/proftpd/mod_quotatab.so
%{_libexecdir}/proftpd/mod_quotatab_file.so
%{_libexecdir}/proftpd/mod_sql.so
%{_sbindir}/*
%dir /var/ftp/
%dir /var/ftp/pub/
%config(noreplace) /var/ftp/welcome.msg

%defattr(0331, ftp, ftp, 0331)
%dir /var/ftp/uploads/

%defattr(0750, root, root, 0750)
%dir /var/log/proftpd/
%exclude %{_libexecdir}/proftpd/*.a
%exclude %{_libexecdir}/proftpd/*.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/proftpd/
%{_libdir}/pkgconfig/proftpd.pc

%files ldap
%defattr(-, root, root, 0755)
%dir %{_libexecdir}/proftpd/
%{_libexecdir}/proftpd/mod_ldap.so
%{_libexecdir}/proftpd/mod_quotatab_ldap.so

%files mysql
%defattr(-, root, root, 0755)
%dir %{_libexecdir}/proftpd/
%{_libexecdir}/proftpd/mod_sql_mysql.so
%{_libexecdir}/proftpd/mod_quotatab_sql.so

%if %{!?_without_postgresql:1}0
%files postgresql
%defattr(-, root, root, 0755)
%dir %{_libexecdir}/proftpd/
%{_libexecdir}/proftpd/mod_sql_postgres.so
%{_libexecdir}/proftpd/mod_quotatab_sql.so
%endif

%changelog
* Thu Mar 12 2009 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Thu Jul  5 2007 Peter Bieringer <pb@bieringer.de> - 1.3.0a-4
- Migrate CVE-2007-2165 patches from Mandrake.

* Tue Feb  6 2007 Matthias Saou <http://freshrpms.net/> 1.3.0a-3
- Patch to fix local user buffer overflow in controls request handling, rhbz
  bug #219938, proftpd bug #2867.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 1.3.0a-2
- Rebuild against new PostgreSQL.

* Mon Nov 27 2006 Matthias Saou <http://freshrpms.net/> 1.3.0a-1
- Update to 1.3.0a, which actually fixes CVE-2006-5815... yes, #214820!).

* Thu Nov 16 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-10
- Fix cmdbufsize patch for missing CommandBufferSize case (#214820 once more).

* Thu Nov 16 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-9
- Include mod_tls patch (#214820 too).

* Mon Nov 13 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-8
- Include cmdbufsize patch (#214820).

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-7
- FC6 rebuild.

* Mon Aug 21 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-6
- Add mod_quotatab, _file, _ldap and _sql (#134291).

* Mon Jul  3 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-5
- Disable sendfile by default since it breaks displaying the download speed in
  ftptop and ftpwho (#196913).

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-4
- Include ctrls restart patch, see #195884 (patch from proftpd.org #2792).

* Wed May 10 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-3
- Add commented section about DSO loading to the default proftpd.conf.
- Update TLS cert paths in the default proftpd.conf to /etc/pki/tls.

* Fri Apr 28 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-2
- Mark pam.d and logrotate.d config files as noreplace.
- Include patch to remove -rpath to DESTDIR/usr/sbin/ in the proftpd binary
  when DSO is enabled (#190122).

* Fri Apr 21 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Update to 1.3.0 final.
- Remove no longer needed PostgreSQL and OpenSSL detection workarounds.
- Remove explicit conflicts on wu-ftpd, anonftp and vsftpd to let people
  install more than one ftp daemon (what for? hmm...) (#189023).
- Enable LDAP, MySQL and PostgreSQL as DSOs by default, and stuff them in
  new sub-packages. This won't introduce any regression since they weren't
  enabled by default.
- Remove useless explicit requirements.
- Rearrange scriplets requirements.
- Enable ctrls (controls via ftpdctl) and facl (POSIX ACLs).
- Using --disable-static makes the build fail, so exclude .a files in %%files.
- Silence harmless IPv6 failure message at startup when IPv6 isn't available.

* Tue Mar  7 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-0.2.rc4
- Update to 1.3.0rc4 (bugfix release).

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-0.2.rc3
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.3.0-0.1.rc3
- Update to 1.3.0rc3, which builds with the latest openssl.

* Thu Nov 17 2005 Matthias Saou <http://freshrpms.net/> 1.2.10-7
- Rebuild against new openssl library... not.

* Wed Jul 13 2005 Matthias Saou <http://freshrpms.net/> 1.2.10-6
- The provided pam.d file no longer works, use our own based on the one from
  the vsftpd package (#163026).
- Rename the pam.d file we use from 'ftp' to 'proftpd'.
- Update deprecated AuthPAMAuthoritative in the config file (see README.PAM).

* Tue May 10 2005 Matthias Saou <http://freshrpms.net/> 1.2.10-4
- Disable stripping in order to get useful debuginfo packages.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.2.10-3
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.2.10-2
- Bump release to provide Extras upgrade path.

* Wed Sep 22 2004 Matthias Saou <http://freshrpms.net/> 1.2.10-1
- Updated to release 1.2.10.

* Tue Jun 22 2004 Matthias Saou <http://freshrpms.net/> 1.2.9-8
- Added ncurses-devel build requires to fix the ftptop utility.

* Fri Feb 26 2004 Magnus-swe <Magnus-swe@telia.com> 1.2.9-7
- Fixed the scoreboard and pidfile issues.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 1.2.9-6
- Pass /var/run/proftpd as localstatedir to configure to fix pid and
  scoreboard file problems.

* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-4
- Fixed the MySQL include path, thanks to Jim Richardson.
- Renamed the postgres conditional build to postgresql.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-3
- Renamed the xinetd service to xproftpd to avoid conflict.
- Only HUP the standalone proftpd through logrotate if it's running.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-2
- Rebuild for Fedora Core 1.
- Modified the init script to make it i18n aware.

* Fri Oct 31 2003 Matthias Saou <http://freshrpms.net/> 1.2.9-1
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

