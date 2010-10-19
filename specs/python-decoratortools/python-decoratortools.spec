# $Id$
# Authority: dag

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

%define real_name DecoratorTools

Summary: Use class and function decorators
Name: python-decoratortools
Version: 1.7
Release: 1%{?dist}
License: Python or ZPLv2.1
Group: Development/Languages
URL: http://cheeseshop.python.org/pypi/DecoratorTools

Source: http://cheeseshop.python.org/packages/source/D/DecoratorTools/%{real_name}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools-devel

%description
Want to use decorators, but still need to support Python 2.3? Wish you could
have class decorators, decorate arbitrary assignments, or match decorated
function signatures to their original functions? Then you need "DecoratorTools"

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.txt
%{python_sitelib}/peak
%{python_sitelib}/%{real_name}-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/%{real_name}-%{version}-py%{pyver}-nspkg.pth

%changelog
* Fri Oct 15 2010 Dag Wieers <dag@wieers.com> - 1.7-1
- Initial package. (using DAR)
