# $Id$
# Authority: shuff
# Upstream: Lele Gaifax <lele$nautilus,homeip,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(0)')

Summary: Translate changesets between version control systems
Name: tailor
Version: 0.9.35
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://progetti.arstecnica.it/tailor

Source: http://darcs.arstecnica.it/tailor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python >= 2.3
#Requires: aegis
#Requires: arx
#Requires: baz
Requires: bzr
#Requires: codeville
Requires: cvs
#Requires: darcs >= 1.0.3
Requires: git
Requires: mercurial
#Requires: monotone
#Requires: perforce
Requires: subversion
#Requires: tla

Provides: %{_bindir}/tailor

%description
Tailor is a tool to migrate changesets between Aegis, ArX, Bazaar, Bazaar-NG,
CVS, Codeville, Darcs, Git, Mercurial, Monotone, Perforce, Subversion and Tla
repositories. There are other tools with a similar goal, most of them tied and
sometime more specialized on a particular system.


%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README.html README.rst
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Fri Jan 29 2010 Steve Huff <shuff@vecna.org> - 0.9.35-1
- Initial package.
