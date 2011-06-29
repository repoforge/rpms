# $Id$
# Authority: cmr
# Upstream: The icinga devel team <icinga-devel at lists.sourceforge.net>
#
# Needs libdbi
#
# ExclusiveDist: el5 el6

%define logdir %{_localstatedir}/log/icinga

%define apacheconfdir  %{_sysconfdir}/httpd/conf.d
%define apacheuser apache

Summary: Open Source host, service and network monitoring program
Name: icinga
Version: 1.4.2
Release: 2%{?dist}
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
#Requires: nagios-plugins
Provides: nagios

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

%package idoutils
Summary: database broker module for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description idoutils
This package contains the idoutils broker module for %{name} which provides
database storage via libdbi.

%package api
Summary: PHP api for %{name}
Group: Applications/System
Requires: php

%description api
PHP api for %{name}

%package doc
Summary: documentation %{name}
Group: Documentation

%description doc
Documentation for %{name}


%prep
%setup -qn %{name}-%{version}

%build
%configure \
    --datadir="%{_datadir}/icinga" \
    --datarootdir="%{_datadir}/icinga" \
    --libexecdir="%{_datadir}/icinga" \
    --localstatedir="%{_localstatedir}/icinga" \
    --with-checkresult-dir="%{_localstatedir}/icinga/checkresults" \
    --sbindir="%{_libdir}/icinga/cgi" \
    --sysconfdir="%{_sysconfdir}/icinga" \
    --with-cgiurl="/icinga/cgi-bin" \
    --with-command-user="icinga" \
    --with-command-group="icingacmd" \
    --with-gd-lib="%{_libdir}" \
    --with-gd-inc="%{_includedir}" \
    --with-htmurl="/icinga" \
    --with-init-dir="%{_initrddir}" \
    --with-lockfile="%{_localstatedir}/icinga/icinga.pid" \
    --with-mail="/bin/mail" \
    --with-icinga-user="icinga" \
    --with-icinga-group="icinga" \
    --with-template-objects \
    --with-template-extinfo \
    --enable-event-broker \
    --enable-embedded-perl \
    --enable-idoutils \
    --with-httpd-conf=%{apacheconfdir} \
    --with-init-dir=%{_initrddir}
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
    install-api \
    DESTDIR="%{buildroot}" \
    INSTALL_OPTS="" \
    INSTALL_OPTS_WEB="" \
    COMMAND_OPTS="" \
    INIT_OPTS=""

