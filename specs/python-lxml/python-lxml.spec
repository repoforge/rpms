# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name lxml

Summary: ElementTree-like Python bindings for libxml2 and libxslt
Name: python-lxml
Version: 1.3.4
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

%changelog
* Tue Sep 11 2007 Dag Wieers <dag@wieers.com> - 1.3.4-1
- Initial package. (using DAR)
