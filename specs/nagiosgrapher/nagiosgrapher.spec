# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

%define real_name NagiosGrapher
%define real_version 1.6.1-rc5-0.5

Summary: Collects the output of Nagios Plugins and generates graphs
Name: nagiosgrapher
Version: 1.6.1
Release: 0.8.rc5%{?dist}
License: GPL
Group: Applications/System
URL: http://www.netways.de/Nagios_Grapher.44.0.html

### Download from http://www.nagiosexchange.org/Charts.42.0.html?&tx_netnagext_pi1[p_view]=195
Source0: NagiosGrapher-%{real_version}.tar.gz
Source1: nagiosgrapher-rh.init
Patch0: nagiosgrapher_makefile-patch-%{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: nagios
Requires: https
Requires: nagios
Requires: perl
Requires: perl(Calendar-Simple)
Requires: perl(GD)
Requires: perl(XML::Parser)
Requires: perl(XML::Simple)
Requires: rrdtool

Provides: NagiosGrapher = %{version}-%{release}
Obsoletes: NagiosGrapher <= %{version}-%{release}

%description
NagiosGrapher is a Nagios graphing system that has the following major features:

- get values from nagios without patching (eg. through "process-service-perfdata")
- realtime graphing (5 minutes delay at maximum)
- recoginzing new hosts/services and automatic graphing of these
- auto pruning and abstructing of stored values
- very slim backend - no need of a database systems
- easy to install 

%prep
%setup -n %{real_name}-%{real_version}
%patch

%{__cat} <<EOF >> config.layout

### Layout for RPM Build
<Layout RPM>
    prefix: %{_prefix}
    nagios_config: %{_sysconfdir}/nagios/nagios.cfg
    nagios_config_cgi: %{_sysconfdir}/nagios/cgi.cfg
    nagios_images: %{_datadir}/nagios/images
    nagios_images_logos: %{_datadir}/nagios/images/logos
    nagios_folder_cgi: %{_libdir}/nagios/cgi
    nagios_contribution: %{_libdir}/nagios/plugins/contrib
    perl_inc: %{perl_vendorlib}
    ng_config: %{_sysconfdir}/nagios
    ng_config_sub: %{_sysconfdir}/nagios/ngraph.d
    ng_daemon: %{_localstatedir}/log/nagios/rw
    ng_srvext_file: %{_sysconfdir}/nagios/serviceextinfo.cfg
    ng_srvext_dir: %{_sysconfdir}/nagios/serviceext
    ng_interface_pipe: %{_localstatedir}/log/nagios/rw/ngraph.pipe
    ng_logfile: %{_localstatedir}/log/nagios/ngraph.log
    ng_rrd: %{_localstatedir}/lib/nagios/rrd
    ng_rrd_font: %{_datadir}/rrdtool/fonts/DejaVuSansMono-Roman.ttf
    ng_cgi: /nagios/cgi-bin
    ng_logos: /nagios/images/logos
    init_script_dir: %{_initrddir}
    logrotate_conf_dir: %{_sysconfdir}/logrotate.d
</Layout>
EOF

%build
autoconf
./configure --with-layout="RPM"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} command-rpm DESTDIR="%{buildroot}"

### Replace upstream initscript with our own
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/nagios_grapher

### collect2.pl is our daemon
%{__install} -Dp -m0755 %{buildroot}%{_libdir}/nagios/plugins/contrib/collect2.pl %{buildroot}%{_sbindir}/collect2.pl

%post
/sbin/chkconfig --add nagios_grapher

%preun
if [ $1 -eq 0 ]; then
    /sbin/service nagios_grapher stop &>/dev/null
    /sbin/chkconfig --del nagios_grapher
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/ABOUT doc/AUTHORS doc/CHANGELOG doc/CONFIG doc/CONTRIBUTORS doc/INSTALL
%doc doc/LAYOUT doc/TODO doc/VERSION
%config %{_initrddir}/nagios_grapher
%config(noreplace) %{_sysconfdir}/logrotate.d/nagios_grapher
%{perl_vendorlib}/NagiosGrapher.pm
%{perl_vendorlib}/NagiosGrapher/HTML.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/Generic.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/ImageGraphTest.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/NG2MySQL.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/RRDUpdateTest.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/SrvExtTest.pm
%{perl_vendorlib}/NagiosGrapher/Hooks/SrvExtWriteHostextInfo.pm

%defattr(-, nagios, nagios, 0644)
%config(noreplace) %{_sysconfdir}/nagios/ngraph-command.cfg
%config(noreplace) %{_sysconfdir}/nagios/ngraph.d/nmgraph.ncfg
%config(noreplace) %{_sysconfdir}/nagios/ngraph.ncfg
%config %{_sysconfdir}/nagios/ngraph.d/templates/*
%{_datadir}/nagios/images/dot.png
%{_datadir}/nagios/images/graph.png
%{_datadir}/nagios/images/logos/dot.png
%{_datadir}/nagios/images/logos/graph.png
%{_libdir}/nagios/cgi/graphs.cgi
%{_libdir}/nagios/cgi/rrd2-graph.cgi
%{_libdir}/nagios/cgi/rrd2-system.cgi
%{_libdir}/nagios/plugins/contrib/fifo_write
%{_libdir}/nagios/plugins/contrib/fifo_write.pl
%{_libdir}/nagios/plugins/contrib/udpecho
%{_localstatedir}/log/nagios/ngraph.log
%{_sbindir}/collect2.pl

%changelog
* Tue Mar 18 2008 Dag Wieers <dag@wieers.com> - 1.6.1-0.8.rc5
- Updated to release 1.6.1rc5-0.5.

* Mon Sep 25 2007 - Christoph Maser <cmr@financial.com> - 1.6.1-0.7.rc5
- Updated to release 1.6.1rc5-0.3.

* Mon Aug 23 2007 - Christoph Maser <cmr@financial.com> - 1.6.1-0.6.rc5
- Updated to release 1.6.1rc5.
- Fix layout dynamically.
- Add Logrotate.
- Create nagios-config-include.

* Mon Nov 13 2006 - Christoph Maser <cmr@financial.com> - 1.6.1-0.4.rc1
- Updated to release 1.6.1rc1.
- Use %{_sysconfdir} and %{_libdir} in pathnames.

* Thu Aug 19 2006 Christoph Maser <cmr@financial.com>
- RH Version.
