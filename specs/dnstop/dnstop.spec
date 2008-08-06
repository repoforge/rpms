# $Id$
# Authority: dag
# Upstream: Duane Wessels <wessels$measurement-factory,com>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Displays various tables of DNS traffic on your network
Name: dnstop
%define real_version 20080502
Version: 0.0.20080502
Release: 1
License: BSD
Group: Applications/Internet
URL: http://dns.measurement-factory.com/tools/dnstop/

Source: http://dns.measurement-factory.com/tools/dnstop/src/dnstop-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, ncurses-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network, including tables of source and
destination IP addresses, query types, top level domains and second
level domains.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
#%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -DUSE_IPV6=1 -DUSE_PPP=0"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__make} install DESTDIR="%{buildroot}" \
    bindir="%{buildroot}%{_sbindir}" \
    mandir="%{buildroot}%{_mandir}"
#%{__install} -Dp -m0755 dnstop %{buildroot}%{_sbindir}/dnstop
#%{__install} -Dp -m0644 dnstop.8 %{buildroot}%{_mandir}/man8/dnstop.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE
%doc %{_mandir}/man8/dnstop.8*
%{_sbindir}/dnstop

%changelog
* Wed Aug 06 2008 Dag Wieers <dag@wieers.com> - 0.0.20080502-1
- Updated to release 20080502.

* Sat Mar 08 2008 Dag Wieers <dag@wieers.com> - 0.0.20070510-1
- Updated to release 20070510.

* Wed Sep 03 2003 Dag Wieers <dag@wieers.com> - 0.0.20030228-0
- Initial package. (using DAR)
