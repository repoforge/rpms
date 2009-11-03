# $Id$
# Authority: dag


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Active operating system fingerprinting tool
Name: xprobe2
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sys-security.com/blog/xprobe2/

Source: http://dl.sf.net/xprobe/xprobe2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Xprobe is an alternative to some tools which are heavily dependent upon the
usage of the TCP protocol for remote active operating system fingerprinting.

Xprobe I combines various remote active operating system fingerprinting methods
using the ICMP protocol, which were discovered during the "ICMP Usage in
Scanning" research project, into a simple, fast, efficient and a powerful way
to detect an underlying operating system a targeted host is using.

Xprobe2 is an active operating system fingerprinting tool with a different
approach to operating system fingerprinting. Xprobe2 rely on fuzzy signature
matching, probabilistic guesses, multiple matches simultaneously, and a
signature database. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING CREDITS README TODO docs/*
%doc %{_mandir}/man1/xprobe2.1*
%config(noreplace) %{_sysconfdir}/xprobe2/
%{_bindir}/xprobe2

%changelog
* Mon May 07 2007 Dag Wieers <dag@wieers.coM> - 0.3-1
- Initial package. (using DAR)
