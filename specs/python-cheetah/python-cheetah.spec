# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name Cheetah

Summary: Template engine and code-generator
Name: python-cheetah
Version: 2.0.1
Release: 1
License: MIT
Group: Development/Libraries
URL: http://cheetahtemplate.org/

Source: http://dl.sf.net/cheetahtemplate/Cheetah-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
Cheetah is an open source template engine and code generation tool, written
in Python. It can be used standalone or combined with other tools and
frameworks. Web development is its principle use, but Cheetah is very
flexible and is also being used to generate C++ game code, Java, sql,
form emails and even Python code.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO
%{_bindir}/cheetah
%{_bindir}/cheetah-compile
%{python_sitearch}/Cheetah/
# FIXME the following leads to warnings about files listed multiple times
%ghost %{python_sitearch}/Cheetah/*.pyo
%ghost %{python_sitearch}/Cheetah/*/*.pyo
%ghost %{python_sitearch}/Cheetah/*/*/*.pyo

%changelog
* Tue Dec 24 2008 Christoph Maser <cmr@financial.com> - 2.0.1-1
- Update Version

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 2.0-0.1.rc8
- Initial package. (using DAR)
