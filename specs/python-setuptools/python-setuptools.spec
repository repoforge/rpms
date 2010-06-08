# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name setuptools

Summary: Download, build, install, upgrade, and uninstall Python packages
Name: python-setuptools
Version: 0.6c7
Release: 1%{?dist}
License: Python or ZPLv2.0
Group: Development/Languages
URL: http://peak.telecommunity.com/DevCenter/setuptools

Source: http://cheeseshop.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3
Requires: python-devel >= 2.3
Provides: python-setuptools-devel = %{version}-%{release}

%description
setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

%prep
%setup -n %{real_name}-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build \
    --root "%{buildroot}" \
    --single-version-externally-managed
find %{buildroot}%{python_sitelib} -name '*.exe' | xargs rm -f
find %{buildroot}%{python_sitelib} -name '*.txt' | xargs chmod -x
chmod +x %{buildroot}%{python_sitelib}/setuptools/command/easy_install.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Mon Jun 07 2010 Dag Wieers <dag@wieers.com> - 0.6c7-1
- Updated to release 0.6c7.

* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.6c6-1
- Initial package. (using DAR)
