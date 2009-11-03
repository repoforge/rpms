# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}
%{?el5:%define _without_lua 1}
%{?el4:%define _without_lua 1}
%{?el3:%define _without_lua 1}
%{?rh9:%define _without_lua 1}

%{?rh7:%define _without_lua 1}
%{?rh7:%define _without_ssl 1}

%{?el2:%define _without_lua 1}
%{?el2:%define _without_ssl 1}

%define webroot /srv/www/lighttpd

Summary: Lightning fast webserver with light system requirements
Name: lighttpd
Version: 1.4.22
Release: 2%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.lighttpd.net/

Source: http://www.lighttpd.net/download/lighttpd-%{version}.tar.bz2
Patch0: lighttpd-1.4.17-defaultconf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pcre-devel, bzip2-devel, zlib-devel, readline-devel
BuildRequires: /usr/bin/awk
%{?_with_gamin:BuildRequires: gamin-devel}
%{!?_without_gdbm:BuildRequires: gdbm-devel}
%{!?_without_lua:BuildRequires: lua-devel >= 5.1}
%{!?_without_ldap:BuildRequires: openldap-devel}
%{!?_without_ssl:BuildRequires: openssl-devel}
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service

%description
Secure, fast, compliant and very flexible web-server which has been optimized
for high-performance environments. It has a very low memory footprint compared
to other webservers and takes care of cpu-load. Its advanced feature-set
(FastCGI, CGI, Auth, Output-Compression, URL-Rewriting and many more) make
it the perfect webserver-software for every server that is suffering load
problems.

Available rpmbuild rebuild options :
--with : gamin webdavprops webdavlocks memcache
--without : ldap gdbm lua (cml) ssl

%package mod_mysql_vhost
Summary: Virtual host module for lighttpd that uses a MySQL database
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}
BuildRequires: mysql-devel

%description mod_mysql_vhost
Virtual host module for lighttpd that uses a MySQL database.

%package fastcgi
Summary: FastCGI module and spawning helper for lighttpd and PHP configuration
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description fastcgi
This package contains the spawn-fcgi helper for lighttpd's automatic spawning
of local FastCGI programs. Included is also a PHP .ini file to change a few
defaults needed for correct FastCGI behavior.
Note that for FastCGI to work with PHP, you will most likely need to find a
tweaked PHP package (--enable-fastcgi and --enable-discard-path added) or
recompile PHP yourself.

%prep
%setup
%patch0 -p1 -b .defaultconf

