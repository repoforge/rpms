# $Id$
# Authority: dag
# Upstream: Thomas Dzubin <dzubin$vcn,bc,ca>

Summary: Utility to ping multiple hosts at once
Name: fping
Version: 3.3
Release: 1%{?dist}
License: distributable
Group: Applications/Internet
URL: http://www.fping.org/

Source: http://fping.org/dist/fping-%{version}.tar.gz
Patch0: fping-ac_fixes.patch
Patch1: fping-ipv6.patch
Patch2: fping-ipv6-ac.patch
Patch3: fping-2.4b2-fflush.patch
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
%setup
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1
#{__aclocal}
#{__autoconf}
#{__autoheader}
#{__automake} --add-missing

%build
%configure --program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}
%{__mv} -f src/fping src/fping6

%configure \
    --program-prefix="%{?_program_prefix}" \
    --disable-ipv6
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m4755 src/fping6 %{buildroot}%{_sbindir}/fping6
%{__ln_s} -f fping.8 %{buildroot}%{_mandir}/man8/fping6.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%doc %{_mandir}/man8/fping.8*
%doc %{_mandir}/man8/fping6.8*

%defattr(4755, root, root)
%{_sbindir}/fping
%{_sbindir}/fping6

%changelog
* Thu Aug 30 2012 Dag Wieers <dag@wieers.com> - 3.3-1
- Updated to release 3.3.

* Fri Jun 08 2012 Dag Wieers <dag@wieers.com> - 3.2-1
- Updated to release 3.2.

* Fri Jan 20 2012 Dag Wieers <dag@wieers.com> - 3.0-1
- Updated to release 3.0.

* Tue Jun 29 2010 Dag Wieers <dag@wieers.com> - 2.4-1.b2.3
- Cosmetic changes.

* Tue Feb 15 2005 Ken Tsukahara <ken.tsukahara@tmt-d.co.jp> 2.4-1.b2
- Flush stdout for each line.
- Fix stdout/stderr confusion in Patch1.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.4-0.b2
- Adapted version to new scheme.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 2.4b2-0
- Initial package. (using DAR)
