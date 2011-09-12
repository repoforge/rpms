# $Id$
# Authority: yury
# Upstream: NetworkX Developers <networkx-discuss$googlegroups,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%{?el5:%define _without_egginfo 1}
%{?el5:%define _without_sphinx 1}

%define real_name pygraphviz

Name: python-pygraphviz
Version: 1.1
Release: 1%{?dist}
Summary: Python interface to Graphviz
Group: Development/Languages
License: BSD
URL: http://networkx.lanl.gov/pygraphviz

Source: http://pypi.python.org/packages/source/p/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4
BuildRequires: graphviz-devel
BuildRequires: pkgconfig

%{!?_without_sphinx:BuildRequires: python-sphinx}

%description
PyGraphviz is a Python interface to the Graphviz graph layout and visualization
package. With PyGraphviz you can create, edit, read, write, and d raw graphs
using Python to access the Graphviz graph data structure and layout algorithms.
PyGraphviz is independent from NetworkX but provides a similar prog ramming
interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{!?_without_sphinx:1}
    PYTHONPATH=%{buildroot}%{python_sitearch} make -C doc html
    mv doc/build/html htmldocs
    rm -rf doc
    rm -f htmldocs/.buildinfo
%endif

mv %{buildroot}%{_docdir}/%{real_name}-%{version}/ otherdocs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO otherdocs/*
%{!?_without_sphinx:%doc htmldocs/}
%{python_sitearch}/%{real_name}/*.py*
%{python_sitearch}/%{real_name}/*.so
%{python_sitearch}/%{real_name}/tests/
%{!?_without_egginfo:%{python_sitearch}/*.egg-info}

%changelog
* Fri Sep 09 2011 Yury V. Zaytsev <yury@shurup.com> - 1.1-1
- Initial package.
