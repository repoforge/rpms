# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name uTidylib

Summary: Python wrapper for tidy, from the HTML tidy project
Name: python-tidy
Version: 0.2
Release: 1%{?dist}
License: MIT
Group: Development/Languages
URL: http://utidylib.berlios.de/

Source: http://download.berlios.de/utidylib/%{real_name}-%{version}.zip
### Upstream bug: http://developer.berlios.de/bugs/?func=detailbug&bug_id=14691&group_id=1810
Patch0: python-tidy-0.2-64bit-safe.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3
Requires: libtidy >= 0.99.0
Requires: python >= 2.3

%description
Python wrapper (bindings) for tidylib, this allows you to tidy HTML
files through a Pythonic interface.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README.txt
%{python_sitelib}/*

%changelog
* Thu Sep 23 2010 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (based on fedora)
