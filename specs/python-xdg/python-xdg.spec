# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python library to access freedesktop.org standards
%define real_name pyxdg
Name: python-xdg
Version: 0.17
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://freedesktop.org/Software/pyxdg

Source: http://www.freedesktop.org/~lanius/pyxdg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel

Obsoletes: pyxdg <= %{version}-%{release}
Provides: pyxdg = %{version}-%{release}

%description
PyXDG is a python library to access freedesktop.org standards.

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
%doc AUTHORS ChangeLog COPYING README TODO
%{python_sitelib}/xdg/
%ghost %{python_sitelib}/xdg/*.pyo

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
