# $Id$
# Authority: matthias

%define webroot /srv/www/lighttpd

Summary: Lightning fast webserver with light system requirements
Name: lighttpd
Version: 1.3.13
Release: 1
License: BSD
Group: System Environment/Daemons
URL: http://www.lighttpd.net/
Source0: http://www.lighttpd.net/download/lighttpd-%{version}.tar.gz
Source1: lighttpd.logrotate
Source2: php.d-lighttpd.ini
Source10: index.html
Source11: lighttpd.png
Source12: powered_by_fedora.png
Patch0: lighttpd-1.3.10-defaultconf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service
BuildRequires: openssl-devel, pcre-devel, bzip2-devel, zlib-devel
%{?_with_ldap:BuildRequires: openldap-devel}

%description
Secure, fast, compliant and very flexible web-server which has been optimized
for high-performance environments. It has a very low memory footprint compared
to other webservers and takes care of cpu-load. Its advanced feature-set
(FastCGI, CGI, Auth, Output-Compression, URL-Rewriting and many more) make
it the perfect webserver-software for every server that is suffering load
problems.

Available rpmbuild rebuild options :
--with : ldap


%package mod_mysql_vhost
Summary: Virtual host module for lighttpd that uses a MySQL database
Group: System Environment/Daemons
Requires: %{name} = %{version}
BuildRequires: mysql-devel

%description mod_mysql_vhost
Virtual host module for lighttpd that uses a MySQL database.


%package fastcgi
Summary: FastCGI module and spawning helper for lighttpd and PHP configuration
Group: System Environment/Daemons
Requires: %{name} = %{version}

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


%build
%configure \
    --libdir="%{_libdir}/lighttpd" \
    --with-openssl \
    --with-mysql \
    %{?_with_ldap:--with-ldap}
%{__make}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
    libdir="%{buildroot}%{_libdir}/lighttpd"

# Install included init script and sysconfig entry
%{__install} -Dp -m 0755 doc/rc.lighttpd.redhat \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/lighttpd
%{__install} -Dp -m 0644 doc/sysconfig.lighttpd \
    %{buildroot}%{_sysconfdir}/sysconfig/lighttpd

# Install (*patched above*) sample config file
%{__install} -Dp -m 0640 doc/lighttpd.conf \
    %{buildroot}%{_sysconfdir}/lighttpd/lighttpd.conf

# Install our own logrotate entry
%{__install} -Dp -m 0644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/logrotate.d/lighttpd

# Install our own php.d ini file
%{__install} -Dp -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/php.d/lighttpd.ini

# Install our own default web page and images
%{__mkdir_p} %{buildroot}%{webroot}
%{__install} -p -m0644 %{SOURCE10} %{SOURCE11} %{SOURCE12} \
    %{buildroot}%{webroot}/

# Install empty log directory to include
%{__mkdir_p} %{buildroot}%{_var}/log/lighttpd


%clean
%{__rm} -rf %{buildroot}


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


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%doc doc/*.txt doc/lighttpd.conf doc/lighttpd.user
%config(noreplace) %{_sysconfdir}/lighttpd/lighttpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/lighttpd
%config(noreplace) %{_sysconfdir}/sysconfig/lighttpd
%{_sysconfdir}/rc.d/init.d/lighttpd
%{_sbindir}/lighttpd
%{_libdir}/lighttpd/
%exclude %{_libdir}/lighttpd/*.la
%exclude %{_libdir}/lighttpd/mod_fastcgi.so
%exclude %{_libdir}/lighttpd/mod_mysql_vhost.so
%{_mandir}/man1/lighttpd.1*
%attr(0750, lighttpd, lighttpd) %{_var}/log/lighttpd/
%{webroot}/

%files mod_mysql_vhost
%defattr(-, root, root, 0755)
%doc doc/mysqlvhost.txt
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_mysql_vhost.so

%files fastcgi
%defattr(-, root, root, 0755)
%doc doc/fastcgi*.txt
%config(noreplace) %{_sysconfdir}/php.d/lighttpd.ini
%{_bindir}/spawn-fcgi
%dir %{_libdir}/lighttpd/
%{_libdir}/lighttpd/mod_fastcgi.so
%{_mandir}/man1/spawn-fcgi.1*


%changelog
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

