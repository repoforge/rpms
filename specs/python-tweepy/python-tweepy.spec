# $Id$
# Authority: shuff
# Upstream: Joshua Roesslein <jroesslein$gmail,com>

## ExcludeDist: el3 el4
# requires python-2.4 or greater

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name tweepy

%{?el5:%define _needs_simplejson 1}

Summary: Python library for Twitter-compatible APIs
Name: python-tweepy
Version: 1.7.1
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: https://github.com/joshthecoder/tweepy/

Source: http://pypi.python.org/packages/source/t/tweepy/tweepy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4
BuildRequires: python-setuptools
Requires: python >= 2.4
%{?_needs_simplejson:Requires: python-simplejson}

%description
A Twitter library for Python! Also works with identi.ca/laconi.ca !

Features:
* OAuth support (including xAuth)
* Covers the entire Twitter API
* Actively under development
* Streaming API support
* Cache system (memory, file)

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{python_sitelib}/*

%changelog
* Thu Mar 24 2011 Steve Huff <shuff@vecna.org> - 1.7.1-1
- Initial package.
