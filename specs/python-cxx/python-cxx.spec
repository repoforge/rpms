# $Id$
# Authority: shuff
# Upstream: Barry Scott <barryscott$tigris,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_siteinc %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_inc(1)')

%define real_name pycxx

Summary: Write Python extensions in C++
Name: python-cxx
Version: 6.1.1
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://CXX.sourceforge.net/

Source: http://prdownloads.sourceforge.net/cxx/pycxx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
Requires: python

Conflicts: pycxx
Obsoletes: pycxx
Provides: pycxx = %{version}

%description
PyCXX is a set of classes to help create extensions of Python in the C++
language. The first part encapsulates the Python C API taking care of
exceptions and ref counting. The second part supports the building of Python
extension modules in C++. 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.html COPYRIGHT Doc/Python2/ 
%{python_siteinc}/*
%{python_sitearch}/*
%{_datadir}/python*/*

%changelog
* Tue Nov 03 2009 Steve Huff <shuff@vecna.org> - 6.1.1-1
- Renamed per RPMforge naming convention.

* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 6.1.1-1
- Initial package.

