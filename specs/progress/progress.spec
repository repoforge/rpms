# $Id$
# Authority: dag

Summary: File I/O Progress Monitor Utility
Name: progress
Version: 1.10
Release: 1%{?dist}
License: BSD
Group: Applications/System
URL: http://progress.unixdev.net/

Source: http://ftp.unixdev.net/pub/debian-udev/pool/main/p/progress/progress_%{version}.orig.tar.gz
Patch1: http://ftp.unixdev.net/pub/debian-udev/pool/main/p/progress/progress_%{version}-2.diff.gz
Patch2: progress-1.10-makefile.patch
Patch3: progress-1.10-asm.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The progress utility allows progress to be monitored of file I/O.
It includes support for gzip-compressed files, so "progress -z -f file.tar.gz
tar xf -" would show progress of extracting file.tar.gz.

It's a port of the original NetBSD progress utility to Linux and Solaris.

%prep
%setup -n %{name}
%patch1 -p1
%patch2
%patch3

%build
%{__chmod} +x ./configure
./configure

%{__make} %{?_smp_mflags} CC="%{__cc}" CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 progress %{buildroot}%{_bindir}/progress
%{__install} -Dp -m0755 progress.1 %{buildroot}%{_mandir}/man1/progress.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/progress.1*
%{_bindir}/progress

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Initial package. (using DAR)
