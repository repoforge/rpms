# $Id$
# Authority: yury
# Upstream: Carl Meyer <carl$dirtcircle,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%{?el5:%define _without_sorl_thumbnail 1}

%define real_name django-form-utils

Name: python-django-form-utils
Version: 0.2.0
Release: 1%{?dist}
Summary: Form utilities for Django
Group: Development/Languages
License: BSD
URL: https://bitbucket.org/carljm/django-form-utils/src

Source: http://pypi.python.org/packages/source/d/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools

Requires: python-django >= 1.1
Requires: python-imaging

%{!?_without_sorl_thumbnail:Requires: python-django-sorl-thumbnail}

%description
This application provides utilities for enhancing Django's form handling.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc AUTHORS.rst CHANGES.rst HGREV LICENSE.txt PKG-INFO README.rst
%{python_sitelib}/form_utils/*.py*
%{python_sitelib}/form_utils/media/
%{python_sitelib}/form_utils/templates/
%{python_sitelib}/form_utils/templatetags/
%{python_sitelib}/*.egg-info

%changelog
* Fri Sep 09 2011 Yury V. Zaytsev <yury@shurup.com> - 0.2.0-1
- Initial package.
