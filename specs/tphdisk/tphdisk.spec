# $Id$
# Authority: dag
# Upstream: Andrew Tridgell <tridge$samba,org>

%define _sbindir /sbin

Summary: Create hibernation file for phoenix notebios laptops
Name: tphdisk
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://samba.org/junkcode/#tphdisk

Source: http://samba.org/ftp/unpacked/junkcode/tphdisk.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: i386

%description
A Linux replacement for phdisk.exe that allows you to create a save2dsk.bin
hibernation file for phoenix notebios laptops. Run tphdisk -h for instructions.

%prep

%build
${CC:-%{__cc}} %{optflags} -o tphdisk %{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 tphdisk %{buildroot}%{_sbindir}/tphdisk

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 18 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
