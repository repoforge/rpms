# $Id$
# Authority: dag

Summary: ARP reply daemon
Name: arpd
Version: 0.2
Release: 1.2
License: OpenSource
Group: Applications/Internet
URL: http://www.citi.umich.edu/u/provos/arpd/

Source: http://www.citi.umich.edu/u/provos/honeyd/arpd-%{version}.tar.gz
Patch: arpd-0.2-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libevent-devel, libpcap
Provides: farpd = %{version}-%{release}

%description
arpd replies to any ARP request for an IP address matching the specified
destination net with the hardware MAC address of the specified interface,
but only after determining if another host already claims it.

%prep
%setup -n %{name}
%patch0 -p1

%{__perl} -pi.orig -e 's|/lib/|/%{_lib}/|g' configure

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
%doc %{_mandir}/man8/arpd.8*
%{_sbindir}/arpd

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 0.2-2
- Fixed a problem with gcc4. (Francisco Monserrat)

* Thu Jan 20 2005 Dag Wieers <dag@wieers.com> - 0.2-1
- Fixed a problem with newer gcc.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
