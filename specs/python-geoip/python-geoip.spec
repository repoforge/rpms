# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name GeoIP-Python

Summary: Python bindings for the GeoIP geographical lookup libraries
Name: python-geoip
Version: 1.2.1
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://www.maxmind.com/download/geoip/api/python/

Source: http://www.maxmind.com/download/geoip/api/python/GeoIP-Python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, geoip-devel
Obsoletes: python-GeoIP < %{version}-%{release}
Provides: python-GeoIP = %{version}-%{release}

%description
This package contains the Python bindings for the GeoIP API, allowing IP to
location lookups to country, city and organization level within Python code.

%prep
%setup -n %{real_name}-%{version}

chmod -x test*.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README test*.py
%{python_sitearch}/GeoIP.so

%changelog
* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
