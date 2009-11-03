# $Id$
# Authority: dag
# Upstream: <pybsddb-users$lists,sf,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name bsddb3

Summary: Python interface for BerkeleyDB 3.x and 4.x
Name: python-bsddb3
Version: 4.6.2
Release: 1%{?dist}
License: Unknown
Group: Development/Libraries
URL: http://www.argo.es/~jcea/programacion/pybsddb.htm
#URL: http://pybsddb.sourceforge.net/

Source: http://pypi.python.org/packages/source/b/bsddb3/bsddb3-%{version}.tar.gz
#Source: http://dl.sf.net/pybsddb/bsddb3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python

%description
Berkeley DB is a programmatic toolkit that provides high-performance
built-in database support for desktop and server applications.

The Berkeley DB access methods include B+tree, Extended Linear Hashing,
Fixed and Variable-length records, and Queues. Berkeley DB provides full
transactional support, database recovery, online backups, multi-threaded
and multi-process access, etc.

The Python wrappers allow you to store Python string objects of any
length, keyed either by strings or integers depending on the database
access method. With the use of another module in the package standard
shelve-like functionality is provided allowing you to store any picklable
Python object!

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi.orig -e '
        s|^(\s*incdir = ).*$|\1 "%{_includedir}/db4"|;
        s|^(\s*libdir = ).*$|\1 "%{_libdir}"|;
    ' setup.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt ChangeLog docs/
%{python_sitearch}/bsddb3/

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 4.6.2-1
- Updated to release 4.6.2.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 4.4.2-1
- Updated to release 4.4.2.

* Wed May 19 2004 Dag Wieers <dag@wieers.com> - 4.2.4-1
- Updated to release 4.2.4.

* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 4.1.6-0
- Initial package. (using DAR)
