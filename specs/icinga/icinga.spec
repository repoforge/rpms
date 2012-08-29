# $Id$
# Authority: cmr
# Upstream: The icinga devel team <icinga-devel at lists.sourceforge.net>
#
# Needs libdbi
#
# ExclusiveDist: el5 el6

%define revision 1

%define logmsg logger -t %{name}/rpm

%define logdir %{_localstatedir}/log/%{name}
%define spooldir %{_localstatedir}/spool/%{name}
%define plugindir %{_libdir}/nagios/plugins

%define apacheconfdir  %{_sysconfdir}/httpd/conf.d
%define apacheuser apache
%define apachegroup apache

Summary: Open Source host, service and network monitoring program
Name: icinga
Version: 1.7.2
Release: %{revision}%{?dist}
License: GPLv2
Group: Applications/System
URL: http://www.icinga.org/

Source0: http://dl.sf.net/icinga/icinga-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: gd-devel > 1.8
BuildRequires: httpd
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libdbi-devel
BuildRequires: perl(ExtUtils::Embed)
### Requires: nagios-plugins

%description
Icinga is an application, system and network monitoring application.
It can escalate problems by email, pager or any other medium. It is
also useful for incident or SLA reporting.

Icinga is written in C and is designed as a background process,
intermittently running checks on various services that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Icinga.

Icinga is a fork of the nagios project.

%package gui
Summary: Web content for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Requires: httpd
Requires: %{name}-doc

%description gui
This package contains the webgui (html,css,cgi etc.) for %{name}

%package idoutils-libdbi-mysql
Summary: database broker module for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Requires: libdbi-dbd-mysql
Conflicts: %{name}-idoutils-libdbi-pgsql

%description idoutils-libdbi-mysql
This package contains the idoutils broker module for %{name} which provides
database storage via libdbi and mysql.

%package idoutils-libdbi-pgsql
Summary: database broker module for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Requires: libdbi-dbd-pgsql
Conflicts: %{name}-idoutils-libdbi-mysql

%description idoutils-libdbi-pgsql
This package contains the idoutils broker module for %{name} which provides
database storage via libdbi and pgsql.


%package doc
Summary: documentation %{name}
Group: Documentation

%description doc
Documentation for %{name}


%prep
%setup -qn %{name}-%{version}

%build
%configure \
    --prefix=%{_datadir}/%{name} \
    --exec-prefix=%{_localstatedir}/lib/%{name} \
    --datadir="%{_datadir}/%{name}" \
    --datarootdir="%{_datadir}/%{name}" \
    --libexecdir="%{plugindir}" \
    --localstatedir="%{_localstatedir}/%{name}" \
    --libdir="%{_libdir}/%{name}" \
    --sbindir="%{_libdir}/%{name}/cgi" \
    --sysconfdir="%{_sysconfdir}/%{name}" \
    --with-cgiurl="/%{name}/cgi-bin" \
    --with-command-user="icinga" \
    --with-command-group="icingacmd" \
    --with-gd-lib="%{_libdir}" \
    --with-gd-inc="%{_includedir}" \
    --with-htmurl="/icinga" \
    --with-init-dir="%{_initrddir}" \
    --with-lockfile="%{_localstatedir}/run/%{name}.pid" \
    --with-mail="/bin/mail" \
    --with-icinga-user="icinga" \
    --with-icinga-group="icinga" \
    --with-template-objects \
    --with-template-extinfo \
    --enable-event-broker \
    --enable-embedded-perl \
    --enable-idoutils \
    --with-httpd-conf=%{apacheconfdir} \
    --with-init-dir=%{_initrddir} \
    --with-log-dir=%{logdir} \
    --enable-cgi-log \
    --with-cgi-log-dir=%{logdir}/gui \
    --with-plugin-dir="%{plugindir}" \
    --with-eventhandler-dir="%{_libdir}/%{name}/eventhandlers" \
    --with-p1-file-dir="%{_libdir}/%{name}" \
    --with-checkresult-dir="%{spooldir}/checkresults" \
    --with-ext-cmd-file-dir="%{spooldir}/cmd" \
    --with-http-auth-file="%{_sysconfdir}/%{name}/passwd" \
    --with-icinga-chkfile="%{spooldir}/icinga.chk" \
    --with-ido2db-lockfile="%{_localstatedir}/run/ido2db.pid" \
    --with-ido-sockfile="%{spooldir}/ido.sock" \
    --with-idomod-tmpfile="%{spooldir}/idomod.tmp" \
    --with-state-dir="%{spooldir}"

