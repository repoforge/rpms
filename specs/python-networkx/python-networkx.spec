# $Id$
# Authority: yury
# Upstream: NetworkX Developers <networkx-discuss$googlegroups,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define real_name networkx

Name: python-networkx
Version: 1.5
Release: 1%{?dist}
Summary: Python package for creating and manipulating graphs and networks
Group: Development/Languages
License: BSD
URL: http://networkx.lanl.gov/

Source: http://pypi.python.org/packages/source/n/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.6

Requires: numpy
Requires: python-matplotlib
Requires: python-pygraphviz

%description
NetworkX is a Python package for the creation, manipulation, and
study of the structure, dynamics, and functions of complex networks.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

mv doc/source doc/rstdocs

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mv %{buildroot}%{_docdir}/%{real_name}-%{version}/ otherdocs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO scripts/ doc/rstdocs/ otherdocs/*
%{python_sitelib}/%{real_name}/*.py*
%{python_sitelib}/%{real_name}/algorithms/
%{python_sitelib}/%{real_name}/classes/
%{python_sitelib}/%{real_name}/drawing/
%{python_sitelib}/%{real_name}/generators/
%{python_sitelib}/%{real_name}/linalg/
%{python_sitelib}/%{real_name}/readwrite/
%{python_sitelib}/%{real_name}/tests/
%{python_sitelib}/*.egg-info

%changelog
* Fri Sep 09 2011 Yury V. Zaytsev <yury@shurup.com> - 1.5-1
- Initial package.
