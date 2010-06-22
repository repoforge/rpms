# $Id$
# Authority: dag
# Tag: test
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`%{__perl} -V:archlib`"; echo $archlib)

%{?el3:%define _without_lmsensors 1}

Summary: Statistics collection daemon for filling RRD files
Name: collectd
Version: 4.10.0
Release: 3%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://collectd.org/

Source: http://collectd.org/files/collectd-%{version}.tar.bz2
Source1: php-collection.conf
Source2: collection3.conf
Patch1: %{name}-4.10.0-configure-OpenIPMI.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: krb5-libs
Requires: curl
Requires: libpcap
Requires: libxml2
Requires: zlib
BuildRequires: krb5-devel
BuildRequires: curl-devel
BuildRequires: libpcap-devel
BuildRequires: libxml2-devel
BuildRequires: python-devel
BuildRequires: zlib-devel
BuildRequires: perl
BuildRequires: which

%{!?_without_lmsensors:BuildRequires: lm_sensors-devel}

Obsoletes: collectd-apache <= %{version}-%{release}
Provides: collectd-apache = %{version}-%{release}
Obsoletes: collectd-sensors <= %{version}-%{release}
Provides: collectd-sensors = %{version}-%{release}

%filter_provides_in %{_docdir} 
%filter_requires_in %{_docdir}
%filter_setup

%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if neccessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package dbi
Summary: dbi plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: libdbi
BuildRequires: libdbi-devel
%description dbi
The DBI plugin uses libdbi, a database abstraction library, to execute SQL statements on a database and read back the result.

%package collection3
Summary: collect perl webfrontent
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: httpd
Requires: perl(Config::General)
Requires: perl(Regexp::Common)
Requires: perl(HTML::Entities)
Requires: perl(RRDs)
%description collection3
collection3 is a graphing front-end for the RRD files created by and filled
with collectd. It is written in Perl and should be run as an CGI-script.
Graphs are generated on-the-fly, so no cron job or similar is necessary.

%package php-collection
Summary: collect php webfrontent
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: httpd
Requires: php
Requires: php-rrdtool
%description php-collection
PHP graphing frontend for RRD files created by and filled with collectd.

%package postgresql
Summary: postgresql plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: postgresql-libs
BuildRequires: postgresql-devel
%description postgresql
The PostgreSQL plugin connects to and executes SQL statements on a PostgreSQL database.

%package libvirt
Summary: libvirt plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: libvirt
Requires: OpenIPMI
BuildRequires: libvirt-devel
BuildRequires: OpenIPMI-devel
BuildRequires: OpenIPMI-libs
%description libvirt
The libvirt plugin uses the virtualization API libvirt, created by RedHat's Emerging Technology group, to gather statistics about virtualized guests on a system.

%package mysql
Summary: xmms plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: mylsq
BuildRequires: mysql-devel
%description mysql
This plugin collects status variable data from mysql

%package notify_desktop
Summary: notify_desktop plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: gtk2
Requires: libnotify
BuildRequires: gtk2-devel
BuildRequires: libnotify-devel
%description notify_desktop
The Notify Desktop plugin uses libnotify to display notifications to the user via the desktop notification specification, i. e. on an X display. 

%package -n perl-Collectd
Summary: Perl bindings for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: perl
%description -n perl-Collectd
This package contains Perl bindings and plugin for collectd. 

%package rrdtool
Summary: xmms plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: rrdtool
Requires: perl-rrdtool
BuildRequires: rrdtool-devel
%description rrdtool
The RRDtool plugin writes values to RRD-files using librrd.

%package snmp
Summary: snmp plugin for collectd
Group: System Environment/Daemons
Requires: collectd = %{version}-%{release}
Requires: net-snmp-libs
BuildRequires: net-snmp-devel
%description snmp
The SNMP plugin uses the Net-SNMP library to read values from network devices using the Simple Network Management Protocol (SNMP). 

%package xmms
Summary: xmms plugin for collectd
Group: System Environment/Daemons
BuildRequires: xmms-devel
Requires: collectd = %{version}-%{release}
Requires: xmms
%description xmms
This plugin collects bit-rate and sampling rate as you play songs


%prep
%setup
%patch1 -p0

%{__perl} -pi.orig -e 's|-Werror||g' Makefile.in */Makefile.in

# Disable Loading of modules in sub-packages
sed -i -e 's/@LOAD_PLUGIN_RRDTOOL@LoadPlugin rrdtool/#@LOAD_PLUGIN_RRDTOOL@LoadPlugin rrdtool/' src/collectd.conf.in

