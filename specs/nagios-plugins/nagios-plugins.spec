# $Id$
# Authority: dag
# Upstream: <devel@monitoring-plugins.org>

%define revision 1

%define logmsg logger -t %{name}/rpm

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

Summary: Host/service/network monitoring program plugins for Nagios/Icinga
Name: nagios-plugins
Version: 1.5
Release: %{revision}%{?dist}
License: GPL
Group: Applications/System
URL: https://www.monitoring-plugins.org

Source: https://www.monitoring-plugins.org/download/nagios-plugins-%{version}.tar.gz
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
Nagios/Icinga package. This package should install cleanly on
almost any RPM-based system.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    bind-utils, mysql, net-snmp-utils, ntp, openldap,
    openssh-clients, openssl, postgresql-libs
    qstat, radiusclient-ng, samba-client, sendmail

%package setuid
Summary: Host/service/network monitoring program plugins for Nagios/Icinga requiring setuid
Group: Applications/System

Obsoletes: nagios-plugins-icmp <= %{version}-%{release}
Obsoletes: nagios-plugins-dhcp <= %{version}-%{release}

%description setuid
This package contains the setuid plugins necessary for use with the
Nagios/Icinga package.

%prep
%setup

%build
PATH="/sbin:%{_sbindir}:$PATH" \
%configure \
    --with-cgiurl="/nagios/cgi-bin" \
    --with-fping-command="/usr/sbin/fping"
#   --with-mysql="%{_prefix}"
#   --with-nagios-user="nagios" \
#   --with-nagios-group="nagios" \
%{__make} %{?_smp_mflags}

### Build some extra plugins
for plugin in %{extraplugins}; do
    %{__make} -C plugins check_$plugin
done

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|^MKINSTALLDIRS.*|MKINSTALLDIRS = ../mkinstalldirs|' po/Makefile
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""
%find_lang %{name}

%{__install} -m0755 plugins/check_* %{buildroot}%{_libdir}/nagios/plugins/
%{__install} -m4755 plugins-root/check_* %{buildroot}%{_libdir}/nagios/plugins/

%{__install} -Dp -m0644 plugins-scripts/utils.pm %{buildroot}%{perl_vendorlib}/utils.pm
%{__install} -Dp -m0644 plugins-scripts/utils.pm %{buildroot}%{_libdir}/nagios/plugins/plugins.pm

### Generate normal (.pyc) and optimized (.pyo) byte-compiled files.
%{__python} -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)' 
%{__python} -O -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)'


### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/nagios/plugins/*.{c,o}

%post
# check for upgrade
if [ $1 -eq 2 ]
then
        %logmsg "Warning: Upstream removed contrib plugins in release 1.5"
fi


%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
#%defattr(-, nagios, nagios, 0755)
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog CODING COPYING FAQ INSTALL LEGAL
%doc NEWS README REQUIREMENTS SUPPORT THANKS
%dir %{_libdir}/nagios/
%dir %{_libdir}/nagios/plugins/
%{_libdir}/nagios/plugins/check_apt
%{_libdir}/nagios/plugins/check_breeze
%{_libdir}/nagios/plugins/check_by_ssh
%{_libdir}/nagios/plugins/check_clamd
%{_libdir}/nagios/plugins/check_cluster
%{_libdir}/nagios/plugins/check_dbi
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
%{_libdir}/nagios/plugins/negate
%{_libdir}/nagios/plugins/plugins.pm
%{_libdir}/nagios/plugins/urlize
%{_libdir}/nagios/plugins/utils.pm
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
* Wed Jan 15 2014 <michael.friedrich@netways.de> - 1.5-1
- new upstream release 1.5
- upstream removed all plugins shipped below contrib/
- upstream removed command.cfg, BUGS
- add check_dbi

* Mon Jul 02 2012 <michael.friedrich@univie.ac.at> - 1.4.16-1
- new upstream release 1.4.16
- remove old patches, verified upstream included

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
