# $Id$
# Authority: dag
# Upstream: Jerome Tournier <jerome,tournier$idealx,com>

Summary: User and group administration tools for Samba-OpenLDAP
Name: smbldap-tools
Version: 0.9.5
Release: 1
License: GPL
Group: System Environment/Base
URL: http://sourceforge.net/projects/smbldap-tools/

Source: http://download.gna.org/smbldap-tools/packages/smbldap-tools-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.6
Requires: perl >= 5.6, openldap, openldap-clients, samba
#Requires: perl(XML::SAX::Base), perl(XML::NamespaceSupport)
#Requires: perl(Convert::ASN1)

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
    ' Makefile configure.pl smb.conf smbldap.conf smbldap_tools.pm doc/*.html

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 smbldap.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap.conf
%{__install} -Dp -m0600 smbldap_bind.conf %{buildroot}%{_sysconfdir}/smbldap-tools/smbldap_bind.conf
%{__install} -Dp -m0755 smbldap_tools.pm %{buildroot}%{_sbindir}/smbldap_tools.pm
for cmd in smbldap-[gpu]*; do
    %{__install} -Dp -m0755 $cmd %{buildroot}%{_sbindir}/$cmd
    pod2man --section=8 $cmd >$cmd.8
    %{__install} -Dp -m0644 $cmd.8 %{buildroot}%{_mandir}/man8/$cmd.8
done


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING FILES INFRA INSTALL README TODO
%doc *.conf configure.pl doc/migration_scripts/ doc/smbldap-*
%doc %{_mandir}/man8/smbldap-groupadd.8*
%doc %{_mandir}/man8/smbldap-groupdel.8*
%doc %{_mandir}/man8/smbldap-groupmod.8*
%doc %{_mandir}/man8/smbldap-groupshow.8*
%doc %{_mandir}/man8/smbldap-passwd.8*
%doc %{_mandir}/man8/smbldap-populate.8*
%doc %{_mandir}/man8/smbldap-useradd.8*
%doc %{_mandir}/man8/smbldap-userdel.8*
%doc %{_mandir}/man8/smbldap-usermod.8*
%doc %{_mandir}/man8/smbldap-userinfo.8*
%doc %{_mandir}/man8/smbldap-userlist.8*
%doc %{_mandir}/man8/smbldap-usershow.8*
%config(noreplace) %{_sysconfdir}/smbldap-tools/
%{_sbindir}/smbldap-groupadd
%{_sbindir}/smbldap-groupdel
%{_sbindir}/smbldap-groupmod
%{_sbindir}/smbldap-groupshow
%{_sbindir}/smbldap-passwd
%{_sbindir}/smbldap-populate
%{_sbindir}/smbldap-useradd
%{_sbindir}/smbldap-userdel
%{_sbindir}/smbldap-usermod
%{_sbindir}/smbldap-userinfo
%{_sbindir}/smbldap-userlist
%{_sbindir}/smbldap-usershow
%{_sbindir}/smbldap_tools.pm

%changelog
* Mon Jul  7 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Sat Aug 18 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Fri Aug 12 2005 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Excluded smbldap-tools.spec. (Simon Perreault)

* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.8.8-1
- Updated to release 0.8.8.

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
