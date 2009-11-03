# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define curl_version %(rpm -q curl-devel --qf '%{RPMTAG_VERSION}' | tail -1)

%define real_name pycurl

Summary: Python interface to libcurl
Name: python-curl
Version: %{curl_version}
Release: 1.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pycurl.sourceforge.net/

Source: http://pycurl.sourceforge.net/download/pycurl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, curl-devel

%description
PycURL is a Python interface to libcurl. PycURL can be used to fetch
objects identified by a URL from a Python program, similar to the
urllib Python module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README INSTALL TODO doc/ examples/ tests/
%{python_sitearch}/pycurl.so
%{python_sitearch}/curl/
%exclude %{_docdir}/pycurl/

%changelog
* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - %{curl_version}-1
- Initial package. (using DAR)
