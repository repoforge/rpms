# $Id$
# Authority: shuff
# Upstream: Alec Thomas <alec$swapoff,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name cly

Summary: Command Line interface in pYthon
Name: python-cly
Version: 0.9
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pypi.python.org/pypi/cly/

Source: http://pypi.python.org/packages/source/c/cly/cly-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python-docutils
BuildRequires: python-setuptools
BuildRequires: python-pygments

%description
A Python module for simplifying the creation of interactive shells.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

# make the docs
pushd doc
%{__make} 
%{__rm} -f Makefile makedocs.py
popd

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README doc/*
%{python_sitelib}/cly/
%{python_sitelib}/cly*.egg-info

%changelog
* Mon Feb 14 2011 Steve Huff <shuff@vecna.org> - 0.9-1
- Initial package.
