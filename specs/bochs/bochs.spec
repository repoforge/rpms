# $Id$
# Authority: dag
# Upstream: <bochs-developers$lists,sf,net>

# Distcc: 0

%define logmsg logger -t %{name}/rpm

Summary: IA-32 (x86) PC emulator
Name: bochs
Version: 2.1.1
Release: 1
License: LGPL
Group: Applications/Emulators
URL: http://bochs.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/bochs/bochs-%{version}.tar.gz
#Source1: http://bochs.sf.net/guestos/dlxlinux4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Bochs is a portable x86 PC emulation software package that emulates enough of
the x86 CPU, related AT hardware, and BIOS to run DOS, Windows '95, Minix 2.0,
and other OS's, all on your workstation. 

%prep
%setup
#setup -a 1

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
	docdir="rpm-doc"
#makeinstall install_dlx
#%{__install} -m0644 dlxlinux/* %{buildroot}%{_datadir}/bochs/dlxlinux/

%post
if [ -x %{_datadir}/bochs/install-x11-fonts ]; then
	%{_datadir}/bochs/install-x11-fonts &>/dev/null || %logmsg "Installation of fonts has failed."
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README-* TESTFORM.txt rpm-doc/* docs-html/*
#doc dlxlinux/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
#%{_libdir}/bochs/
%{_datadir}/bochs/

%changelog
* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sun Feb 01 2004 Dag Wieers <dag@wieers.com> - 2.1-0
- Updated to release 2.1.

* Sun Sep 14 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Initial package. (using DAR)
