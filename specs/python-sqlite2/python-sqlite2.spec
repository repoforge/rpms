# $Id$
# Authority: yury
# Upstream: Gerhard Haering <gh$ghaering,de>
#
# ExclusiveDist: el4 el5
#
# Python 2.6 in RHEL6 provides python-sqlite2 as python-sqlite
#

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysqlite

Summary: DB-API 2.0 interface for SQLite 3.x
Name: python-sqlite2
Version: 2.6.3
Release: 1%{?dist}
License: zlib/libpng
Group: Development/Languages
URL: http://code.google.com/p/pysqlite/

Source: http://%{real_name}.googlecode.com/files/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3
BuildRequires: sqlite-devel >= 3.3.6

Requires: python >= 2.3

%description
pysqlite is an interface to the SQLite 3.x embedded relational database
engine. It is almost fully compliant with the Python database API version
2.0 also exposes the unique features of SQLite.

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
%doc LICENSE
%{python_sitearch}/pysqlite2/_sqlite.so
%{python_sitearch}/pysqlite2/*.py*
%{python_sitearch}/pysqlite2/test/*.py*
%exclude %{_prefix}/pysqlite2-doc/install-source.txt

%changelog
* Sun Aug 14 2011 Yury V. Zaytsev <yury@shurup.com> - 2.6.3-1
- Updated to release 2.6.3.

* Sat Jul 07 2007 Heiko Adams <info@fedora-blog.de> - 2.3.3-1
- Rebuild for RPMforge.

* Wed Dec 28 2005 Dawid Gajownik <gajownik@gmail.com> - 2.0.5-1
- Initial RPM release.
