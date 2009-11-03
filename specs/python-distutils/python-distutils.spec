# $Id$
# Authority: dag

# ExclusiveDist: el2 rh7

%define python_version %(%{__python} -c 'import sys, string; print string.split(sys.version, " ")[0]')
### We can't use this macro on python 1.5.2 without distutils
#%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name Distutils

Summary: System for processing plaintext documentation
Name: python-distutils
Version: 1.0.2
Release: 1%{?dist}
Group: Development/Libraries
License: Public Domain, BSD, Python License, GPL - see COPYING.txt
URL: http://www.python.org/community/sigs/current/distutils-sig/

Source: http://www.python.org/community/sigs/current/distutils-sig/download/Distutils-1.0.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel <= 1.6
Requires: python >= %{python_version}, python <= 1.6

%description
The distutils package provides support for building and installing additional
modules into a Python installation. The new modules may be either 100%-pure
Python, or may be extension modules written in C, or may be collections
of Python packages which include modules coded in both Python and C.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root "%{buildroot}"
	
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt README.txt TODO USAGE.txt
%{_libdir}/python1.5/site-packages/distutils/

%changelog
* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
