# $Id$
# Authority: shuff
# Upstream: Ryan MacDonald <ryan$r-fx,org>

%define real_version 9.7-1
%define apf_dir %{_sysconfdir}/apf
%define apf_bin %{_bindir}/apf

Summary: Advanced policy firewall
Name: apf
Version: 9.7_1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.rfxn.com/projects/advanced-policy-firewall/

Source: http://www.rfxn.com/downloads/apf-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: chkconfig
Requires: crontabs
Requires: logrotate
Requires: /bin/uname
Requires: /sbin/ifconfig
Requires: /sbin/ip
Requires: /sbin/iptables
Requires: /sbin/iptables-restore
Requires: /sbin/iptables-save
Requires: /sbin/lsmod
Requires: /sbin/modprobe
Requires: /sbin/rmmod
Requires: /usr/bin/diff
Requires: /usr/bin/md5sum

Provides: %{_sbindir}/apf
Provides: %{_sbindir}/firewall
Provides: %{_sbindir}/fwmgr

%description
Advanced Policy Firewall (APF) is an iptables(netfilter) based firewall system
designed around the essential needs of today's Internet deployed servers and
the unique needs of custom deployed Linux installations. The configuration of
APF is designed to be very informative and present the user with an easy to
follow process, from top to bottom of the configuration file. The management of
APF on a day-to-day basis is conducted from the command line with the 'apf'
command, which includes detailed usage information and all the features one
would expect from a current and forward thinking firewall solution.

%prep
%setup -n %{name}-%{real_version}

%build
sed -i -e 's!/etc/apf!%{apf_dir}!' files/conf.apf

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{apf_dir}
%{__install} -d %{buildroot}%{apf_dir}/internals
%{__install} -d %{buildroot}%{apf_dir}/vnet
%{__install} -d %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -d %{buildroot}%{_sysconfdir}/logrotate.d
%{__install} -d %{buildroot}%{_initrddir}
%{__install} -d %{buildroot}%{_sbindir}

%{__install} -m 0640 -t %{buildroot}%{apf_dir} files/*.rules files/conf.apf
%{__install} -m 0640 -t %{buildroot}%{apf_dir} files/VERSION
%{__install} -m 0750 -t %{buildroot}%{apf_dir} files/apf files/firewall
%{__install} -m 0640 -t %{buildroot}%{apf_dir}/internals files/internals/*
%{__install} -t %{buildroot}%{apf_dir}/vnet files/vnet/*

%{__install} -m 0750 %{buildroot}%{apf_dir}/apf %{buildroot}%{_sbindir}/apf
pushd %{buildroot}%{_sbindir}
%{__ln_s} apf fwmgr
popd

%{__install} -m 0755 cron.daily %{buildroot}%{_sysconfdir}/cron.daily/apf
%{__install} -m 0755 apf.init %{buildroot}%{_initrddir}/apf
%{__install} -m 0755 logrotate.d.apf %{buildroot}%{_sysconfdir}/logrotate.d/apf

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add apf
    /sbin/chkconfig --level 345 apf on

    %{apf_dir}/vnet/vnetgen
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del apf
fi

%files
%defattr(-, root, root, 0640)
%doc README.apf CHANGELOG COPYING.GPL 
%config(noreplace) %{apf_dir}/conf.apf
%{apf_dir}/apf
%{apf_dir}/firewall
%{apf_dir}/internals
%{apf_dir}/vnet
%{apf_dir}/*.rules
%{apf_dir}/VERSION
%attr(0750,root,root) %{_sbindir}/*
%attr(0750,root,root) %{_initrddir}/*
%attr(0755,root,root) %{_sysconfdir}/cron.daily/*
%attr(0755,root,root) %{_sysconfdir}/logrotate.d/*

%changelog
* Wed Dec 16 2009 Steve Huff <shuff@vecna.org> - 9.7.1-1
- Initial package.
