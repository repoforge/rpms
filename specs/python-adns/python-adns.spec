# $Id$
# Authority: dag
# Upstream: Andy Dustman <webmaster$dustman,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name adns-python

Summary: Python bindings for GNU adns library
Name: python-adns
Version: 1.0.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://dustman.net/andy/python/adns-python/

Source: http://dustman.net/andy/python/adns-python/%{version}/adns-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, adns-devel
Requires: python, adns

%description
python-adns is a Python module that interfaces to the adns asynchronous
resolver library.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags} -fPIC -fomit-frame-pointer -DPIC" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root="%{buildroot}" \
	--prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc GPL license.py README
%{python_sitearch}/*

%changelog
* Mon May 10 2004 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Added missing adns-devel buildrequires. (Chong Kai Xiong)

* Sat Aug 02 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
