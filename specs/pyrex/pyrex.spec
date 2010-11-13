# $Id$
# Authority: dag
# Upstream: Grew Ewing <greg.ewing$canterbury,ac,nz>

### EL6 ships with Pyrex-0.9.8.4-4.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name Pyrex

Summary: Compiler/language for writing Python extension modules.
Name: pyrex
Version: 0.9.9
Release: 1%{?dist}
License: Public Domain
Group: Development/Languages
URL: http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/

Source: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

BuildRequires: python-devel >= 2.3, dos2unix, findutils
Requires: python >= 2.3
Obsoletes: Pyrex <= %{version}-%{release}
Provides: Pyrex <= %{version}-%{release}

%description
Pyrex is Python with C types.  It is specially designed to allow you to
write extension modules for Python that have the speed of C and the
simplicity and readability of Python.  You write your code in a Python-like
language with C-typed variables, then use the pyrexc compiler to transform
it into a C representation.  This is useful for speeding up critical sections
of your Python code or wrapping an external library.

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
%doc CHANGES.txt README.txt ToDo.txt USAGE.txt Demos/ Doc/ Tools/
%{_bindir}/pyrexc
%{python_sitelib}/Pyrex/

%changelog
* Tue May 18 2010 Steve Huff <shuff@vecna.org> - 0.9.9-1
- Updated to release 0.9.9.

* Fri Nov 16 2007 Dag Wieers <dag@wieers.com> - 0.9.6.2-1
- Updated to release 0.9.6.2.

* Sat Dec 16 2006 Dag Wieers <dag@wieers.com> - 0.9.4.1-1
- Initial package. (using DAR)
