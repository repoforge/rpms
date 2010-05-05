# $Id$
# Authority: dag
# Upstream: Teemu Toivola <tst$iki,fi>

Summary: Console-based network traffic monitor
Name: vnstat
Version: 1.10
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://humdi.net/vnstat/

Source: http://humdi.net/vnstat/vnstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
vnstat is a network traffic monitor that keeps a log of daily network
traffic for the selected interface(s). vnstat is not a packet sniffer.

%prep
%setup

%{__cat} <<EOF >vnstat.sysconfig
VNSTAT_OPTIONS="-i eth0"
EOF

%{__cat} <<'EOF' >vnstat.cron
#!/bin/bash
VNSTAT_CONFIG="%{_sysconfdir}/sysconfig/%{name}"

if [ ! -r "$VNSTAT_CONFIG" ]; then
    echo "vnstat.cron: File \"$VNSTAT_CONFIG\" could not be read." >&2
    exit 1
fi

source "$VNSTAT_CONFIG"

if [ -z "$VNSTAT_OPTIONS" ]; then
    echo "vnstat.cron: Options VNSTAT_OPTIONS not defined in file \"$VNSTAT_CONFIG\"." >&2
    exit 1
fi

%{_bindir}/vnstat -u $VNSTAT_OPTIONS $@
EOF

%{__cat} <<EOF >vnstat.crond
MAILTO=root

*/5 * * * * nobody %{_sbindir}/vnstat.cron
EOF

%build
%{__make} %{?_smp_mflags} \
    CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/vnstat/
%{__install} -Dp -m0644 man/vnstat.1 %{buildroot}%{_mandir}/man1/vnstat.1
%{__install} -Dp -m0755 src/vnstat %{buildroot}%{_bindir}/vnstat
%{__install} -Dp -m0755 vnstat.cron %{buildroot}%{_sbindir}/vnstat.cron
%{__install} -Dp -m0644 vnstat.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/vnstat
%{__install} -Dp -m0644 vnstat.crond %{buildroot}%{_sysconfdir}/cron.d/vnstat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING FAQ INSTALL README
#doc cron/
%doc %{_mandir}/man1/vnstat.1*
%config(noreplace) %{_sysconfdir}/sysconfig/vnstat
%config %{_sysconfdir}/cron.d/vnstat
%{_bindir}/vnstat
%{_sbindir}/vnstat.cron

%defattr(0755, nobody, nobody, 0755)
%{_localstatedir}/lib/vnstat/

%changelog
* Wed Apr 14 2010 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Thu Apr 30 2009 Christoph Maser <cmr@financial.com> - 1.7-1
- Updated to release 1.7.

* Sun Sep 14 2008 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Sat Jul 23 2005 Dag Wieers <dag@wieers.com> - 1.4-3
- Fixed permissions of /etc/cron.d/vnstat. (Alexander Dalloz)

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.4-2
- Fixed cron job and sysv script. (Alexander Dalloz)

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
