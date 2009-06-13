# $Id$
# Authority: dries
# Upstream: J. Alexander Treuman <jat$spatialrift,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Python MPD client library
Name: python-mpd
Version: 0.2.1
Release: 1
License: GPL
Group: Development/Libraries
URL: http://pypi.python.org/pypi/python-mpd/

Source: http://pypi.python.org/packages/source/p/python-mpd/python-mpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel
Requires: python

%description
An MPD (Music Player Daemon) client library written in pure Python.

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
%doc *.txt PKG-INFO doc
%{python_sitelib}/mpd.p*
%{python_sitelib}/python_mpd*.egg-info

%changelog
* Fri Jun  5 2009 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Initial package.
