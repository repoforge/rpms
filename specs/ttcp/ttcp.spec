# $Id$

# Authority: dag

# Upstream: Danny Davids <daniel.davids@cern.ch>

Summary: A tool to do memory to memory performance measurements with TCP/IP. 
Name: ttcp
Version: 3.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://it-div-cs.web.cern.ch/it-div-cs/public/projects/atm/ttcp.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%{__cp} -af %{SOURCE0} %{SOURCE1} %{SOURCE2} .

%build
${CC:-%{__cc}} %{optflags} -o ttcp ttcp.c

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 ttcp %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Aug 17 2003 Dag Wieers <dag@wieers.coM> - 3.7-1
- Added manpage and README. (Matthew Bogosian)

* Mon Aug 04 2003 Dag Wieers <dag@wieers.com> - 3.7-0
- Initial package. (using DAR)
