# $Id$
# Authority: dries

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Scan logfiles and ban ip addresses with too many password failures
Name: fail2ban
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/System
URL: http://fail2ban.sourceforge.net/

Source: http://dl.sf.net/fail2ban/fail2ban-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, dos2unix
Requires: python

%description
Fail2Ban monitors log files like /var/log/pwdfail or /var/log/apache/error_log
and bans failure-prone addresses. It updates firewall rules to reject the IP
address or executes user defined commands.

%prep
%setup
%{__perl} -pi -e "s|# chkconfig: 345 |# chkconfig: - |g;" config/redhat-initd
dos2unix config/redhat-initd

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__install} -D -m0600 config/fail2ban.conf.iptables %{buildroot}%{_sysconfdir}/fail2ban.conf
%{__install} -D -m0755 config/redhat-initd %{buildroot}%{_initrddir}/fail2ban
%{__install} -D -m0644 man/fail2ban.conf.5 %{buildroot}%{_mandir}/man5/fail2ban.conf.5
%{__install} -D -m0644 man/fail2ban.8 %{buildroot}%{_mandir}/man8/fail2ban.8

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
%doc CHANGELOG README TODO
%doc %{_mandir}/man5/fail2ban.conf.5*
%doc %{_mandir}/man8/fail2ban.8*
%config(noreplace) %{_sysconfdir}/fail2ban.conf
%config %{_initrddir}/fail2ban
%{_bindir}/fail2ban
%{_libdir}/fail2ban/

%changelog
* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Initial package.
