%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

%define _upstream_nvr   elementtree-1.2.6-20050316
%define _upstream_cnvr  cElementTree-1.0.2-20050302    

Name: python-elementtree
Version: 1.2.6
Release: 4
Summary: Fast XML parser and writer
Group: Development/Libraries
License: PSF
URL: http://effbot.org/zone/element-index.htm
Source0: http://effbot.org/downloads/%{_upstream_nvr}.zip
Source1: http://effbot.org/downloads/%{_upstream_cnvr}.zip
Source2: cElementTree-system-expat-setup.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: expat-devel, python-devel
Requires: python-abi = %(%{__python} -c "import sys ; print sys.version[:3]")

%description
The Element type is a simple but flexible container object, designed
to store hierarchical data structures, such as simplified XML
infosets, in memory. The element type can be described as a cross
between a Python list and a Python dictionary.

This package also includes the C implementation, %{_upstream_cnvr}.

%prep
%setup -n %{_upstream_nvr} -a 1

## Take care of cElementTree
pushd %{_upstream_cnvr}
mv -f setup.py setup.py-orig
cp -f %{SOURCE2} setup.py
cp -f README ../README-cElementTree
cp -f CHANGES ../CHANGES-cElementTree
popd


%build
%{__python} setup.py build
pushd %{_upstream_cnvr}
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
popd


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
pushd %{_upstream_cnvr}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
popd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc benchmark.py CHANGES* docs README* samples
%dir %{python_sitelib}/elementtree
%{python_sitelib}/elementtree/*.py
%{python_sitelib}/elementtree/*.pyc
%ghost %{python_sitelib}/elementtree/*.pyo
%{python_sitearch}/*.so

%changelog
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

