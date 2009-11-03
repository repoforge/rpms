# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyBluez

Summary: Python API for the BlueZ bluetooth stack 
Name: python-bluez
Version: 0.15
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://code.google.com/p/pybluez/

Source: http://pybluez.googlecode.com/files/PyBluez-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bluez-libs-devel
BuildRequires: python-devel

Provides: pybluez = %{version}-%{release}
Provides: PyBluez = %{version}-%{release}
Obsoletes: pybluez <= %{version}-%{release}
Obsoletes: PyBluez <= %{version}-%{release}


%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README examples/
%dir %{python_sitearch}/bluetooth/
%{python_sitearch}/bluetooth/_bluetooth.so
%{python_sitearch}/bluetooth/*.py
%{python_sitearch}/bluetooth/*.pyc
%ghost %{python_sitearch}/bluetooth/*.pyo

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
