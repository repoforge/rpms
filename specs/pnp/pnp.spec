Name:		pnp
Version: 	0.4.13	
Release:	1%{?dist}
Summary: 	PNP is not PerfParse. A Nagios perfdata graphing solution	

Group:	 	Applications/System	
License:	GPLv2
URL:		http://www.pnp4nagios.org/
Source:	 	http://downloads.sourceforge.net/pnp4nagios/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	rrdtool-devel nagios perl-rrdtool
Requires:	rrdtool	nagios perl-rrdtool

%description
NagiosPowered PNP is an addon to nagios which analyzes performance data provided by plugins and stores them automatically into RRD-databases.

%prep
%setup 


%build
sed -i -e 's/INSTALL_OPTS="-o $nagios_user -g $nagios_grp"/INSTALL_OPTS=""/' configure
sed -i -e 's/INIT_OPTS=-o root -g root/INIT_OPTS=/' scripts/Makefile.in
%configure --with-perfdata-logfile=%{_localstatedir}/log/perfdata.log \
	--sysconfdir=%{_sysconfdir}/nagios/pnp \
	--datarootdir=%{_datadir}/pnp
make %{?_smp_mflags} all


%install
rm -rf %{buildroot}
make fullinstall DESTDIR=%{buildroot}
mv %{buildroot}%{_sysconfdir}/nagios/pnp/check_commands/check_nwstat.cfg-sample %{buildroot}%{_sysconfdir}/nagios/pnp/check_commands/check_nwstat.cfg
mv %{buildroot}%{_sysconfdir}/nagios/pnp/npcd.cfg-sample %{buildroot}%{_sysconfdir}/nagios/pnp/npcd.cfg
mv %{buildroot}%{_sysconfdir}/nagios/pnp/pages/web_traffic.cfg-sample %{buildroot}%{_sysconfdir}/nagios/pnp/pages/web_traffic.cfg
mv %{buildroot}%{_sysconfdir}/nagios/pnp/process_perfdata.cfg-sample %{buildroot}%{_sysconfdir}/nagios/pnp/process_perfdata.cfg
mv %{buildroot}%{_sysconfdir}/nagios/pnp/rra.cfg-sample %{buildroot}%{_sysconfdir}/nagios/pnp/rra.cfg


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,nagios,nagios,-)
%config(noreplace) %{_sysconfdir}/nagios/pnp/check_commands/check_nwstat.cfg
%config(noreplace) %{_sysconfdir}/nagios/pnp/npcd.cfg
%config(noreplace) %{_sysconfdir}/nagios/pnp/pages/web_traffic.cfg
%config(noreplace) %{_sysconfdir}/nagios/pnp/process_perfdata.cfg
%config(noreplace) %{_sysconfdir}/nagios/pnp/rra.cfg
%{_sysconfdir}/nagios/pnp/background.pdf
%{_sysconfdir}/nagios/pnp/config.php
%{_sysconfdir}/nagios/pnp/pnp4nagios_release
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/npcd
%{_bindir}/npcd
%{_bindir}/npcdmod.o
%{_libexecdir}/check_pnp_rrds.pl
%{_libexecdir}/process_perfdata.pl
%{_datadir}/pnp


%changelog
* Mon Mar 23 2009 Christoph Maser <cmr@financial.com> -  0.4.13 - 1
- Initial package (using brain ;)

