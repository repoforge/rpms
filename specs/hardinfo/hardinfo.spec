# $Id$
# Authority: dag
# Upstream: Leandro Pereira <leandro@hardinfo.org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Displays information about your hardware and operating system
Name: hardinfo
Version: 0.5.1
Release: 1
License: GPL
Group: Applications/System
URL: http://hardinfo.org/

Source: http://download.berlios.de/hardinfo/hardinfo-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.6, pciutils
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: pciutils

%description
HardInfo is a small application that displays information about your
hardware and operating system. Currently it knows about PCI, ISA PnP,
USB, IDE, SCSI, Serial and parallel port devices.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/hardinfo
%{_datadir}/applications/hardinfo.desktop
%{_datadir}/hardinfo/
%{_libdir}/hardinfo/

%changelog
* Fri Apr 17 2009 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.4.2.3-1
- Updated to release 0.4.2.3.

* Sat Jul 21 2007 Dag Wieers <dag@wieers.com> - 0.4.2.2-1
- Updated to release 0.4.2.2.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.4.2.1-1
- Updated to release 0.4.2.1.

* Wed Apr 04 2007 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Thu Feb 02 2006 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Fri Oct 31 2003 Dag Wieers <dag@wieers.com> - 0.3.6-0
- Updated to release 0.3.6.

* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.3.5-0
- Updated to release 0.3.5.

* Mon Jun 23 2003 Dag Wieers <dag@wieers.com> - 0.3.4-0
- Updated to release 0.3.4.

* Sat Jun 21 2003 Dag Wieers <dag@wieers.com> - 0.3.3-0
- Initial package. (using DAR)