%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{apacheconfdir}
%{__make} install-unstripped \
    install-init \
    install-commandmode \
    install-config \
    install-webconf \
    install-idoutils \
    install-eventhandlers \
    DESTDIR="%{buildroot}" \
    INSTALL_OPTS="" \
    INSTALL_OPTS_WEB="" \
    COMMAND_OPTS="" \
    INIT_OPTS=""

### strip binary
%{__strip} %{buildroot}%{_bindir}/{icinga,icingastats,log2ido,ido2db}
%{__strip} %{buildroot}%{_libdir}/icinga/cgi/*.cgi

### move idoutils sample configs to final name
mv %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg-sample %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg
mv %{buildroot}%{_sysconfdir}/icinga/idomod.cfg-sample %{buildroot}%{_sysconfdir}/icinga/idomod.cfg
mv %{buildroot}%{_sysconfdir}/icinga/modules/idoutils.cfg-sample %{buildroot}%{_sysconfdir}/icinga/modules/idoutils.cfg

### remove icinga-api
%{__rm} -rf %{buildroot}%{_datadir}/icinga/icinga-api

# install logrotate rule
install -D -m 0644 icinga.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# install sample htpasswd file
install -D -m 0644 icinga.htpasswd %{buildroot}%{_sysconfdir}/%{name}/passwd

%pre
# Add icinga user
%{_sbindir}/groupadd icinga 2> /dev/null || :
%{_sbindir}/groupadd icingacmd 2> /dev/null || :
%{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/%{name} -G icingacmd -g icinga icinga 2> /dev/null || :


%post
/sbin/chkconfig --add icinga
# restart httpd for auth change
/sbin/service httpd condrestart > /dev/null 2>&1 || :

# if this is an upgrade, and we found an old retention.dat, copy it to new location before starting icinga
if [ $1 -eq 2 ]
then
# stop icinga
/sbin/service icinga stop &>/dev/null || :
# check for retention.dat
if [ -f /var/icinga/retention.dat ]
then
    cp /var/icinga/retention.dat %{spooldir}/retention.dat
    rm /var/icinga/retention.dat
fi
# same for objects.precache
if [ -f /var/icinga/objects.precache ]
then
    cp /var/icinga/objects.precache %{spooldir}/objects.precache
    rm /var/icinga/objects.precache
fi

# we must then check all changed config locations (and we enforce that change to icinga.cfg only once)
# cgi.cfg luckily knows where icinga.cfg is and does not need an update
# retention.dat, objects.cache, objects.precache, status.dat, cmdfile, pidfile, checkresults
%{__perl} -pi -e '
        s|/var/icinga/retention.dat|%{spooldir}/retention.dat|;
        s|/var/icinga/objects.precache|%{spooldir}/objects.precache|;
        s|/var/icinga/objects.cache|%{spooldir}/objects.cache|;
        s|/var/icinga/status.dat|%{spooldir}/status.dat|;
        s|/var/icinga/rw/icinga.cmd|%{spooldir}/cmd/icinga.cmd|;
        s|/var/icinga/icinga.pid|/var/run/icinga.pid|;
	s|/var/icinga/checkresults|%{spooldir}/checkresults|;
   ' /etc/icinga/icinga.cfg

# start icinga
/sbin/service icinga start &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service icinga stop &>/dev/null || :
    /sbin/chkconfig --del icinga
fi

%postun
/sbin/service httpd condrestart > /dev/null 2>&1 || :

%pre gui
# Add apacheuser in the icingacmd group
  %{_sbindir}/usermod -a -G icingacmd %{apacheuser}


%post idoutils-libdbi-mysql
/sbin/chkconfig --add ido2db

# delete old bindir/idomod.o if it exists
if [ -f %{_bindir}/idomod.o ]
then
    rm -f %{_bindir}/idomod.o
fi

%logmsg "idoutils-libdbi-mysql installed. don't forget to install/upgrade db schema, check README.RHEL.idoutils"

%preun idoutils-libdbi-mysql
if [ $1 -eq 0 ]; then
    /sbin/service ido2db stop &>/dev/null || :
    /sbin/chkconfig --del ido2db
fi

%post idoutils-libdbi-pgsql
/sbin/chkconfig --add ido2db
# delete old bindir/idomod.o if it exists
if [ -f %{_bindir}/idomod.o ]
then
    rm -f %{_bindir}/idomod.o
fi
### change ido2db.cfg to match pgsql config
# check if this is an upgrade
if [ $1 -eq 2 ]
then
	%{__cp} %{_sysconfdir}/icinga/ido2db.cfg %{_sysconfdir}/icinga/ido2db.cfg.pgsql
	%{__perl} -pi -e '
		s|db_servertype=mysql|db_servertype=pgsql|;
		s|db_port=3306|db_port=5432|;
		' %{_sysconfdir}/icinga/ido2db.cfg.pgsql
	%logmsg "Warning: upgrade, pgsql config written to ido2db.cfg.pgsql"
fi
# install
if [ $1 -eq 1 ]
then
	%{__perl} -pi -e '
		s|db_servertype=mysql|db_servertype=pgsql|;
		s|db_port=3306|db_port=5432|;
		' %{_sysconfdir}/icinga/ido2db.cfg
fi

%logmsg "idoutils-libdbi-pgsql installed. don't forget to install/upgrade db schema, check README.RHEL.idoutils"


%preun idoutils-libdbi-pgsql
if [ $1 -eq 0 ]; then
    /sbin/service ido2db stop &>/dev/null || :
    /sbin/chkconfig --del ido2db
fi


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING README.RHEL
%attr(755,-,-) %{_initrddir}/icinga
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/modules
%config(noreplace) %{_sysconfdir}/%{name}/icinga.cfg
%dir %{_sysconfdir}/%{name}/objects
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/objects/commands.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/contacts.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/notifications.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/localhost.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/printer.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/switch.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/templates.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/timeperiods.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/windows.cfg
%config(noreplace) %attr(640,icinga,icinga) %{_sysconfdir}/%{name}/resource.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(755,-,-) %{_bindir}/icinga
%attr(755,-,-) %{_bindir}/icingastats
%attr(755,-,-) %{_libdir}/icinga/p1.pl
%{_libdir}/%{name}/eventhandlers
%defattr(-,icinga,icinga,-)
%{logdir}
%{logdir}/archives
%dir %{_localstatedir}/spool/%{name}
%dir %{_localstatedir}/spool/%{name}/checkresults
%attr(2755,icinga,icingacmd) %{_localstatedir}/spool/%{name}/cmd

%files doc
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING README.RHEL
%{_datadir}/%{name}/docs

%files gui
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING README.RHEL
%config(noreplace) %{apacheconfdir}/icinga.conf
%config(noreplace) %{_sysconfdir}/%{name}/cgi.cfg
%config(noreplace) %{_sysconfdir}/%{name}/cgiauth.cfg
%attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/passwd
%{_libdir}/%{name}/cgi/avail.cgi
%{_libdir}/%{name}/cgi/cmd.cgi
%{_libdir}/%{name}/cgi/config.cgi
%{_libdir}/%{name}/cgi/extinfo.cgi
%{_libdir}/%{name}/cgi/histogram.cgi
%{_libdir}/%{name}/cgi/history.cgi
%{_libdir}/%{name}/cgi/notifications.cgi
%{_libdir}/%{name}/cgi/outages.cgi
%{_libdir}/%{name}/cgi/showlog.cgi
%{_libdir}/%{name}/cgi/status.cgi
%{_libdir}/%{name}/cgi/statusmap.cgi
%{_libdir}/%{name}/cgi/statuswml.cgi
%{_libdir}/%{name}/cgi/statuswrl.cgi
%{_libdir}/%{name}/cgi/summary.cgi
%{_libdir}/%{name}/cgi/tac.cgi
%{_libdir}/%{name}/cgi/trends.cgi
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/contexthelp
%{_datadir}/%{name}/images
%{_datadir}/%{name}/index.html
%{_datadir}/%{name}/js
%{_datadir}/%{name}/main.html
%{_datadir}/%{name}/media
%{_datadir}/%{name}/menu.html
%{_datadir}/%{name}/robots.txt
%{_datadir}/%{name}/sidebar.html
%{_datadir}/%{name}/ssi
%{_datadir}/%{name}/stylesheets
%attr(2775,icinga,icingacmd) %dir %{logdir}/gui
%attr(664,icinga,icingacmd) %{logdir}/gui/index.htm
%attr(664,icinga,icingacmd) %{logdir}/gui/.htaccess


%files idoutils-libdbi-mysql
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING module/idoutils/db README.RHEL README.RHEL.idoutils
%attr(755,-,-) %{_initrddir}/ido2db
%attr(660,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ido2db.cfg
%config(noreplace) %{_sysconfdir}/%{name}/idomod.cfg
%config(noreplace) %{_sysconfdir}/%{name}/modules/idoutils.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/ido2db_check_proc.cfg
%{_bindir}/ido2db
%{_bindir}/log2ido
%{_libdir}/%{name}/idomod.so

%files idoutils-libdbi-pgsql
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING module/idoutils/db README.RHEL README.RHEL.idoutils
%attr(755,-,-) %{_initrddir}/ido2db
%attr(660,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ido2db.cfg
%config(noreplace) %{_sysconfdir}/%{name}/idomod.cfg
%config(noreplace) %{_sysconfdir}/%{name}/modules/idoutils.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/ido2db_check_proc.cfg
%{_bindir}/ido2db
%{_bindir}/log2ido
%{_libdir}/%{name}/idomod.so


%changelog
* Tue Aug 21 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.2-1
- bump version
- forgot to check on old icinga.cfg entries not matching - enforce that once
- change permissions on ido2db.cfg, not being world readable (Aaron Russo) #2987

* Mon Jun 18 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.1-1
- bump to 1.7.1

* Sun May 06 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.0-1
- drop idoutils, add idoutils-libdbi-mysql and idoutils-libdbi-pgsql
- add requires for libdbi drivers mysql and pgsql
- add conflicts vice versa to mysql and pgsql libdbi package
- sed ido2db.cfg for idoutils-libdbi-pgsql to match pgsql config on upgrade
- log info message for idoutils to create db
- use the _sbindir macro instead of hardcoded /usr/sbin
- move pid file to _localstatedir/run/icinga.pid
- use name macro instead of hardcoded "icinga" everywhere
- introduce plugindir macro for global usage
- install icinga.logrotate example
- move ext cmd file location to _localstatedir/spool/icinga/cmd/icinga.cmd
- set icinga user's home to _localstatedir/spool/icinga
- move checkresults to _localstatedir/spool/icinga/checkresults
- use --with-http-auth-file from #2533
- add default /etc/icinga/passwd with icingaadmin:icingaadmin default login
- use ido2db.lock, ido.sock, idomod.tmp, icinga.chk location change from configure params #1856
- use --with-state-dir=$spooldir for status.dat, objects.cache etc
- kick provides: nagios again, as this will cause dependency problems. addons must be fixed.
- copy old retention.dat and objects.precache if found #2585
- add most valuable changes to README.RHEL*
- delete old bindir/idomod.o if found

* Sat Feb 25 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-5
- add README.RHEL README.RHEL.idoutils to docs, thx Michael Gruener, Stefan Marx #2212
- use newly introduced --with-eventhandler-dir and make install-eventhandlers
- install sample eventhandlers to {_libdir}/icinga/eventhandlers
- use --enable-cgi-log from upstream instead of manual sed
- add {_sysconfdir}/icinga/conf.d because upstream will include that with cfg_dir

* Fri Feb 24 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-4
- rename idomod.o to idomod.so - see #2354
- use --libdir={_libdir}/icinga to install idomod.so instead of {_bindir} - see #2346
- list {_libdir}/icinga/cgi/ cgis one by one, removing build warnings
- remove macros in changelog warnings from rpmlint
- use custom revision macro, don't forget that on spec updates
- drop webuser/group, was used only by deprecated icinga-api (thx Michael Gruener) #2356
- change ownership of docs to root (thx Michael Gruener)
- add "README LICENSE Changelog UPGRADING" to all packages as docs (thx Michael Gruener) #2212
- change permissions of resource.cfg to icinga:icinga 640 (thx Michael Gruener)
- users who use cgi.cfg authorized_for_full_command_resolution must add apache user to group themselves (security risk)
- put module/idoutils/db into docs instead of manually copying to /etc/icinga/idoutils (thx Michael Gruener) #2357
- revamp the file permissions based on proposals by Michael Gruener <michael.gruener@topalis.com>

* Thu Feb 23 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-3
- use --with-plugin-dir instead of --libexexdir for nagios plugins dir introduced in #2344

* Wed Feb 22 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-2
- re-add provides nagios for compatibility reasons

* Fri Dec 02 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-1
- bump to 1.6.1

* Sun Nov 27 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.0-1
- set to 1.6.0 target
- add --with-web-user/group
- add objects/ido2db_check_proc.cfg
- drop api package as this is now deprecated and not shipped anymore with icinga package
- remove provides nagios, inaccurate
- enable cmd.cgi logging by default, {logdir}/gui used
- fix --libexecdir to point to possible location of nagios-plugins in resource.cfg:$USER1$

* Fri Sep 09 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.5.1-1
- bump to 1.5.1

* Wed Jun 29 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.5.0-1
- set to 1.5.0 target, remove provides nagios version, set idoutils.cfg-sample
- move all logging to one location https://bugzilla.redhat.com/show_bug.cgi?id=693608
- add log-dir, cgi-log-dir, phpapi-log-dir to configure, remove the manual creation
- remove manual logdir creation and movings, as no longer needed
- add objects/notifications.cfg for further examples
- fix file perms and locations of cfgs
- fix group for doc

* Wed May 11 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.4.0-2
- undo changes on icinga-cmd group, use icingacmd like before

* Thu Apr 28 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.4.0-1
- update for release 1.4.0
- remove perl subst for eventhandler submit_check_result, this is now done by configure
- remove top.html, doxygen
- set cgi log permissions to apache user
- honour modules/ in icinga cfg and modules/idoutils.cfg for neb definitions
- add /icinga/log for cmd.cgi logging, includes .htaccess

* Tue Mar 31 2011 Christoph Maser <cmaser@gmx.de> - 1.3.1-1
- update for release 1.3.1

* Tue Feb 15 2011 Christoph Maser <cmaser@gmx.de> - 1.3.0-2
- move cgis to libdir
- remove suse suppot (packages available at opensuse build system)
- add doxygen docs

* Wed Nov 03 2010 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.3.0-1
- prepared 1.3.0, added log2ido for idoutils install

* Mon Oct 25 2010 Christoph Maser <cmaser@gmx.de> - 1.2.1-1
- update for release 1.2.1
- add build dep for httpd
- set INSTALL_OPTS_WEB=""

* Thu Sep 30 2010 Christoph Maser <cmaser@gmx.de> - 1.2.0-1
- update for release 1.2.0

* Mon Sep 20 2010 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.0.3-4
- remove php depency for classic gui

* Wed Sep 01 2010 Christoph Maser <cmaser@gmx.de> - 1.0.3-3
- Put documentation in a separate package

* Tue Aug 31 2010 Christoph Maser <cmaser@gmx.de> - 1.0.3-2
- Set icinga-api logdir ownership to apache user 
- add php dependency for icinga-gui subpackage

* Wed Aug 18 2010 Christoph Maser <cmaser@gmx.de> - 1.0.3-1
- Update to 1.0.3-1

* Thu Jul 05 2010 Christoph Maser <cmaser@gmx.de> - 1.0.2-2
- Enable debuginfo

* Thu Jun 24 2010 Christoph Maser <cmaser@gmx.de> - 1.0.2-1
- Update to 1.0.2-1

* Wed Mar 03 2010 Christoph Maser <cmr@financial.com> - 1.0.1-1
- Update to 1.0.1-1

* Tue Dec 15 2009 Christoph Maser <cmr@financial.com> - 1.0-1
- Update to 1.0-1

* Mon Oct 26 2009 Christoph Maser <cmr@financial.com> - 1.0-0.RC1.2
- Split out icinga-api in sub package

* Mon Oct 26 2009 Christoph Maser <cmr@financial.com> - 1.0-0.RC1.1
- Update to 1.0-RC1
- Correct checkconfig --del in idoutils #preun

* Mon Oct 26 2009 Christoph Maser <cmr@financial.com> - 0.8.4-3
- Use icinga-cmd group and add apache user to that group instead
  of using apachegroup as icinga command group.

* Wed Oct 07 2009 Christoph Maser <cmr@financial.com> - 0.8.4-2
- make packages openSUSE compatible
- add #apachecondir, #apacheuser, #apachegroup depending on vendor
- configure add --with-httpd-conf=#{apacheconfdir} 
- configure add --with-init-dir=#{_initrddir}

* Wed Sep 16 2009 Christoph Maser <cmr@financial.com> - 0.8.4-1
- Update to version 0.8.4.

* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 0.8.3-3
- Apply patch from 
  https://git.icinga.org/index?p=icinga-core.git;a=commit;h=8b3505883856310472979b152b9960f81cdbaad7

* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 0.8.3-2
- Apply patch from 
  https://git.icinga.org/index?p=icinga-core.git;a=commit;h=068baf7bfc99a2a5a88b64d06df49d7395008b40

* Wed Sep 09 2009 Christoph Maser <cmr@financial.com> - 0.8.3-1
- Update to version 0.8.3.

* Thu Aug 27 2009 Christoph Maser <cmr@financial.com> - 0.8.2-3
- fix dir name ndoutils -> idoutils

* Thu Aug 27 2009 Christoph Maser <cmr@financial.com> - 0.8.2-2
- fix idututils post script
- copy database scripts from source to sysconfigdir

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.8.2-1
- Update to release 0.8.2.
- remove idoutils-init, init-script for ido2db is shipped now 

* Sun Jul 19 2009 Christoph Maser <cmr@financial.com> - 0.8.1-1
- initial package

