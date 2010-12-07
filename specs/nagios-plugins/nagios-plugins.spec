# $Id$
# Authority: dag
# Upstream: <nagiosplug-devel$lists,sf,net>

%{?el5:%define _with_apt 1}

%{?el4:%define _with_apt 1}

%{?el3:%define _with_apt 1}
%{?el3:%define _without_gettextdevel 1}

%{?el2:%define _with_apt 1}
%{?el2:%define _without_gettextdevel 1}
%{?el2:%define _without_net_snmp 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define _libexecdir %{_libdir}/nagios/plugins

%define extraplugins ide_smart ldap pgsql

Summary: Host/service/network monitoring program plugins for Nagios
Name: nagios-plugins
Version: 1.4.15
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://nagiosplug.sourceforge.net/

Source: http://downloads.sourceforge.net/project/nagiosplug/nagiosplug/%{version}/nagios-plugins-%{version}.tar.gz
Patch0: nagios-plugins-1.4.3-ntpd.patch
Patch1: nagios-plugins-1.4.4-check_ide_smart.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

AutoReq: no
%{?_with_apt:BuildRequires: apt}
#BuildRequires: bind-devel (not needed for check_dns)
BuildRequires: bind-utils
BuildRequires: fping
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: mysql-devel
#BuildRequires: nagios-devel
BuildRequires: ntp
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: perl(Net::SNMP)
BuildRequires: postgresql-devel
BuildRequires: python
BuildRequires: qstat
BuildRequires: radiusclient-ng-devel
BuildRequires: samba-client
BuildRequires: %{_bindir}/mailq
%{!?_without_net_snmp:BuildRequires: net-snmp-devel, net-snmp-utils}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel, ucd-snmp-utils}
%{!?_without_gettextdevel:BuildRequires: gettext-devel}

Requires: fping
#Requires: mysql
#Requires: nagios
#Requires: openldap
#Requires: openssl
Requires: perl
Requires: perl(Net::SNMP)
#Requires: postgresql-libs

%description
This package contains the basic plugins necessary for use with the
Nagios package. This package should install cleanly on almost any
RPM-based system.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    bind-utils, mysql, net-snmp-utils, ntp, openldap,
    openssh-clients, openssl, postgresql-libs
    qstat, radiusclient-ng, samba-client, sendmail

%package setuid
Summary: Host/service/network monitoring program plugins for Nagios requiring setuid
Group: Applications/System

Obsoletes: nagios-plugins-icmp <= %{version}-%{release}
Obsoletes: nagios-plugins-dhcp <= %{version}-%{release}

%description setuid
This package contains the setuid plugins necessary for use with the
Nagios package.

%prep
%setup
%patch0 -p0
#patch1 -p1

### FIXME: Change to real perl and plugins location. (Please fix upstream)
find contrib -type f -exec %{__perl} -pi -e '
        s|^#!/.*bin/perl|#!%{__perl}|i;
        s|/usr/local/nagios/libexec/|%{_libdir}/nagios/plugins/|;
        s|/usr/libexec/nagios/plugins/|%{_libdir}/nagios/plugins/|;
    ' {} \;

%build
PATH="/sbin:%{_sbindir}:$PATH" \
%configure \
    --with-cgiurl="/nagios/cgi-bin" \
    --with-fping-command="/usr/sbin/fping"
#   --with-mysql="%{_prefix}"
#   --with-nagios-user="nagios" \
#   --with-nagios-group="nagios" \
%{__make} %{?_smp_mflags}

### Build some extra and contrib plugins
for plugin in %{extraplugins}; do
    %{__make} -C plugins check_$plugin
done

