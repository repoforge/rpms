# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Python bindings for FUSE - filesystem in userspace
Name: fuse-python
Version: 0.2.1
Release: 1%{?dist}
License: LGPLv2
Group: System Environment/Base
URL: http://sourceforge.net/apps/mediawiki/fuse/index.php?title=FusePython

Source: http://dl.sf.net/fuse/fuse-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: python-fuse = %{version}-%{release}

BuildRequires: fuse-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: python-setuptools-devel

%description
This package provides python bindings for FUSE. FUSE makes it possible
to implement a filesystem in a userspace program.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Changelog COPYING FAQ README* example/
%{python_sitearch}/fuse*

%changelog
* Sat Nov 20 2010 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
