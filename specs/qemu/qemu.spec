# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Fabrice Bellard <fabrice@bellard.org>

Summary: CPU emulator
Name: qemu
Version: 0.5.4
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://fabrice.bellard.free.fr/qemu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fabrice.bellard.free.fr/qemu/qemu-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
QEMU is a FAST! processor emulator using dynamic translation to achieve good
emulation speed. QEMU has two operating modes:

	Full system emulation. In this mode, QEMU emulates a full system (for
	example a PC), including a processor and various peripherials. It can
	be used to launch different Operating Systems without rebooting the PC
	or to debug system code.

	User mode emulation (Linux host only). In this mode, QEMU can launch
	Linux processes compiled for one CPU on another CPU. It can be used to
	launch the Wine Windows API emulator or to ease cross-compilation and
	cross-debugging. 

As QEMU requires no host kernel patches to run, it is very safe and easy to use.
QEMU is a FAST! processor emulator. By using dynamic translation it achieves a
reasonnable speed while being easy to port on new host CPUs.

%prep
%setup

%{__perl} -pi.orig -e '
		s|\$\(sharedir\)|\$(datadir)/qemu|;
		s|\$\(prefix\)/bin|\$(bindir)|;
	' Makefile*

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING* README* TODO *.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/qemu/

%changelog
* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (using DAR)
