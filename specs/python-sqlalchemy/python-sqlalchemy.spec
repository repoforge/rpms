# $Id$
# Authority: dries
# Upstream: <mike$zzzcomputing,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: SQL toolkit and object relational mapper for Python
Name: python-sqlalchemy
Version: 0.3.11
Release: 1%{?dist}
License: MIT/X Consortium License
Group: Development/Libraries
URL: http://www.sqlalchemy.org/

Source: http://dl.sf.net/sqlalchemy/SQLAlchemy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python
Requires: python

%description
SQLAlchemy is a SQL toolkit and object relational mapper for Python. It 
encourages "relational mapping" as opposed to "table mapping" and includes 
enterprise-level features such as eager loading, unit-of-work object commits, 
topological dependency sorting, and full usage of bind parameters. It 
supports MySQL, Postgres, Oracle, and SQLite.

%prep
%setup -n SQLAlchemy-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/*
%{python_sitelib}/sqlalchemy/
%{python_sitelib}/SQLAlchemy-%{version}-py*.egg-info/

%changelog
* Thu Feb 28 2008 Dries Verachtert <dries@ulyssis.org> - 0.3.11-1
- Updated to release 0.3.11.

* Sat Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.4-1
- Initial package.
