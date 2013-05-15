# $Id:$
# Upstream:	pnp4nagios-devel@lists.sourceforge.net


%define logmsg logger -t %{name}/rpm

Name:		pnp4nagios
Version:	0.6.21
Release:	1
Summary:	PNP is not PerfParse. A Nagios/Icinga perfdata graphing solution

Group:		Applications/System
License:	GPLv2
URL:		http://www.pnp4nagios.org/
Source:		http://downloads.sourceforge.net/pnp4nagios/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	rrdtool-devel
BuildRequires:	perl-rrdtool
BuildRequires:	perl(Time::HiRes)
Requires:	rrdtool
Requires:	perl-rrdtool
Requires: 	perl(Time::HiRes)

%description
PNP is an addon to Nagios/Icinga which analyzes performance data provided by plugins and stores them automatically into RRD-databases.

%prep
%setup -q


%build
sed -i -e 's/INSTALL_OPTS="-o $nagios_user -g $nagios_grp"/INSTALL_OPTS=""/' configure
sed -i -e 's/INIT_OPTS=-o root -g root/INIT_OPTS=/' scripts/Makefile.in
# hardcode that until a proper fix is upstream
sed -i -e 's/MANDIR=@mandir@/MANDIR=\/usr\/share\/man/' man/Makefile.in
%configure --with-perfdata-logfile=%{_localstatedir}/log/nagios/perfdata.log \
	--sysconfdir=%{_sysconfdir}/%{name} \
	--datarootdir=%{_datadir}/%{name} \
	--with-perfdata-dir=%{_datadir}/%{name}/perfdata \
	--with-perfdata-spool-dir=%{_localstatedir}/spool/nagios \
	--mandir=%{_mandir} \
	--libdir=%{_libdir}/%{name}  # only kohana is installed there and maybe we have a system wide kohana already
make %{?_smp_mflags} all


%install
rm -rf %{buildroot}
%{__mkdir} -p  %{buildroot}%{_sysconfdir}/httpd/conf.d/
make fullinstall DESTDIR=%{buildroot}
mv %{buildroot}%{_sysconfdir}/%{name}/check_commands/check_nwstat.cfg-sample %{buildroot}%{_sysconfdir}/%{name}/check_commands/check_nwstat.cfg
mv %{buildroot}%{_sysconfdir}/%{name}/pages/web_traffic.cfg-sample %{buildroot}%{_sysconfdir}/%{name}/pages/web_traffic.cfg
mv %{buildroot}%{_sysconfdir}/%{name}/rra.cfg-sample %{buildroot}%{_sysconfdir}/%{name}/rra.cfg

sed -i -e 's*log_file = /var/npcd.log*log_file = /var/log/nagios/npcd.log*' %{buildroot}%{_sysconfdir}/%{name}/npcd.cfg
# fix paths in nagios.cfg sample and create an icinga compliant sample too (pkg locations!)
cp %{buildroot}%{_sysconfdir}/%{name}/nagios.cfg-sample %{buildroot}%{_sysconfdir}/%{name}/icinga.cfg-sample
mv %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample-nagios
cp %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample-nagios %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample-icinga

# fix faulty perfdata file locations
sed -i -e 's/\/var\/service-perfdata/\/var\/spool\/nagios\/service-perfdata/g;
	s/\/var\/host-perfdata/\/var\/spool\/nagios\/host-perfdata/g
	' %{buildroot}%{_sysconfdir}/%{name}/nagios.cfg-sample
sed -i -e 's/\/var\/service-perfdata/\/var\/spool\/nagios\/service-perfdata/g;
	s/\/var\/host-perfdata/\/var\/spool\/nagios\/host-perfdata/g
	' %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample-nagios

sed -i -e 's/\/var\/service-perfdata/\/var\/spool\/icinga\/service-perfdata/g;
	s/\/var\/host-perfdata/\/var\/spool\/icinga\/host-perfdata/g
	' %{buildroot}%{_sysconfdir}/%{name}/icinga.cfg-sample

sed -i -e 's/\/var\/service-perfdata/\/var\/spool\/icinga\/service-perfdata/g;
	s/\/var\/host-perfdata/\/var\/spool\/icinga\/host-perfdata/g;
	s/\/var\/spool\/nagios\/service-perfdata/\/var\/spool\/icinga\/perfdata\/service-perfdata/g;
	s/\/var\/spool\/nagios\/host-perfdata/\/var\/spool\/icinga\/perfdata\/host-perfdata/g
	' %{buildroot}%{_sysconfdir}/%{name}/misccommands.cfg-sample-icinga


