# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name cElementTree

Summary: Fast XML parser and writer (written in C)
Name: python-celementtree
%define real_version 1.0.5-20051216
Version: 1.0.5
Release: 2%{?dist}
License: MIT
Group: Development/Libraries
URL: http://effbot.org/zone/celementtree.htm

Source: http://effbot.org/media/downloads/cElementTree-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, expat-devel, python-devel
Requires: python >= %{python_version}, expat
Conflicts: python-elementtree

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
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README samples/
%{python_sitearch}/cElementTree.so

%changelog
* Mon Apr 21 2008 Matthias Saou <http://freshrpms.net/> 1.0.5-2
- Actually update to 1.0.5 by fixing real_version (was still 1.0.2).
- Update source URL.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Mon May 09 2005 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
