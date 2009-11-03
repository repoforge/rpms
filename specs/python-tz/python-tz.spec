# $Id$
# Authority: dag

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define real_name pytz

Summary: World Timezone Definitions for Python
Name: python-tz
Version: 2006p
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: http://pytz.sourceforge.net/

Source: http://dl.sf.net/pytz/pytz-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

Provides: pytz = %{version}-%{release}
Obsoletes: pytz <= %{version}-%{release}

%description
pytz brings the Olson tz database into Python. This library allows accurate
and cross platform timezone calculations using Python 2.3 or higher. It
also solves the issue of ambiguous times at the end of daylight savings,
which you can read more about in the Python Library Reference
(datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__chmod} +x %{buildroot}%{python_sitelib}/pytz/*.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE.txt README.txt
%dir %{python_sitelib}/pytz/
%{python_sitelib}/pytz/*.py
%{python_sitelib}/pytz/*.pyc
%ghost %{python_sitelib}/pytz/*.pyo
%{python_sitelib}/pytz/locales/
%dir %{python_sitelib}/pytz/zoneinfo/
%dir %{python_sitelib}/pytz/zoneinfo/*/
%{python_sitelib}/pytz/zoneinfo/*/*.py
%{python_sitelib}/pytz/zoneinfo/*/*.pyc
%ghost %{python_sitelib}/pytz/zoneinfo/*/*.pyo
%dir %{python_sitelib}/pytz/zoneinfo/*/*/
%{python_sitelib}/pytz/zoneinfo/*/*/*.py
%{python_sitelib}/pytz/zoneinfo/*/*/*.pyc
%ghost %{python_sitelib}/pytz/zoneinfo/*/*/*.pyo
%{python_sitelib}/pytz/zone.tab

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 2006p-1
- Initial package. (using DAR)
