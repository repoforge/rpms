# Authority: dag
# Distcc: 0

%define rversion 2.00pre3

Summary: Unusual TCP/IP testing tools.
Name: paketto
Version: 2.00
Release: 0.pre3
License: GPL
Group: Applications/Internet
URL: http://www.doxpara.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.doxpara.com/%{name}-%{rversion}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libpcap, bison, flex

%description
The Paketto Keiretsu is a collection of tools that use new and unusual
strategies for manipulating TCP/IP networks.

This package includes:

	scanrand (very fast port, host, and network trace scanner),
	minewt (user space NAT/MAT gateway)
	linkcat(lc) (provides direct access to the network level 2)
	paratrace (traceroute-like tool using existing TCP connections)
and	phentropy (plots a large data source onto a 3D matrix)

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{rversion}

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
* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 2.00-0.pre3
- Initial package. (using DAR)
