# $Id$
# Authority: cmr
# Upstream: The icinga devel team <icinga-devel at lists.icinga.org>
#
# Needs libdbi
#
# ExclusiveDist: el5 el6

%define revision 0

%define logmsg logger -t %{name}/rpm

%define logdir %{_localstatedir}/log/%{name}
%define spooldir %{_localstatedir}/spool/%{name}
%define plugindir %{_libdir}/nagios/plugins

%if "%{_vendor}" == "suse"
%define apacheuser wwwrun
%define apachegroup www
%define apachename apache2
%define apacheconfdir  %{_sysconfdir}/%{apachename}/conf.d
%define extcmdfile %{_localstatedir}/icinga/rw/icinga.cmd
%define extcmdfiledir %{_localstatedir}/icinga/rw
%define readme README.SUSE
%define readmeido README.SUSE.idoutils
%endif
%if "%{_vendor}" == "redhat"
%define apachename httpd
%define apacheconfdir %{_sysconfdir}/%{apachename}/conf.d
%define apacheuser apache
%define apachegroup apache
%define extcmdfile %{_localstatedir}/spool/icinga/cmd/icinga.cmd
%define extcmdfiledir %{_localstatedir}/spool/icinga/cmd
%define readme README.RHEL
%define readmeido README.RHEL.idoutils
%endif

# Systemd support for Fedora >= 15
%if 0%{?fedora} >= 15
%define using_systemd 1
%else
%define using_sysvinit 1
%endif

# Check to see if we're allowed to use macroized systemd scriptlets, as
# introduced in Fedora 18.
%if 0%{?using_systemd}
%if 0%{?fedora} >= 18
%define systemd_macro_scriptlet 1
%else
%define systemd_macro_scriptlet 0
%endif  # Fedora >= 18
%endif  # using_systemd

Summary: Open Source host, service and network monitoring program
Name: icinga
Version: 1.11.0
Release: %{revision}%{?dist}
License: GPLv2
Group: Applications/System
URL: http://www.icinga.org/

Source0: https://github.com/Icinga/icinga-core/releases/download/v%{version}/icinga-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%if 0%{?using_systemd}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif

BuildRequires: gcc
BuildRequires: gd-devel > 1.8
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libdbi-devel
BuildRequires: perl(ExtUtils::Embed)
### Requires: nagios-plugins
BuildRequires: %{apachename}
%if "%{_vendor}" == "suse"
BuildRequires: libopenssl-devel
%endif



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
Summary: Classic UI for %{name}
Group: Applications/System
Requires: %{apachename}
Requires: %{name}-doc
Requires: %{name}-classicui-config

%description gui
This package contains the Classic UI for %{name}. Requires %{name}-doc
for the documentation module.

%package gui-config
Summary: Classic UI configuration for %{name}
Group: Applications/System
Requires: %{apachename}
Provides: %{name}-classicui-config
Conflicts: icinga2-classicui-config

%description gui-config
This packages contains the classic ui configuration for %{name}.


%package devel
Summary: Provides include files that Icinga-related applications may compile against
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides include files that Icinga-related applications
may compile against.

%package idoutils
Summary: transitional package, use idoutils-libdbi-* instead
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Requires: %{name}-idoutils-libdbi-mysql

%description idoutils
Transitional package. Idoutils has been splitted into
idoutils-libdbi-mysql and idoutils-libdbi-pgsql. Use one
of these. This package pulls in idoutils-libdbi-mysql.
This package can be safely uninstalled, it provides no
files and nothing depends on it.

%package idoutils-libdbi-mysql
Summary: database broker module for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
%if 0%{?suse_version} >= 1210
# opensuse
Requires: libdbi-drivers-dbd-mysql
%else
Requires: libdbi-dbd-mysql
%endif
Conflicts: %{name}-idoutils-libdbi-pgsql

%description idoutils-libdbi-mysql
This package contains the idoutils broker module for %{name} which provides
database storage via libdbi and mysql.

