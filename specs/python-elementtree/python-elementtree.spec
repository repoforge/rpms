# $Id$
# Authority: dag

### EL5 ships with python-elementtree-1.2.6-5
# ExcludeDist: el5

#define python_abi %(%{__python} -c 'import sys; print ".".join(sys.version.split(".")[:2])')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name elementtree

Summary: Fast XML parser and writer
Name: python-elementtree
%define real_version 1.2.6-20050316
%define real_version_celementtree 1.0.2-20050302
Version: 1.2.6
Release: 7%{?dist}
License: PSF
Group: Development/Libraries
URL: http://effbot.org/zone/element-index.htm

Source0: http://effbot.org/downloads/elementtree-%{real_version}.tar.gz
Source1: http://effbot.org/downloads/cElementTree-%{real_version_celementtree}.zip
Source2: cElementTree-system-expat-setup.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: expat-devel, python-devel
#Requires: python-abi = %{python_abi}
Obsoletes: python-celementtree
Provides: cElementTree.so

%description
The Element type is a simple but flexible container object, designed
to store hierarchical data structures, such as simplified XML
infosets, in memory. The element type can be described as a cross
between a Python list and a Python dictionary.

This package also includes the C implementation, %{real_version_celementtree}.

%prep
%setup -a1 -n %{real_name}-%{real_version}
pushd cElementTree-%{real_version_celementtree}
%{__mv} -f setup.py setup.py-orig
%{__cp} -f %{SOURCE2} setup.py
%{__mv} -f CHANGES ../CHANGES-cElementTree
%{__mv} -f README ../README-cElementTree
popd

%build
%{__python} setup.py build
pushd cElementTree-%{real_version_celementtree}
CFLAGS="%{optflags}" %{__python} setup.py build
popd

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
pushd cElementTree-%{real_version_celementtree}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES* README* benchmark.py docs/ samples/
%{python_sitelib}/elementtree/
%ghost %{python_sitelib}/elementtree/*.pyo
%{python_sitearch}/*.so

%changelog
* Sun Aug 13 2006 Dag Wieers <dag@wieers.com> - 1.2.6-7
- Provide cElementtree.so because external packages (vzyum) require it.

* Fri Jan 27 2006 Dag Wieers <dag@wieers.com> - 1.2.6-6
- Removed python-abi since older releases do not provide it.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 1.2.6-5
- Obsoleted python-celementtree.

* Tue Jul 26 2005 Jeff Pitman <symbiont+pyvault@berlios.de> 1.2.6-4.1
- pyvaultize

* Mon Apr  4 2005 Jeremy Katz <katzj@redhat.com> - 1.2.6-4
- rebuild for core
- use %%setup -q -a 1 instead of unzipping source1

* Tue Mar 30 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.2.6-3
- Use python_sitearch for the C library.

* Tue Mar 29 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.2.6-2
- Use python_sitelib
- Own the elementtree dir in site-packages
- BuildRequire python-devel
- Do not namely require expat
- Do not use INSTALLED_FILES (safer)
- Use ghosting for .pyo

* Thu Mar 17 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.2.6-1
- Version 1.2.6 of ElementTree.

* Thu Mar 10 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.2.5-1
- Rename as python-elementtree.

* Sat Mar  5 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.2.5-1
- Initial RPM release.
