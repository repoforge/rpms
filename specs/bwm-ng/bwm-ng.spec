# $Id$
# Authority: dag
# Upstream: Volker Gropp <bwmng$gropp,org>

Summary: Curses based bandwidth monitor
Name: bwm-ng
Version: 0.5
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.gropp.org/

Source: http://www.gropp.org/bwm-ng/bwm-ng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Bandwidth Monitor NG is a small and simple console-based live bandwidth
monitor.

Short list of features:
- supports /proc/net/dev, netstat, getifaddr, sysctl, kstat and libstatgrab
- unlimited number of interfaces supported
- interfaces are added or removed dynamically from list
- white-/blacklist of interfaces
- output of KB/s, Kb/s, packets, errors, average, max and total sum
- output in curses, plain console, CSV or HTML
- configfile

%prep
%setup

%build
%configure \
	--enable-html \
	--enable-csv \
	--enable-extendedstats \
	--enable-configfile \
	--enable-64bit \
	--enable-netstatpath \
	--enable-netstatbyte \
	--enable-netstatlink \
	--with-ncurses \
	--with-time \
	--with-getopt_long \
	--with-getifaddrs \
	--with-sysctl \
	--with-procnetdev \
	--with-netstatlinux
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 src/bwm-ng %{buildroot}%{_bindir}/bwm-ng
%{__install} -Dp -m0644 bwm-ng.1 %{buildroot}%{_mandir}/man1/bwm-ng.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS bwm-ng.conf-example changelog README
%doc %{_mandir}/man1/bwm-ng.1*
%{_bindir}/bwm-ng

%changelog
* Thu Mar 03 2005 Dag Wieers <dag@wieers.com> - 0.5-2
- Synced with upstream SPEC file.

* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Fri Dec 10 2004 Dag Wieers <dag@wieers.com> - 0.3-2
- Fixed Group tag.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
