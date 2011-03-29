# $Id$
# Authority: shuff
# ExcludeDist: el3 el4

# we need Augeas >= 0.8 for Apache conf manipulation
# el6 ships with 0.7.x
%{?el6:# Tag: rfx}

%define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')

# no Ruby SELinux support in el5
%{?el5:%define _without_ruby_selinux 1}

# these are RHEL packages
%define confdir conf/redhat

Summary: Network tool for managing many disparate systems
Name: puppet
Version: 2.6.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://puppetlabs.com/projects/puppet/

Source: http://puppetlabs.com/downloads/puppet/puppet-%{version}.tar.gz
Patch0: puppet-2.6.5_rackup.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: facter >= 1.5
BuildRequires: ruby >= 1.8.1
BuildRequires: ruby-devel >= 1.8.1
BuildRequires: ruby-rdoc >= 1.8.1
Requires: augeas-libs >= 0.8
Requires: facter >= 1.5
Requires: ruby >= 1.8.1
Requires: ruby(abi) = 1.8
Requires: ruby-augeas
Requires: ruby-shadow
%{!?_without_ruby_selinux:Requires: libselinux-ruby}
%{!?_without_ruby_selinux:Requires: ruby(selinux)}

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

%package -n emacs-puppet
Group: Applications/Text
Summary: Emacs mode for Puppet
Requires: emacs-common

%description -n emacs-puppet
Emacs mode for editing Puppet files.

%package -n vim-puppet
Group: Applications/Text
Summary: Vim mode for Puppet
Requires: vim-common

%description -n vim-puppet
Vim support for editing Puppet files.

%prep
%setup
%patch0 -p1

%{__perl} -pi -e 's|^#!.*$|#!/usr/bin/ruby|' bin/*

%build
# Fix some rpmlint complaints
for f in mac_dscl.pp mac_dscl_revert.pp \
         mac_pkgdmg.pp ; do
  sed -i -e'1d' examples/$f
  %{__chmod} a-x examples/$f
done
for f in external/nagios.rb network/http_server/mongrel.rb relationship.rb; do
  %{__sed} -i -e '1d' lib/puppet/$f
done
%{__chmod} +x ext/puppetstoredconfigclean.rb

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

# puppet-queue.conf is more of an example, used for stompserver
%{__mv} conf/puppet-queue.conf examples/etc/puppet/

%install
%{__rm} -rf %{buildroot}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc

install -d -m0755 %{buildroot}%{_sysconfdir}/puppet/manifests
install -d -m0755 %{buildroot}%{_datadir}/%{name}/modules
install -d -m0755 %{buildroot}%{_localstatedir}/lib/puppet
install -d -m0755 %{buildroot}%{_localstatedir}/run/puppet
install -d -m0750 %{buildroot}%{_localstatedir}/log/puppet
install -Dp -m0644 %{confdir}/client.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppet
install -Dp -m0755 %{confdir}/client.init %{buildroot}%{_initrddir}/puppet
install -Dp -m0644 %{confdir}/server.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/puppetmaster
install -Dp -m0755 %{confdir}/server.init %{buildroot}%{_initrddir}/puppetmaster
install -Dp -m0644 %{confdir}/fileserver.conf %{buildroot}%{_sysconfdir}/puppet/fileserver.conf
install -Dp -m0644 %{confdir}/puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppet.conf
install -Dp -m0644 conf/auth.conf %{buildroot}%{_sysconfdir}/puppet/auth.conf
install -Dp -m0644 %{confdir}/logrotate %{buildroot}%{_sysconfdir}/logrotate.d/puppet

touch %{buildroot}%{_sysconfdir}/puppet/puppetca.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppetd.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppetmasterd.conf

# Install the ext/ directory to %{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a ext/ %{buildroot}%{_datadir}/%{name}
# emacs and vim bits are installed elsewhere
rm -rf %{buildroot}%{_datadir}/%{name}/ext/{emacs,vim}

# Install emacs mode files
emacsdir=%{buildroot}%{_datadir}/emacs/site-lisp
install -Dp -m0644 ext/emacs/puppet-mode.el $emacsdir/puppet-mode.el
install -Dp -m0644 ext/emacs/puppet-mode-init.el \
    $emacsdir/site-start.d/puppet-mode-init.el

# Install vim syntax files
vimdir=%{buildroot}%{_datadir}/vim/vimfiles
install -Dp -m0644 ext/vim/ftdetect/puppet.vim $vimdir/ftdetect/puppet.vim
install -Dp -m0644 ext/vim/syntax/puppet.vim $vimdir/syntax/puppet.vim

### Clean up buildroot
find %{buildroot}%{ruby_sitelibdir} -type f -perm +ugo+x -print0 | xargs -0 -r %{__chmod} a-x

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING LICENSE README examples/ ext/
%doc %{_mandir}/man?/filebucket.?.gz
%doc %{_mandir}/man?/pi.?.gz
%doc %{_mandir}/man?/puppet.?.gz
%doc %{_mandir}/man?/puppetd.?.gz
%doc %{_mandir}/man?/puppet.conf.?.gz
%doc %{_mandir}/man?/ralsh.?.gz
%exclude %doc %{_mandir}/man?/puppetdoc.?.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/puppet
%config(noreplace) %{_sysconfdir}/puppet/auth.conf
%config(noreplace) %{_sysconfdir}/puppet/puppet.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/puppet
%{_bindir}/filebucket
%{_bindir}/pi
%{_bindir}/puppet
%{_bindir}/ralsh
%{_datadir}/puppet
%{_sbindir}/puppetd
%{_initrddir}/puppet
%{ruby_sitelibdir}/*
%exclude %{_bindir}/puppetdoc

%defattr(-, puppet, puppet, 0755)
%{_localstatedir}/lib/puppet/
%{_localstatedir}/log/puppet/
%{_localstatedir}/run/puppet/

%files server
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/puppetca.?.gz
%doc %{_mandir}/man?/puppetmasterd.?.gz
%doc %{_mandir}/man?/puppetqd.?.gz
%doc %{_mandir}/man?/puppetrun.?.gz
%config(noreplace) %{_sysconfdir}/puppet/fileserver.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetca.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetmasterd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/puppetmaster
%{_initrddir}/puppetmaster
%{_sbindir}/puppetca
%{_sbindir}/puppetmasterd
%{_sbindir}/puppetqd
%{_sbindir}/puppetrun
%dir %{_sysconfdir}/puppet/manifests/

%files -n emacs-puppet
%defattr(-, root, root, -)
%{_datadir}/emacs/site-lisp/*

%files -n vim-puppet
%defattr(-, root, root, -)
%{_datadir}/vim*/vimfiles/*/puppet.vim

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
* Tue Mar 29 2011 Steve Huff <shuff@vecna.org> - 2.6.7-1
- Update to version 2.6.7.

* Wed Mar 16 2011 Steve Huff <shuff@vecna.org> - 2.6.6-1
- Update to version 2.6.6.
- Improvements to rackup config.
- Require Augeas 0.8 for Apache config lens.

* Mon Mar 07 2011 Steve Huff <shuff@vecna.org> - 2.6.5-1
- Update to version 2.6.5.
- Port rackup config from Debian to Red Hat.

* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 2.6.4-1
- Update to version 2.6.4 (el5 and el6 only).

* Fri Jan 28 2011 Steve Huff <shuff@vecna.org> - 0.23.2-1
- Update to version 0.23.2.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.22.4-1
- Initial package. (using DAR)
