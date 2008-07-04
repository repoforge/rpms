# $Id$
# Authority: dag

Summary: Low-level fullscreen SVGA graphics library
Name: svgalib
Version: 1.9.25
Release: 1
Group: System Environment/Libraries
License: Public Domain
URL: http://www.svgalib.org/

Source0: http://www.arava.co.il/matan/svgalib/svgalib-%{version}.tar.gz
Patch0: svgalib-1.9.21-makefiles.patch
Patch1: svgalib-1.4.3-fhs.patch
Patch2: svgalib-1.9.21-demos.patch
Patch3: svgalib-1.9.21-cfg.patch
Patch4: svgalib-1.9.25-kernel-2.6.26.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Exclusivearch: %{ix86} x86_64

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux.  SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Some games and
utilities use SVGAlib for their graphics. For details on
supported chipsets, see man 7 svgalib (when svgalib is installed).

%package devel
Summary: Development tools for the SVGAlib graphics library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Provides: libvga-devel = %{version}-%{release}

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%prep
%setup
%patch0 -p1 -b .makefiles
%patch1 -p1 -b .fhs
%patch2 -p1
%patch3 -p1 -b .defaultcfg
%patch4 -p1

#the testlinear demo needs svgalib's internal libvga header, so copy it to the
#demo dir
cp src/libvga.h demos

%build
#%{?_smp_mflags} doesn't work on x86_64 chances are it will fail on
#some i386 machines too.
%{__make} shared OPTIMIZE="%{optflags}" LDFLAGS= \
  prefix="%{_prefix}" \
  NO_HELPER="y" \
  INCLUDE_ET4000_DRIVER="y" \
  INCLUDE_OAK_DRIVER="y" \
  INCLUDE_MACH32_DRIVER="y" \
  INCLUDE_ET3000_DRIVER="y" \
  INCLUDE_GVGA6400_DRIVER="y" \
  INCLUDE_ATI_DRIVER="y" \
  INCLUDE_G450C2_DRIVER="y" \
  INCLUDE_ET4000_DRIVER_TEST="y" \
  INCLUDE_FBDEV_DRIVER_TEST="y" \
  INCLUDE_VESA_DRIVER_TEST="y"
make -C utils OPTIMIZE="%{optflags}" LDFLAGS="" \
  prefix="%{_prefix}"
make -C threeDKit OPTIMIZE="%{optflags} -I../gl" LDFLAGS="" \
  prefix="%{_prefix}" lib3dkit.so.%{version}


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/vga
%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__make} install \
  TOPDIR="%{buildroot}" \
  prefix="%{buildroot}%{_prefix}" \
  mandir="%{buildroot}%{_mandir}" \
  sharedlibdir="%{buildroot}%{_libdir}" \
  NO_HELPER="y" \
  MANFORMAT="compressed" \
  INSTALL_PROGRAM="install -p -m0755" \
  INSTALL_SCRIPT="install -p -m0755" \
  INSTALL_SHLIB="install -p -m0755" \
  INSTALL_DATA="install -p -m0644"
%{__ln_s} -f libvga.so.%{version} %{buildroot}%{_libdir}/libvga.so.1
%{__ln_s} -f libvgagl.so.%{version} %{buildroot}%{_libdir}/libvgagl.so.1
%{__ln_s} -f lib3dkit.so.%{version} %{buildroot}%{_libdir}/lib3dkit.so.1
#for %ghost
touch %{buildroot}%{_sysconfdir}/vga/fontdata
touch %{buildroot}%{_sysconfdir}/vga/textregs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/CHANGES doc/README.joystick doc/README.keymap lrmi-0.6m/README
%doc doc/README.multi-monitor doc/README.vesa doc/TODO doc/dual-head-howto
%doc %{_mandir}/man[^3]/*
%dir %{_sysconfdir}/vga/
%config(noreplace) %{_sysconfdir}/vga/dvorak-us.keymap
%config(noreplace) %{_sysconfdir}/vga/libvga.config
%config(noreplace) %{_sysconfdir}/vga/libvga.et4000
%config(noreplace) %{_sysconfdir}/vga/null.keymap
%ghost %{_sysconfdir}/vga/fontdata
%ghost %{_sysconfdir}/vga/textregs
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc demos doc/DESIGN doc/Driver-programming-HOWTO doc/README.patching
%doc %{_mandir}/man3/*.3*
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Thu Jul 03 2008 Dag Wieers <dag@wieers.com> - 1.9.25-1
- Initial package. (based on Fedora)