%build
### FIXME: --with-libmysql support not working
%configure \
    --enable-static=no \
    --enable-libvirt \
    --with-libmysql="%{_libdir}/mysql/" \
    --with-perl-bindings=INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir} -p  %{buildroot}/%{_sysconfdir}/collectd.d

%{__install} -Dp -m0644 src/collectd.conf %{buildroot}%{_sysconfdir}/collectd.conf
%{__install} -Dp -m0755 contrib/fedora/init.d-collectd %{buildroot}%{_initrddir}/collectd

%{__mkdir} -p  %{buildroot}/%{_sysconfdir}/httpd/conf.d
%{__mkdir} -p %{buildroot}%{_localstatedir}/www

%{__cp} -a contrib/php-collection  %{buildroot}%{_localstatedir}/www
%{__cp} -a %{SOURCE1}  %{buildroot}/%{_sysconfdir}/httpd/conf.d/

%{__cp} -a contrib/collection3  %{buildroot}%{_localstatedir}/www
%{__cp} -a %{SOURCE2}  %{buildroot}/%{_sysconfdir}/httpd/conf.d/


%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/collectd/

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%{__rm} -f %{buildroot}/%{perl_vendorarch}/auto/Collectd/.packlist
%{__rm} -f %{buildroot}/%{perl_archlib}/perllocal.pod

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
%doc %{_mandir}/man1/collectdmon.1*
%doc %{_mandir}/man1/collectd-nagios.1*
%doc %{_mandir}/man5/collectd.conf.5*
%doc %{_mandir}/man5/collectd-email.5*
%doc %{_mandir}/man5/collectd-exec.5*
%doc %{_mandir}/man5/collectd-java.5*
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man5/collectd-python.5*
%doc %{_mandir}/man5/collectd-snmp.5*
%doc %{_mandir}/man5/collectd-unixsock.5*
%doc %{_mandir}/man5/types.db.5*
%config(noreplace) %{_sysconfdir}/collectd.conf
%dir %{_sysconfdir}/collectd.d
%config %{_initrddir}/collectd
%{_bindir}/collectd-nagios
%{_datadir}/collectd/
%dir %{_libdir}/collectd/
%{_libdir}/collectd/apache.so
%{_libdir}/collectd/apcups.so
%{_libdir}/collectd/ascent.so
%{_libdir}/collectd/battery.so
%{_libdir}/collectd/bind.so
%{_libdir}/collectd/conntrack.so
%{_libdir}/collectd/contextswitch.so
%{_libdir}/collectd/cpu.so
%{_libdir}/collectd/cpufreq.so
%{_libdir}/collectd/csv.so
%{_libdir}/collectd/curl.so
%{_libdir}/collectd/curl_xml.so
%{_libdir}/collectd/df.so
%{_libdir}/collectd/disk.so
%{_libdir}/collectd/dns.so
%{_libdir}/collectd/email.so
%{_libdir}/collectd/entropy.so
%{_libdir}/collectd/exec.so
%{_libdir}/collectd/filecount.so
%{_libdir}/collectd/fscache.so
%{_libdir}/collectd/hddtemp.so
%{_libdir}/collectd/interface.so
%{_libdir}/collectd/ipmi.so
%{_libdir}/collectd/iptables.so
%{_libdir}/collectd/irq.so
%{_libdir}/collectd/load.so
%{_libdir}/collectd/logfile.so
%{_libdir}/collectd/madwifi.so
%{_libdir}/collectd/match_empty_counter.so
%{_libdir}/collectd/match_hashed.so
%{_libdir}/collectd/match_regex.so
%{_libdir}/collectd/match_timediff.so
%{_libdir}/collectd/match_value.so
%{_libdir}/collectd/mbmon.so
%{_libdir}/collectd/memcached.so
%{_libdir}/collectd/memory.so
%{_libdir}/collectd/multimeter.so
%{_libdir}/collectd/network.so
%{_libdir}/collectd/nfs.so
%{_libdir}/collectd/nginx.so
%{_libdir}/collectd/ntpd.so
%{_libdir}/collectd/olsrd.so
%{_libdir}/collectd/openvpn.so
%{_libdir}/collectd/perl.so
%{_libdir}/collectd/powerdns.so
%{_libdir}/collectd/processes.so
%{_libdir}/collectd/protocols.so
%{_libdir}/collectd/python.so
%{_libdir}/collectd/sensors.so
%{_libdir}/collectd/serial.so
%{_libdir}/collectd/swap.so
%{_libdir}/collectd/syslog.so
%{_libdir}/collectd/table.so
%{_libdir}/collectd/tail.so
%{_libdir}/collectd/target_notification.so
%{_libdir}/collectd/target_replace.so
%{_libdir}/collectd/target_scale.so
%{_libdir}/collectd/target_set.so
%{_libdir}/collectd/tcpconns.so
%{_libdir}/collectd/teamspeak2.so
%{_libdir}/collectd/ted.so
%{_libdir}/collectd/thermal.so
%{_libdir}/collectd/unixsock.so
%{_libdir}/collectd/uptime.so
%{_libdir}/collectd/users.so
%{_libdir}/collectd/uuid.so
%{_libdir}/collectd/vmem.so
%{_libdir}/collectd/vserver.so
%{_libdir}/collectd/wireless.so
%{_libdir}/collectd/write_http.so
%{_libdir}/libcollectdclient.so.*
%{_sbindir}/collectd
%{_sbindir}/collectdmon
%dir %{_localstatedir}/lib/collectd/

