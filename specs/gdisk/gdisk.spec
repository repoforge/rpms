# $Id$
# Authority: dag

Summary: Fdisk-like partitioning tool for GPT disks
Name: gdisk
Version: 0.6.8
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://www.rodsbooks.com/gdisk/

Source: http://dl.sf.net/gptfdisk/gdisk-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: libuuid-devel
#BuildRequires: popt-devel

%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%setup

%build
%{__make} CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 gdisk.8 %{buildroot}%{_mandir}/man8/gdisk.8
%{__install} -p -m0644 sgdisk.8 %{buildroot}/%{_mandir}/man8/sgdisk.8
%{__install} -Dp -m0755 gdisk %{buildroot}%{_sbindir}/gdisk
%{__install} -p -m0755 sgdisk %{buildroot}%{_sbindir}/sgdisk

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man8/gdisk.8*
%doc %{_mandir}/man8/sgdisk.8*
%{_sbindir}/gdisk
%{_sbindir}/sgdisk

%changelog
* Mon Aug 16 2010 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Initial package. (using DAR)
