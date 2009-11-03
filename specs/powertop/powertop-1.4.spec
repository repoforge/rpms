# $Id$
# Authority: dag
# Upstream: <power$bughost,org>

Summary: Tool that helps you find what software is using the most power
Name: powertop
Version: 1.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.linuxpowertop.org/

Source: http://www.linuxpowertop.org/download/powertop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gettext

%description
powertop is a Linux tool that finds the software component(s) that make your
laptop use more power than necessary while it is idle. As of Linux kernel
version 2.6.21, the kernel no longer has a fixed 1000Hz timer tick. This
will (in theory) give a huge power savings because the CPU stays in low
power mode for longer periods of time during system idle.

However... there are many things that can ruin the party, both inside the
kernel and in userspace. PowerTOP combines various sources of information
from the kernel into one convenient screen so that you can see how well
your system is doing, and which components are the biggest problem. 

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc Changelog COPYING README
%doc %{_mandir}/man1/powertop.1*
%{_bindir}/powertop

%changelog
* Mon May 28 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