%package idoutils-libdbi-pgsql
Summary: database broker module for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
%if 0%{?suse_version} >= 1210
# opensuse
Requires: libdbi-drivers-dbd-pgsql
%else
Requires: libdbi-dbd-pgsql
%endif
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

cat << EOF > README.idoutils.transitional
Transitional package. Idoutils has been splitted into
idoutils-libdbi-mysql and idoutils-libdbi-pgsql. Use one
of these. This package pulls in idoutils-libdbi-mysql.
This package can be safely uninstalled, it provides no
files and nothing depends on it.
EOF

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
    --with-gd-lib="%{_libdir}" \
    --with-gd-inc="%{_includedir}" \
    --with-htmurl="/icinga" \
    --with-cgiurl="/%{name}/cgi-bin" \
    --with-mainurl="/%{name}/cgi-bin/status.cgi?host=all&type=detail&servicestatustypes=29" \
    --with-init-dir="%{_initrddir}" \
    --with-lockfile="%{_localstatedir}/run/%{name}.pid" \
    --with-mail="/bin/mail" \
    --with-icinga-user="icinga" \
    --with-icinga-group="icinga" \
    --enable-event-broker \
    --enable-embedded-perl \
    --enable-idoutils \
    --with-httpd-conf=%{apacheconfdir} \
    --with-log-dir=%{logdir} \
    --enable-cgi-log \
    --with-cgi-log-dir=%{logdir}/gui \
    --with-plugin-dir="%{plugindir}" \
    --with-eventhandler-dir="%{_libdir}/%{name}/eventhandlers" \
    --with-p1-file-dir="%{_libdir}/%{name}" \
    --with-checkresult-dir="%{spooldir}/checkresults" \
    --with-ext-cmd-file-dir="%{extcmdfiledir}" \
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

# Our make install invocation will differ depending on whether or not we're
# using systemd.
#   without:  make ... install-init ...
#   with:     make ... install-systemd ...
%if 0%{?using_systemd}
%define init_install systemd
%else
%define init_install init
%endif

%{__make} install-unstripped \
    install-%{init_install} \
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

