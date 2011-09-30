# $Id$
# Authority: yury
# Upstream: Ask Solem Hoel <ask$celeryproject,org>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global real_name kombu

Name: python-kombu
Version: 1.4.1
Release: 1%{?dist}
Summary: AMQP Messaging Framework for Python
Group: Development/Languages
License: BSD and Python
URL: http://pypi.python.org/pypi/%{real_name}

Source0: http://pypi.python.org/packages/source/k/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools

Requires: python-anyjson >= 0.3.1
Requires: python-amqplib >= 1.0

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is RabbitMQ.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and
also provide proven and tested solutions to common messaging problems.

%prep
%setup -q -n %{real_name}-%{version}

# Remove shehang
sed -i -e '/^#!\//, 1d' kombu/tests/test_serialization.py
# Remove hidden files
rm -rf docs/.static

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS Changelog FAQ LICENSE READ* THANKS TODO examples/ docs/
%{python_sitelib}/%{real_name}/
%{python_sitelib}/%{real_name}*.egg-info

%changelog
* Wed Sep 28 2011 Yury V. Zaytsev <yury@shurup.com> - 1.4.1-1
- Imported into RepoForge with minor changes.
- Updated to release 1.4.1.

* Fri Jul 15 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 1.1.3-1
- initial spec.
- derived from the one written by Fabian Affolter
- spec patch from Lakshmi Narasimhan
