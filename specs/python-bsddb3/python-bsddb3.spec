# $Id$

# Authority: dag

%define rname bsddb3

Summary: Python interface for BerkeleyDB 3.1 and 3.2
Name: python-bsddb3
Version: 4.1.6
Release: 0
License: Unknown
Group: Development/Libraries
URL: http://pybsddb.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/pybsddb/bsddb3-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: python
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
%setup -n %{rname}-%{version}
%{__perl} -pi.orig -e '
		s|^(\s*incdir = ).*$|\1 "%{_includedir}/db4"|;
		s|^(\s*libdir = ).*$|\1 "%{_libdir}"|;
	' setup.py

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--prefix="%{_prefix}" \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog *.txt docs/
%{_libdir}/python*/site-packages/bsddb3/

%changelog
* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 4.1.6-0
- Initial package. (using DAR)
