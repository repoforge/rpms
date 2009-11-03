# $Id$
# Authority: dag
# Upstream: Dan Kaminsky <dan$doxpara,com>
# Distcc: 0

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Unusual TCP/IP testing tools
Name: paketto
%define real_version 2.00pre5
Version: 2.00
Release: 1.pre5.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.doxpara.com/

Source: http://www.doxpara.com/paketto-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, bison, flex
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
The Paketto Keiretsu is a collection of tools that use new and unusual
strategies for manipulating TCP/IP networks.

This package includes:

	scanrand (very fast port, host, and network trace scanner),
	minewt (user space NAT/MAT gateway)
	linkcat(lc) (provides direct access to the network level 2)
	paratrace (traceroute-like tool using existing TCP connections)
and	phentropy (plots a large data source onto a 3D matrix)

%prep
%setup -n %{name}-%{real_version}

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*

%changelog
* Fri Jan 06 2006 Dag Wieers <dag@wieers.com> - 2.00-1.pre5
- Updated to release 2.00pre5.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 2.00-1.pre3
- Cosmetic rebuild for Group-tag.

* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 2.00-0.pre3
- Initial package. (using DAR)
