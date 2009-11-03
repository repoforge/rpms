# $Id$
# Authority: dries
# Upstream: Laurent Constantin <laurent$constantin,aql,fr>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Functions for network programs
Name: netwib
Version: 5.35.0
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.laurentconstantin.com/en/netw/netwib/

Source: http://www.laurentconstantin.com/common/netw/netwib/download/v5/netwib-%{version}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Netwib provides most functions needed by network programs. Its objective is
to let programmers easily create network programs. This library provides
features for Ethernet, IPv4, IPv6, UDP, TCP, ICMP, ARP, and RARP protocols.
It supports spoofing, sniffing, client, and server creation. Furthermore,
netwib contains high level functions dealing with data handling.

This package contains the header files, the static library and development
documentation.

%prep
%setup -n %{name}-%{version}-src

%build
cd src
./genemake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd src
%makeinstall INSTINCLUDE=%{buildroot}%{_includedir} INSTLIB=%{buildroot}%{_libdir} INSTBIN=%{buildroot}%{_bindir} INSTMAN3=%{buildroot}%{_mandir}/man3

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/* README.TXT
%doc %{_mandir}/man3/netwib*
%{_bindir}/netwib*-config
%{_includedir}/netwib*/
%{_includedir}/netwib*.h
%{_libdir}/libnetwib*.a

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 5.35.0-1
- Updated to release 5.35.0.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 5.34.0-1
- Updated to release 5.34.0.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 5.33.0-1
- Updated to release 5.33.0.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 5.32.0-1
- Updated to release 5.32.0.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 5.31.0-1
- Initial package.
