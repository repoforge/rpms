# $Id$
# Authority: dag
# Upstream: Adrian Bunk <bunk@kernel.org>

# ExclusiveDist: el3 el4 el5

%{?el3:%define _without_gettextdevel 1}

%define real_name util-linux
%define real_version 2.13-pre7

Summary: Curses based disk partition table manipulator
Name: cfdisk
Version: 2.13
Release: 0.0.1%{?dist}
License: distributable
Group: System Environment/Base
URL: http://www.kernel.org/pub/linux/utils/util-linux/

Source: http://www.kernel.org/pub/linux/utils/util-linux/testing/util-linux-%{real_version}.tar.bz2
Patch0: util-linux-2.13-pre7-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel
%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}

Conflicts: util-linux > 2.13

%description
cfdisk is a curses based program for partitioning any hard disk drive.

%prep
%setup -n %{real_name}-%{real_version}
%patch0 -p1

%build
%configure
%{__make} -C fdisk %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 fdisk/cfdisk %{buildroot}%{_sbindir}/cfdisk
%{__install} -Dp -m0755 fdisk/cfdisk.8 %{buildroot}%{_mandir}/man8/cfdisk.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README fdisk/README.cfdisk
%doc %{_mandir}/man8/cfdisk.8*
%{_sbindir}/cfdisk

%changelog
* Sat Jun 26 2010 Dag Wieers <dag@wieers.com> - 2.13-0.0.1
- Updated to release 2.13-pre7

* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 2.12r-0.1
- Initial package. (using DAR)
