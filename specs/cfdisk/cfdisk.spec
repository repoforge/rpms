# $Id$
# Authority: dag
# Upstream: Adrian Bunk <bunk@kernel.org>

# ExclusiveDist: el2 rh7 rh9 el3 el4 el5


%{?el3:%define _without_gettextdevel 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh7:%define _without_gettextdevel 1}
%{?el2:%define _without_gettextdevel 1}

%define real_name util-linux

Summary: Curses based disk partition table manipulator
Name: cfdisk
Version: 2.12r
Release: 0.1%{?dist}
License: distributable
Group: System Environment/Base
URL: ftp://ftp.kernel.org/pub/linux/utils/util-linux/

Source: ftp://ftp.kernel.org/pub/linux/utils/util-linux/util-linux-%{version}.tar.bz2
Patch0: util-linux-2.12r-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel
%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}

Conflicts: util-linux > 2.13

%description
cfdisk is a curses based program for partitioning any hard disk drive.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 fdisk/cfdisk %{buildroot}%{_sbindir}/cfdisk
%{__install} -Dp -m0755 fdisk/cfdisk.8 %{buildroot}%{_mandir}/man8/cfdisk.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY MAINTAINER fdisk/README.cfdisk
%doc %{_mandir}/man8/cfdisk.8*
%{_sbindir}/cfdisk

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 2.12r-0.1
- Initial package. (using DAR)
