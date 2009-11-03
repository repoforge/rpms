# $Id$
# Authority: dag
# Upstream: Jason Ish <jason$codemonkey,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Very simple ARP scanner
Name: arpscan
Version: 0.2
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ish.cx/~jason/arpscan/

Source: http://ish.cx/~jason/arpscan/arpscan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
arpscan is a very simple scanner which sends out arp requests for the
given IP addresses and displays a list of the found hosts.

%prep
%setup

### FIXME: Change NTOHL() by ntohl(). (Please fix upstream)
%{__perl} -pi.orig -e 's|NTOHL|ntohl|g' arpscan.c

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/*

%changelog
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
