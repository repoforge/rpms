# $Id$
# Authority: dag

%define python_version %(%{__python} -c 'import sys; print sys.version.split(" ")[0]')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Python module implementing Linux inotify support
Name: python-inotify
Version: 0.1.0
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://rudd-o.com/projects/python-inotify/

Source: http://rudd-o.com/wp-content/projects/files/python-inotify/python-inotify-%{version}.tar.gz
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
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

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
%ghost %{python_sitearch}/FSTree.pyo
%ghost %{python_sitearch}/inotify.pyo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.0-1.2
- Rebuild for Fedora Core 5.

* Wed Feb 08 2006 Dag Wieers <dag@wieers.com> - 0.1.0-1
- Updated to release 0.1.0.

* Mon May 30 2005 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
