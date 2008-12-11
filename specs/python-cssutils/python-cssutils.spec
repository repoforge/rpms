# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name cssutils

Summary: CSS Cascading Style Sheets library for Python
Name: python-cssutils
Version: 0.9.5.1
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://cthedot.de/cssutils/

Source: http://cssutils.googlecode.com/files/cssutils-%{version}.zip
Patch0: cssutils-0.9.5.1-nohashbang.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-setuptools

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities.

%package doc
Summary: Documentation for the CSS Cascading Style Sheets library for Python
Group: Documentation

%description doc
This is the documentation for python-cssutils, a Python package to parse and
build CSS Cascading Style Sheets.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed \

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.txt COPYING* README.txt docs/
%{_bindir}/csscapture
%{_bindir}/csscombine
%{_bindir}/cssparse
%{python_sitelib}/cssutils-*.egg-info/
%{python_sitelib}/cssutils/
%{python_sitelib}/encutils/
# This is a way too generic name!
%exclude %{python_sitelib}/tests/

%files doc
%defattr(-, root, root, 0755)
%doc doc/*

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.9.5.1-1
- Initial package. (based on fedora)
