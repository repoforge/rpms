# Authority: dag

# Upstream: Dug Song <dugsong@monkey.org>

Summary: Fragrouter is a network intrusion detection evasion toolkit.
Name: fragrouter
Version: 1.6
Release: 0
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/fragrouter/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Fragrouter is a network intrusion detection evasion toolkit. It
implements most of the attacks described in the Secure Networks
"Insertion, Evasion, and Denial of Service: Eluding Network Intrusion
Detection" paper of January 1998.

This program was written in the hopes that a more precise testing
methodology might be applied to the area of network intrusion
detection, which is still a black art at best. 

Conceptually, fragrouter is just a one-way fragmenting router - IP
packets get sent from the attacker to the fragrouter, which transforms
them into a fragmented data stream to forward to the victim.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -m0644 fragrouter.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%doc CHANGES CREDITS LICENSE README TODO VERSION
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Initial package. (using DAR)
