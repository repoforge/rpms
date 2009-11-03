# $Id$
# Authority: dag
# Upstream: Andrew Chatham <pyogg@andrewchatham.com>

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_includedir %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_inc()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyao

Summary: Python bindings for libao
Name: python-ao
Version: 0.82
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.andrewchatham.com/pyogg/

Source: http://www.andrewchatham.com/pyogg/download/pyao-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel, libao-devel
Requires: python >= %{python_version}

%description
Python bindings for libao

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >Setup
ao_libs = ao
ao_lib_dir = %{_libdir}
ao_include_dir = %{_includedir}
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
%doc AUTHORS ChangeLog COPYING README
%{python_sitearch}/aomodule.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.82-1.2
- Rebuild for Fedora Core 5.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.82-1
- Initial package. (using DAR)
