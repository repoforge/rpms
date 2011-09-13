# $Id$
# Authority: dag

### EL6 ships with python-lxml-2.2.3-1.1.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}
%{?el3:%define _without_egg_info 1}
%{?el2:%define _without_egg_info 1}

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name lxml

Summary: ElementTree-like Python bindings for libxml2 and libxslt
Name: python-lxml
Version: 2.3
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://codespeak.net/lxml/

Source: http://codespeak.net/lxml/lxml-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: libxslt-devel
#BuildRequires: python-setuptools-devel

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%prep
%setup -n %{real_name}-%{version}

%{__chmod} a-x doc/rest2html.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt CREDITS.txt LICENSES.txt PKG-INFO README.txt doc/
%{python_sitearch}/lxml/
%ghost %{python_sitearch}/lxml/*.pyo
%{!?_without_egg_info:%{python_sitearch}/*.egg-info}

%changelog
* Tue Sep 13 2011 David Hrbáč <david@hrbac.cz> - 2.3-12.3-1
- new upstream release

* Tue Sep 11 2007 Dag Wieers <dag@wieers.com> - 1.3.4-1
- Initial package. (using DAR)
