# $Id: $
# Authority: dries

Summary: Updates dynamic DNS entries
Name: ddclient
Version: 3.6.5
Release: 3
License: GPL
Group: Applications/Internet
URL: http://ddclient.sourceforge.net/

Source: http://dl.sf.net/ddclient/ddclient-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

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
%{__install} -D -m0755 ddclient %{buildroot}%{_sbindir}/ddclient
%{__install} -D -m0644 sample-etc_rc.d_init.d_ddclient.redhat %{buildroot}%{_sysconfdir}/rc.d/init.d/ddclient
%{__install} -D -m0644 sample-etc_ddclient.conf %{buildroot}%{_sysconfdir}/ddclient/ddclient.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT COPYING README README.cisco sample-*
%{_sbindir}/ddclient
%config(noreplace) %{_sysconfdir}/ddclient/ddclient.conf
%{_sysconfdir}/rc.d/init.d/ddclient


%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.5-3
- Fixed the location of ddclient.conf (Thanks to Andi Mueller)

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.5-2
- Update to release 3.6.5.

* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-2
- Install additional files fix (Thanks to Thilo Pfennig 
  and Jorge I Bartos)

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-1
- Initial package.
