# $Id$

# Authority: dag
# Upstream: Jerome Tournier <jerome.tournier@idealx.com>

Summary: User and group administration tools for Samba-OpenLDAP.
Name: smbldap-tools
version: 0.8.4
Release: 0
License: GPL
Group: System Environment/Base
URL: http://samba.idealx.org/index.en.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://samba.idealx.org/dist/smbldap-tools-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 5.6
Requires: perl >= 5.6, openldap, openldap-clients, samba

%description
In settings with OpenLDAP and Samba-LDAP servers, this collection is
useful to add, modify and delete users and groups, and to change
Unix and Samba passwords. In those context they replace the system
tools to manage users, groups and passwords.

%prep
%setup
%{__tar} -xvzf mkntpwd.tar.gz

%{__perl} -pi.orig -e 's| \$\(PREFIX\)/sbin/| \$(sbindir)/|' mkntpwd/Makefile
%{__perl} -pi.default -e '
		s|_SLAVELDAP_|localhost|;
		s|_MASTERLDAP_|localhost|;
		s|_SUFFIX_|dc=IDEALX,dc=org|;
		s|_USERS_|Users|;
		s|_COMPUTERS_|Computers|;
		s|_GROUPS_|Groups|;
		s|_LOGINSHELL_|/bin/bash|;
		s|_HOMEPREFIX_|/home/|;
		s|_BINDDN_|cn=Manager,\$suffix|;
		s|_BINDPW_|secret|;
		s|_PDCNAME_|PDC-SRV|;
		s|_HOMEDRIVE_|H:|;
	' smbldap_conf.pm

%build
%{__make} %{?_smp_mflags} -C mkntpwd

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%makeinstall -C mkntpwd
%{__install} -m0555 *.pl smbldap_tools.pm %{buildroot}%{_sbindir}
%{__install} -m0700 smbldap_conf.pm %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%post
#chgrp 512 %{prefix}/sbin/smbldap-useradd.pl %{prefix}/sbin/smbldap_conf.pm || echo "An error occured while changing groups of smbldap-useradd.pl and smbldap_conf.pm in /usr/local/sbin. For proper operations, please ensure that they have the same posix group as the Samba domain administrator if there's a local Samba PDC."

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING FILES INFRA README TODO
%config(noreplace) %{_sbindir}/smbldap_conf.pm
%{_sbindir}/*.pl
%{_sbindir}/mkntpwd
%{_sbindir}/smbldap_tools.pm

%changelog
* Wed Feb 11 2004 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Fri Dec 05 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Initial package. (using DAR)
