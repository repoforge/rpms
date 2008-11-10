# $Id$
# Authority: dag
# Upstream: Adrian Bunk <bunk@kernel.org>

# ExclusiveDist: el2 rh7 rh9 el3 el4 el5

%define real_name util-linux

Summary: Tool that recognizes ext2, FAT, swap and extended partition tables
Name: rescuept
Version: 2.12r
Release: 0.1
License: distributable
Group: System Environment/Base
URL: ftp://ftp.kernel.org/pub/linux/utils/util-linux/

Source: ftp://ftp.kernel.org/pub/linux/utils/util-linux/util-linux-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Conflicts: util-linux > 2.13

%description
rescuept is a utility that recognizes ext2 superblocks, FAT partitions, swap
partitions, and extended partition tables. It may also recognize BSD
disklabels and Unixware 7 partitions. rescuept prints out information that is
suitable as input to sfdisk to reconstruct the partition table.

%prep
%setup -n %{real_name}-%{version}/rescuept

%build
%{__cc} %{optflags} rescuept.c -o rescuept

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 rescuept %{buildroot}%{_bindir}/rescuept

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/rescuept

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 2.12r-0.1
- Initial package. (using DAR)
