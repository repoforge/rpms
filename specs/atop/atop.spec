# $Id$
# Authority: dag

%define logmsg logger -t %{name}/rpm

Summary: AT Computing System and Process Monitor
Name: atop
Version: 1.14
Release: 1
License: GPL
Group: Applications/System
URL: ftp://ftp.atcomputing.nl/pub/tools/linux/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.atcomputing.nl/pub/tools/linux/atop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, ncurses-devel

%description
The program atop is an interactive monitor to view the load on
a Linux-system. It shows the occupation of the most critical
hardware-resources (from a performance point of view) on system-level,
i.e. cpu, memory, disk and network. It also shows which processes are
responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).

The program atop can also be used to log system- and process-level
information in raw format for long-term analysis.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m0755 atop %{buildroot}%{_bindir}/atop
%{__install} -D -m0644 man/atop.1 %{buildroot}%{_mandir}/man1/atop.1

%{__install} -D -m0755 atop.init %{buildroot}%{_initrddir}/atop
%{__install} -D -m0644 atop.cron %{buildroot}%{_sysconfdir}/cron.d/atop
%{__install} -D -m0711 atop.daily %{buildroot}%{_sysconfdir}/atop/atop.daily
%{__install} -D -m0711 atop.24hours %{buildroot}%{_sysconfdir}/atop/atop.24hours

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/atop

%clean
%{__rm} -rf %{buildroot}

%preun
if [ $1 -eq 0 ]; then
	killall atop &>/dev/null || :
	/sbin/chkconfig --del atop
fi

%post
/sbin/chkconfig --add atop

if [ -f /etc/logrotate.d/psacct ]; then
	> /tmp/atop.timeref

	ACCTFILE="$(awk '$2 == "{" {print $1}' /etc/logrotate.d/psacct)"

	if [ -f "$ACCTFILE" -a "$ACCTFILE" -nt /tmp/atop.timeref ]; then
		rm -f /etc/cron.d/atop
		%logmsg 'Install provisions for automatic daily logging manually'
		%logmsg '(see section RAW DATA STORAGE in man-page) ....'
	else
		/etc/atop/atop.daily
		%logmsg 'Automatic daily logging is activated ...'
	fi
	rm -f /tmp/atop.timeref
else
	/etc/atop/atop.daily
	logmsg 'Automatic daily logging is activated ...'
fi

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/atop.1*
%config(noreplace) %{_sysconfdir}/atop/
%config(noreplace) %{_sysconfdir}/cron.d/atop
%config %{_initrddir}/atop
%{_bindir}/atop

%changelog
* Wed Dec 22 2004 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
