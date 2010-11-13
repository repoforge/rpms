# $Id$
# Authority: matthias

### EL6 ships with python-memcached-1.43-5.3.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Python interface to the memcached memory cache daemon
Name: python-memcached
Version: 1.31
Release: 1%{?dist}
License: Unknown
Group: Development/Libraries
URL: ftp://ftp.tummy.com/pub/python-memcached/
Source: ftp://ftp.tummy.com/pub/python-memcached/python-memcached-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python
BuildArch: noarch


%description
Python interface to the memcached memory cache daemon.


%prep
%setup


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_prefix}/lib/python*/site-packages/memcache.py
%{_prefix}/lib/python*/site-packages/memcache.pyc
%ghost %{_prefix}/lib/python*/site-packages/memcache.pyo


%changelog
* Thu Aug 31 2006 Matthias Saou <http://freshrpms.net/> 1.31-1
- Initial RPM release.
- A license should really be chosen for this project...

