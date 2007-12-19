# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_lmsensors 1}

Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 4.2.2
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://collectd.org/

Source: http://collectd.org/files/collectd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel, rrdtool-devel
%{!?_without_lmsensors:BuildRequires: lm_sensors-devel}

Obsoletes: collectd-apache <= %{version}-%{release}
Provides: collectd-apache = %{version}-%{release}
Obsoletes: collectd-mysql <= %{version}-%{release}
Provides: collectd-mysql = %{version}-%{release}
Obsoletes: collectd-sensors <= %{version}-%{release}
Provides: collectd-sensors = %{version}-%{release}

%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if neccessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.

%prep
%setup

%{__perl} -pi.orig -e 's|-Werror||g' Makefile.in */Makefile.in

%build
### FIXME: --with-libmysql support not working
%configure \
    --disable-static \
    --with-libmysql="%{_libdir}/mysql/"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
%{__install} -Dp -m0755 contrib/fedora/init.d-collectd %{buildroot}%{_initrddir}/collectd

%{__install} -Dp -m0755 contrib/collection.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/collection.cgi

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%post
/sbin/chkconfig --add collectd

%preun
if [ $1 -eq 0 ]; then
    /sbin/service collectd stop &>/dev/null || :
    /sbin/chkconfig --del collectd
fi

%postun
/sbin/service collectd condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README contrib/
%doc %{_mandir}/man1/collectd.1*
%doc %{_mandir}/man1/collectd-nagios.1*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-email.5*
%doc %{_mandir}/man5/collectd-exec.5*
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man5/collectd-snmp.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%config(noreplace) %{_sysconfdir}/collectd.conf
%config %{_initrddir}/collectd
%{_bindir}/collectd-nagios
%{_libdir}/collectd/
%{_localstatedir}/www/cgi-bin/collection.cgi
%{_sbindir}/collectd
%dir %{_localstatedir}/lib/collectd/
%{perl_sitelib}/Collectd.pm
%{perl_sitelib}/Collectd/
%exclude %{_libdir}/collectd/*.la
%exclude %{perl_archlib}
%exclude %{perl_sitearch}

%changelog
* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 4.2.2-1
- Updated to release 4.2.2.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 4.2.1-1
- Updated to release 4.2.1.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 4.2.0-1
- Updated to release 4.2.0.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 3.11.5-1
- Initial package. (using DAR)
