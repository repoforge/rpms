# $Id$
# Authority: dag
# Upstream: Danny Davids <daniel,davids$cern,ch>

Summary: tool to do memory to memory performance measurements with TCP/IP.
Name: ttcp
Version: 3.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://it-div-cs.web.cern.ch/it-div-cs/public/projects/atm/ttcp.html

Source0: http://it-div-cs.web.cern.ch/it-div-cs/public/projects/atm/ttcp.c
Source1: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.1
Source2: ftp://ftp.sgi.com/sgi/src/ttcp/README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The TTCP program is used to do memory to memory performance measurements
with TCP/IP. The program we use, comes from the public domain and has
been adapted and modified by several persons.

%prep
%setup -c -T
%{__cp} -afp %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
${CC:-%{__cc}} %{optflags} -o ttcp ttcp.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ttcp %{buildroot}%{_bindir}/ttcp
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/ttcp.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.7-1.2
- Rebuild for Fedora Core 5.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 3.7-1
- Added manpage and README. (Matthew Bogosian)

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 3.7-0
- Initial package. (using DAR)
