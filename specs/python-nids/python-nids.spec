# $Id$
# Authority: dag
# Upstream: <mjp$pilcrow,madison,wi,us>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define real_name pynids

Summary: Python bindings for GNU adns library
Name: python-nids
Version: 0.5
Release: 1
License: GPL
Group: Development/Libraries
URL: http://pilcrow.madison.wi.us/pynids/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://pilcrow.madison.wi.us/pynids/pynids-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, python-devel, libnids
Requires: python >= 2.2, adns, libpcap, libnet, libnids

%description
pynids is a python wrapper for libnids, a Network Intrusion Detection System
library offering sniffing, IP defragmentation, TCP stream reassembly and TCP
port scan detection. Let your own python routines examine (or kill) network
conversations.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags} -fPIC -fomit-frame-pointer -DPIC" python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--prefix="%{_prefix}" \
	--root="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING Example README
%{python_sitearch}/*

%changelog
* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
