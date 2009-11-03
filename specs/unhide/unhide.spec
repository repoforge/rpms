# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3: %define _without_kernel26 1}
%{?rh9: %define _without_kernel26 1}
%{?rh7: %define _without_kernel26 1}
%{?el2: %define _without_kernel26 1}


Summary: Tool to find hidden processes and TCP/UDP ports from rootkits
Name: unhide
%define real_version 20080519
Version: 0.0.20080519
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.security-projects.com/?Unhide

Source: http://www.security-projects.com/unhide%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Unhide is a forensic tool to find processes and TCP/UDP ports hidden by
rootkits, Linux kernel modules or by other techniques. It includes two
utilities: unhide and unhide-tcp.

Unhide detects hidden processes using three techniques:

 - comparing the output of /proc and /bin/ps
 - comparing the information gathered from /bin/ps with the one gathered
   from system calls (syscall scanning)
 - full scan of the process ID space (PIDs bruteforcing)

unhide-tcp identifies TCP/UDP ports that are listening but are not listed
in /bin/netstat through brute forcing of all TCP/UDP ports available.

%prep
%setup -n %{name}-%{real_version}

%build
%{?_without_kernel26:%{__cc} --static %{optflags} unhide.c -o unhide}
%{!?_without_kernel26:%{__cc} --static %{optflags} unhide-linux26.c -o unhide}
%{__cc} --static %{optflags} unhide-tcp.c -o unhide-tcp

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 unhide %{buildroot}%{_sbindir}/unhide
%{__install} -Dp -m0755 unhide-tcp %{buildroot}%{_sbindir}/unhide-tcp
%{__install} -Dp -m0644 man/unhide.8 %{buildroot}%{_mandir}/man8/unhide.8
%{__install} -Dp -m0644 man/unhide-tcp.8 %{buildroot}%{_mandir}/man8/unhide-tcp.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING *.txt
%doc %{_mandir}/man8/unhide.8*
%doc %{_mandir}/man8/unhide-tcp.8*
%{_sbindir}/unhide
%{_sbindir}/unhide-tcp

%changelog
* Tue Jul 01 2008 Dag Wieers <dag@wieers.com> - 0.0.20080519-1
- Initial package. (using DAR)
