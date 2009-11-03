# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python OpenID libraries
Name: python-openid
Version: 1.2.0
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://www.openidenabled.com/openid/libraries/python/

Source: http://www.openidenabled.com/resources/downloads/python-openid/python-openid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel, python-urljr, python-yadis
Requires: python, python-urljr, python-yadis

%description
The OpenID library with batteries included.

The library features:

  refined and easy-to-use API,
  extensive documentation,
  many storage implemetations including file-based, SQL, and memcached,
  simple examples to help you get started and
  licensed under the LGPL.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README doc/ examples/
%{python_sitelib}/openid/
%ghost %{python_sitelib}/openid/*.pyo

%changelog
* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Initial package. (using DAR)