%files collection3
%{_localstatedir}/www/collection3
%{_sysconfdir}/httpd/conf.d/collection3.conf

%files dbi
%{_libdir}/collectd/dbi.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/collectd/
%{_libdir}/libcollectdclient.so
%{_libdir}/pkgconfig/libcollectdclient.pc
%exclude %{_libdir}/collectd/*.la
%exclude %{_libdir}/libcollectdclient.la

%files libvirt
%{_libdir}/collectd/libvirt.so

%files mysql
%{_libdir}/collectd/mysql.so

%files notify_desktop
%{_libdir}/collectd/notify_desktop.so

%files -n perl-Collectd
%{_libdir}/collectd/perl.so
%{perl_vendorlib}/Collectd.pm
%{perl_vendorlib}/Collectd/
%doc %{_mandir}/man5/collectd-perl.5*
%doc %{_mandir}/man3/Collectd::Unixsock.3pm* 

%files php-collection
%{_localstatedir}/www/php-collection
%{_sysconfdir}/httpd/conf.d/php-collection.conf

%files postgresql
%{_libdir}/collectd/postgresql.so

%files rrdtool
%{_libdir}/collectd/rrdtool.so
%{_libdir}/collectd/rrdcached.so

%files snmp
%{_libdir}/collectd/snmp.so

%files xmms
%{_libdir}/collectd/xmms.so

%changelog
* Tue Jun 22 2010 Christoph Maser <cmaser@gmx.de> 4.10.0-3
- Add httpd-config snippets for webapps
- remove obsolete for collectd-mysql
- create /etc/collectd.d dir

* Fri May 14 2010 Christoph Maser <cmaser@gmx.de> 4.10.0-2
- New rrdtool supports rrdcached
- more sub-packages

* Thu May 13 2010 Christoph Maser <cmaser@gmx.de> 4.10.0-1
- Updated to release 4.10.0.
- Work around OpenIPMI pgk-config bug https://bugzilla.redhat.com/show_bug.cgi?id=591646
- Split up in multiple packages to reduce dependencies

* Tue Mar 23 2010 Dag Wieers <dag@wieers.com> - 4.9.1-1
- Updated to release 4.9.1.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 4.9.0-1
- Updated to release 4.9.0.

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 4.8.0-1
- Updated to release 4.8.0.

* Wed Jul 29 2009 Dag Wieers <dag@wieers.com> - 4.7.2-1
- Updated to release 4.7.2.

* Sun Jul 12 2009 Dag Wieers <dag@wieers.com> - 4.7.1-1
- Updated to release 4.7.1.

* Fri Jul 03 2009 Christoph Maser <cmr@financial.com> - 4.6.3-1
- Updated to release 4.6.3.

* Mon Mar 23 2009 Dag Wieers <dag@wieers.com> - 4.6.2-1
- Updated to release 4.6.2.

* Sun Sep 14 2008 Dag Wieers <dag@wieers.com> - 4.5.0-1
- Updated to release 4.5.0.

* Tue Jul 29 2008 Dag Wieers <dag@wieers.com> - 4.4.2-1
- Updated to release 4.4.2.

* Sun Apr 27 2008 Dag Wieers <dag@wieers.com> - 4.3.3-1
- Updated to release 4.3.3.

* Sat Apr 05 2008 Dag Wieers <dag@wieers.com> - 4.3.2-1
- Updated to release 4.3.2.

* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 4.3.0-1
- Updated to release 4.3.0.

* Tue Dec 18 2007 Dag Wieers <dag@wieers.com> - 4.2.2-1
- Updated to release 4.2.2.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 4.2.1-1
- Updated to release 4.2.1.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 4.2.0-1
- Updated to release 4.2.0.

* Mon Oct 29 2007 Dag Wieers <dag@wieers.com> - 3.11.5-1
- Initial package. (using DAR)
