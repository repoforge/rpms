# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Fabrice Bellard <fabrice$bellard,org>

#%define _use_internal_dependency_generator 0

Summary: CPU emulator
Name: qemu
Version: 0.6.0
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://fabrice.bellard.free.fr/qemu/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fabrice.bellard.free.fr/qemu/qemu-%{version}.tar.gz
Patch: qemu-0.5.5-glibc-private.patch
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
#%{?fc2:%patch0}

%build
%configure

%{__perl} -pi.orig -e '
		s|\$\(sharedir\)|\$(datadir)/qemu|;
		s|\$\(prefix\)/bin|\$(bindir)|;
		s|/usr/share|\$(datadir)|;
	' Makefile* config-host.mak

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

#echo -e "#!/bin/sh\nexec %{__find_requires} | grep -v GLIBC_PRIVATE" >%{_builddir}/%{buildsubdir}/find-requires
#chmod +x %{_builddir}/%{buildsubdir}/find-requires
#%define __find_requires %{_builddir}/%{buildsubdir}/find-requires

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING* README* TODO *.html
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/qemu/
%exclude %{_docdir}

%changelog
* Tue Jul 20 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Updated to release 0.6.0.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.5.5-3
- Fixed SDL relocation error on fc2. (David Woodhouse)

* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.5.5-2
- Fixed libc.so.6(GLIBC_PRIVATE) dependency for fc2. (Christopher Stone)

* Wed May 12 2004 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Initial package. (using DAR)
