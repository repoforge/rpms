# $Id$
# Authority: yury
# Upstream: Ask Solem Hoel <ask$celeryproject,org>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global real_name djkombu
%global tar_name django-kombu

Name: python-django-kombu
Version: 0.9.4
Release: 1%{?dist}
Summary: Kombu transport using the Django database as a message store
Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/django-kombu

Source0: http://pypi.python.org/packages/source/d/%{tar_name}/%{tar_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools

Requires: python-django
Requires: python-kombu

%description
Django application that enables you to use the Django database as the
message store for Kombu. Kombu is an AMQP messaging framework for Python.
AMQP is the Advanced Message Queuing Protocol, an open standard protocol for
message orientation, queuing, routing, reliability and security.

%prep
%setup -q -n %{tar_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%doc AUTHORS Changelog LICENSE PKG-INFO README* THANKS TODO
%{python_sitelib}/%{real_name}/
%{python_sitelib}/*.egg-info

%changelog
* Fri Sep 30 2011 Yury V. Zaytsev <yury@shurup.com> - 0.9.4-1
- Imported into RepoForge with minor changes.
- Updated to release 0.9.4.

* Sat Jul 16 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.2-1
- New upstream release
- Drop defattr

* Thu Apr 14 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.0-1
- initial spec
