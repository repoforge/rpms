# $Id$
# Authority: dag

### EL6 ships with python-lxml-2.2.3-1.1.el6
# ExclusiveDist: el5

%{?el5:%global _without_egg_info 1}

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%global python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%endif

%global real_name lxml

Summary: ElementTree-like Python bindings for libxml2 and libxslt
Name: python-lxml
Version: 2.3.1
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://lxml.de

Source0: http://lxml.de/files/%{real_name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.4
BuildRequires: libxslt-devel

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%prep
%setup -n %{real_name}-%{version}

%{__chmod} a-x doc/rest2html.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt CREDITS.txt LICENSES.txt PKG-INFO README.txt doc/
%{python_sitearch}/%{real_name}/
%{!?_without_egg_info:%{python_sitearch}/*.egg-info}

%changelog
* Sat Oct 22 2011 Yury V. Zaytsev <yury@shurup.com> - 2.3.1-1
- Updated to release 2.3.1.

* Tue Sep 13 2011 David Hrbáč <david@hrbac.cz> - 2.3-12.3-1
- new upstream release

* Tue Sep 11 2007 Dag Wieers <dag@wieers.com> - 1.3.4-1
- Initial package. (using DAR)
