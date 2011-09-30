# $Id$
# Authority: yury
# Upstream: Barry Pederson <bp$barryp,org>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global real_name amqplib

Name: python-amqplib
Version: 1.0.2
Release: 1%{?dist}
Summary: Client library for AMQP
Group: Development/Languages
License: LGPLv2+
URL: http://pypi.python.org/pypi/amqplib

Source0: http://pypi.python.org/packages/source/a/%{real_name}/%{real_name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools

%description
Client library for AMQP (Advanced Message Queuing Protocol)

%prep
%setup -q -n %{real_name}-%{version}

find . -type f -name \*.py | xargs -n 1 sed -i -e 's"^#!/usr/bin/env python"#!/usr/bin/python"'

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE PKG-INFO README TODO docs/ demo/ extras/
%{python_sitelib}/%{real_name}/
%{python_sitelib}/%{real_name}*.egg-info

%changelog
* Fri Sep 30 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.2-1
- Updated to release 1.0.2.

* Wed Sep 28 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.0-1
- Imported into RepoForge with minor changes.
- Updated to release 1.0.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Fabian Affolter <fabian@bernewireless.net> - 0.6.1-2
- Added python-nose as BR
- Remove old python stuff for Fedora 12

* Sat Jul 03 2010 Fabian Affolter <fabian@bernewireless.net> - 0.6.1-1
- Initial package
