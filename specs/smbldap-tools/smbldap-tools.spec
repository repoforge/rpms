# $Id$
# Authority: dag
# Upstream: Jerome Tournier <jerome,tournier$idealx,com>

Summary: User and group administration tools for Samba-OpenLDAP
Name: smbldap-tools
Version: 0.8.7
Release: 2
License: GPL
Group: System Environment/Base
URL: http://samba.idealx.org/index.en.html

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
%{__perl} -pi.orig -e '
		s|/etc/opt/IDEALX|/etc|g;
		s|/opt/IDEALX||g;
	' Makefile smb.conf smbldap.conf doc/*.html smbldap_tools.pm

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -p -m0755 smbldap-* smbldap_tools.pm %{buildroot}%{_sbindir}
%{__install} -Dp -m0644 smbldap.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap.conf
%{__install} -Dp -m0600 smbldap_bind.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap_bind.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING FILES INFRA INSTALL README TODO
%doc configure.pl *.conf doc/html/*.html
%config(noreplace) %{_sysconfdir}/smbldap-tools/
%{_sbindir}/*

%changelog
* Wed Feb 16 2005 Dag Wieers <dag@wieers.com> - 0.8.7-2
- Fixed locations, removed /opt/IDEALX. (Alain Rykaert)

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 0.8.7-1
- Updated to release 0.8.7.

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
