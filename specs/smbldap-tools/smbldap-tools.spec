# $Id$
# Authority: dag
# Upstream: Jerome Tournier <jerome,tournier$idealx,com>

Summary: User and group administration tools for Samba-OpenLDAP
Name: smbldap-tools
Version: 0.8.6
Release: 1
License: GPL
Group: System Environment/Base
URL: http://samba.idealx.org/index.en.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://samba.idealx.org/dist/smbldap-tools-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.6
Requires: perl >= 5.6, openldap, openldap-clients, samba

BuildArch: noarch

%description
In settings with OpenLDAP and Samba-LDAP servers, this collection is
useful to add, modify and delete users and groups, and to change
Unix and Samba passwords. In those context they replace the system
tools to manage users, groups and passwords.

%prep
%setup
#%{__tar} -xvzf mkntpwd.tar.gz

#%{__perl} -pi.orig -e 's| \$\(PREFIX\)/sbin/| \$(sbindir)/|' mkntpwd/Makefile
%{__perl} -pi.orig -e 's|/usr/local/sbin|%{_sbindir}|' smb.conf smbldap.conf

%build
#%{__make} %{?_smp_mflags} -C mkntpwd

%install
%{__rm} -rf %{buildroot}
#makeinstall -C mkntpwd
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -m0755 smbldap-* smbldap_tools.pm %{buildroot}%{_sbindir}
%{__install} -D -m0644 smbldap.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap.conf
%{__install} -D -m0600 smbldap_bind.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap_bind.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING FILES INFRA INSTALL README TODO
%doc configure.pl *.conf doc/html/
%config(noreplace) %{_sysconfdir}/smbldap-tools/
%{_sbindir}/*

%changelog
* Sat Jan 22 2005 Dag Wieers <dag@wieers.com> - 0.8.6-1
- Updated to release 0.8.6.

* Sun Jun 20 2004 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Fri Dec 05 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Initial package. (using DAR)
