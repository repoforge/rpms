# $Id$
# Authority: The icinga devel team <icinga-devel at lists.sourceforge.net>
# Upstream: The icinga devel team <icinga-devel at lists.sourceforge.net>
# ExcludeDist: el4 el3

%define revision 2

%define logdir %{_localstatedir}/log/%{name}
%define cachedir %{_localstatedir}/cache/%{name}
%define reportingcachedir %{_localstatedir}/cache/%{name}/reporting

%if "%{_vendor}" == "suse"
%define phpname php5
%endif
%if "%{_vendor}" == "redhat"
%define phpname php
%endif

# on RHEL5 php is php-5.1 and php53 is php-5.3
# icinga-web requires at least php-5.2.3 so
# enforce the correct php package name on RHEL5
%if 0%{?el5}
%define phpname php53
%endif

%if "%{_vendor}" == "suse"
%define apacheconfdir  %{_sysconfdir}/apache2/conf.d
%define apacheuser wwwrun
%define apachegroup www
%endif
%if "%{_vendor}" == "redhat"
%define apacheconfdir  %{_sysconfdir}/httpd/conf.d
%define apacheuser apache
%define apachegroup apache
%endif

%if "%{_vendor}" == "suse"
%define extcmdfile %{_localstatedir}/icinga/rw/icinga.cmd
%endif
%if "%{_vendor}" == "redhat"
%define extcmdfile %{_localstatedir}/spool/icinga/cmd/icinga.cmd
%endif


Summary: Open Source host, service and network monitoring Web UI
Name: icinga-web
Version: 1.8.2
Release: %{revision}%{?dist}
License: GPLv3
Group: Applications/System
URL: http://www.icinga.org/
BuildArch: noarch
%if "%{_vendor}" == "suse"
AutoReqProv: Off
%endif

# Source0: icinga-web-%{version}.tar.gz
Source0: https://downloads.sourceforge.net/project/icinga/icinga-web/%{version}/icinga-web-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: %{phpname} >= 5.2.3
BuildRequires: %{phpname}-gd
BuildRequires: %{phpname}-ldap
BuildRequires: %{phpname}-pdo

%if "%{_vendor}" == "redhat"
BuildRequires: %{phpname}-xml
BuildRequires: php-pear
%endif
%if "%{_vendor}" == "suse"
BuildRequires: %{phpname}-devel >= 5.2.3 
BuildRequires: %{phpname}-json
BuildRequires: %{phpname}-sockets
BuildRequires: %{phpname}-xsl
BuildRequires: %{phpname}-dom
BuildRequires: %{phpname}-pear
%endif


Requires: perl(Locale::PO)
Requires: %{phpname} >= 5.2.3
Requires: %{phpname}-gd
Requires: %{phpname}-ldap
Requires: %{phpname}-pdo
%if "%{_vendor}" == "redhat"
Requires: %{phpname}-common
Requires: %{phpname}-xml
Requires: php-pear
%endif
%if "%{_vendor}" == "suse"
Requires: %{phpname}-pear
Requires: %{phpname}-xsl
Requires: %{phpname}-dom
Requires: %{phpname}-tokenizer
Requires: %{phpname}-gettext
Requires: %{phpname}-ctype
Requires: %{phpname}-json
Requires: %{phpname}-pear
Requires: apache2-mod_php5
%endif
Requires: pcre >= 7.6


##############################
%description
##############################
Icinga Web for Icinga Core, uses Icinga IDOUtils DB as data source.

##############################
%package module-pnp
##############################
Summary: PNP Integration module for Icinga Web
Group: Applications/System
Requires: pnp4nagios
Requires: %{name} = %{version}-%{release}

##############################
%description module-pnp
##############################
PNP Integration module for Icinga Web

##############################
%package module-nagiosbp
##############################
Summary: Nagios Business Process Addon Integration module for Icinga Web
Group: Applications/System
Requires: nagios-business-process-addon-icinga
Requires: %{name} = %{version}-%{release}

##############################
%description module-nagiosbp
##############################
Summary: Nagios Business Process Addon Integration module for Icinga Web


##############################
%prep
##############################
%setup -q -n %{name}-%{version}

##############################
%build
##############################
%configure \
    --prefix="%{_datadir}/%{name}" \
    --datadir="%{_datadir}/%{name}" \
    --datarootdir="%{_datadir}/%{name}" \
    --sysconfdir="%{_sysconfdir}/%{name}" \
    --with-conf-dir='%{_sysconfdir}/%{name}/conf.d' \
    --with-web-user='%{apacheuser}' \
    --with-web-group='%{apachegroup}' \
    --with-api-cmd-file='%{extcmdfile}' \
    --with-log-dir='%{logdir}' \
    --with-cache-dir='%{cachedir}' \
    --with-reporting-tmp-dir='%{reportingcachedir}' \
    --with-icinga-bin='%{_bindir}/icinga' \
    --with-icinga-cfg='%{_sysconfdir}/icinga/icinga.cfg' \
    --with-icinga-objects-dir='%{_sysconfdir}/icinga/objects' \
    --with-clearcache-path='%{_bindir}' \
    --with-web-apache-path=%{apacheconfdir}

