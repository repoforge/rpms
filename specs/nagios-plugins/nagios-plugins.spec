# $Id$

# Authority: dag

### FIXME: When using Soapbox configure has problems with defining PS_COMMAND and PS_FORMAT
# Soapbox: 0

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

%define _libexecdir %{_libdir}/nagios/plugins
%define extraplugins check_cluster check_dhcp

Summary: Host/service/network monitoring program plugins for Nagios.
Name: nagios-plugins
Version: 1.3.1
Release: 7
License: GPL
Group: Applications/System
URL: http://nagiosplug.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/nagiosplug/nagiosplug-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


AutoReq: no
#BuildRequires: nagios-devel
#BuildRequires: bind-devel (not needed for check_dns)
BuildRequires: openssl-devel, openldap-devel, mysql-devel, radiusclient-devel
BuildRequires: fping, bind-utils, ntp, samba-client, openssh-clients, qstat
BuildRequires: perl(Net::SNMP)
%{?rhfc1:BuildRequires: net-snmp-devel, net-snmp-utils, postgresql-devel}
%{?rhel3:BuildRequires: net-snmp-devel, net-snmp-utils}
%{?rh90:BuildRequires: net-snmp-devel, net-snmp-utils, postgresql-devel}
%{?rh80:BuildRequires: net-snmp-devel, net-snmp-utils, postgresql-devel}
%{?rh73:BuildRequires: ucd-snmp-devel, ucd-snmp-utils, postgresql-devel}
%{?rhel21:BuildRequires: ucd-snmp-devel, ucd-snmp-utils, postgresql-devel}
%{?rh62:BuildRequires: ucd-snmp-devel, ucd-snmp-utils, postgresql-devel}

#Requires: openldap, openssl, mysql, postgresql-libs
Requires: nagios, perl, perl(Net::SNMP), fping

%description
This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    bind, mysql, net-snmp-utils, ntp, openldap,
    openssh-clients, openssl, postgresql-libs
    qstat, radiusclient, samba-client, sendmail

%prep
%setup

### Allow non-root builds
#%{__perl} -pi.orig -e 's|^INSTALL_OPTS|#INSTALL_OPTS|' configure

### FIXME: Change to real perl and plugins location. (Please fix upstream)
find contrib -type f -exec %{__perl} -pi -e '
		s|^#!/.*bin/perl|#!%{__perl}|i;
		s|/usr/local/nagios/libexec/|%{_libdir}/nagios/plugins/|;
		s|/usr/libexec/nagios/plugins/|%{_libdir}/nagios/plugins/|;
	' {} \;

%build
%configure \
	--with-cgiurl="/nagios/cgi-bin" \
	--with-nagios-user="nagios" \
	--with-nagios-group="nagios"
%{__make} %{?_smp_mflags}

### Build some contrib plugins
for plugin in %{extraplugins}; do
	${CC:-%{__cc}} %{optflags} -o $plugin contrib/$plugin.c
	%{__rm} -f contrib/$plugin.c
done

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib/ \
			%{buildroot}%{perl_archlib} \
			%{buildroot}%{_sysconfdir}/nagios/
%{__install} -m0755 %{extraplugins} %{buildroot}%{_libdir}/nagios/plugins/
%{__install} -m0755 contrib/check* %{buildroot}%{_libdir}/nagios/plugins/contrib/
%{__install} -m0644 plugins-scripts/utils.pm %{buildroot}%{perl_archlib}
%{__install} -m0644 command.cfg %{buildroot}%{_sysconfdir}/nagios/command-plugins.cfg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, nagios, nagios, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README REQUIREMENTS command.cfg
%config(noreplace) %{_sysconfdir}/nagios/
%{_libdir}/nagios/plugins/
%{perl_archlib}

%changelog
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
