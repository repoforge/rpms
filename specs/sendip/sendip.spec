# $Id$

# Authority: dag

# Upstream: Mike Ricketts <mike@earth.li>

Summary: Command line tool to allow sending arbitrary IP packets
Name: sendip
Version: 2.4
Release: 0
License: GPL
Group: Applications/Internet
URL: http://www.earth.li/projectpurple/progs/sendip.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.earth.li/projectpurple/files/sendip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A command line tool to send arbitrary IP packets. It has a large number of
command line options to specify the content of every header of a NTP, BGP,
RIP, RIPng, TCP, UDP, ICMP, or raw IPv4 or IPv6 packet.  It also allows any 
data to be added to the packet.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	LIBDIR="%{_libdir}/sendip"
#	CFLAGS="%{optflags} -DSENDIP_LIBS=\"%{_libdir}/sendip\""

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	BINDIR="%{buildroot}%{_bindir}" \
	LIBDIR="%{buildroot}%{_libdir}/sendip" \
	MANDIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README TODO VERSION
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/sendip/

%changelog
* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 2.4-0
- Initial package. (using DAR)
