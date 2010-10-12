# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>
# ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Revision rewrite support for Bazaar
Name: bzr-rewrite
Version: 0.6.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://bazaar-vcs.org/Rebase/

Source: http://launchpad.net/bzr-rewrite/trunk/%{version}/+download/bzr-rewrite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4
BuildRequires: bzr >= 2.1
Requires: python >= 2.4
Requires: bzr >= 2.1

%description
Plugin for Bazaar that provides various ways of rewriting existing revisions,
including a rebase command similar to git's rebase.

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
%doc AUTHORS COPYING NEWS README
%{python_sitearch}/bzrlib/plugins/rewrite/

%changelog
* Tue Oct 12 2010 Steve Huff <shuff@vecna.org> - 1.0.4
- Initial package.
