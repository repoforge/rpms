# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>
# ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name subvertpy

Summary: Alternative Python interface to Subversion
Name: python-subvertpy
Version: 0.7.5
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: https://launchpad.net/subvertpy/

Source: http://launchpad.net/subvertpy/trunk/%{version}/+download/subvertpy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: neon-devel
BuildRequires: python-devel >= 2.4
BuildRequires: python-sqlite2
BuildRequires: subversion-devel >= 1.6.5
Requires: neon 
Requires: python >= 2.4
Requires: python-sqlite2
Requires: subversion >= 1.6.5

%description
Alternative Python bindings for Subversion. The goal is to have complete,
portable and "Pythonic" Python bindings. 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS TODO examples/
%{_bindir}/*
%{python_sitearch}/*

%changelog
* Thu Dec 23 2010 Steve Huff <shuff@vecna.org> - 0.7.5-1
- Update to version 0.7.5.
- Captured pysqlite dependency.

* Tue Oct 12 2010 Steve Huff <shuff@vecna.org> - 0.7.4-1
- Initial package.
