# $Id$
# Authority: dag

Summary: Various IPMI server management utilities
Name: ipmiutil
Version: 2.0.2
Release: 1%{?dist}
License: BSD
Group: System Environment/Kernel
URL: http://ipmiutil.sourceforge.net/

Source: http://dl.sf.net/ipmiutil/ipmiutil-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The ipmiutil component package provides utilities to view the SEL (showsel), 
perform a hardware reset (hwreset), set up the BMC LAN and Platform 
Event Filter entry to allow SNMP alerts (pefconfig), and other IPMI tasks.  
These can be invoked with the metacommand, ipmiutil, as well.  Man pages
are provided.

An IPMI driver can be provided by either the Intel IPMI driver (/dev/imb) 
or the OpenIPMI driver (/dev/ipmi0).  If used locally and no driver is
detected, ipmiutil will use user-space register I/Os instead.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#rm -f %{buildroot}/usr/sbin/xmlconfig 2>/dev/null

%{__install} -Dp -m0644 doc/bmclanpet.mib %{buildroot}%{_datadir}/snmp/mibs/BMCLAN-PET-MIB.txt
%{__install} -Dp -m0755 doc/checksel %{buildroot}%{_sysconfdir}/cron.daily/checksel
%{__install} -Dp -m0755 doc/ipmi_port.sh %{buildroot}%{_initrddir}/ipmi_port

touch %{buildroot}%{_datadir}/ipmiutil/ipmi_if.txt
touch %{buildroot}%{_datadir}/ipmiutil/sensor_out.txt

%post
/sbin/ldconfig
#/sbin/chkconfig --add ipmi_port
### Writes %{_datadir}/ipmiutil/ipmi_if.txt
%{_datadir}/ipmiutil/ipmi_if.sh  || :
%{_sbindir}/ipmiutil sensor >%{_datadir}/ipmiutil/sensor_out.txt || :
%{_sbindir}/ipmiutil lan -r >/tmp/pefcfg.tmp || :

%preun
#if [ $1 -eq 0 ]; then
#    /sbin/service ipmi_port stop &>/dev/null || :
#    /sbin/chkconfig --del ipmi_port
#fi

%postun
/sbin/ldconfig
#/sbin/service ipmi_port condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/UserGuide doc/*.txt
%doc %{_mandir}/man8/alarms.8*
%doc %{_mandir}/man8/bmchealth.8*
%doc %{_mandir}/man8/fruconfig.8*
%doc %{_mandir}/man8/getevent.8*
%doc %{_mandir}/man8/hwreset.8*
%doc %{_mandir}/man8/icmd.8*
%doc %{_mandir}/man8/idiscover.8*
%doc %{_mandir}/man8/ipmiutil.8*
%doc %{_mandir}/man8/isolconsole.8*
%doc %{_mandir}/man8/pefconfig.8*
%doc %{_mandir}/man8/sensor.8*
%doc %{_mandir}/man8/showsel.8*
%doc %{_mandir}/man8/tmconfig.8*
%doc %{_mandir}/man8/wdt.8*
%config %{_sysconfdir}/cron.daily/checksel
%config %{_initrddir}/ipmi_port
%{_datadir}/ipmiutil/
%ghost %{_datadir}/ipmiutil/ipmi_if.txt
%ghost %{_datadir}/ipmiutil/sensor_out.txt
%dir %{_datadir}/snmp/
%dir %{_datadir}/snmp/mibs/
%{_datadir}/snmp/mibs/BMCLAN-PET-MIB.txt
%{_libdir}/libipmi_lanplus.so*
%{_sbindir}/alarms
%{_sbindir}/bmchealth
%{_sbindir}/fruconfig
%{_sbindir}/getevent
%{_sbindir}/hwreset
%{_sbindir}/icmd
%{_sbindir}/idiscover
%{_sbindir}/ipmiutil
%{_sbindir}/isolconsole
%{_sbindir}/pefconfig
%{_sbindir}/sensor
%{_sbindir}/showsel
%{_sbindir}/tmconfig
%{_sbindir}/xmlconfig
%{_sbindir}/wdt
%exclude %{_libdir}/libipmi_lanplus.a
%exclude %{_libdir}/libipmi_lanplus.la

%changelog
* Tue Oct 30 2007 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Initial package. (using DAR)
