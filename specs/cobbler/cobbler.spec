# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Boot server configurator
Name: cobbler
Version: 0.5.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://cobbler.et.redhat.com/

Source: http://cobbler.et.redhat.com/download/cobbler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3
Requires: python-devel >= 2.3, python-cheetah, httpd, mod_python
Requires: tftp-server, createrepo, yum-utils

%description
Cobbler is a command line tool for configuration of network boot and update
servers. It is also available as a Python library. Cobbler supports PXE,
provisioning virtualized images and reinstalling machines that are already
running (over SSH).

The last two modes require a helper tool called 'koan' that integrates with
cobbler. Cobbler's advanced features include importing distributions from
rsync mirrors, kickstart templating, integrated yum mirroring, kickstart
monitoring, and auto-managing dhcpd.conf.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%post
/sbin/chkconfig --add cobblerd

%preun
if [ $1 -eq 0 ]; then
	/sbin/service cobblerd stop &>/dev/null || :
	chkconfig --del cobblerd
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service cobblerd condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING NEWS README
%doc %{_mandir}/man1/cobbler.1*
%config(noreplace) %{_sysconfdir}/cobbler/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/cobbler.conf
#%config %{_initrddir}/cobblerd
%config %{_sysconfdir}/init.d/cobblerd
%dir /tftpboot/
%dir /tftpboot/pxelinux.cfg/
%dir /tftpboot/images/
%{_bindir}/cobbler
%{_bindir}/cobblerd
%{python_sitelib}/cobbler/
%ghost %{python_sitelib}/cobbler/*.pyo
%{python_sitelib}/cobbler/yaml/
%ghost %{python_sitelib}/cobbler/yaml/*.pyo
%dir %{_localstatedir}/log/cobbler/syslog/

%defattr(0644, root, root 2550)
%dir %{_localstatedir}/lib/cobbler/
%{_localstatedir}/lib/cobbler/elilo-3.6-ia64.efi
%{_localstatedir}/lib/cobbler/menu.c32
%dir %{_localstatedir}/lib/cobbler/triggers/
%dir %{_localstatedir}/lib/cobbler/triggers/add/
%dir %{_localstatedir}/lib/cobbler/triggers/add/distro/
%dir %{_localstatedir}/lib/cobbler/triggers/add/profile/
%dir %{_localstatedir}/lib/cobbler/triggers/add/repo/
%dir %{_localstatedir}/lib/cobbler/triggers/add/system/
%dir %{_localstatedir}/lib/cobbler/triggers/delete/
%dir %{_localstatedir}/lib/cobbler/triggers/delete/distro/
%dir %{_localstatedir}/lib/cobbler/triggers/delete/profile/
%dir %{_localstatedir}/lib/cobbler/triggers/delete/repo/
%dir %{_localstatedir}/lib/cobbler/triggers/delete/system/

%defattr(-, apache, apache, 2755)
%dir %{_localstatedir}/log/cobbler/
%dir %{_localstatedir}/log/cobbler/kicklog/
%dir %{_localstatedir}/www/cobbler/
%dir %{_localstatedir}/www/cobbler/distros/
%dir %{_localstatedir}/www/cobbler/images/
%dir %{_localstatedir}/www/cobbler/kickstarts/
%dir %{_localstatedir}/www/cobbler/kickstarts_sys/
%dir %{_localstatedir}/www/cobbler/ks_mirror/
%dir %{_localstatedir}/www/cobbler/ks_mirror/config/
%dir %{_localstatedir}/www/cobbler/links/
%dir %{_localstatedir}/www/cobbler/localmirror/
%dir %{_localstatedir}/www/cobbler/profiles/
%dir %{_localstatedir}/www/cobbler/repo_mirror/
%dir %{_localstatedir}/www/cobbler/systems/

%changelog
* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Initial package. (using DAR)
