# $Id$
# Authority: dag
# Upstream: <mjp$pilcrow,madison,wi,us>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pynids

Summary: Python wrapper for libnids (Network Intrusion Detection System)
Name: python-nids
Version: 0.5
Release: 2.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pilcrow.madison.wi.us/pynids/

Source: http://pilcrow.madison.wi.us/pynids/pynids-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.2, libnids, libpcap, libnet, libnids
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

Requires: python >= 2.2, libpcap, libnet, libnids

%description
pynids is a python wrapper for libnids, a Network Intrusion Detection System
library offering sniffing, IP defragmentation, TCP stream reassembly and TCP
port scan detection. Let your own python routines examine (or kill) network
conversations.

%prep
%setup -n %{real_name}-%{version}

%build
%{expand: %%define optflags -O2}
CFLAGS="%{optflags} -fPIC -fomit-frame-pointer -DPIC" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING Example README
%{python_sitearch}/nidsmodule.so

%changelog
* Sat Mar 19 2005 Dag Wieers <dag@wieers.com> - 0.5-2
- Fixed left-over stuff from python-adns. (Jeff Pitman)

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
