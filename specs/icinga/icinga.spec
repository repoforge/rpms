# $Id$
# Authority: cmr
# Upstream: The icinga devel team <icinga-devel at lists.sourceforge.net>
# Needs libdbi
# ExcludeDist: el4 el3

%define logdir %{_localstatedir}/log/icinga

%if "%{_vendor}" == "suse"
%define apacheconfdir  %{_sysconfdir}/apache2/conf.d
%define apacheuser wwwrun
%endif
%if "%{_vendor}" == "redhat"
%define apacheconfdir  %{_sysconfdir}/httpd/conf.d
%define apacheuser apache
%endif

Summary: Open Source host, service and network monitoring program
Name: icinga
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.icinga.org/

Source0: http://dl.sf.net/icinga/icinga-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc
BuildRequires: gd-devel > 1.8
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libdbi-devel
BuildRequires: perl(ExtUtils::Embed)
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
Group: Applications/System
 
%description doc
Documentation for %{name}


%prep
%setup -n %{name}-%{version}

# /usr/local/nagios is hardcoded in many places
%{__perl} -pi.orig -e 's|/usr/local/nagios/var/rw|%{_localstatedir}/nagios/rw|g;' contrib/eventhandlers/submit_check_result

%build
%configure \
    --datadir="%{_datadir}/icinga" \
    --datarootdir="%{_datadir}/icinga" \
    --libexecdir="%{_datadir}/icinga" \
    --localstatedir="%{_localstatedir}/icinga" \
    --with-checkresult-dir="%{_localstatedir}/icinga/checkresults" \
    --sbindir="%{_datadir}/icinga/cgi" \
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
    COMMAND_OPTS="" \
    INIT_OPTS=""

### FIX log-paths
%{__perl} -pi -e '
        s|log_file.*|log_file=%{logdir}/icinga.log|;
        s|log_archive_path=.*|log_archive_path=%{logdir}/archives|;
        s|debug_file=.*|debug_file=%{logdir}/icinga.debug|;
   ' %{buildroot}%{_sysconfdir}/icinga/icinga.cfg

### make logdirs
%{__mkdir} -p %{buildroot}%{logdir}/
%{__mkdir} -p %{buildroot}%{logdir}/archives/

### move idoutils sample configs to final name
mv %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg-sample %{buildroot}%{_sysconfdir}/icinga/ido2db.cfg
mv %{buildroot}%{_sysconfdir}/icinga/idomod.cfg-sample %{buildroot}%{_sysconfdir}/icinga/idomod.cfg

### copy idutils db-script
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
%if "%{_vendor}" == "suse"
  /usr/sbin/groupmod -A %{apacheuser} icingacmd
%endif
%if "%{_vendor}" == "redhat"
  /usr/sbin/usermod -a -G icingacmd %{apacheuser}
%endif

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
%config(noreplace) %{_sysconfdir}/icinga/cgi.cfg
%config(noreplace) %{_sysconfdir}/icinga/icinga.cfg
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
%{logdir}
%dir %{_localstatedir}/icinga
%dir %{_localstatedir}/icinga/checkresults
%attr(2755,icinga,icingacmd) %{_localstatedir}/icinga/rw/

%files doc
%defattr(-,icinga,icinga,-)
%{_datadir}/icinga/docs

%files gui
%defattr(-,icinga,icinga,-)
%config(noreplace) %attr(-,root,root) %{apacheconfdir}/icinga.conf
%dir %{_datadir}/icinga
%{_datadir}/icinga/cgi
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
%{_datadir}/icinga/top.html

%files idoutils
%defattr(-,icinga,icinga,-)
%attr(755,root,root) %{_initrddir}/ido2db
%config(noreplace) %{_sysconfdir}/icinga/ido2db.cfg
%config(noreplace) %{_sysconfdir}/icinga/idomod.cfg
%{_sysconfdir}/icinga/idoutils
%{_bindir}/ido2db
%{_bindir}/idomod.o

%files api
%defattr(-,icinga,icinga,-)
%{_datadir}/icinga/icinga-api
%attr(-,%{apacheuser},%{apacheuser}) %{_datadir}/icinga/icinga-api/log


%changelog
* Mon Oct 25 2010 Christoph Maser <cmaser@gmx.de> - 1.2.1-1
- update for release 1.2.1

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
- Correct checkconfig --del in idoutils %preun

* Mon Oct 26 2009 Christoph Maser <cmr@financial.com> - 0.8.4-3
- Use icingacmd group and add apache user to that group instead
  of using apachegroup as icinga command group.

* Wed Oct 07 2009 Christoph Maser <cmr@financial.com> - 0.8.4-2
- make packages openSUSE compatible
- add %apachecondir, %apacheuser, %apachegroup depending on vendor
- configure add --with-httpd-conf=%{apacheconfdir} 
- configure add --with-init-dir=%{_initrddir}

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

