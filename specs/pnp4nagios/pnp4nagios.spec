# $Id:$
# Upstream:     pnp4nagios-devel@lists.sourceforge.net
Name:		pnp4nagios
Version: 	0.6.19
Release:	1
Summary: 	PNP is not PerfParse. A Nagios/Icinga perfdata graphing solution

Group:	 	Applications/System
License:	GPLv2
URL:		http://www.pnp4nagios.org/
Source: 	http://downloads.sourceforge.net/pnp4nagios/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	rrdtool-devel
BuildRequires:  perl-rrdtool
Requires:	rrdtool
Requires:	perl-rrdtool
Obsoletes:	pnp

%description
PNP is an addon to Nagios/Icinga which analyzes performance data provided by plugins and stores them automatically into RRD-databases.

%prep
%setup


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

# drop local versioning, we already provide our own upgrade safety
rm -f %{buildroot}%{_sysconfdir}/%{name}/config.php.%{version}
rm -f %{buildroot}%{_sysconfdir}/%{name}/config_local.php


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,nagios,nagios,-)
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
%{_sysconfdir}/%{name}/misccommands.cfg-sample
%{_sysconfdir}/%{name}/nagios.cfg-sample
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

* Thu Dec 24 2009 Christoph Maser <cmr@financial.com> -  0.6.2 - 2
- add --with-perfdata-spool-dir and --with-perfdata--dir
- mark httpd-config snippet as config file

* Thu Dec 24 2009 Christoph Maser <cmr@financial.com> -  0.6.2 - 1
- Update to version 0.6.2
- Rename to pnp4nagios

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -  0.4.14 - 2
- Update to version 0.4.14

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -  0.4.13 - 2
- modify log path
- add documentation files

* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -  0.4.13 - 1
- Initial package (using brain ;)

