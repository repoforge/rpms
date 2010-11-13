# $Id$
# Authority: dag

### EL6 ships with python-zope-interface-3.5.2-2.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name ZopeInterface

Summary: Zope 3 Interface Infrastructure
Name: python-zope-interface
Version: 3.0.1
Release: 1%{?dist}
License: ZPL
Group: Development/Libraries
URL: http://pypi.python.org/pypi/zope.interface

Source: http://zope.org/Products/ZopeInterface/%{version}final/ZopeInterface-%{version}.tgz
Patch0: ZopeInterface-3.0.1-declbug.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
#BuildRequires: python-setuptools

%description
Interfaces are a mechanism for labeling objects as conforming to a given API
or contract.

This is a separate distribution of the zope.interface package used in Zope 3.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
find %{buildroot} -name \*.so -exec %{__chmod} 0755 {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt
%{python_sitearch}/zope*

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Initial package. (based on fedora)
