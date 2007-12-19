%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pymssql

Summary: Basic MS SQL module for Python
Name: python-mssql
Version: 0.8.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://pymssql.sourceforge.net/

Source: http://dl.sf.net/pymssql/pymssql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: x86_64 i386
BuildRequires: python-devel >= 2.4, freetds-devel >= 0.63
Requires: freetds >= 0.63

Provides: python-mssql
Obsoletes: python-mssql <= %{version}-%{release}

%description
This module provides access to Microsoft SQL Servers from Python scripts. Supports
connecting to Microsoft SQL 2000 and SQL 2005 servers, all editions and service pack
levels, named instances, non-standard port numbers, multiple query/multiple result,
and "most of the DB-API 2.0".

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
%doc README
%{python_sitearch}/_mssql.so
%{python_sitearch}/pymssql.py
%{python_sitearch}/pymssql.pyc
%ghost %{python_sitearch}/pymssql.pyo

%changelog
* Wed Dec 19 2007 Jim Nelson  - 0.8.0-1
- Initial package.
