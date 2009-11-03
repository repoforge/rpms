# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define real_name PyRSS2Gen

Summary: SSH2 protocol for Python
Name: python-pyrss2gen
Version: 1.0.0
Release: 2.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.dalkescientific.com/Python/PyRSS2Gen.html

Source: http://www.dalkescientific.com/Python/PyRSS2Gen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3

Provides: PyRSS2Gen = %{version}-%{release}

%description
A Python RSS2 generator.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README example.py test.py
%{python_sitelib}/PyRSS2Gen.py
%{python_sitelib}/PyRSS2Gen.pyc
%ghost %{python_sitelib}/PyRSS2Gen.pyo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.0-2.2
- Rebuild for Fedora Core 5.

* Fri Mar 10 2006 Dag Wieers <dag@wieers.com> - 1.0.0-2
- Added .pyo ghost files.

* Thu Feb 09 2006 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
