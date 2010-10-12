# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>
# ExcludeDist el3 el4

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define major_version 1.0

Summary: Subversion branch support for Bazaar
Name: bzr-svn
Version: 1.0.4
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: https://launchpad.net/bzr-svn/

Source: http://launchpad.net/bzr-svn/%{major_version}/%{version}/+download/bzr-svn-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-subvertpy
BuildRequires: python-devel >= 2.4
BuildRequires: bzr >= 2.1
Requires: python-subvertpy
Requires: python >= 2.4
Requires: bzr >= 2.1

%description
Bazaar plugin that adds support for foreign Subversion repositories. This
allows committing changes to Subversion branches as if they were native Bazaar
branches.

This makes it possible to run the standard Bazaar subcommands ("bzr branch",
"bzr log", "bzr commit") against local Subversion working copies and remote
Subversion repositories.

Also provided is a Bazaar subcommand for converting complete Subversion
repositories to Bazaar.

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
%doc AUTHORS COPYING FAQ HACKING INSTALL NEWS README TODO UPGRADING *.example
%{python_sitearch}/bzrlib/plugins/svn/

%changelog
* Tue Oct 12 2010 Steve Huff <shuff@vecna.org> - 1.0.4
- Initial package.