##############################
%install
##############################
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{apacheconfdir}
%{__mkdir} -p %{buildroot}/%{_bindir}
%{__make} install \
    install-apache-config \
    DESTDIR="%{buildroot}" \
    INSTALL_OPTS="" \
    COMMAND_OPTS="" \
    INSTALL_OPTS_WEB="" \
    INSTALL_OPTS_CACHE="" \
    INIT_OPTS=""

# we only want clearcache.sh prefixed in {_bindir}, generated from configure
%{__mv} %{buildroot}%{_bindir}/clearcache.sh %{buildroot}%{_bindir}/%{name}-clearcache

# wipe the rest of bin/, we don't need prepackage stuff in installed envs
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/bin

# place the pnp templates for -module-pnp
%{__cp} contrib/PNP_Integration/templateExtensions/* %{buildroot}%{_datadir}/%{name}/app/modules/Cronks/data/xml/extensions/

# place the nagiosbp files for -module-nagiosbp
%{__mkdir} %{buildroot}%{_datadir}/%{name}/app/modules/BPAddon
%{__cp} -r contrib/businessprocess-icinga-cronk/BPAddon/* %{buildroot}%{_datadir}/%{name}/app/modules/BPAddon/
# adjust the config for the packaged nagiosbp
%{__sed} -i -e 's|/usr/local/nagiosbp/etc|/etc/nagiosbp|' \
	-i -e 's|/usr/local/nagiosbp/bin|/usr/bin|' \
	%{buildroot}%{_datadir}/%{name}/app/modules/BPAddon/config/bp.xml
%{__sed} -i -e 's|\(name="pass">\)icingaadmin|\1password|' \
	%{buildroot}%{_datadir}/%{name}/app/modules/BPAddon/config/cronks.xml

##############################
%pre
##############################

# Add apacheuser in the icingacmd group
# If the group exists, add the apacheuser in the icingacmd group.
# It is not neccessary that icinga-web is installed on the same system as
# icinga and only on systems with icinga installed the icingacmd
# group exists. In all other cases the user used for ssh access has
# to be added to the icingacmd group on the remote icinga server.
getent group icingacmd > /dev/null

if [ $? -eq 0 ]; then
%{_sbindir}/usermod -a -G icingacmd %{apacheuser}
fi

# uncomment if building from git
# %{__rm} -rf %{buildroot}%{_datadir}/icinga-web/.git

##############################
%preun
##############################

##############################
%post
##############################

# clean config cache, e.g. after upgrading
%{__rm} -rf %{cachedir}/config/*.php

##############################
%post module-pnp
##############################

# clean cronk template cache
%{__rm} -rf %{cachedir}/CronkTemplates/*.php

##############################
%post module-nagiosbp
##############################

%{_bindir}/%{name}-clearcache

##############################
%clean
##############################

%{__rm} -rf %{buildroot}

##############################
%files
##############################
# main dirs
%defattr(-,root,root)
%doc etc/schema doc/README.RHEL doc/AUTHORS doc/CHANGELOG-1.7 doc/CHANGELOG-1.x doc/LICENSE
# packaged by subpackages
%exclude %{_datadir}/%{name}/app/modules/BPAddon
%exclude %{_datadir}/%{name}/app/modules/Cronks/data/xml/extensions
%{_datadir}/%{name}/app
%{_datadir}/%{name}/doc
%{_datadir}/%{name}/etc
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/pub
# configs
%defattr(-,root,root)
%config(noreplace) %attr(-,root,root) %{apacheconfdir}/icinga-web.conf
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %attr(644,-,-) %{_sysconfdir}/%{name}/conf.d/*
# logs+cache
%attr(2775,%{apacheuser},%{apachegroup}) %dir %{logdir}
%attr(-,%{apacheuser},%{apachegroup}) %{cachedir}
%attr(-,%{apacheuser},%{apachegroup}) %{cachedir}/config
# binaries
%defattr(-,root,root)
%{_bindir}/%{name}-clearcache

##############################
%files module-pnp
##############################
# templates, experimental treatment as configs (noreplace)
%defattr(-,root,root)
%doc contrib/PNP_Integration/README contrib/PNP_Integration/INSTALL
%doc contrib/PNP_Integration/doc contrib/nginx
%dir %{_datadir}/icinga-web/app/modules/Cronks/data/xml/extensions
%config(noreplace) %attr(644,-,-) %{_datadir}/%{name}/app/modules/Cronks/data/xml/extensions/*

%files module-nagiosbp
##############################
# templates, experimental treatment as configs (noreplace)
%defattr(-,root,root)
%doc contrib/businessprocess-icinga-cronk/doc
%config(noreplace) %{_datadir}/%{name}/app/modules/BPAddon/config/*
%{_datadir}/%{name}/app/modules/BPAddon

##############################
%changelog
##############################
* Fri Feb 15 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.2-2
- fix rpmlint errors/warnings

* Wed Feb 11 2013 Markus Frosch <markus.frosch@netways.de> - 1.8.2-1
- bump to 1.8.2

* Wed Feb 06 2013 Michael Friedrich <michael.friedrich@netways.de> - 1.8.1-3
- fix php5-pear reqs
- fix php5-dom (suse), php-xml (rhel) and other missing/faulty reqs

* Fri Jan 25 2013 Christian Dengler <christian.dengler@netways.de> - 1.8.1-2
- add BuildRequires; add subpackage for nagiosbp

* Wed Dec 5 2012 Marius Hein <marius.hein@netways.de> - 1.8.1-1
- bump to 1.8.1

* Mon Sep 24 2012 Michael Friedrich <michael.friedrich@gmail.com> - 1.8.0-1
- bump to 1.8.0

* Tue Aug 7 2012 Marius Hein <marius.hein@netways.de> - 1.7.2-1
- bump to 1.7.2

* Mon Jun 18 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.1-1
- bump to 1.7.1

* Tue Apr 24 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.7.0-1
- bump to 1.7.0
- use name macro instead of hardcoded
- use _sbindir macro instead of hardcoded
- define extcmdfile macro for suse and redhat
- set extcmdfile to _localstatedir/spool/icinga/cmd/icinga.cmd for rhel as changed in icinga.spec
- update Changelog for docs - this requires more generic addin
- use --with-clearcache-path, but still rename to be prefixed
- correct license to gplv3

* Wed Feb 29 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.2-2
- move etc/schema sql scripts to docs (thx Michael Gruener) #2381
- install etc/conf.d to {_sysconfdir}/icinga-web/conf.d saving main dir for other configs #2382
- install clearcache.sh as {_bindir}/icinga-web-clearcache #2115
- remove rest of bin/, won't be needed on package install #2116
- add contrib/ and partly doc/ to docs section #2384
- add experimental package icinga-web-module-pnp for automated pnp integration. use with caution and report bugs. #2385
- add requires for module-pnp: icinga-web and pnp4nagios
- set --with-reporting-tmp-dir= {_localstatedir}/cache/icinga-web/reporting
- set configure for access.xml: --with-icinga-bin=,--with-icinga-cfg=,--with-icinga-objects= matching icinga rpm #2259

* Mon Feb 20 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.2-1
- bump to 1.6.2
- clean config cache in post (important for upgrades) #2217

* Mon Dec 12 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.1-1
- bump to 1.6.1
- fix forgotten sla.xml inclusion

* Sat Oct 22 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.6.0-1
- bump to 1.6.0
- add --with-cache-dir and use _localstatedir/cache/icinga-web

* Thu Sep 15 2011 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.5.2-1
- drop icinga-api dependency
- drop BuildRequires - not needed at this stage
- add --with-api-cmd-file, using same location as icinga rpm _localstatedir/icinga/rw/icinga.cmd
- change new config location from default $prefix/etc/conf.d to _sysconfdir/icinga-web
- mark all config xmls as config noreplace
- set _localstatedir/log/icinga-web and use it instead of $prefix/logs
- set apache user/group to write logdir
- reorder files to be included in the package

* Thu May 5 2011 Michael Friedrich - 1.4.0-1
- update for upcoming release

* Mon Jan 10 2011 Michael Friedrich - 1.3.0-1
- update for upcoming release

* Tue Aug 31 2010 Christoph Maser <cmaser@gmx.de> - 1.0.3-2
- add icinga-api as build dependency, --with-icinga-api wil be ignored otherwise
- change icinga-api path to value used in icinga-api-rpm
- set defattr
- set ownership to apache for log-dirs

* Tue Aug 17 2010 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.0.3-1
- updated for 1.0.3, removed fix-priv fix-libs as this is now in make install

* Tue Jun 29 2010 Michael Friedrich <michael.friedrich@univie.ac.at> - 1.0.1-1
- updated for 1.0.1

* Fri Apr 16 2010 Michael Friedrich <michael.friedrich@univie.ac.at> - 0.9.1-1
- initial creation