%{__cat} <<EOF >lighttpd.logrotate
%{_localstatedir}/log/lighttpd/*log {
    missingok
    notifempty
    sharedscripts
    postrotate
        /sbin/service lighttpd reload > /dev/null 2>/dev/null || true
    endscript
}
EOF

%{__cat} <<EOF >php.d-lighttpd.ini
; Required so that PHP_SELF gets set correctly when using PHP through
; FastCGI with lighttpd (see main php.ini for more about this option)
cgi.fix_pathinfo = 1
EOF

%build
%configure \
    --libdir="%{_libdir}/lighttpd" \
    --program-prefix="%{?_program_prefix}" \
    %{?_with_gamin:--with-fam} \
    %{!?_without_gdbm:--with-gdbm} \
    %{!?_without_ldap:--with-ldap} \
    %{?!_without_lua:--with-lua} \
    %{?_with_memcache:--with-memcache} \
    --with-mysql \
    %{?_without_ssl:--without-openssl} \
    %{!?_without_ssl:--with-openssl} \
    %{?_with_webdavlocks:--with-webdav-locks} \
    %{?_with_webdavprops:--with-webdav-props}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Install included init script and sysconfig entry
%{__install} -Dp -m0755 doc/rc.lighttpd.redhat %{buildroot}%{_sysconfdir}/rc.d/init.d/lighttpd
%{__install} -Dp -m0644 doc/sysconfig.lighttpd %{buildroot}%{_sysconfdir}/sysconfig/lighttpd

### Install (*patched above*) sample config file
%{__install} -Dp -m0640 doc/lighttpd.conf %{buildroot}%{_sysconfdir}/lighttpd/lighttpd.conf

### Install our own logrotate entry
%{__install} -Dp -m0644 lighttpd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/lighttpd

### Install our own php.d ini file
%{__install} -Dp -m0644 php.d-lighttpd.ini %{buildroot}%{_sysconfdir}/php.d/lighttpd.ini

### Install empty log directory to include
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/lighttpd

### Install empty run directory to include (for the example fastcgi socket)
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/lighttpd

### Create an empty document root
%{__install} -d -m0755 %{buildroot}%{webroot}


%pre
/usr/sbin/useradd -s /sbin/nologin -M -r -d %{webroot} \
    -c "lighttpd web server" lighttpd &>/dev/null || :

%post
/sbin/chkconfig --add lighttpd

%preun
if [ $1 -eq 0 ]; then
    /sbin/service lighttpd stop &>/dev/null || :
    /sbin/chkconfig --del lighttpd
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service lighttpd condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.txt doc/lighttpd.conf doc/lighttpd.user
%doc %{_mandir}/man1/lighttpd.1*
%dir %{_sysconfdir}/lighttpd/
%config(noreplace) %{_sysconfdir}/lighttpd/lighttpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/lighttpd
%config(noreplace) %{_sysconfdir}/sysconfig/lighttpd
%{_sysconfdir}/rc.d/init.d/lighttpd
%{_sbindir}/lighttpd
%{_sbindir}/lighttpd-angel
%{_libdir}/lighttpd/
%{webroot}/
%exclude %{_libdir}/lighttpd/*.la
%exclude %{_libdir}/lighttpd/mod_fastcgi.so
%exclude %{_libdir}/lighttpd/mod_mysql_vhost.so

%defattr(-, lighttpd, lighttpd, 0750)
%{_localstatedir}/log/lighttpd/

%files mod_mysql_vhost
%defattr(-, root, root, 0755)
%doc doc/mysqlvhost.txt
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_mysql_vhost.so

%files fastcgi
%defattr(-, root, root, 0755)
%doc doc/fastcgi*.txt
%doc %{_mandir}/man1/spawn-fcgi.1*
%config(noreplace) %{_sysconfdir}/php.d/lighttpd.ini
%{_bindir}/spawn-fcgi
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_fastcgi.so

%changelog
 * Sun Mar 15 2009 Stanis Trendelenburg <stanis.trendelenburg@gmail.com> - 1.4.22-2
- Fix the logrotate script.

* Fri Mar 13 2009 Dries Verachtert <dries@ulyssis.org> - 1.4.22-1
- Updated to release 1.4.22.

* Wed Oct 15 2008 Tomas Brandysky <shamot@kilian.no-ip.org> - 1.4.20
- Updated to release 1.4.20.

* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 1.4.19-1
- Updated to release 1.4.19.

* Mon Oct 01 2007 Dag Wieers <dag@wieers.com> - 1.4.18-1
- Updated to release 1.4.18.

* Mon Aug  1 2005 Matthias Saou <http://freshrpms.net/> 1.3.16-1
- Update to 1.3.16.

* Mon Jul 18 2005 Matthias Saou <http://freshrpms.net/> 1.3.15-1
- Update to 1.3.15.

* Mon Jun 20 2005 Matthias Saou <http://freshrpms.net/> 1.3.14-1
- Update to 1.3.14.

* Mon Apr  4 2005 Matthias Saou <http://freshrpms.net/> 1.3.13-2
- Change signal sent from the logrotate script from USR1 to HUP, as that's the
  correct one.
- Add /etc/lighttpd directory (Michael Schwendt).

* Sun Mar  6 2005 Matthias Saou <http://freshrpms.net/> 1.3.13-1
- Update to 1.3.13.

* Wed Mar  2 2005 Matthias Saou <http://freshrpms.net/> 1.3.12-1
- Update to 1.3.12.
- Remove obsolete empty_cgi_handler patch.

* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 1.3.11-2
- Add missing defattr to sub-packages (#150018).

* Mon Feb 21 2005 Matthias Saou <http://freshrpms.net/> 1.3.11-0
- Update to 1.3.11.
- Remove cleanconf and init.d patches (merged upstream).
- Add empty_cgi_handler patch.

* Fri Feb 18 2005 Matthias Saou <http://freshrpms.net/> 1.3.10-0
- Split off -fastcgi sub-package.
- Include php.d entry to set sane FastCGI defaults.

* Wed Feb 16 2005 Matthias Saou <http://freshrpms.net/> 1.3.10-0
- Spec file cleanup for freshrpms.net/Extras.
- Compile OpenSSL support unconditionally.
- Put modules in a subdirectory of libdir.
- Don't include all of libdir's content to avoid debuginfo content.
- Add optional LDAP support.
- Add patch to change the default configuration.
- Add dedicated lighttpd user/group creation.
- Add logrotate entry.
- Include a nice little default page for the default setup.
- Split off mod_mysql_vhost sub-package, get dep only there.
- Use webroot in /srv by default.
- Exclude .la files, I doubt anyone will need them.

* Thu Sep 30 2004 <jan@kneschke.de> 1.3.1
- upgraded to 1.3.1

* Tue Jun 29 2004 <jan@kneschke.de> 1.2.3
- rpmlint'ed the package
- added URL
- added (noreplace) to start-script
- change group to Networking/Daemon (like apache)

* Sun Feb 23 2003 <jan@kneschke.de>
- initial version

