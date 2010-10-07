# $Id:$
# Upstream:     pnp4nagios-devel@lists.sourceforge.net
Name:		pnp4nagios
Version:	0.6.7
Release:	1
Summary: 	PNP is not PerfParse. A Nagios perfdata graphing solution	

Group:	 	Applications/System	
License:	GPLv2
URL:		http://www.pnp4nagios.org/
Source: 	http://downloads.sourceforge.net/pnp4nagios/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	rrdtool-devel 
BuildRequires:  nagios
BuildRequires:  perl-rrdtool
Requires:	rrdtool
Requires:	nagios
Requires:	perl-rrdtool
Obsoletes:	pnp

%description
NagiosPowered PNP is an addon to nagios which analyzes performance data provided by plugins and stores them automatically into RRD-databases.

%prep
%setup 


%build
sed -i -e 's/INSTALL_OPTS="-o $nagios_user -g $nagios_grp"/INSTALL_OPTS=""/' configure
sed -i -e 's/INIT_OPTS=-o root -g root/INIT_OPTS=/' scripts/Makefile.in
%configure --with-perfdata-logfile=%{_localstatedir}/log/perfdata.log \
	--sysconfdir=%{_sysconfdir}/nagios/%{name} \
	--datarootdir=%{_datadir}/nagios/%{name} \
	--with-perfdata-dir=%{_datadir}/%{name}/perfdata \
	--with-perfdata-spool-dir=%{_localstatedir}/nagios/spool \
	--libdir=%{_libdir}/%{name}  # only kohana is installed there and maybe we have a system wide kohana already
make %{?_smp_mflags} all


%install
rm -rf %{buildroot}
%{__mkdir} -p  %{buildroot}%{_sysconfdir}/httpd/conf.d/
make fullinstall DESTDIR=%{buildroot}
mv %{buildroot}%{_sysconfdir}/nagios/%{name}/check_commands/check_nwstat.cfg-sample %{buildroot}%{_sysconfdir}/nagios/%{name}/check_commands/check_nwstat.cfg
mv %{buildroot}%{_sysconfdir}/nagios/%{name}/npcd.cfg-sample %{buildroot}%{_sysconfdir}/nagios/%{name}/npcd.cfg
mv %{buildroot}%{_sysconfdir}/nagios/%{name}/pages/web_traffic.cfg-sample %{buildroot}%{_sysconfdir}/nagios/%{name}/pages/web_traffic.cfg
mv %{buildroot}%{_sysconfdir}/nagios/%{name}/process_perfdata.cfg-sample %{buildroot}%{_sysconfdir}/nagios/%{name}/process_perfdata.cfg
mv %{buildroot}%{_sysconfdir}/nagios/%{name}/rra.cfg-sample %{buildroot}%{_sysconfdir}/nagios/%{name}/rra.cfg

sed -i -e 's*log_file = /var/npcd.log*log_file = /var/log/nagios/npcd.log*' %{buildroot}%{_sysconfdir}/nagios/%{name}/npcd.cfg

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
%config(noreplace) %{_sysconfdir}/nagios/%{name}/check_commands/check_all_local_disks.cfg-sample
%config(noreplace) %{_sysconfdir}/nagios/%{name}/check_commands/check_nrpe.cfg-sample
%config(noreplace) %{_sysconfdir}/nagios/%{name}/check_commands/check_nwstat.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{name}/npcd.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{name}/pages/web_traffic.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{name}/process_perfdata.cfg
%config(noreplace) %{_sysconfdir}/nagios/%{name}/rra.cfg
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_sysconfdir}/nagios/%{name}/background.pdf
%{_sysconfdir}/nagios/%{name}/config.php
%{_sysconfdir}/nagios/%{name}/misccommands.cfg-sample
%{_sysconfdir}/nagios/%{name}/nagios.cfg-sample
%{_sysconfdir}/nagios/%{name}/pnp4nagios_release
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/npcd
%{_bindir}/npcd
%{_libdir}/pnp4nagios/npcdmod.o
%{_libdir}/%{name}
%{_libexecdir}/check_pnp_rrds.pl
%{_libexecdir}/process_perfdata.pl
%{_libexecdir}/verify_pnp_config.pl
%{_libexecdir}/rrd_convert.pl
%{_datadir}/nagios/%{name}


%changelog
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

