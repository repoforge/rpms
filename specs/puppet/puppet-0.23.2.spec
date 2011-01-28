# $Id$
# Authority: dag
# ExcludeDist: el3 el4

%define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

Summary: Network tool for managing many disparate systems
Name: puppet
Version: 0.23.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://puppetlabs.com/projects/puppet/

Source: http://puppetlabs.com/downloads/puppet/puppet-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: ruby-devel >= 1.8.1
Requires: facter >= 1.1.4
Requires: ruby >= 1.8.1
Requires: ruby(api) = 1.8
Requires: ruby-shadow

%description
Puppet lets you centrally manage every important aspect of your system using a 
cross-platform specification language that manages all the separate elements 
normally aggregated in different files, like users, cron jobs, and hosts, 
along with obviously discrete elements like packages, services, and files.

%package server
Group: System Environment/Base
Summary: Server for the puppet system management tool
Requires: %{name} = %{version}-%{release}

%description server
Provides the central puppet server daemon which provides manifests to clients.
The server can also function as a certificate authority and file server.

%prep
%setup

%{__perl} -pi -e 's|^#!.*$|#!/usr/bin/ruby|' bin/*

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -Dp -m0755 bin/* %{buildroot}%{_sbindir}

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__mv} -f %{buildroot}%{_sbindir}/puppet %{buildroot}%{_bindir}/puppet
%{__mv} -f %{buildroot}%{_sbindir}/puppetrun %{buildroot}%{_bindir}/puppetrun

%{__install} -Dp -m0644 lib/puppet.rb %{buildroot}%{ruby_sitelibdir}/puppet.rb
%{__cp} -av lib/puppet %{buildroot}%{ruby_sitelibdir}

%{__install} -Dp -m0644 conf/redhat/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/puppet
%{__install} -Dp -m0644 conf/redhat/client.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppet
%{__install} -Dp -m0755 conf/redhat/client.init %{buildroot}%{_initrddir}/puppet
%{__install} -Dp -m0644 conf/redhat/server.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppetmaster
%{__install} -Dp -m0755 conf/redhat/server.init %{buildroot}%{_initrddir}/puppetmaster
%{__install} -Dp -m0644 conf/redhat/fileserver.conf %{buildroot}%{_sysconfdir}/puppet/fileserver.conf
%{__install} -Dp -m0644 conf/redhat/puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppet.conf
%{__ln_s} puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppetmasterd.conf
%{__ln_s} puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppetca.conf

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/puppet/manifests/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/puppet/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/puppet/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/puppet/

### Clean up buildroot
find %{buildroot}%{ruby_sitelibdir} -type f -perm +ugo+x -print0 | xargs -0 -r %{__chmod} a-x

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING LICENSE README examples/
%config %{_initrddir}/puppet
%config(noreplace) %{_sysconfdir}/logrotate.d/puppet
%config(noreplace) %{_sysconfdir}/puppet/puppet.conf
%config(noreplace) %{_sysconfdir}/sysconfig/puppet
%{_bindir}/puppet
%{_sbindir}/filebucket
%{_sbindir}/puppetd
%{_sbindir}/ralsh
%{ruby_sitelibdir}/puppet.rb
%{ruby_sitelibdir}/puppet/

%defattr(-, puppet, puppet, 0755)
%{_localstatedir}/lib/puppet/
%{_localstatedir}/log/puppet/
%{_localstatedir}/run/puppet/
%exclude %{_sbindir}/puppetdoc

%files server
%defattr(-, root, root, 0755)
%config %{_initrddir}/puppetmaster
%config(noreplace) %{_sysconfdir}/puppet/
%config(noreplace) %{_sysconfdir}/sysconfig/puppetmaster
%{_bindir}/puppetrun
%{_sbindir}/puppetca
%{_sbindir}/puppetmasterd

%pre
/usr/sbin/groupadd -r puppet 2>/dev/null || :
/usr/sbin/useradd -g puppet -c "Puppet" -s /sbin/nologin -r -d %{_localstatedir}/lib/puppet puppet 2>/dev/null || :
if [ $1 -gt 1 ] ; then
	/usr/sbin/usermod -d %{_localstatedir}/lib/puppet puppet || :
fi

%post
/sbin/chkconfig --add puppet

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service puppet stop &>/dev/null
	/sbin/chkconfig --del puppet
fi

%post server
/sbin/chkconfig --add puppetmaster

%preun server
if [ $1 -eq 0 ] ; then
	/sbin/service puppetmaster stop &>/dev/null
	/sbin/chkconfig --del puppetmaster
fi

%postun server
if [ $1 -ge 1 ]; then
	/sbin/service puppetmaster condrestart &>/dev/null
fi

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 0.23.2-1
- Update to version 0.23.2.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.22.4-1
- Initial package. (using DAR)
