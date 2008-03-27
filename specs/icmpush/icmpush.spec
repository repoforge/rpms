# $Id$
# Authority: dag

Summary: Send icmp error packets to receive remote system info
Name: icmpush
%define real_version 22
Version: 2.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.securityfocus.com/data/tools/

Source: http://www.securityfocus.com/data/tools/icmpush%{real_version}.tar.gz
Patch0: icmpush-debian.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
icmpush is a program that sends icmp error packets and obtains remote info
through icmp packets. Supports spoof and broadcasting. This new release
supports the following ICMP error types: Unreach, Parameter Problem, Redirect
and Source Quench; ICMP information types: Timestamp, Address Mask Request,
Information Request, Router Solicitation (Router Discovery), Router
Advertisement (Router Discovery) and Echo Request. This program features an
excellent interface with a wide number of options (flags) and values. As an
added bonus, Slayer has included a mini-script called try_reset that tries
to reset existing telnet or rlogin connections. Your security auditing toolkit
is not complete without this program! One of the few 5-star programs.

%prep
%setup
%patch0 -p1 -b .debian

%build
%{__make} linuz

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man8/
%{__make} install INST_DIR="%{buildroot}%{_bindir}" MAN_DIR="%{buildroot}%{_mandir}/man8/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES COPYING GREETINGS IMPORTANT INSTALL LICENSE README SITES
%doc %{_mandir}/man8/icmpush.8*
%{_bindir}/icmpush

%changelog
* Wed Mar 26 2008 Oliver Hookins <oliver.hookins@anchor.com.au> - 2.2-1
- Initial packaging of icmpush
