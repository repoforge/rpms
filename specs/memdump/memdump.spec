# $Id$
# Authority: dag

Summary: Tool to dump memory
Name: memdump
Version: 1.01
Release: 1%{?dist}
License: GPL
Group: Utilities
URL: http://www.porcupine.org/forensics/tct.html

Source: http://www.porcupine.org/forensics/memdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
What can you expect to find in a system memory dump? Bits from the
operating system, from running processes, and from every file and
directory that has been accessed recently. Depending on the operating
system you may even find some information from deleted files and
exited processes, although that information tends to be short-lived.

To dump physical memory: 

    memdump | nc host port
    memdump | openssl s_client -connect host:port

For best results send output off-host over the network. Writing to      
file risks clobbering all the memory in the file system cache. Use
netcat, stunnel, or openssl, depending on your requirements.

%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 memdump %{buildroot}%{_bindir}/memdump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{_bindir}/memdump

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
