# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name yapsnmp

Summary: Yet Another Python SNMP Module
Name: python-yapsnmp
Version: 0.7.8
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://yapsnmp.sourceforge.net/

Source: http://dl.sf.net/yapsnmp/yapsnmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: net-snmp-devel
BuildRequires: python-devel
BuildRequires: swig
Requires: net-snmp >= 5
Requires: openssl
Requires: python
Requires: zlib

%description
The yapsnmp package contains an SNMP module for the Python programming
language, built on top of the NET-SNMP toolkit. The main module tries
to be as high level as possible, removing the complexity out of using
SNMP from Python. There is also a low level module exposing most of
the toolkit's functionality, in case you need something not available
via the high level interface.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --enable-site-packages-prefix

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README doc/
%{python_sitelib}/

%changelog
* Thu Sep 15 2011 Dag Wieers <dag@wieers.com> - 0.7.8-1
- Initial package (using DAR)
