# $Id$
# Authority: dag

Summary: Kernel spinlock metering
Name: lockstat
Version: 1.4.11
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://oss.sgi.com/projects/lockmeter/

Source0: ftp://oss.sgi.com/projects/lockmeter/download/lockstat-%{version}.tar.gz
Source1: ftp://oss.sgi.com/projects/lockmeter/download/locksort
Patch0: lockstat-1.4.11-time.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kernel-headers

%description
The Linux SMP kernel uses spinlocks to protect data structures from
concurrent, potentially conflicting accesses. lockstat allows you to
perform simple "metering" (record-keeping) of spinlock usage.

lockstat is used to instruct the kernel to turn lock metering on or off,
and to retrieve the metering data from the kernel and display it in a
human-readable format.

%prep
%setup -n %{name}
%patch0 -p1

%{__cp} -av %{SOURCE1} .

%build
%{__make} %{?_smp_mflags} LINUX_INC_ROOT="/usr/include -I./include"

%install
%{__rm} -rf %{buildroot}
#%{__make} install INSTALLROOT="%{buildroot}"
%{__install} -Dp -m0755 locksort %{buildroot}%{_sbindir}/locksort
%{__install} -Dp -m0755 lockstat %{buildroot}%{_sbindir}/lockstat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_sbindir}/locksort
%{_sbindir}/lockstat

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.4.11-1
- Initial package. (using DAR)
