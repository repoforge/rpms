# $Id$
# Authority: dag
# Upstream: <nagiosplug-devel$lists,sf,net>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_net_snmp 1}
%{?el2:%define _without_net_snmp 1}
%{?rh6:%define _without_net_snmp 1}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define _libexecdir %{_libdir}/nagios/plugins
%define extraplugins cluster cluster2 cpqarray hltherm ipxping logins rbl timeout uptime

Summary: Host/service/network monitoring program plugins for Nagios
Name: nagios-plugins
Version: 1.4.1
Release: 1
License: GPL
Group: Applications/System
URL: http://nagiosplug.sourceforge.net/

Source: http://dl.sf.net/nagiosplug/nagios-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

AutoReq: no
#BuildRequires: nagios-devel
#BuildRequires: bind-devel (not needed for check_dns)
BuildRequires: openssl-devel, radiusclient-devel
BuildRequires: fping, bind-utils, ntp, samba-client, openssh-clients, qstat
BuildRequires: openldap-devel, mysql-devel, postgresql-devel
BuildRequires: perl(Net::SNMP)
%{!?_without_net_snmp:BuildRequires: net-snmp-devel, net-snmp-utils}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel, ucd-snmp-utils}

#Requires: openldap, openssl, mysql, postgresql-libs
Requires: perl, perl(Net::SNMP), fping
#Requires: nagios

%description
This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    bind-utils, mysql, net-snmp-utils, ntp, openldap,
    openssh-clients, openssl, postgresql-libs
    qstat, radiusclient, samba-client, sendmail

%prep
%setup

### Allow non-root builds
%{__perl} -pi.orig -e 's|^INSTALL_OPTS|#INSTALL_OPTS|' configure

### FIXME: Change to real perl and plugins location. (Please fix upstream)
find contrib -type f -exec %{__perl} -pi -e '
		s|^#!/.*bin/perl|#!%{__perl}|i;
		s|/usr/local/nagios/libexec/|%{_libdir}/nagios/plugins/|;
		s|/usr/libexec/nagios/plugins/|%{_libdir}/nagios/plugins/|;
	' {} \;

%build
PATH="/sbin:/bin:/usr/sbin:/usr/sbin:$PATH" \
%configure \
	--with-cgiurl="/nagios/cgi-bin" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios"
%{__make} %{?_smp_mflags}

### Build some contrib plugins
for plugin in %{extraplugins}; do
	${CC:-%{__cc}} %{optflags} -I. -Iplugins/ -I%{_datadir}/gettext/ -o check_$plugin contrib/check_$plugin.c || :
done

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib/
%{__install} -m0755 contrib/check* %{buildroot}%{_libdir}/nagios/plugins/contrib/
%{__install} -m0755 check_* %{buildroot}%{_libdir}/nagios/plugins/

%{__install} -Dp -m0644 plugins-scripts/utils.pm %{buildroot}%{perl_vendorlib}/utils.pm
%{__install} -Dp -m0644 command.cfg %{buildroot}%{_sysconfdir}/nagios/command-plugins.cfg

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
#%defattr(-, nagios, nagios, 0755)
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS BUGS ChangeLog CHANGES COPYING FAQ INSTALL
%doc LEGAL NEWS README REQUIREMENTS SUPPORT THANKS command.cfg
%config(noreplace) %{_sysconfdir}/nagios/
%dir %{_libdir}/nagios/
%{_libdir}/nagios/plugins/
%{perl_vendorlib}/utils.pm

%changelog
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
