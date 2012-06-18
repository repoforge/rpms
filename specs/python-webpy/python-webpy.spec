# $Id$
# Authority: shuff
# Upstream: Anand Chitipothu <anandology$gmail,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define real_name web.py

Name: python-webpy
Version: 0.36
Release: 1%{?dist}
Summary: Simple, powerful Python web framework
Group: Development/Languages
License: Public Domain
URL: http://webpy.org/

Source: http://webpy.org/static/web.py-%{version}.tar.gz
Patch0: webpy-python2.4.3.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools
#Requires: DBUtils
#Requires: python-markdown
#Requires: python-MySQLdb
Requires: python-psycopg2
Requires: python-sqlite2

Provides: webpy = %{version}-%{release}

%description
web.py is a web framework for Python that is as simple as it is powerful.
web.py is in the public domain; you can use it for whatever purpose with
absolutely no restrictions.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0 -b .python

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Mon May 28 2012 David Hrbáč <david@hrbac.cz> - 0.36-1
- new upstream release
- patch to run on python 2.4.3

* Mon Mar 12 2012 Steve Huff <shuff@vecna.org> - 0.35-1
- Initial package.
