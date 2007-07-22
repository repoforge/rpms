# $Id$
# Authority:    hadams

%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           python-CDDB
Version:        1.4
Release:        2
Summary:        CDDB and FreeDB audio CD track info access in Python

Group:          Development/Languages
License:        GPL
URL:            http://cddb-py.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/cddb-py/CDDB-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel

%description
This is actually a set of three modules to access the CDDB and FreeDB
online databases of audio CD track titles and information. It includes
a C extension module to fetch track lengths under Linux, FreeBSD,
OpenBSD, Mac OS X, Solaris, and Win32, which is easily ported to other
operating systems.

%prep
%setup -q -n CDDB-%{version}
%{__sed} -e '/^#!/,1d' < CDDB.py > CDDB.py.tmp
mv CDDB.py.tmp CDDB.py
%{__sed} -e '/^#!/,1d' < DiscID.py > DiscID.py.tmp
mv DiscID.py.tmp DiscID.py

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc CHANGES COPYING README
%{python_sitearch}/*

%changelog
* Sun Jul 22 2007 Heiko Adams <info@fedora-blog.de> - 1.4-2
- rebuild for rpmforge

* Mon Dec 11 2006 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4-1
- First version for Fedora Extras

