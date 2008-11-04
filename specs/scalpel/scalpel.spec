# $Id$
# Authority: dag

Summary: Frugal, high-performance file carver
Name: scalpel
Version: 1.60
Release: 1
License: GPL
Group: Applications/File
URL: http://www.digitalforensicssolutions.com/Scalpel/

Source: http://www.digitalforensicssolutions.com/Scalpel/scalpel-%{version}.tar.gz
Patch1: scalpel-1.60-configfile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Scalpel is a fast file carver that reads a database of header and footer
definitions and extracts matching files from a set of image files or raw
device files. Scalpel is filesystem-independent and will carve files from
FATx, NTFS, ext2/3, or raw partitions. It is useful for both digital
forensics investigation and file recovery.

%prep
%setup
%patch1 -p1

%{__perl} -pi -e 's|$(CC) -c|$(CC) %{optflags} -c|' Makefile
%{__perl} -pi -e 's|scalpel.conf|%{_sysconfdir}/scalpel.conf|' scalpel.h

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 scalpel %{buildroot}%{_bindir}/scalpel
%{__install} -Dp -m0644 scalpel.1 %{buildroot}%{_mandir}/man1/scalpel.1
%{__install} -Dp -m0644 scalpel.conf %{buildroot}%{_sysconfdir}/scalpel.conf

%files
%defattr(-, root, root, 0775)
%doc %{_mandir}/man1/scalpel.1*
%config(noreplace) %{_sysconfdir}/scalpel.conf
%{_bindir}/scalpel

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 1.60-1
- Initial package. (using DAR)
