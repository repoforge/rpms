# $Id$

# Authority: dag

Summary: Squid native log format (NLF) analyzer and report generator
Name: calamaris
Version: 2.57
Release: 0
License: GPL
Group: Applications/Internet
URL: http://calamaris.cord.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
		%{buildroot}%{_mandir}/man1
%{__install} -m0755 calamaris %{buildroot}%{_bindir}
%{__install} -m0644 calamaris.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES EXAMPLES README
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.57-0
- Initial package. (using DAR)
