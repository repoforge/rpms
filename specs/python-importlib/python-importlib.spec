# $Id$
# Authority: yury
# Upstream: Brett Cannon <brett$python,org>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

%global real_name importlib

Name: python-importlib
Version: 1.0.2
Release: 1%{?dist}
Summary: Backport of importlib.import_module() from Python 2.7
Group: Development/Languages
License: Python
URL: http://pypi.python.org/pypi/importlib

Source0: http://pypi.python.org/packages/source/i/%{real_name}/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel

Conflicts: python(abi) = 2.7

%description
This package contains the code from importlib as found in Python 2.7.
It is provided so that people who wish to use importlib.import_module()
with a version of Python prior to 2.7 or in 3.0 have the function
readily available. The code in no way deviates from what can be found
in the 2.7 trunk.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*


%changelog
* Fri Sep 30 2011 Yury V. Zaytsev <yury@shurup.com> - 1.0.2-1
- Imported into RepoForge with minor changes.

* Tue Jun 21 2011 Andrew Colin Kissa <andrew@topdog.za.net> 1.0.2-1
- Initial package
