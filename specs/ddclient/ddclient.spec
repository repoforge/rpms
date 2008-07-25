# $Id$
# Authority: dries

Summary: Updates dynamic DNS entries
Name: ddclient
Version: 3.7.3
Release: 2
License: GPL
Group: Applications/Internet
URL: http://ddclient.sourceforge.net/

Source: http://dl.sf.net/ddclient/ddclient-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl(IO::Socket::SSL)

%description
Ddclient is a Perl client used to update dynamic DNS entries for accounts on
Dynamic DNS Network Services' free DNS service.

DDclient is a small but full featured client requiring only Perl and no
additional modules. It runs under most UNIX OSes and has been tested under
GNU/Linux and FreeBSD. Supported features include: operating as a daemon,
manual and automatic updates, static and dynamic updates, optimized updates
for multiple addresses, MX, wildcards, abuse avoidance, retrying failed
updates, and sending update status to syslog and through e-mail.

%prep
%setup

%build
# nothing to do

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ddclient %{buildroot}%{_sbindir}/ddclient
%{__install} -Dp -m0755 sample-etc_rc.d_init.d_ddclient.redhat %{buildroot}%{_initrddir}/ddclient
%{__install} -Dp -m0600 sample-etc_ddclient.conf %{buildroot}%{_sysconfdir}/ddclient/ddclient.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/cache/ddclient

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add ddclient
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service ddclient stop &>/dev/null || :
    /sbin/chkconfig --del ddclient
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service ddclient condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING COPYRIGHT README* sample-*
%config(noreplace) %{_sysconfdir}/ddclient/
%config %{_initrddir}/ddclient
%{_sbindir}/ddclient
%dir %{_localstatedir}/cache/ddclient

%changelog
* Fri Jul 25 2008 Jim <quien-sabe@metaorg.com - 3.7.3-2
- Added step to create new required cache directory

* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.3-1
- Updated to release 3.7.3.

* Mon Feb 12 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.1-1
- Updated to release 3.7.1.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 3.7.0-2
- Added perl(IO::Socket::SSL) dependency since ssl=yes is enabled by default. (Jim Richardson)

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.7.0-1
- Updated to release 3.7.0.

* Sun Dec 18 2005 Dries Verachtert <dries@ulyssis.org> - 3.6.7-1
- Updated to release 3.6.7.

* Sun Mar 13 2005 Dries Verachtert <dries@ulyssis.org> - 3.6.5-4
- Fixed the permissions of the ddclient init script (Thanks to Stef Van Dessel)

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.5-3
- Fixed the location of ddclient.conf (Thanks to Andi Mueller)

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.5-2
- Update to release 3.6.5.

* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-2
- Install additional files fix (Thanks to Thilo Pfennig
  and Jorge I Bartos)

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-1
- Initial package.
