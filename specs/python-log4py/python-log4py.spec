# $Id$
# Authority: dries
# Upstream: Martin Preishuber <Martin,Preishuber$eclipt,at>

# Screenshot: http://www.its4you.at/images/screenshots/log4py.png

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name log4py

Summary: Python logging module similar to log4j
Name: python-log4py
Version: 1.3
Release: 1.2%{?dist}
License: MIT
Group: Development/Libraries
URL: http://www.its4you.at/english/log4py.html

Source: http://www.its4you.at/downloads/files/log4py-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python

%description
Log4Py is a python logging module similar to log4j. It supports logging to
files (including logfile rotation) or to stdout/stderr, variable log-levels,
configurable output formats and configuration via configuration files.

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
%doc doc/* log4py.conf readme.txt
%{python_sitearch}/log4py.py*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
