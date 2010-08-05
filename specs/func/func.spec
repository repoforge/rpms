# $Id$
# Authority: shuff
# Upstream: Adrian Likins <alikins$redhat,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Remote management framework
Name: func
Version: 0.25
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: https://fedorahosted.org/func/
Source: http://people.fedoraproject.org/~alikins/files/func/func-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: gettext-devel
BuildRequires: pyOpenSSL
BuildRequires: python-setuptools
Requires: certmaster
Requires: chkconfig
Requires: logrotate
Requires: pyOpenSSL

%description
Func allows for running commands on remote systems in a secure way, like SSH,
but offers several improvements.

* Func allows you to manage an arbitrary group of machines all at once.
* Func automatically distributes certificates to all "slave" machines. There's
  almost nothing to configure.
* Func comes with a command line for sending remote commands and gathering
  data.
* There are lots of modules already provided for common tasks.
* Anyone can write their own modules using the simple Python module API.
* Everything that can be done with the command line can be done with the Python
  client API. The hack potential is unlimited.
* You'll never have to use "expect" or other ugly hacks to automate your
  workflow.
* It's really simple under the covers. Func works over XMLRPC and SSL.
* Since func uses certmaster, any program can use func certificates, latch on
  to them, and take advantage of secure master-to-slave communication.
* There are no databases or crazy stuff to install and configure. Again,
  certificate distribution is automatic too. 

%prep
%setup

%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
touch %{buildroot}%{_localstatedir}/log/func/func.log
touch %{buildroot}%{_localstatedir}/log/func/audit.log

# fix init script location
%{__install} -m0755 -d %{buildroot}%{_initrddir}
%{__mv} %{buildroot}%{_sysconfdir}/init.d/funcd %{buildroot}%{_initrddir}/
%{__rm} -rf %{buildroot}%{_sysconfdir}/init.d/

%clean
%{__rm} -rf %{buildroot}

%post -p "/sbin/chkconfig --add funcd"

%preun
if [ "$1" = 0 ]; then
    /sbin/service funcd stop >/dev/null 2>&1
    /sbin/chkconfig --del func >/dev/null 2>&1
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGES LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_initrddir}/*
%dir %{_sysconfdir}/func/
%dir %{_sysconfdir}/func/minion-acl.d/
%dir %{_sysconfdir}/func/modules/
%config(noreplace) %{_sysconfdir}/func/*.conf
%config(noreplace) %{_sysconfdir}/func/modules/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/*
%{python_sitelib}/func/
%dir %{_localstatedir}/log/func
%attr(0600,root,root) %config(noreplace) %{_localstatedir}/log/func/*
%dir %{_localstatedir}/lib/func/

%changelog
* Thu Aug 05 2010 Steve Huff <shuff@vecna.org> - 0.25-1
- Initial package, ported from Fedora.
