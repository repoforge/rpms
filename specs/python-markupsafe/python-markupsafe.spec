# $Id$
# Authority: arrfab

### EL6 ships with python-markupsafe-0.9.2-4.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib(1))')

Name: python-markupsafe
Version: 0.11
Release: 1%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python-devel python-setuptools

%description
A library for safe markup escaping.

%prep
%setup -n MarkupSafe-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README.rst
%{python_sitearch}/*

%changelog
* Mon Oct 25 2010 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.11-1
- Initial package for RPMforge
