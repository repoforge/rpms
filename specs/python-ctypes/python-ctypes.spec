# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name ctypes

Summary: Create and manipulate C data types from Python
Name: python-ctypes
Version: 1.0.0
Release: 2%{?dist}
License: MIT
Group: Development/Libraries
URL: http://starship.python.net/crew/theller/ctypes/

Source: http://dl.sf.net/ctypes/ctypes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3

%description
python-ctypes is a python module to create and manipulate C data types in
Python, and to call functions in dynamic link libraries/shared dlls.
It allows wrapping these libraries in pure Python.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKS ANNOUNCE BUGS ChangeLog LICENSE.txt README.*
%{python_sitearch}/_ctypes.so
%{python_sitearch}/_ctypes_test.so
%{python_sitearch}/ctypes/

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Fixed group name.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