### strip binary
%{__strip} %{buildroot}%{_bindir}/{icinga,icingastats,log2ido,ido2db}
%{__strip} %{buildroot}%{_libdir}/icinga/cgi/*.cgi

### FIX log-paths
%{__perl} -pi -e '
        s|log_file.*|log_file=%{logdir}/icinga.log|;
        s|log_archive_path=.*|log_archive_path=%{logdir}/archives|;
        s|debug_file=.*|debug_file=%{logdir}/icinga.debug|;
   ' %{buildroot}%{_sysconfdir}/icinga/icinga.cfg

### make logdirs
%{__mkdir} -p %{buildroot}%{logdir}/
%{__mkdir} -p %{buildroot}%{logdir}/api/
%{__mkdir} -p %{buildroot}%{logdir}/gui/
%{__mkdir} -p %{buildroot}%{logdir}/archives/

### remove PLACEHOLDER
rm %{buildroot}%{_datadir}/icinga/icinga-api/log/PLACEHOLDER
### Move all logging to logdir
rmdir %{buildroot}%{_datadir}/icinga/icinga-api/log
%{__perl} -pi -e '
        s|define\("DEFAULT_API_LOG_FILE",.*|define\("DEFAULT_API_LOG_FILE","%{logdir}/api/icinga-api.log"\);|;
   ' %{buildroot}%{_datadir}/icinga/icinga-api/objects/debug/debugTargets/icingaApiFileDebugger.php
mv %{buildroot}%{_datadir}/icinga/log/{.htaccess,index.htm} %{buildroot}%{logdir}/gui
rmdir %{buildroot}%{_datadir}/icinga/log/

%{__perl} -pi -e '
        s|cgi_log_file.*|cgi_log_file=%{logdir}/gui/icinga-cgi.log|;
        s|cgi_log_archive_path=.*|cgi_log_archive_path=%{logdir}/archives|;
   ' %{buildroot}%{_sysconfdir}/icinga/cgi.cfg
%{__perl} -pi -e "
        s|^use constant\tDEBUG_LOG_PATH.*|use constant\tDEBUG_LOG_PATH\t=> '/var/log/icinga/' ;|
   " %{buildroot}%{_bindir}/p1.pl


### move idoutils sample configs to final name
mv %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg-sample %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg
mv %{buildroot}%{_sysconfdir}/icinga/idomod.cfg-sample %{buildroot}%{_sysconfdir}/icinga/idomod.cfg
mv %{buildroot}%{_sysconfdir}/icinga/modules/idoutils.cfg-sample %{buildroot}%{_sysconfdir}/icinga/modules/idoutils.cfg

### copy idoutils db-script
cp -r module/idoutils/db %{buildroot}%{_sysconfdir}/icinga/idoutils



%pre
# Add icinga user
/usr/sbin/groupadd icinga 2> /dev/null || :
/usr/sbin/groupadd icingacmd 2> /dev/null || :
/usr/sbin/useradd -c "icinga" -s /sbin/nologin -r -d /var/icinga -G icingacmd -g icinga icinga 2> /dev/null || :


%post
/sbin/chkconfig --add icinga

%preun
if [ $1 -eq 0 ]; then
    /sbin/service icinga stop &>/dev/null || :
    /sbin/chkconfig --del icinga
fi

%pre gui
# Add apacheuser in the icingacmd group
  /usr/sbin/usermod -a -G icingacmd %{apacheuser}

%post idoutils
/sbin/chkconfig --add ido2db

%preun idoutils
if [ $1 -eq 0 ]; then
    /sbin/service idoutils stop &>/dev/null || :
    /sbin/chkconfig --del ido2db
fi


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,icinga,icinga,-)
%attr(755,root,root) %{_initrddir}/icinga
%dir %{_sysconfdir}/icinga
%dir %{_sysconfdir}/icinga/modules
%config(noreplace) %{_sysconfdir}/icinga/icinga.cfg
%dir %{_sysconfdir}/icinga/objects
%config(noreplace) %{_sysconfdir}/icinga/objects/commands.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/contacts.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/localhost.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/printer.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/switch.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/templates.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/timeperiods.cfg
%config(noreplace) %{_sysconfdir}/icinga/objects/windows.cfg
%config(noreplace) %{_sysconfdir}/icinga/resource.cfg
%{_bindir}/icinga
%{_bindir}/icingastats
%{_bindir}/p1.pl
%dir %{_localstatedir}/icinga
%dir %{_localstatedir}/icinga/checkresults
%attr(2755,icinga,icingacmd) %{_localstatedir}/icinga/rw/
%{logdir}
%{logdir}/archives

%files doc
%defattr(-,icinga,icinga,-)
%{_datadir}/icinga/docs

%files gui
%defattr(-,icinga,icinga,-)
%config(noreplace) %attr(-,root,root) %{apacheconfdir}/icinga.conf
%config(noreplace) %{_sysconfdir}/icinga/cgi.cfg
%config(noreplace) %{_sysconfdir}/icinga/cgiauth.cfg
%{_libdir}/icinga
%{_libdir}/icinga/cgi
%{_libdir}/icinga/cgi/*.cgi
%dir %{_datadir}/icinga
%{_datadir}/icinga/contexthelp
%{_datadir}/icinga/images
%{_datadir}/icinga/index.html
%{_datadir}/icinga/js
%{_datadir}/icinga/main.html
%{_datadir}/icinga/media
%{_datadir}/icinga/menu.html
%{_datadir}/icinga/robots.txt
%{_datadir}/icinga/sidebar.html
%{_datadir}/icinga/ssi
%{_datadir}/icinga/stylesheets
#%attr(0755,%{apacheuser},%{apachegroup}) %{_datadir}/icinga/log
%attr(2775,icinga,icingacmd) %dir %{logdir}/gui
%attr(664,icinga,icingacmd) %{logdir}/gui/index.htm
%attr(664,icinga,icingacmd) %{logdir}/gui/.htaccess

%files idoutils
%defattr(-,icinga,icinga,-)
%attr(755,root,root) %{_initrddir}/ido2db
%config(noreplace) %{_sysconfdir}/icinga/ido2db.cfg
%config(noreplace) %{_sysconfdir}/icinga/idomod.cfg
%config(noreplace) %{_sysconfdir}/icinga/modules/idoutils.cfg
%{_sysconfdir}/icinga/idoutils
%{_bindir}/ido2db
%{_bindir}/log2ido
%{_bindir}/idomod.o

%files api
%defattr(-,icinga,icinga,-)
%dir %{_datadir}/icinga/icinga-api
%{_datadir}/icinga/icinga-api/IcingaApi.php
%{_datadir}/icinga/icinga-api/contrib
%{_datadir}/icinga/icinga-api/objects
%{_datadir}/icinga/icinga-api/tests
%attr(2775,icinga,icingacmd) %dir %{logdir}/api


%changelog
* Wed Jun 29 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.2-2
- Merged the submission by Michael Friedrich (thanks!)

* Mon Jun 20 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.4.2-1
- update to 1.4.2
- mv idoutils.cfg-sample
- move all logging to one location https://bugzilla.redhat.com/show_bug.cgi?id=693608
- fix file perms and locations of cfgs
- fix group for doc

* Sun Jun 05 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.4.1-1
- update to 1.4.1

* Wed May 18 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.4.0-3
- undo provides nagios version

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
