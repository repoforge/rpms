# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Powerful extensions to the standard datetime module
Name: python-dateutil
Version: 1.2
Release: 1
License: Python Software Foundation License
Group: Development/Libraries
URL: http://labix.org/python-dateutil

Source: http://labix.org/download/python-dateutil/python-dateutil-%{version}.tar.bz2
Patch0: python-dateutil-1.1-x86_64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

%description
The dateutil module provides powerful extensions to the standard datetime
module available in Python 2.3+.

%prep
%setup
%patch -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc example.py LICENSE NEWS README
%dir %{python_sitelib}/dateutil/
%{python_sitelib}/dateutil/*.py
%{python_sitelib}/dateutil/*.pyc
%ghost %{python_sitelib}/dateutil/*.pyo
%dir %{python_sitelib}/dateutil/zoneinfo/
%{python_sitelib}/dateutil/zoneinfo/*.py
%{python_sitelib}/dateutil/zoneinfo/*.pyc
%{python_sitelib}/dateutil/zoneinfo/zoneinfo-2007f.tar.gz
%ghost %{python_sitelib}/dateutil/zoneinfo/*.pyo

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
