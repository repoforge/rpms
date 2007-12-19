# $Id$
# Authority: dries
# Upstream:  Phil Schwartz <phil_schwartz$users,sourceforge,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')

%define real_name DenyHosts

Summary: Scan ssh server logs and block hosts
Name: denyhosts
Version: 2.6
Release: 3
License: GPL
Group: Applications/Internet
URL: http://denyhosts.sourceforge.net/

Source: http://dl.sf.net/denyhosts/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Obsoletes: DenyHosts <= %{version}
BuildRequires: python-devel >= 2.3
Requires: python >= 2.3

%description
DenyHosts is a script intended to help Linux system administrators thwart
ssh server attacks. DenyHosts scans an ssh server log, updates
/etc/hosts.deny after a configurable number of failed attempts from a
rogue host is determined, and alerts the administrator of any suspicious
logins.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"
%{__rm} -Rf %{buildroot}%{_datadir}/denyhosts
%{__mkdir_p} %{buildroot}%{_sysconfdir}/init.d
%{__cp} daemon-control-dist %{buildroot}%{_sysconfdir}/init.d/denyhosts
%{__mkdir_p} %{buildroot}%{_sysconfdir}/denyhosts
%{__cp} denyhosts.cfg-dist %{buildroot}%{_sysconfdir}/denyhosts/denyhosts.cfg
%{__sed} -i -e 's@^DENYHOSTS_CFG   =.*@DENYHOSTS_CFG   = "%{_sysconfdir}/denyhosts/denyhosts.cfg"@g' %{buildroot}%{_sysconfdir}/init.d/denyhosts

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x %{_initrddir}/%{name} ]; then
  /sbin/chkconfig --add %{name}
fi

%preun
if [ "$1" = 0 ]; then
  if [ -x %{_initrddir}/%{name} ]; then
    %{_initrddir}/%{name} stop
    /sbin/chkconfig --del %{name}
  fi
fi

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.txt daemon-control-dist denyhosts.cfg-dist LICENSE.txt README.txt
%{_bindir}/denyhosts.py*
%{python_sitearch}/DenyHosts/
%config (noreplace) /etc/denyhosts/denyhosts.cfg
/etc/init.d/denyhosts

%changelog
* Tue Dec 18 2007 Laurence Hurst <l.a.hurst@lboro.ac.uk> - 2.6-3
- run chkconfig on the newly installed init script upon install and uninstall.

* Fri Aug 10 2007 Christoph Maser <cmr$financial,com> - 2.6-2 
- make /etc/denyhosts
- copy dist-conf to /etc/denyhosts/denyhosts.cfg
- copy daemon-control-dist /etc/init.d/denyhosts
- edit /etc/init.d/denyhosts to use /etc/denyhosts/denyhosts.cfg
- ignore arch in %{python_sitearch} since python setup ignores it too

* Sun Dec 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 15 2006 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Wed Nov 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Tue Sep 27 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Updated to release 1.1.0.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Initial package.
