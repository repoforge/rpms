# $Id$
# Authority: dries

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Scan logfiles and ban ip addresses with too many password failures
Name: fail2ban
Version: 0.8.2
Release: 3%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://fail2ban.sourceforge.net/

Source: http://dl.sf.net/fail2ban/fail2ban-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: dos2unix
BuildRequires: python-devel >= 2.3, python-devel
Requires: gamin-python
Requires: iptables
Requires: python
Requires: tcp_wrappers

%description
Fail2Ban monitors log files like /var/log/pwdfail or /var/log/apache/error_log
and bans failure-prone addresses. It updates firewall rules to reject the IP
address or executes user defined commands.

%prep
%setup
%{__perl} -pi -e 's|^# chkconfig:.+$|# chkconfig: 345 92 08|' files/redhat-initd
%{__perl} -pi -e 's|/tmp/fail2ban.sock|/var/run/fail2ban/fail2ban.sock|g;' files/redhat-initd

%{__cat} <<EOF >fail2ban.logrotate
/var/log/fail2ban.log {
    missingok
    notifempty
    size 30k
    create 0600 root root
    postrotate
        /usr/bin/fail2ban-client reload 2> /dev/null || true
    endscript
}
EOF

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__install} -Dp -m0755 files/redhat-initd %{buildroot}%{_initrddir}/fail2ban
%{__install} -Dp -m0644 fail2ban.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/fail2ban
%{__install} -Dp -m0644 man/fail2ban-client.1 %{buildroot}%{_mandir}/man1/fail2ban-client.1
%{__install} -Dp -m0644 man/fail2ban-regex.1 %{buildroot}%{_mandir}/man1/fail2ban-regex.1
%{__install} -Dp -m0644 man/fail2ban-server.1 %{buildroot}%{_mandir}/man1/fail2ban-server.1
%{__install} -d %{buildroot}%{_var}/run/fail2ban

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add fail2ban
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service fail2ban stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del fail2ban
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service fail2ban condrestart >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_mandir}/man1/fail2ban-client.1*
%doc %{_mandir}/man1/fail2ban-regex.1*
%doc %{_mandir}/man1/fail2ban-server.1*
%config(noreplace) %{_sysconfdir}/fail2ban/
%config(noreplace) %{_sysconfdir}/logrotate.d/fail2ban
%config %{_initrddir}/fail2ban
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-regex
%{_bindir}/fail2ban-server
%{_datadir}/fail2ban/
%dir %{_var}/run/fail2ban

%changelog
* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 0.8.2-3
- Fix group.

* Sat Apr 12 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.2-2
- Fix location of fail2ban.sock file in init script, thanks to John Thomas.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.
- Python requirement changed from 2.4 to 2.3.

* Mon Dec 31 2007 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.
- Incorporated appropriate changes from fedora SPEC.

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Initial package.
