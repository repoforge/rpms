# $Id$
# Authority: shuff
# Upstream: Adrian Likins <alikins$redhat,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Remote certificate distribution framework
Name: certmaster
Version: 0.25
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: https://fedorahosted.org/certmaster/
Source: http://people.fedoraproject.org/~alikins/files/certmaster/certmaster-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: gettext-devel
BuildRequires: pyOpenSSL
BuildRequires: python-setuptools
Requires: chkconfig
Requires: logrotate
Requires: pyOpenSSL

%description
Certmaster is a set of tools and a library for easily distributing SSL
certificates to applications that need them.

%prep
%setup

%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
ln -s %{_bindir}/certmaster-sync %{buildroot}%{_localstatedir}/lib/certmaster/triggers/sign/post/certmaster-sync
ln -s %{_bindir}/certmaster-sync %{buildroot}%{_localstatedir}/lib/certmaster/triggers/remove/post/certmaster-sync
touch %{buildroot}%{_localstatedir}/log/certmaster/certmaster.log
touch %{buildroot}%{_localstatedir}/log/certmaster/audit.log

# fix init script location
%{__install} -m0755 -d %{buildroot}%{_initrddir}
%{__mv} %{buildroot}%{_sysconfdir}/init.d/certmaster %{buildroot}%{_initrddir}/
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d/

%clean
%{__rm} -rf %{buildroot}

%post -p "/sbin/chkconfig --add certmaster"

%preun
if [ "$1" = 0 ]; then
    /sbin/service certmaster stop >/dev/null 2>&1
    /sbin/chkconfig --del certmaster >/dev/null 2>&1
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_initrddir}/*
%dir %{_sysconfdir}/certmaster/
%dir %{_sysconfdir}/certmaster/minion-acl.d/
%dir %{_sysconfdir}/pki/certmaster/
%config(noreplace) %{_sysconfdir}/certmaster/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%{python_sitelib}/certmaster/
%dir %{_localstatedir}/log/certmaster
%attr(0600,root,root) %config(noreplace) %{_localstatedir}/log/certmaster/*
%attr(0600,root,root) %dir %{_localstatedir}/lib/certmaster/
%attr(0600,root,root) %dir %{_localstatedir}/lib/certmaster/certmaster/
%attr(0600,root,root) %dir %{_localstatedir}/lib/certmaster/certmaster/certs/
%attr(0600,root,root) %dir %{_localstatedir}/lib/certmaster/certmaster/csrs/
%dir %{_localstatedir}/lib/certmaster/peers/
%dir %{_localstatedir}/lib/certmaster/triggers/sign/
%dir %{_localstatedir}/lib/certmaster/triggers/sign/pre/
%dir %{_localstatedir}/lib/certmaster/triggers/sign/post/
%{_localstatedir}/lib/certmaster/triggers/sign/post/certmaster-sync
%dir %{_localstatedir}/lib/certmaster/triggers/request/
%dir %{_localstatedir}/lib/certmaster/triggers/request/pre/
%dir %{_localstatedir}/lib/certmaster/triggers/request/post/
%dir %{_localstatedir}/lib/certmaster/triggers/remove/
%dir %{_localstatedir}/lib/certmaster/triggers/remove/pre/
%dir %{_localstatedir}/lib/certmaster/triggers/remove/post/
%{_localstatedir}/lib/certmaster/triggers/remove/post/certmaster-sync


%changelog
* Thu Aug 05 2010 Steve Huff <shuff@vecna.org> - 0.25-1
- Initial package, ported from Fedora.
