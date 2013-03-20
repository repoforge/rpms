# $Id$
# Authority: dag
# Upstream: <power$bughost,org>

### EL6 ships with powertop-1.11-3.1.el6
%{?el6:# Tag: rfx}

Summary: Tool that helps you find what software is using the most power
Name: powertop
Version: 2.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.lesswatts.org/projects/powertop/

Source: https://01.org/powertop/sites/default/files/downloads/powertop-%{version}.tar.bz2
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
%configure
%{__make} %{?_smp_mflags} #CFLAGS="%{optflags} -D VERSION=\"%{version}\""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc Changelog COPYING README
%doc %{_mandir}/man8/powertop.8*
%{_bindir}/powertop

%changelog
* Fri Jun 08 2012 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Fri Nov 02 2007 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Fri Aug 24 2007 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Tue Jun 19 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Mon May 28 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
