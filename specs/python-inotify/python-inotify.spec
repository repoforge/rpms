# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Python module implementing Linux inotify support
Name: python-inotify
Version: 0.0.6
Release: 1
License: UNKNOWN
Group: Development/Libraries
URL: http://www.amautacorp.com/staff/Rudd-O/projects/search-services/

Source: http://www.amautacorp.com/staff/Rudd-O/projects/files/search-services/python-inotify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python >= %{python_version}

%description
python-inotify is a Python interface to the Linux inotify file
notification system.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README TODO
%{_bindir}/inotify
%{python_sitearch}/FSTree.py
%{python_sitearch}/FSTree.pyc
%{python_sitearch}/_inotify.so
%{python_sitearch}/inotify.py
%{python_sitearch}/inotify.pyc

%changelog
* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