# install headers for development package
install -d -m0755 "%{buildroot}%{_includedir}/%{name}/"
install -m0644 include/*.h "%{buildroot}%{_includedir}/%{name}"

# create perfdata dir by default
install -d -m0755 "%{buildroot}%{_localstatedir}/spool/%{name}/perfdata"

%pre
# Add icinga user
%{_sbindir}/groupadd -r icinga 2> /dev/null || :
%{_sbindir}/groupadd -r icingacmd 2> /dev/null || :
%{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/%{name} -G icingacmd -g icinga icinga 2> /dev/null || :


%post

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_post icinga.service
%else
# manual systemd scriptlet
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
# No systemd, just plain old sysvinit
/sbin/chkconfig --add icinga
%endif

# restart httpd for auth change
/sbin/service %{apachename} condrestart > /dev/null 2>&1 || :

# start icinga
/sbin/service icinga start &>/dev/null || :

%preun

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_preun icinga.service
%else
if [ $1 -eq 0 ]; then
    # manual systemd scriptlet
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable icinga.service > /dev/null 2>&1 || :
    /bin/systemctl stop icinga.service > /dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -eq 0 ]; then
    # No systemd, just plain old sysvinit
    /sbin/service icinga stop &>/dev/null || :
    /sbin/chkconfig --del icinga
fi
%endif

%postun
/sbin/service %{apachename} condrestart > /dev/null 2>&1 || :

%pre gui
# Add apacheuser in the icingacmd group
# If the group exists, add the apacheuser in the icingacmd group.
# It is not neccessary that icinga-cgi is installed on the same system as
# icinga 1.x and only on systems with icinga installed the icingacmd
# group exists.
getent group icingacmd > /dev/null

if [ $? -eq 0 ]; then
%if "%{_vendor}" == "suse"
  %{_sbindir}/usermod -G icingacmd %{apacheuser}
%else
  %{_sbindir}/usermod -a -G icingacmd %{apacheuser}
%endif
fi

%post idoutils-libdbi-mysql

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_post ido2db.service
%else
# manual systemd scriptlet
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
# No systemd, just plain old sysvinit
/sbin/chkconfig --add ido2db
%endif

%logmsg "idoutils-libdbi-mysql installed. don't forget to install/upgrade db schema, check %{readmeido}"

%preun idoutils-libdbi-mysql

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_preun ido2db.service
%else
if [ $1 -eq 0 ]; then
    # manual systemd scriptlet
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable ido2db.service > /dev/null 2>&1 || :
    /bin/systemctl stop ido2db.service > /dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -eq 0 ]; then
    # No systemd, just plain old sysvinit
    /sbin/service ido2db stop &>/dev/null || :
    /sbin/chkconfig --del ido2db
fi
%endif

%post idoutils-libdbi-pgsql

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_post ido2db.service
%else
# manual systemd scriptlet
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
# No systemd, just plain old sysvinit
/sbin/chkconfig --add ido2db
%endif

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

%logmsg "idoutils-libdbi-pgsql installed. don't forget to install/upgrade db schema, check %{readmeido}"


%preun idoutils-libdbi-pgsql

%if 0%{?using_systemd}
%if 0%{?systemd_macro_scriptlet}
%systemd_preun ido2db.service
%else
if [ $1 -eq 0 ]; then
    # manual systemd scriptlet
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable ido2db.service > /dev/null 2>&1 || :
    /bin/systemctl stop ido2db.service > /dev/null 2>&1 || :
fi
%endif
%else
if [ $1 -eq 0 ]; then
    # No systemd, just plain old sysvinit
    /sbin/service ido2db stop &>/dev/null || :
    /sbin/chkconfig --del ido2db
fi
%endif


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING %{readme}
%if 0%{?using_systemd}
%attr(755,-,-)  %{_unitdir}/icinga.service
%attr(644,-,-)  %{_sysconfdir}/sysconfig/icinga
%else
%attr(755,-,-) %{_initrddir}/icinga
%endif
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
%dir %{logdir}
%dir %{logdir}/archives
%dir %{_localstatedir}/spool/%{name}
%dir %{_localstatedir}/spool/%{name}/perfdata
%dir %{_localstatedir}/spool/%{name}/checkresults
%attr(2755,icinga,icingacmd) %{extcmdfiledir}

%files doc
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING %{readme}
%{_datadir}/%{name}/docs

%files gui
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING %{readme}
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
%{_libdir}/%{name}/cgi/summary.cgi
%{_libdir}/%{name}/cgi/tac.cgi
%{_libdir}/%{name}/cgi/trends.cgi
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/images
%{_datadir}/%{name}/index.html
%{_datadir}/%{name}/js
%{_datadir}/%{name}/main.html
%{_datadir}/%{name}/media
%{_datadir}/%{name}/menu.html
%{_datadir}/%{name}/robots.txt
%{_datadir}/%{name}/ssi
%{_datadir}/%{name}/stylesheets
%{_datadir}/%{name}/jquery-ui
%{_datadir}/%{name}/jquery-ui-addon
%attr(2775,icinga,icingacmd) %dir %{logdir}/gui
%attr(664,icinga,icingacmd) %{logdir}/gui/index.htm
%attr(664,icinga,icingacmd) %{logdir}/gui/.htaccess

%files gui-config
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING %{readme}
%config(noreplace) %{_sysconfdir}/%{name}/cgi.cfg
%config(noreplace) %{_sysconfdir}/%{name}/cgiauth.cfg
%config(noreplace) %{apacheconfdir}/icinga.conf
%config(noreplace) %attr(0640,root,%{apachegroup}) %{_sysconfdir}/%{name}/passwd


%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/

%files idoutils
%defattr(-,root,root)
%doc README.idoutils.transitional

%files idoutils-libdbi-mysql
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING module/idoutils/db %{readme} %{readmeido}
%if 0%{?using_systemd}
%attr(644,-,-)  %{_unitdir}/ido2db.service
%else
%attr(755,-,-) %{_initrddir}/ido2db
%endif
%attr(660,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ido2db.cfg
%config(noreplace) %{_sysconfdir}/%{name}/idomod.cfg
%config(noreplace) %{_sysconfdir}/%{name}/modules/idoutils.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/ido2db_check_proc.cfg
%{_bindir}/ido2db
%{_bindir}/log2ido
%{_libdir}/%{name}/idomod.so

%files idoutils-libdbi-pgsql
%defattr(-,root,root,-)
%doc README LICENSE Changelog UPGRADING module/idoutils/db %{readme} %{readmeido}
%if 0%{?using_systemd}
%attr(644,-,-)  %{_unitdir}/ido2db.service
%else
%attr(755,-,-) %{_initrddir}/ido2db
%endif
%attr(660,root,root) %config(noreplace) %{_sysconfdir}/%{name}/ido2db.cfg
%config(noreplace) %{_sysconfdir}/%{name}/idomod.cfg
%config(noreplace) %{_sysconfdir}/%{name}/modules/idoutils.cfg
%config(noreplace) %{_sysconfdir}/%{name}/objects/ido2db_check_proc.cfg
%{_bindir}/ido2db
%{_bindir}/log2ido
%{_libdir}/%{name}/idomod.so


%changelog
* Thu Mar 13 2014 Michael Friedrich <michael.friedrich@netways.de> - 1.11.0-1
- bump 1.11.0

* Tue Feb 11 2014 Michael Friedrich <michael.friedrich@netways.de> - 1.10.3-1
- bump 1.10.3

* Thu Dec 05 2013 Ricardo Bartels <ricardo@bitchbrothers.com> - 1.10.2-1
- bump 1.10.2

* Mon Nov 04 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.10.1-1
- bump 1.10.1

* Wed Oct 16 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.10.0-1
- bump 1.10.0

* Sun Jul 07 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.9.3-1
- bump 1.9.3

* Sun Jun 30 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.9.2-1
- bump 1.9.2

* Wed May 22 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.9.1-1
- bump 1.9.1

* Tue May 07 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.9.0-1
- bump 1.9.0

* Tue Mar 05 2013 Rene Koch <r.koch@ovido.at> - 1.8.4-5
- fixed double logdir/gui/ definitions in icinga and icinga-gui

* Fri Feb 15 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.4-4
- fix rpmlint errors/warnings

* Wed Feb 06 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.4-3
- add idoutils as transitional package (thx Stefan Marx, Michael Grüner)

* Fri Feb 01 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.4-2
- fix sf.net url

* Sun Jan 13 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.4-1
- 1.8.4 bump

* Wed Dec 12 2012 Michael Friedrich <michael.friedrich@netways.de> - 1.8.3-1
- 1.8.3 bump

* Tue Oct 30 2012 Michael Friedrich <michael.friedrich@gmail.com> - 1.8.2-1
- 1.8.2 bump

* Thu Oct 25 2012 Michael Friedrich <michael.friedrich@gmail.com> - 1.8.1-1
- 1.8.1 release with a quickfix for faulty macros

* Thu Oct 18 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.8.0-1
- bump version
- add devel package, installing header files to include/
- use --with-mainurl from upstream to set the default to /icinga/cgi-bin/status.cgi?host=all&type=detail&servicestatustypes=29
- forgot to check on old icinga.cfg entries not matching - enforce that once
- change permissions on ido2db.cfg, not being world readable (Aaron Russo) #2987
- drop unsupported configure options causing warnings #3037
- fix new jquery-ui files from icinga-gui datetime picker #3009

* Thu Aug 30 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.2-2
- include a fix for epn failure from upstream

* Tue Aug 21 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.2-1
- bump version

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