# drop local versioning, we already provide our own upgrade safety
rm -f %{buildroot}%{_sysconfdir}/%{name}/config.php.%{version}
rm -f %{buildroot}%{_sysconfdir}/%{name}/config_local.php

%pre

%post

# do that on fresh installs only
if [ $1 -eq 1 ] ; then

# check wether icinga or nagios rpm is installed, and their users
if [ -f /etc/nagios/nagios.cfg ] && [ -f /usr/bin/nagios ] ; then
		# otherwise, stick with nagios
	getent group nagios >/dev/null || %{_sbindir}/groupadd nagios
	getent group nagiocmd >/dev/null || %{_sbindir}/groupadd nagiocmd
	getent passwd nagios >/dev/null || %{_sbindir}/useradd -c "nagios" -s /sbin/nologin -r -d %{_localstatedir}/log/nagios -G nagiocmd -g nagios nagios

	# some paths are really broken for nagios as well
	sed -i -e 's/\/usr\/local\/nagios\/etc\/htpasswd.users/\/etc\/nagios\/htpasswd.users/g' %{_sysconfdir}/httpd/conf.d/pnp4nagios.conf

	%logmsg "Detected Nagios Package, adjusted configuration to match it."
	%logmsg "(see /etc/httpd/conf.d/pnp4nagios.conf, /etc/pnp4nagios/{config.php,npcd.cfg,process_perfdata.cfg}, /etc/rc.d/init.d/npcd)."
else
	getent group icinga >/dev/null || %{_sbindir}/groupadd icinga
	getent group icingacmd >/dev/null || %{_sbindir}/groupadd icingacmd
	getent passwd icinga >/dev/null || %{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/icinga -G icingacmd -g icinga icinga

	# now fix all the paths and users
	sed -i -e 's/Nagios Access/Icinga Access/g;
		s/\/usr\/local\/nagios\/etc\/htpasswd.users/\/etc\/icinga\/passwd/g
		' %{_sysconfdir}/httpd/conf.d/pnp4nagios.conf
	sed -i -e 's/\/nagios\/cgi-bin/\/icinga\/cgi-bin/g' %{_sysconfdir}/%{name}/config.php
	sed -i -e 's/user = nagios/user = icinga/g;
		s/group = nagios/group = icinga/g;
		s/log_file = \/var\/log\/nagios\/npcd.log/log_file = \/var\/log\/icinga\/npcd.log/g;
		s/perfdata_spool_dir = \/var\/spool\/nagios/perfdata_spool_dir = \/var\/spool\/icinga\/perfdata/g
		' %{_sysconfdir}/%{name}/npcd.cfg
	sed -i -e 's/LOG_FILE = \/var\/log\/nagios\/perfdata.log/LOG_FILE = \/var\/log\/icinga\/perfdata.log/g' %{_sysconfdir}/%{name}/process_perfdata.cfg
	sed -i -e 's/USER = nagios/USER = icinga/g' %{_sysconfdir}/rc.d/init.d/pnp_gearman_worker
	sed -i -e 's/NpcdUser=nagios/NpcdUser=icinga/g;
		s/NpcdGroup=nagios/NpcdGroup=icinga/g
		' %{_sysconfdir}/rc.d/init.d/npcd

	%logmsg "Detected Icinga Package, adjusted configuration to match it."
	%logmsg "(see /etc/httpd/conf.d/pnp4nagios.conf, /etc/pnp4nagios/{config.php,npcd.cfg,process_perfdata.cfg}, /etc/rc.d/init.d/npcd)."
fi
fi



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc INSTALL
%doc README
%doc THANKS
%config(noreplace) %{_sysconfdir}/%{name}/check_commands/check_all_local_disks.cfg-sample
%config(noreplace) %{_sysconfdir}/%{name}/check_commands/check_nrpe.cfg-sample
%config(noreplace) %{_sysconfdir}/%{name}/check_commands/check_nwstat.cfg
%config(noreplace) %{_sysconfdir}/%{name}/npcd.cfg
%config(noreplace) %{_sysconfdir}/%{name}/pages/web_traffic.cfg
%config(noreplace) %{_sysconfdir}/%{name}/process_perfdata.cfg
%config(noreplace) %{_sysconfdir}/%{name}/rra.cfg
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_sysconfdir}/%{name}/background.pdf
%{_sysconfdir}/%{name}/config.php
%{_sysconfdir}/%{name}/misccommands.cfg-sample-nagios
%{_sysconfdir}/%{name}/misccommands.cfg-sample-icinga
%{_sysconfdir}/%{name}/nagios.cfg-sample
%{_sysconfdir}/%{name}/icinga.cfg-sample
%{_sysconfdir}/%{name}/pnp4nagios_release
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/npcd
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/pnp_gearman_worker
%{_bindir}/npcd
%{_libdir}/pnp4nagios/npcdmod.o
%{_libdir}/%{name}
%{_libexecdir}/check_pnp_rrds.pl
%{_libexecdir}/process_perfdata.pl
%{_libexecdir}/rrd_convert.pl
%{_libexecdir}/rrd_modify.pl
%{_datadir}/%{name}
%{_mandir}/man8/npcd.8.gz


