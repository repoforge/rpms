# $Id$
# Authority: shuff
# Upstream: Jelmer Vernooij <jelmer$samba,org>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name dulwich

%{?el3:%define _conflict_pyrex 1}
%{?el4:%define _conflict_pyrex 1}
%{?el5:%define _conflict_pyrex 1}

Name: python-dulwich
Version: 0.7.1
Release: 1%{?dist}
Summary: Pure-Python implementation of Git file formats and protocols

Group: Development/Languages
License: GPL
URL: http://samba.org/~jelmer/dulwich/

Source: http://samba.org/~jelmer/dulwich/dulwich-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# BuildArch: noarch

BuildRequires: python-setuptools 

# pyrex sometimes causes a build failure
%{?_conflict_pyrex:BuildConflicts: pyrex}
%{?_conflict_pyrex:BuildConflicts: Pyrex}

Provides: dulwich = %{version}-%{release}

%description
Dulwich aims to give an interface to git repos that doesn't call out to git
directly but instead uses pure Python.

The project is named after the part of London that Mr. and Mrs. Git live in in
the particular Monty Python sketch. It is based on the Python-Git module that
James Westby released in 2007 and now maintained by Jelmer Vernooij and John
Carr.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING HACKING NEWS README docs/*
%{_bindir}/*
%{python_sitearch}/*

%changelog
* Thu Apr 14 2011 Steve Huff <shuff@vecna.org> - 0.7.1-1
- Update to version 0.7.1.

* Thu Mar 24 2011 Steve Huff <shuff@vecna.org> - 0.7.0-1
- D'oh, sitearch, not sitelib :(
- Update to version 0.7.0.

* Tue Nov 30 2010 Steve Huff <shuff@vecna.org> - 0.6.2-1
- Initial package.
