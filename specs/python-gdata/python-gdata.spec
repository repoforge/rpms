# $Id$
# Authority: shuff

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name gdata

Summary: Google Data APIs Python Client Library
Name: python-gdata
Version: 2.0.10
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://code.google.com/p/gdata-python-client/

Source: http://gdata-python-client.googlecode.com/files/gdata-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2
BuildRequires: python-elementtree
Requires: python >= 2.2
Requires: python-elementtree

%description
The Google Data APIs (Google Data) provide a simple protocol for reading and
writing data on the web. Though it is possible to use these services with a
simple HTTP client, this library provides helpful tools to streamline your code
and keep up with server-side changes. 

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL.txt README.txt RELEASE_NOTES.txt samples/
%{python_sitelib}/*

%changelog
* Mon Jun 21 2010 Steve Huff <shuff@vecna.org> - 2.0.10-1
- Initial package.
