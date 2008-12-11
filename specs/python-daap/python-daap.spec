# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PythonDaap

Summary: DAAP client implemented in Python
Name: python-daap
Version: 0.7.1
Release: 1
License: LGPL
Group: Development/Languages
URL: http://jerakeen.org/code/PythonDaap/

Source: http://jerakeen.org/files/PythonDaap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-setuptools

%description
A DAAP client implemented in Python.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE PKG-INFO README examples/
%{python_sitearch}/daap.py*
%{python_sitearch}/md5daap.so

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (based on fedora)
