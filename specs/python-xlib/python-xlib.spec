# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Complete X11R6 client-side implementation
Name: python-xlib
Version: 0.13
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://sourceforge.net/projects/python-xlib

Source: http://dl.sf.net/python-xlib/python-xlib-%{version}.tar.gz
Patch0: python-xlib-0.13-recvbuff.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel

%description
The Python X Library is a complete X11R6 client-side implementation, written 
in pure Python. It can be used to write low-levelish X Windows client 
applications in Python.

%prep
%setup
%patch -p0

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README TODO
%{python_sitelib}/Xlib/

%changelog
* Tue Jan 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.
