# Authority: nac
# $Id$

%define version     1.0.5
%define release     6.0
%define name        cricket
%define httpd_user  apache

# /usr/lib/cricket will be the "cricket home"
#    - www/cgi will hold CGIs
#    - www/images will hold images
%define app_dir     %{_libdir}/%{name}/
%define cgi_dir     %{app_dir}/www/cgi/
%define img_dir     %{app_dir}/www/images/

# Cache graphs here; must be writable by web server!
%define cache_dir   %{_var}/cache/%{name}/

# /var/lib/cricket/ will contain RRD data
%define data_dir    %{_var}/lib/%{name}/

# /var/log/cricket will contain logs (duh)
%define log_dir     %{_var}/log/%{name}/

# /etc/cricket/config will be the default config tree
%define etc_dir     %{_sysconfdir}/%{name}/
%define config_dir  %{etc_dir}/config/

%define cron_dir    %{_sysconfdir}/cron.d/
%define httpd_dir   %{_sysconfdir}/httpd/conf.d/


Summary: Network statistics collection tool
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Applications/System
URL: http://cricket.sourceforge.net
Requires: perl(RRDs), perl(DB_File), perl(Time::HiRes), perl-SNMP_Session
Requires: perl(Date::Format), perl(Digest::MD5), perl(LWP), webserver
Source0: http://download.sourceforge.net/cricket/%{name}-%{version}.tar.gz
Source1: cricket.cron
Source2: cricket.apache
Patch1: cricket-paths.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
AutoReq: 0
AutoProv: 0

%description
Cricket is a high performance, extremely flexible system for monitoring
trends in time-series data. Cricket was expressly developed to help
network managers visualize and understand the traffic on their networks,
but it can be used all kinds of other jobs, as well.

Cricket has two components, a collector and a grapher. The collector
runs from cron every 5 minutes (or at a different rate, if you want),
and stores data into a data structure managed by RRD Tool. Later, when
you want to check on the data you have collected, you can use a web-based
interface to view graphs of the data.

%prep
%setup
./configure
%patch1 -p1 -b .paths

%install
%{__rm} -rf %{buildroot}

%{__install} -d %{buildroot}/%{app_dir}
%{__install} -m 555 collect-subtrees collector compile %{buildroot}/%{app_dir}

%{__cp} -a util lib %{buildroot}/%{app_dir}

%{__install} -d %{buildroot}/%{cgi_dir}
%{__install} -m 555 grapher.cgi mini-graph.cgi %{buildroot}/%{cgi_dir}

%{__install} -d %{buildroot}/%{img_dir}
%{__install} -m 444 images/* %{buildroot}/%{img_dir}

%{__install} -d %{buildroot}/%{cache_dir}
%{__install} -d %{buildroot}/%{data_dir}
%{__install} -d %{buildroot}/%{log_dir}

%{__install} -d -m 0771 %{buildroot}/%{etc_dir}
%{__install} -m 0664 subtree-sets %{buildroot}/%{etc_dir}
%{__install} -m 0664 cricket-conf.pl %{buildroot}/%{etc_dir}

%{__install} -d -m 0771 %{buildroot}/%{config_dir}
%{__install} -m 0660 sample-config/Defaults %{buildroot}%{config_dir}/

%{__install} -D %{SOURCE1} %{buildroot}/%{cron_dir}/%{name}

%{__install} -D -m 0664 %{SOURCE2} \
    %{buildroot}/%{_sysconfdir}/httpd/conf.d/50_%{name}.conf


%clean
%{__rm} -rf %{buildroot}

%pre
id cricket >/dev/null 2>&1
if [ $? -ne 0 ]; then
    useradd -r -d %{_libdir}/%{name} -c "Cricket SNMP Monitor" cricket
fi

%postun
if [ $1 -eq 0 ]; then
    userdel cricket
fi

%files
%defattr(-, root, cricket, 0755)
%dir %attr(0755,%{httpd_user},cricket) %{cache_dir}
%dir %attr(0775,root,cricket) %{data_dir}
%dir %attr(0775,root,cricket) %{log_dir}
%attr(-, cricket, %{httpd_user}) %config(noreplace) %{etc_dir}
%config(noreplace) %{cron_dir}/*
%config(noreplace) %{httpd_dir}/*
%{app_dir}

%doc CHANGES COPYING DEV-INFO README THANKS TODO VERSION doc sample-config

%changelog
* Wed Apr 06 2005 Wil Cooley <wcooley@nakedape.cc> - 1.0.5-6.nac.0.0
- Patched mini-grapher.cgi to look in the right place for grapher.cgi.
- Fixed scripts to not remove user on upgrade.

* Wed Apr 06 2005 Wil Cooley <wcooley@nakedape.cc> - 1.0.5-5.nac.0.0
- Fixed broken Apache config.
- Changed config files to noreplace.
- Fixed broken perms.

* Wed Apr 06 2005 Wil Cooley <wcooley@nakedape.cc> - 1.0.5-4.nac.0.0
- Updated to 1.0.5.
- Switched to a new, more standard layout.
- Disable to automatic provides also, since the bundled Perl modules are in
  a non-standard place.
- Added SNMP_Session; unfortunately, must hard-code package name due to
  package errors with smokeping.

* Fri Sep 24 2004 Wil Cooley <wcooley@nakedape.cc> - 1.0.4-3.nac.0.0
- Updated to 1.0.4.
- Pass PATH to configure so it'll find /usr/bin/perl before /usr/local/bin/perl.

* Fri Sep 24 2004 Wil Cooley <wcooley@nakedape.cc> - 1.0.3-3.nac.0.0
- Change Perl dependencies
- Rebuild on EL3
- Fix file listing for more restrictive newer versions of RPM
- Disable automatic requirements

* Tue Jan 22 2002 Wil Cooley <wcooley@nakedape.cc>
- Be a little more careful with cricket-config.
- Create the cricket user automatically.
- Added dependencies on various modules.

* Wed Dec 6 2000 Wil Cooley <wcooley@WireX.com>
- Initial creation
