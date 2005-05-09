# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name cElementTree
%define real_version 1.0.2-20050302

Summary: Fast XML parser and writer (written in C)
Name: python-celementtree
Version: 1.0.2
Release: 1
License: MIT
Group: Development/Libraries
URL: http://effbot.org/zone/celementtree.htm

Source: http://effbot.org/downloads/cElementTree-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, expat-devel
Requires: python >= %{python_version}, expat

%description
The Element type is a simple but flexible container object, designed
to store hierarchical data structures, such as simplified XML
infosets, in memory. The element type can be described as a cross
between a Python list and a Python dictionary.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CHANGES README samples/
%{python_sitearch}/cElementTree.so

%changelog
* Mon May 09 2005 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
