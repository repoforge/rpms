# $Id$
# Authority: dag

Summary: Squid native log format (NLF) analyzer and report generator
Name: calamaris
Version: 2.59
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://calamaris.cord.de/

Source: http://calamaris.cord.de/calamaris-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl >= 0:5.00503, perl(Getopt::Std), perl(Sys::Hostname), perl(Time::Local)
AutoReq: no

%description
Calamaris parses the Squid Native Log and genereates reports
about Peak-usage, Request-Methods, Status-reports of incoming
and outgoing requests, second and Top-level destinations,
content-types and performance.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 calamaris %{buildroot}%{_bindir}/calamaris
%{__install} -Dp -m0644 calamaris.1 %{buildroot}%{_mandir}/man1/calamaris.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES EXAMPLES README
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.59-1.2
- Rebuild for Fedora Core 5.

* Tue Jun 08 2004 Dag Wieers <dag@wieers.com> - 0.59-1
- Updated to release 0.59.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.57-0
- Initial package. (using DAR)