for plugin in contrib/*.c; do
    ${CC:-%{__cc}} %{optflags} -I. -Iplugins/ -I%{_datadir}/gettext/ -o ${plugin%.c} $plugin || :
done

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|^MKINSTALLDIRS.*|MKINSTALLDIRS = ../mkinstalldirs|' po/Makefile
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib/
%{__install} -m0755 plugins/check_* %{buildroot}%{_libdir}/nagios/plugins/
%{__install} -m4755 plugins-root/check_* %{buildroot}%{_libdir}/nagios/plugins/
%{__install} -m0755 contrib/check_* %{buildroot}%{_libdir}/nagios/plugins/contrib/

%{__install} -Dp -m0644 plugins-scripts/utils.pm %{buildroot}%{perl_vendorlib}/utils.pm
%{__install} -Dp -m0644 plugins-scripts/utils.pm %{buildroot}%{_libdir}/nagios/plugins/plugins.pm
%{__install} -Dp -m0644 contrib/utils.py %{buildroot}%{_libdir}/nagios/plugins/utils.py

%{__install} -Dp -m0644 command.cfg %{buildroot}%{_sysconfdir}/nagios/command-plugins.cfg

### Generate normal (.pyc) and optimized (.pyo) byte-compiled files.
%{__python} -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)' 
%{__python} -O -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)'


### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/nagios/plugins/*.{c,o}
%{__rm} -f %{buildroot}%{_libdir}/nagios/plugins/contrib/*.orig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
#%defattr(-, nagios, nagios, 0755)
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS BUGS ChangeLog CODING COPYING FAQ INSTALL LEGAL
%doc NEWS README REQUIREMENTS SUPPORT THANKS command.cfg
%config(noreplace) %{_sysconfdir}/nagios/
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/plugins/
%{_libdir}/nagios/plugins/check_apt
%{_libdir}/nagios/plugins/check_breeze
%{_libdir}/nagios/plugins/check_by_ssh
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_cluster
%{_libdir}/nagios/plugins/check_dig
%{_libdir}/nagios/plugins/check_disk
%{_libdir}/nagios/plugins/check_disk_smb
%{_libdir}/nagios/plugins/check_dns
%{_libdir}/nagios/plugins/check_dummy
%{_libdir}/nagios/plugins/check_file_age
%{_libdir}/nagios/plugins/check_flexlm
%{_libdir}/nagios/plugins/check_fping
%{_libdir}/nagios/plugins/check_ftp
%{_libdir}/nagios/plugins/check_game
%{_libdir}/nagios/plugins/check_hpjd
%{_libdir}/nagios/plugins/check_http
%{_libdir}/nagios/plugins/check_ide_smart
%{_libdir}/nagios/plugins/check_ifoperstatus
%{_libdir}/nagios/plugins/check_ifstatus
%{_libdir}/nagios/plugins/check_imap
%{_libdir}/nagios/plugins/check_ircd
%{_libdir}/nagios/plugins/check_jabber
%{_libdir}/nagios/plugins/check_ldap
%{_libdir}/nagios/plugins/check_ldaps
%{_libdir}/nagios/plugins/check_load
%{_libdir}/nagios/plugins/check_log
%{_libdir}/nagios/plugins/check_mailq
%{_libdir}/nagios/plugins/check_mrtg
%{_libdir}/nagios/plugins/check_mrtgtraf
%{_libdir}/nagios/plugins/check_mysql
%{_libdir}/nagios/plugins/check_mysql_query
%{_libdir}/nagios/plugins/check_nagios
%{_libdir}/nagios/plugins/check_nntp
%{_libdir}/nagios/plugins/check_nntps
%{_libdir}/nagios/plugins/check_nt
%{_libdir}/nagios/plugins/check_ntp
%{_libdir}/nagios/plugins/check_ntp_peer
%{_libdir}/nagios/plugins/check_ntp_time
%{_libdir}/nagios/plugins/check_nwstat
%{_libdir}/nagios/plugins/check_oracle
%{_libdir}/nagios/plugins/check_overcr
%{_libdir}/nagios/plugins/check_pgsql
%{_libdir}/nagios/plugins/check_ping
%{_libdir}/nagios/plugins/check_pop
%{_libdir}/nagios/plugins/check_procs
%{_libdir}/nagios/plugins/check_radius
%{_libdir}/nagios/plugins/check_real
%{_libdir}/nagios/plugins/check_rpc
%{_libdir}/nagios/plugins/check_sensors
%{_libdir}/nagios/plugins/check_simap
%{_libdir}/nagios/plugins/check_smtp
%{_libdir}/nagios/plugins/check_snmp
%{_libdir}/nagios/plugins/check_spop
%{_libdir}/nagios/plugins/check_ssh
%{_libdir}/nagios/plugins/check_ssmtp
%{_libdir}/nagios/plugins/check_swap
%{_libdir}/nagios/plugins/check_tcp
%{_libdir}/nagios/plugins/check_time
%{_libdir}/nagios/plugins/check_udp
%{_libdir}/nagios/plugins/check_ups
%{_libdir}/nagios/plugins/check_users
%{_libdir}/nagios/plugins/check_wave
%dir %{_libdir}/nagios/plugins/contrib/
%{_libdir}/nagios/plugins/contrib/check_adptraid.sh
%{_libdir}/nagios/plugins/contrib/check_apache.pl
%{_libdir}/nagios/plugins/contrib/check_apc_ups.pl
%{_libdir}/nagios/plugins/contrib/check_appletalk.pl
%{_libdir}/nagios/plugins/contrib/check_arping.pl
%{_libdir}/nagios/plugins/contrib/check_asterisk.pl
%{_libdir}/nagios/plugins/contrib/check_axis.sh
%{_libdir}/nagios/plugins/contrib/check_backup.pl
%{_libdir}/nagios/plugins/contrib/check_bgpstate.pl
%{_libdir}/nagios/plugins/contrib/check_breeze.pl
%{_libdir}/nagios/plugins/contrib/check_cluster
%{_libdir}/nagios/plugins/contrib/check_cluster.c
%{_libdir}/nagios/plugins/contrib/check_cluster2
%{_libdir}/nagios/plugins/contrib/check_cluster2.README
%{_libdir}/nagios/plugins/contrib/check_cluster2.c
%{_libdir}/nagios/plugins/contrib/check_compaq_insight.pl
%{_libdir}/nagios/plugins/contrib/check_cpqarray.c
%{_libdir}/nagios/plugins/contrib/check_digitemp.pl
%{_libdir}/nagios/plugins/contrib/check_dlswcircuit.pl
%{_libdir}/nagios/plugins/contrib/check_dns_random.pl
%{_libdir}/nagios/plugins/contrib/check_email_loop.pl
%{_libdir}/nagios/plugins/contrib/check_fan_cpq_present
%{_libdir}/nagios/plugins/contrib/check_fan_fsc_present
%{_libdir}/nagios/plugins/contrib/check_flexlm.pl
%{_libdir}/nagios/plugins/contrib/check_frontpage
%{_libdir}/nagios/plugins/contrib/check_hltherm.c
%{_libdir}/nagios/plugins/contrib/check_hprsc.pl
%{_libdir}/nagios/plugins/contrib/check_http-with-client-certificate.c
%{_libdir}/nagios/plugins/contrib/check_hw.sh
%{_libdir}/nagios/plugins/contrib/check_ica_master_browser.pl
%{_libdir}/nagios/plugins/contrib/check_ica_metaframe_pub_apps.pl
%{_libdir}/nagios/plugins/contrib/check_ica_program_neigbourhood.pl
%{_libdir}/nagios/plugins/contrib/check_inodes-freebsd.pl
%{_libdir}/nagios/plugins/contrib/check_inodes.pl
%{_libdir}/nagios/plugins/contrib/check_ipxping.c
%{_libdir}/nagios/plugins/contrib/check_javaproc.pl
%{_libdir}/nagios/plugins/contrib/check_joy.sh
%{_libdir}/nagios/plugins/contrib/check_linux_raid.pl
%{_libdir}/nagios/plugins/contrib/check_lmmon.pl
%{_libdir}/nagios/plugins/contrib/check_log2.pl
%{_libdir}/nagios/plugins/contrib/check_lotus.pl
%{_libdir}/nagios/plugins/contrib/check_maxchannels.pl
%{_libdir}/nagios/plugins/contrib/check_maxwanstate.pl
%{_libdir}/nagios/plugins/contrib/check_mem.pl
%{_libdir}/nagios/plugins/contrib/check_ms_spooler.pl
%{_libdir}/nagios/plugins/contrib/check_mssql.sh
%{_libdir}/nagios/plugins/contrib/check_nagios.pl
%{_libdir}/nagios/plugins/contrib/check_nagios_db.pl
%{_libdir}/nagios/plugins/contrib/check_nagios_db_pg.pl
%{_libdir}/nagios/plugins/contrib/check_netapp.pl
%{_libdir}/nagios/plugins/contrib/check_nmap.py
%{_libdir}/nagios/plugins/contrib/check_nmap.pyc
%ghost %{_libdir}/nagios/plugins/contrib/check_nmap.pyo
%{_libdir}/nagios/plugins/contrib/check_ora_table_space.pl
%{_libdir}/nagios/plugins/contrib/check_oracle_instance.pl
%{_libdir}/nagios/plugins/contrib/check_oracle_tbs
%{_libdir}/nagios/plugins/contrib/check_pcpmetric.py
%{_libdir}/nagios/plugins/contrib/check_pcpmetric.pyc
%ghost %{_libdir}/nagios/plugins/contrib/check_pcpmetric.pyo
%{_libdir}/nagios/plugins/contrib/check_pfstate
%{_libdir}/nagios/plugins/contrib/check_qmailq.pl
%{_libdir}/nagios/plugins/contrib/check_rbl.c
%{_libdir}/nagios/plugins/contrib/check_remote_nagios_status.pl
%{_libdir}/nagios/plugins/contrib/check_rrd_data.pl
%{_libdir}/nagios/plugins/contrib/check_sap.sh
%{_libdir}/nagios/plugins/contrib/check_smart.pl
%{_libdir}/nagios/plugins/contrib/check_smb.sh
%{_libdir}/nagios/plugins/contrib/check_snmp_disk_monitor.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_printer.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_process_monitor.pl
%{_libdir}/nagios/plugins/contrib/check_snmp_procs.pl
%{_libdir}/nagios/plugins/contrib/check_sockets.pl
%{_libdir}/nagios/plugins/contrib/check_temp_cpq
%{_libdir}/nagios/plugins/contrib/check_temp_fsc
%{_libdir}/nagios/plugins/contrib/check_timeout
%{_libdir}/nagios/plugins/contrib/check_timeout.c
%{_libdir}/nagios/plugins/contrib/check_traceroute-pure_perl.pl
%{_libdir}/nagios/plugins/contrib/check_traceroute.pl
%{_libdir}/nagios/plugins/contrib/check_uptime.c
%{_libdir}/nagios/plugins/contrib/check_vcs.pl
%{_libdir}/nagios/plugins/contrib/check_wave.pl
%{_libdir}/nagios/plugins/contrib/check_wins.pl
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/plugins.pm
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
%{_libdir}/nagios/plugins/utils.py
%{_libdir}/nagios/plugins/utils.pyc
%ghost %{_libdir}/nagios/plugins/utils.pyo
%{_libdir}/nagios/plugins/utils.sh
%{perl_vendorlib}/utils.pm
%exclude %{_libdir}/nagios/plugins/check_dhcp
%exclude %{_libdir}/nagios/plugins/check_icmp

%files setuid
%defattr(4755, root, root, 0755)
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/plugins/
%{_libdir}/nagios/plugins/check_dhcp
%{_libdir}/nagios/plugins/check_icmp

%changelog
* Fri Nov 26 2010 Dag Wieers <dag@wieers.com> - 14.15-2
- Rebuild against radiusclient-ng 0.5.6.

* Thu Sep 16 2010 Christoph Maser <cmaser@gmx.de> - 1.4.15-1
- Updated to version 1.4.15.

* Tue Apr 06 2010 Dag Wieers <dag@wieers.com> - 1.4.14-1
- Updated to release 1.4.14.

* Mon Dec 29 2008 Christoph Maser <cmr@financial.com> - 1.4.13-1
- Updated to release 1.4.13.

* Thu Jul 24 2008 Christoph Maser <cmr@financial.com> - 1.4.12-1
- Updated to release 1.4.12.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 1.4.11-1
- Updated to release 1.4.11.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 1.4.9-1
- Updated to release 1.4.9.

* Fri Apr 20 2007 Dag Wieers <dag@wieers.com> - 1.4.8-2
- Restored utils.pm in %%{perl_vendorlib}. (Nathan Grennan)

* Wed Apr 18 2007 Dag Wieers <dag@wieers.com> - 1.4.8-1
- Updated to release 1.4.8.

* Wed Mar 14 2007 Dag Wieers <dag@wieers.com> - 1.4.6-1
- Updated to release 1.4.6.

* Tue Dec 12 2006 Dag Wieers <dag@wieers.com> - 1.4.5-1
- Updated to release 1.4.5.
- Added setuid sub-package for setuid plugins. (Philip Chase)

* Wed Nov 01 2006 Dag Wieers <dag@wieers.com> - 1.4.4-1
- Updated to release 1.4.4.
- Fixed the problem where --with-pgsql defaults to 'yes'. (Jason Kim)

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4.3.

* Tue Mar 07 2006 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Updated to release 1.4.2.

* Fri Aug 05 2005 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 1.4-2
- Fixed setuid bit for ping and fping.
- Added /sbin and /usr/sbin to $PATH.
- Updated to release 1.4.

* Tue Apr 27 2004 Dag Wieers <dag@wieers.com> - 1.3.1-10
- Everything owned by user root. (James Wilkinson)

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 1.3.1-9
- Removed nagios requirement (for nrpe). (James Wilkinson)

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 1.3.1-8
- Added postgresql plugins for RHEL3.

* Mon Mar 01 2004 Dag Wieers <dag@wieers.com> - 1.3.1-7
- Added net-snmp-utils as a BuildRequires. (Dan Tucny)

* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 1.3.1-6
- Changed BuildRequires to allow building for RHEL.

* Tue Oct 14 2003 Dag Wieers <dag@wieers.com> - 1.3.1-5
- Fixed a problem with check_ping on RH80. (Tom Diehl)
- With user nagios and group nagios. (Tom Diehl)
- Added commands-plugins.cfg.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 1.3.1-4
- Added check_game.

* Sat Oct 04 2003 Dag Wieers <dag@wieers.com> - 1.3.1-3
- Fixed build environment /etc/mtab for check_disk command.

* Mon Aug 18 2003 Dag Wieers <dag@wieers.com> - 1.3.1-2
- Added check_cluster and check_dhcp.
- Moved the needed perl module to perl include path.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Fixed paths of some scripts.
- Updated to release 1.3.1.

* Fri Apr 18 2003 Dag Wieers <dag@wieers.com> - 1.3.0-0
- Updated to release 1.3.0.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 1.2.93-0
- Updated to release 1.3.0-beta3.
- Initial package. (using DAR)
