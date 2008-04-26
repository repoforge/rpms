# $Id$
# Authority: dag

%define logmsg logger -t %{name}/rpm

Summary: AT Computing System and Process Monitor
Name: atop
Version: 1.23
Release: 1
License: GPL
Group: Applications/System
URL: ftp://ftp.atcomputing.nl/pub/tools/linux/

Source: http://www.atconsultancy.nl/atop/packages/atop-%{version}.tar.gz
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
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 atop %{buildroot}%{_bindir}/atop
%{__install} -Dp -m0644 man/atop.1 %{buildroot}%{_mandir}/man1/atop.1

%{__install} -Dp -m0755 atop.init %{buildroot}%{_initrddir}/atop
%{__install} -Dp -m0644 atop.cron %{buildroot}%{_sysconfdir}/cron.d/atop
%{__install} -Dp -m0711 atop.daily %{buildroot}%{_sysconfdir}/atop/atop.daily
#%{__install} -Dp -m0711 atop.24hours %{buildroot}%{_sysconfdir}/atop/atop.24hours

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
%doc COPYING README
%doc %{_mandir}/man1/atop.1*
%config(noreplace) %{_sysconfdir}/atop/
%config(noreplace) %{_sysconfdir}/cron.d/atop
%config %{_initrddir}/atop
%{_bindir}/atop
%dir %{_localstatedir}/log/atop/

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Fri Aug 24 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Thu Jan 18 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Thu Nov 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 1.16-1
- Updated to release 1.16.

* Sat May 20 2006 Dag Wieers <dag@wieers.com> - 1.15-2
- Added missing %%{_localstatedir}/log/atop/. (Jose J. Garcia)

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Wed Dec 22 2004 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
