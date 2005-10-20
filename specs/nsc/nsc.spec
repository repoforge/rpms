# $Id$
# Authority: dag
# Upstream: Stig H. Jacobsen <nsc$gothix,dk>

Summary: Console monitor for Nagios
Name: nsc
Version: 0.71
Release: 1
License: GPL
Group: Applications/System
URL: http://www.goth.dk/nsc/

Source: http://www.goth.dk/nsc/nsc-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: nagios, perl(Curses)

%description
nsc is a curses-based console monitor for Nagios. It allows you to monitor
Nagios services without the expense or availability of a GUI.

%prep
%setup -c

%{__perl} -pi.orig -e '
		s|/usr/local/nagios/var/status.log|%{_localstatedir}/log/nagios/status.log|;
		s|/usr/local/nagios/etc/services.cfg|%{_sysconfdir}/nagios/services.cfg|;
	' nsc.pl

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nsc.pl %{buildroot}%{_sbindir}/nsc
%{__install} -Dp -m0644 nsc.1 %{buildroot}%{_mandir}/man1/nsc.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE NOTES.txt nsc.doc README.txt status.log
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 0.71-1
- Initial package. (using DAR)
