# $Id$

# Authority: dag

%define rversion 2.4b2

Summary:  A utility to ping multiple hosts at once.
Name: fping
Version: 2.4
Release: 0.b2
License: distributable
Group: Applications/Internet
URL: http://www.fping.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.fping.com/download/%{name}-%{rversion}.tar.gz
Patch0: fping-ac_fixes.patch
Patch1: fping-ipv6.patch
Patch2: fping-ipv6-ac.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: autoconf, automake

%description
fping is a ping-like program which uses the Internet Control Message
Protocol (ICMP) echo request to determine if a target host is responding.

fping is different from ping in that you can specify any number of hosts
on the command line, or specify a file containing the lists of hosts to
ping. Instead of trying one host until it timeouts or replies, fping will
send out a ping packet and move on to the next host in a round-robin fashion.
If a host replies, it is noted and removed from the list of hosts to check.
If a host does not respond within a certain time limit and/or retry limit it
will be considered unreachable.

%prep
%setup -n %{name}-%{rversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} --add-missing

%build
%configure
%{__make} %{?_smp_mflags}
%{__mv} -f fping fping6

%configure --disable-ipv6
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -m4750 fping6 %{buildroot}%{_sbindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man8/*
%attr(4750, root, adm) %{_sbindir}/*

%changelog
* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.4-0.b2
- Adapted version to new scheme.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.4b2-0
- Initial package. (using DAR)
