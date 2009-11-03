# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Cisco Discovery Protocol reporter
Name: cdpr
Version: 2.3
Release: 1%{?dist}
License: GPLv2+ 
Group: Applications/System
URL: http://sourceforge.net/projects/cdpr/

Source: http://dl.sf.net/sourceforge/cdpr/cdpr-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires: libpcap-devel}

%description
cdpr is used to decode a Cisco Disovery Protocol (CDP) packet, by default it 
will report the device ID, the IP Address (of the device), and the port
number that the machine is connected to. 
Optionally it will decode the entire CDP packet.

%prep
%setup
%{__perl} -pi -e 's|\r||g' COPYING README

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 cdpr %{buildroot}%{_bindir}/cdpr

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING license.txt README* cdprs/
%{_bindir}/cdpr

%changelog
* Sat Sep 20 2008 Dag Wieers <dag@wieers.com> - 2.3-1
- Initial package. (using DAR)
