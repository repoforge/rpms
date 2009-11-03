# $Id$
# Authority: dag
# Upstream: Andrew Chatham <pyogg@andrewchatham.com>

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_includedir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_inc()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyogg

Summary: Python bindings for libogg
Name: python-ogg
Version: 1.3
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.andrewchatham.com/pyogg/

Source: http://www.andrewchatham.com/pyogg/download/pyogg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, libogg-devel
Requires: python >= %{python_version}

%description
Python bindings for libogg

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >Setup
ogg_libs = ogg
ogg_lib_dir = %{_libdir}
ogg_include_dir = %{_includedir}
EOF

%build
export CFLAGS="%{optflags}"
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitearch}/ogg/
%{python_includedir}/pyogg/

%changelog
* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 1.3-1
- Initial package. (using DAR)
