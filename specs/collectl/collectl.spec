# $Id$
# Authority: dag

# Tag: test

Summary: Utility to collect Linux performance data
Name: collectl
Version: 3.1.0
Release: 1
License: GPLv2+ or Artistic
Group: Applications/System
URL: http://collectl.sourceforge.net

Source0: http://download.sourceforge.net/collectl/collectl-%{version}.src.tar.gz
Source1: collectl.initd
Source2: collectl.sysconfig
Source3: collectl.logrotate
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: chkconfig
Requires: initscripts
Requires: perl(Compress::Zlib)
Requires: perl(Sys::Syslog)
Requires: perl(Time::HiRes)

%description
collectl is a utility to collect Linux performance data.

%prep
%setup

%build
%{__cat} <<'EOF' > collectl
#!/bin/sh
cd %{_libexecdir}/collectl
exec %{__perl} collectl.pl $@
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 collectl %{buildroot}%{_bindir}/collectl
%{__install} -Dp -m0755 readS %{buildroot}%{_bindir}/readS
%{__install} -Dp -m0755 collectl.pl %{buildroot}%{_libexecdir}/collectl.pl
%{__install} -Dp -m0644 formatit.ph %{buildroot}%{_libexecdir}/collectl/formatit.ph
%{__install} -Dp -m0644 sexpr.ph %{buildroot}%{_libexecdir}/collectl/sexpr.ph
%{__install} -Dp -m0644 lexpr.ph %{buildroot}%{_libexecdir}/collectl/lexpr.ph
%{__install} -Dp -m0644 vmstat.ph %{buildroot}%{_libexecdir}/collectl/vmstat.ph
%{__install} -Dp -m0644 man1/collectl.1 %{buildroot}%{_mandir}/man1/collectl.1
%{__install} -Dp -m0644 collectl.conf %{buildroot}%{_sysconfdir}/collectl.conf
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/collectl
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/collectl
%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/collectl
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/collectl/

%post
/sbin/chkconfig --add collectl

%postun
if [ $1 -ge 1 ]; then
    /sbin/service collectl condrestart &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service collectl stop &>/dev/null || :
    /sbin/chkconfig --del collectl
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ARTISTIC COPYING GPL RELEASE-collectl docs/
%doc %{_mandir}/man1/collectl.1*
%config(noreplace) %{_sysconfdir}/collectl.conf
%config %{_initrddir}/collectl
%config(noreplace) %{_sysconfdir}/sysconfig/collectl
%config(noreplace) %{_sysconfdir}/logrotate.d/collectl
%{_bindir}/collectl
%{_bindir}/readS
%{_libexecdir}/collectl/
%{_libexecdir}/collectl.pl
%{_localstatedir}/log/collectl/

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 3.1.0-1
- Initial package. (using DAR)
