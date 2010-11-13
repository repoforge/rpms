# $Id$
# Authority: dag

### EL6 ships with latencytop-0.5-3.el6
# DistExclusive: el2 el3 el4 el5

Summary: Kernel latency measuring tool
Name: latencytop
Version: 0.5
Release: 1%{?dist}
License: GPLv2
Group: System/Monitoring
URL: http://www.latencytop.org/

Source: http://www.latencytop.org/download/latencytop-%{version}.tar.gz
Patch0: latencytop-warning-fixes.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig

%description
LatencyTOP is a Linux* tool for software developers (both kernel and
userspace), aimed at identifying where in the system latency is
happening, and what kind of operation/action is causing the latency to
happen so that the code can be changed to avoid the worst latency
hiccups. A version with graphic interface is available as xlatencytop.

%prep
%setup
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%{__make} %{?_smp_mflags}
%{__mv} -f latencytop xlatencytop
%{__make} clean
%{__perl} -pi.orig -e 's|^HAS_GTK_GUI = 1|HAS_GTK_GUI = 0|' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 xlatencytop %{buildroot}%{_sbindir}/xlatencytop

%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 latencytop.8 %{buildroot}%{_mandir}/man8/latencytop.8
%{__ln_s} -f latencytop.8 %{buildroot}%{_mandir}/man8/xlatencytop.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/latencytop.8*
%doc %{_mandir}/man8/xlatencytop.8*
%{_datadir}/latencytop/
%{_sbindir}/latencytop
%{_sbindir}/xlatencytop

%changelog
* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
