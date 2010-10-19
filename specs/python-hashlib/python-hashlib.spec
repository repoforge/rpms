# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name hashlib

Summary: Secure hash and message digest algorithm library
Name: python-hashlib
Version: 20081119
Release: 1%{?dist}
License: Python
Group:   Development/Libraries
URL: http://code.krypto.org/python/hashlib/

Source: http://code.krypto.org/python/hashlib/hashlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel
BuildRequires: python-devel

%description
This is a stand alone packaging of the hashlib library introduced in 
Python 2.5 so that it can be used on older versions of Python.

%prep
%setup -n %{real_name}-%{version}

dos2unix ChangeLog README.txt

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README.txt
%{python_sitearch}/_*.so
%{python_sitearch}/hashlib.py
%{python_sitearch}/hashlib.pyc
%ghost %{python_sitearch}/hashlib.pyo

%changelog
* Fri Oct 15 2010 Dag Wieers <dag@wieers.com> - 20081119-1
- Initial package. (using DAR)
