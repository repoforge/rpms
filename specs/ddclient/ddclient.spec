# $Id: $

# Authority: dries

Summary: Updates dynamic DNS entries
Name: ddclient
Version: 3.6.5
Release: 2
License: GPL
Group: Applications/Internet
URL: http://ddclient.sourceforge.net/

BuildArch: noarch

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/ddclient/ddclient-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__install} -D sample-etc_rc.d_init.d_ddclient.redhat %{buildroot}%{_sysconfdir}/rc.d/init.d/ddclient
%{__install} -D sample-etc_ddclient.conf %{buildroot}%{_sysconfdir}/ddclient.conf
%{__install} -D ddclient %{buildroot}%{_sbindir}/ddclient

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT COPYING README README.cisco sample-*
%{_sbindir}/ddclient
%config(noreplace) %{_sysconfdir}/ddclient.conf
%{_sysconfdir}/rc.d/init.d/ddclient


%changelog
* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.5-1
- Update to release 3.6.5.

* Sun Dec 05 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-2
- Install additional files.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.4-1
- Initial package.
