# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name PyRSS2Gen

Summary: SSH2 protocol for Python
Name: python-pyrss2gen
Version: 1.0.0
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.dalkescientific.com/Python/PyRSS2Gen.html

Source: http://www.dalkescientific.com/Python/PyRSS2Gen-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3

Provides: PyRSS2Gen = %{version}-%{release}

%description
A Python RSS2 generator.

%prep
%setup -n %{real_name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README example.py test.py
%{python_sitelib}/PyRSS2Gen.py
%{python_sitelib}/PyRSS2Gen.pyc
#%ghost %{python_sitelib}/PyRSS2Gen.pyo

%changelog
* Thu Feb 09 2006 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
