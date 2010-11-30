# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>
# ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define major_version 1.0

Summary: Git branch support for Bazaar
Name: bzr-git
Version: 0.5.2
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: https://launchpad.net/bzr-git/

Source: http://launchpad.net/bzr-git/trunk/%{version}/+download/bzr-git-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-dulwich >= 0.6.2
BuildRequires: python-devel >= 2.4
BuildRequires: bzr >= 2.0
Requires: python-dulwich >= 0.6.2
Requires: python >= 2.4
Requires: bzr >= 2.0

%description
Bazaar plugin that adds support for foreign Git repositories. This allows
committing changes to Git branches as if they were native Bazaar branches.

This plugin also includes helper utilities.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING HACKING INSTALL NEWS README TODO notes/*
%{_bindir}/*
%{python_sitearch}/bzrlib/plugins/git/

%changelog
* Tue Nov 30 2010 Steve Huff <shuff@vecna.org> - 0.5.2-1
- Initial package.
