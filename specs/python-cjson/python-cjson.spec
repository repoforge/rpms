# $Id$
# Authority: yury
# Upstream: Dan Pascu <dan$ag-projects,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%{?el5:%define _without_egginfo 1}
%{?el4:%define _without_egginfo 1}

Name: python-cjson
Version: 1.0.5
Release: 1%{?dist}
Summary: Fast JSON encoder/decoder for Python
Group: Development/Languages
License: LGPLv2+
URL: http://pypi.python.org/pypi/python-cjson

Source0: http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0: python-cjson-1.0.5-CVE-2010-1666.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
JSON stands for JavaScript Object Notation and is a text based lightweight
data exchange format which is easy for humans to read/write and for machines
to parse/generate. JSON is completely language independent and has multiple
implementations in most of the programming languages, making it ideal for
data exchange and storage.

The module is written in C and it is up to 250 times faster when compared to
the other python JSON implementations which are written directly in python.
This speed gain varies with the complexity of the data and the operation and
is the the range of 10-200 times for encoding operations and in the range of
100-250 times for decoding operations.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}

%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE PKG-INFO README
%{python_sitearch}/cjson.so
%{!?_without_egginfo:%{python_sitearch}/*.egg-info}

%changelog
* Fri Sep 09 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.5-1
- Initial package.
