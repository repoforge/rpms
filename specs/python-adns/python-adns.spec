# $Id$

# Authority: dag

%define rname adns-python

Summary: Python bindings for GNU adns library.
Name: python-adns
Version: 1.0.0
Release: 0
License: Unknown
Group: Development/Libraries
URL: http://dustman.net/andy/python/adns-python/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dustman.net/andy/python/adns-python/%{version}/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: python
Requires: python, adns

%description
python-adns is a Python module that interfaces to the adns asynchronous
resolver library.

%prep
%setup -n %{rname}-%{version}

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
%doc GPL license.py README
%{_libdir}/python*/site-packages/*

%changelog
* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
