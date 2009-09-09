# $Id$
# Authority: cmr
# Upstream: The icinga devel team <icinga-devel at lists.sourceforge.net>
# Needs libdbi
# ExcludeDist: el4 el3

%define logdir %{_localstatedir}/log/icinga

Summary: Open Source host, service and network monitoring program
Name: icinga
Version: 0.8.3
Release: 1
License: GPL
Group: Applications/System
URL: http://www.icinga.org/

Source0: http://dl.sf.net/icinga/icinga-%{version}.tar.gz
#Source1: idoutils-init
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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

%description gui
This package contains the webgui (html,css,cgi etc.) for %{name}

%package idoutils
Summary: Web content for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description idoutils
This package contains the idoutils addon for %{name} wich provides 
database storage via libdbi.


%prep
%setup

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
    --with-command-user="apache" \
    --with-command-group="apache" \
    --with-gd-lib="%{_libdir}" \
    --with-gd-inc="%{_includedir}" \
    --with-htmurl="/icinga" \
    --with-init-dir="%{_initrddir}" \
    --with-lockfile="%{_localstatedir}/run/icinga.pid" \
    --with-mail="/bin/mail" \
    --with-icinga-user="icinga" \
    --with-icinga-group="icinga" \
    --with-template-objects \
    --with-template-extinfo \
    --enable-event-broker \
    --enable-embedded-perl \
    --enable-idoutils
%{__make} %{?_smp_mflags} all

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/etc/httpd/conf.d
%{__make} install install-init install-commandmode install-config \
    install-webconf install-idoutils \
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
/usr/sbin/useradd -c "icinga" -s /sbin/nologin -r -d /var/icinga -G apache icinga 2> /dev/null || :


%post
/sbin/chkconfig --add icinga

%preun
if [ $1 -eq 0 ]; then
    /sbin/service icinga stop &>/dev/null || :
    /sbin/chkconfig --del icinga
fi


%post idoutils
/sbin/chkconfig --add ido2db

%preun idoutils
if [ $1 -eq 0 ]; then
    /sbin/service idoutils stop &>/dev/null || :
    /sbin/chkconfig --del idoutils
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
%attr(2755,icinga,apache) %{_localstatedir}/icinga/rw/

%files gui
%defattr(-,icinga,icinga,-)
%config(noreplace) %attr(-,root,root) %{_sysconfdir}/httpd/conf.d/icinga.conf
%{_datadir}/icinga

%files idoutils
%defattr(-,icinga,icinga,-)
%attr(755,root,root) %{_initrddir}/ido2db
%config(noreplace) %{_sysconfdir}/icinga/ido2db.cfg
%config(noreplace) %{_sysconfdir}/icinga/idomod.cfg
%{_sysconfdir}/icinga/idoutils
%{_bindir}/ido2db
%{_bindir}/idomod.o


%changelog
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

