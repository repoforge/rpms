# $Id$
# Authority: yury
# Upstream: self.anderson$gmail,com

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define real_version eb8c63016125
%define real_name offline-django-bbmarkup-%{real_version}

Name: python-django-bbmarkup
Version: 0.0.1
Release: 0.%{real_version}.1%{?dist}
Summary: Django application for converting BBCode text to HTML
Group: Development/Languages
License: BSD
URL: http://bitbucket.org/offline/django-bbmarkup/wiki/Home

Source: https://bitbucket.org/offline/django-bbmarkup/get/%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools

Requires: python-django

%description
Django application for converting BBCode text to HTML

%prep
%setup -n %{real_name}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{python_sitelib}/bbmarkup/*.py*
%{python_sitelib}/*.egg-info

%changelog
* Wed Sep 07 2011 Yury V. Zaytsev <yury@shurup.com> - 0.0.1-0.eb8c63016125.1
- Initial package.
