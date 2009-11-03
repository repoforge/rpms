# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name fpconst

Summary: Python module for handling IEEE 754 floating point special values
Name: python-fpconst
Version: 0.7.3
Release: 1%{?dist}
License: ASL 2.0
Group: Development/Languages
URL: http://research.warnes.net/statcomp/projects/RStatServer/fpconst

Source: http://dl.sf.net/rsoap/fpconst-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

%description
This python module implements constants and functions for working with
IEEE754 double-precision special values.  It provides constants for
Not-a-Number (NaN), Positive Infinity (PosInf), and Negative Infinity
(NegInf), as well as functions to test for these values.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README pep-0754.txt
%{python_sitelib}/*.py
%{python_sitelib}/*.pyc
%{python_sitelib}/*.pyo

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Initial package. (based on fedora)
