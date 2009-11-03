# $Id$
# Authority: dag
# Upstream: <bochs-developers$lists,sf,net>

# Distcc: 0


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define logmsg logger -t %{name}/rpm

Summary: IA-32 (x86) PC emulator
Name: bochs
Version: 2.2.1
Release: 1%{?dist}
License: LGPL
Group: Applications/Emulators
URL: http://bochs.sf.net/

Source: http://dl.sf.net/bochs/bochs-%{version}.tar.gz
#Source1: http://bochs.sf.net/guestos/dlxlinux4.tar.gz
Patch: bochs-2.1.1-gcc342.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
Bochs is a portable x86 PC emulation software package that emulates enough of
the x86 CPU, related AT hardware, and BIOS to run DOS, Windows '95, Minix 2.0,
and other OS's, all on your workstation.

%prep
%setup
#setup -a 1
#patch -b .gcc243

%build
%configure \
	--enable-4meg-pages \
	--enable-cdrom \
	--enable-icache \
	--enable-ne2000 \
	--enable-pae \
	--enable-pci \
	--enable-sb16="linux" \
	--enable-vbe \
	--enable-all-optimizations
#	--with-all-libs
#	--enable-plugins
#	--enable-sse="2"

%{__perl} -pi.orig -e 's|/usr/lib/|%{_libdir}/|' Makefile

%{__make} %{?_smp_mflags}
### must use prefix=/usr since this step sets up the paths in dlx bochsrc file.
#%{__make} %{?_smp_mflags} unpack_dlx

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir} \
			%{buildroot}%{_datadir}/bochs/dlxlinux/
%makeinstall \
	docdir="doc-rpm"
#makeinstall install_dlx
#%{__install} -p -m0644 dlxlinux/* %{buildroot}%{_datadir}/bochs/dlxlinux/

%post
if [ -x %{_datadir}/bochs/install-x11-fonts ]; then
	%{_datadir}/bochs/install-x11-fonts &>/dev/null || %logmsg "Installation of fonts has failed."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README-* TESTFORM.txt doc-rpm/* docs-html/*
#doc dlxlinux/*.txt
%doc %{_mandir}/man?/*
%exclude %{_mandir}/man1/bochs-dlx.1*
%{_bindir}/*
#%{_libdir}/bochs/
%{_datadir}/bochs/

%changelog
* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 2.2.1-2
- Excluded bochs-dlx manpage.

* Sun Dec 11 2005 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Added patch for fc3/i386. (Nigel Smith)

* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Feb 01 2004 Dag Wieers <dag@wieers.com> - 2.1-0
- Updated to release 2.1.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Initial package. (using DAR)