%changelog
* Thu Apr 18 2013 David Hrbáč <david@hrbac.cz> - 0.6.21-1
- new upstream release

* Fri Feb 15 2013 Michael Friedrich <michael.friedrich@netways.de> - 0.6.19-4
- if nagios is installed, use default config, otherwise fallback to icinga
- only sed config in sysconfdir on fresh installs, upgrades are not-to-be overridden
- fix rpmlint warnings

* Thu Feb 14 2013 Michael Friedrich <michael.friedrich@netways.de> - 0.6.19-3
- fix permissions on docs (root instead of nagios)

* Fri Dec 28 2012 Michael Friedrich <michael.friedrich@netways.de> - 0.6.19-2
- add logmsg
- mv misccommands.cfg-sample to misccommands.cfg-sample-{nagios,icinga}
- create icinga.cfg-sample from nagios.cfg-sample
- fix paths for nagios/icinga packages in misccommands.cfg-sample-{nagios,icinga} and {nagios,icinga}.cfg-sample
- add detection of nagios or icinga pkg install to pre (/etc/{nagios,icinga}/{nagios,icinga}.cfg)
- if icinga pkg detected, correct all config and initscript attributes to properly match icinga
- fix location of htpasswd.users in pnp4nagios.conf for nagios
- FIXME: package detection of nagios or icinga is pretty poor, needs proper method

* Thu Oct 11 2012 David Hrbáč <david@hrbac.cz> - 0.6.19-1
- new upstream release

* Sun Jul 01 2012 David Hrbáč <david@hrbac.cz> - 0.6.18-1
- new upstream release

* Wed Apr 18 2012 David Hrbáč <david@hrbac.cz> - 0.6.17-1
- new upstream release

* Mon Feb 06 2012 Michael Friedrich <michael.friedrich@univie.ac.at> - 0.6.16-1
- Updated to version 0.6.16.
- drop (Build)Requires nagios, we can use other core(s) as well
- verify_pnp_config.pl => verify_pnp_config_v2.pl not installed anymore
- npcd.cfg and process_perfdata.cfg get now installed by make install w/o -sample suffix
- recognize new initscript for pnp_gearman_worker
- autoremove versionized config.php, we use config(noreplace)
- drop config_local.php which would override default settings
- fix npcd.8 man page prefix install

* Tue Feb 15 2011 Christoph Maser <cmr@financial.com> - 0.6.11-1
- Updated to version 0.6.11.

* Tue Aug 31 2010 Christoph Maser <cmr@financial.com> - 0.6.6-1
- Updated to version 0.6.6.

* Thu Dec 24 2009 Christoph Maser <cmr@financial.com> -	0.6.2 - 2
- add --with-perfdata-spool-dir and --with-perfdata--dir
- mark httpd-config snippet as config file

* Thu Dec 24 2009 Christoph Maser <cmr@financial.com> -	0.6.2 - 1
- Update to version 0.6.2
- Rename to pnp4nagios

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -	0.4.14 - 2
- Update to version 0.4.14

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -	0.4.13 - 2
- modify log path
- add documentation files

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -	0.4.13 - 1
- Initial package (using brain ;)

