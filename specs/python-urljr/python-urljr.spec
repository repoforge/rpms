# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Common interface to urllib2 and curl for making HTTP requests
Name: python-urljr
Version: 1.0.1
Release: 1%{?dist}
License: LGPL
Group: Development/Languages
URL: http://www.openidenabled.com/openid/libraries/python/urljr/

Source: http://www.openidenabled.com/resources/downloads/python-openid/python-urljr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel, python-curl
Requires: python, python-curl

%description
python-urljr contains the "fetchers" module, which provides a common interface
to urllib2 and curl for making HTTP requests.

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
%doc COPYING README
%{python_sitelib}/urljr/
%ghost %{python_sitelib}/urljr/*.pyo

%changelog
* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
