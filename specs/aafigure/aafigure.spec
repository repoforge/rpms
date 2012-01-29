# $Id$
# Authority: dag

%{?el5:%define _without_egg_info 1}
%{?el4:%define _without_egg_info 1}
%{?el3:%define _without_egg_info 1}
%{?el2:%define _without_egg_info 1}

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: ASCII art to image converter
Name: aafigure
Version: 0.5
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: https://launchpad.net/aafigure

Source: http://pypi.python.org/packages/source/a/aafigure/aafigure-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.2
Requires: python >= 2.2
Requires: python-imaging

%description
ASCII art figures can be parsed and output as SVG, PNG, JPEG, PDF and more.
This project provides a python package and a command line script.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt README.txt examples/
%{_bindir}/aafigure
%{python_sitelib}/aafigure/
%{!?_without_egg_info:%{python_sitelib}/*.egg-info}

%changelog
* Mon Dec 19 2011 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
