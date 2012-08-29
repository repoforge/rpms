# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define _tftpbootdir /var/lib/tftpboot
%{?el5:%define tftpbootdir /tftpboot}

%{?el5:%define _without_pyegg 1}

#define _binaries_in_noarch_packages_terminate_build 0

Summary: Boot server configurator
Name: cobbler
%define real_version cobbler-96ee39b
Version: 2.2.2
Release: 1%{?dist}
License: GPLv2+
Group: Applications/System
URL: http://cobbler.github.com/

Source: https://github.com/downloads/cobbler/cobbler/cobbler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#AutoReq: no

BuildRequires: python-cheetah
BuildRequires: python-setuptools
BuildRequires: python-yaml
BuildRequires: redhat-rpm-config
Requires: createrepo
Requires: httpd
Requires: mod_wsgi
Requires: python >= 2.3
Requires: python-cheetah
Requires: python-netaddr
Requires: python-simplejson
Requires: python-urlgrabber
Requires: python-yaml
Requires: rsync
Requires: tftp-server
%{?el6:Requires: genisoimage}
%{?el5:Requires: mkisofs}
%{?el5:Requires: yum-utils}
Requires(post):  /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service

%description
Cobbler is a network install server.  Cobbler supports PXE, virtualized
installs, and re-installing existing Linux machines.  The last two modes
use a helper tool, 'koan', that integrates with cobbler.  There is also
a web interface 'cobbler-web'.  Cobbler's advanced features include
importing distributions from DVDs and rsync mirrors, kickstart templating,
integrated yum mirroring, and built-in DHCP/DNS Management.  Cobbler has
a XMLRPC API for integration with other applications.

%package -n cobbler-web
Summary: Web interface for Cobbler
Group: Applications/System
Requires: cobbler
Requires: python-django

%description -n cobbler-web
Web interface for Cobbler that allows visiting
http://server/cobbler_web to configure the install server.

%package -n koan
Summary: Helper tool that performs cobbler orders on remote machines
Group: Applications/System
Requires: python >= 2.0
Requires: python-simplejson

%description -n koan
Koan stands for kickstart-over-a-network and allows for both
network installation of new virtualized guests and reinstallation
of an existing system.  For use with a boot-server configured with Cobbler

%prep
%setup -n %{name}-%{real_version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%{__install} -Dp -m0644 config/cobbler.conf %{buildroot}/etc/httpd/conf.d/cobbler.conf
%{__install} -Dp -m0644 config/cobbler_web.conf %{buildroot}/etc/httpd/conf.d/cobbler_web.conf

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/spool/koan/
%{__install} -d -m0755 %{buildroot}%{_tftpbootdir}/images/

### Clean up buildroot
%{__rm} -f %{buildroot}/etc/cobbler/cobblerd

%post
if (( $1 == 1 )); then
    chkconfig --add cobblerd
fi

%preun
if (( $1 == 0 )); then
    service cobblerd stop &>/dev/null || :
    chkconfig --del cobblerd || :
fi

%postun
if (( $1 >= 1 )); then
    service cobblerd condrestart &>/dev/null || :
    service httpd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING README
%doc %{_mandir}/man1/cobbler.1*
%config(noreplace) %{_sysconfdir}/cobbler/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/cobbler.conf
%config(noreplace) %{_localstatedir}/lib/cobbler/
%config %{_sysconfdir}/init.d/cobblerd
%{_bindir}/cobbler
%{_bindir}/cobbler-ext-nodes
%{_bindir}/cobblerd
%{_sbindir}/tftpd.py*
%{python_sitelib}/cobbler/
%{_localstatedir}/log/cobbler/
%{_localstatedir}/www/cobbler/
%{!?_without_pyegg:%{python_sitelib}/cobbler-%{version}-py*.egg-info}
%{_tftpbootdir}/images/

%files -n koan
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING README
%doc %{_mandir}/man1/koan.1*
%doc %{_mandir}/man1/cobbler-register.1*
%{_bindir}/cobbler-register
%{_bindir}/koan
%{python_sitelib}/koan/
%dir %{_localstatedir}/lib/koan/config/
%dir %{_localstatedir}/log/koan/
%dir %{_localstatedir}/spool/koan/

%files -n cobbler-web
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CHANGELOG README
%config(noreplace) /etc/httpd/conf.d/cobbler_web.conf

%defattr(-, apache, apache, 0755)
%{_datadir}/cobbler/web/
%{_localstatedir}/www/cobbler_webui_content/
%dir %{_localstatedir}/lib/cobbler/webui_sessions/

%changelog
* Fri May 11 2012 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Initial package. (using DAR)
