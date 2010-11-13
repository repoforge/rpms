# $Id$
# Authority: arrfab

### EL6 ships with python-mako-0.3.4-1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Name: python-mako
Version: 0.3.5
Release: 1%{?dist}
Summary: Mako template library for Python

Group: Development/Languages
License: MIT
URL: http://www.makotemplates.org/
Source0: http://www.makotemplates.org/downloads/Mako-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: python-setuptools 
BuildRequires: python-nose 
BuildRequires: python-markupsafe

Requires: python-beaker
Requires: python-markupsafe

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep
%setup -n Mako-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README doc examples
%{_bindir}/mako-render
%{python_sitelib}/*

%changelog
* Mon Oct 25 2010 Fabian Arrotin <fabian.arrotin@arrfab.net> - 0.3.5-1
- Initial package for RPMforge
