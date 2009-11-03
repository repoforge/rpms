# $Id: python-sqlite.spec 3576 2005-09-13 00:54:46Z dag $
# Authority: dag
# Upstream: <pysqlite-devel$lists,sf,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysqlite

Summary: Python bindings for sqlite
Name: python-sqlite
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pysqlite.org/

Source: http://initd.org/pub/software/pysqlite/releases/1.0/%{version}/pysqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2, sqlite-devel

%description
This packages allows you to use sqlite with python.
sqlite is a simple database engine.

%prep
%setup -n %{real_name}
%{__rm} -f doc/rest/.*swp

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README* doc/rest/manual.txt examples/
%{python_sitearch}/_sqlite.so
%{python_sitearch}/sqlite/
%ghost %{python_sitearch}/sqlite/*.pyo

%changelog
* Mon Jan 09 2006 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
