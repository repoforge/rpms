# $Id$
# Authority: arrfab

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Name: python-beaker
Version: 1.5.3
Release: 1%{?dist}
Summary: WSGI middleware layer to provide sessions

Group: Development/Languages
License: BSD
URL: http://beaker.groovie.org/
Source0: http://pypi.python.org/packages/source/B/Beaker/Beaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python-setuptools

%description
Beaker is a caching library that includes Session and Cache objects built on
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to
manage Session objects and signed cookies.


%prep
%setup -q -n Beaker-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE CHANGELOG
%{python_sitelib}/beaker/
%{python_sitelib}/Beaker*


%changelog
* Tue Oct 26 2010 Fabian Arrotin <fabian.arrotin@arrfab.net> - 1.5.3-1
- Initial package for RPMforge
