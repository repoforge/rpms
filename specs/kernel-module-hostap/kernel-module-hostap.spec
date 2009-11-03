# $Id$
# Authority: matthias

# What kernel are we building for?
%{!?kernel: %define kernel %(uname -r)}
# Get the correct kernel package release by stripping kernel modifiers
%define krel %(echo %{kernel} | sed -e s/smp//g -)
# Get a type modifier for the kernel, (null) or -smp
%if %(echo %{kernel} | grep -c smp)
    %{expand:%%define ktype -smp}
%else
    %define ktype %{nil}
%endif

# What kernel "flavor" are we building for ?
%{expand:%%define post26 %(echo %{kernel} | grep "^2\.[0-4]\." >/dev/null && echo 0 || echo 1)}

# Don't build debuginfo packages for kernel modules
%define debug_package %{nil}

# Don't have build fail when i386 modules aren't packaged
%define _unpackaged_files_terminate_build 0

# Where the kernel build tree lives for post 2.6
%define basedeveldir %{_libdir}/kernel-module-devel-%{krel}


Summary: Driver for Intersil Prism2/2.5/3 802.11b wireless cards
Name: kernel-module-hostap
Version: 0.1.3
Release: 0%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://hostap.epitest.fi/
Source: http://hostap.epitest.fi/releases/hostap-driver-%{version}.tar.gz
Patch0: hostap-makefile.patch
Patch1: hostap-compat.patch
Patch2: hostap-download.patch
Patch3: hostap-autotools.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{post26}
BuildRequires: kernel-module-devel-%{krel}
%else
BuildRequires: kernel-source = %{krel}
%endif
BuildRequires: autoconf, automake

%description
This is a Linux driver for wireless LAN cards based on Intersil's
Prism2/2.5/3 chipset. The driver supports a so called Host AP mode, i.e.,
it takes care of IEEE 802.11 management functions in the host computer and
acts as an access point. This does not require any special firmware for the
wireless LAN card. In addition to this, it has support for normal station
operations in BSS and possible also in IBSS.

To rebuild this package you should use :
--define "kernel <uname -r output>"
--target <arch>

Available rpmbuild rebuild options :
--without : download (build the driver without firmware download support)


%package devel-%{krel}
Summary: Headers and symbol versions for hostap
Group: Development/Libraries
Provides: %{name} = %{version}-%{release}
%if %{post26}
Requires: kernel-module-devel-%{krel}
%endif

%description devel-%{krel}
This is a Linux driver for wireless LAN cards based on Intersil's
Prism2/2.5/3 chipset. The driver supports a so called Host AP mode, i.e.,
it takes care of IEEE 802.11 management functions in the host computer and
acts as an access point. This does not require any special firmware for the
wireless LAN card. In addition to this, it has support for normal station
operations in BSS and possible also in IBSS.

This package contains headers and symbol versions for all archs and types
of kernel.


%package %{kernel}
Summary: Driver for Intersil Prism2/2.5/3 802.11b wireless cards
Group: System Environment/Kernel
Provides: %{name} = %{version}-%{release}, kernel-module
Requires(post): modutils
Requires(postun): modutils
Requires: /boot/vmlinuz-%{kernel}

%description %{kernel}
This is a Linux driver for wireless LAN cards based on Intersil's
Prism2/2.5/3 chipset. The driver supports a so called Host AP mode, i.e.,
it takes care of IEEE 802.11 management functions in the host computer and
acts as an access point. This does not require any special firmware for the
wireless LAN card. In addition to this, it has support for normal station
operations in BSS and possible also in IBSS.


%prep
%setup -q -n hostap-driver-%{version}
%patch0 -p0
%patch1 -p1
%{!?_without_download:%patch2 -p1}
%patch3 -p2


%if %{post26}

# if "lowest" arch (i.e. i386), build enough times to get all devel stuff
# if "higher" arch (i.e. i586/i686), just build the module
%build
# All build is actually done in install


%install
%{__rm} -rf %{buildroot}
echo "Post 2.6 build, devel package"
%ifarch i386
    %define types "" "-smp"
    # i386 is last in order to leave the correct files around
    %define targets i686 i586
%else
    %define types ""
    %define targets %{_target_cpu}
%endif
# Build and install as many times as necessary to get all development files
sh autogen.sh || true
for type in %{types}
do
    for target in %{targets}
    do
        %define develdir %{basedeveldir}/kernel${type}-%{krel}.${target}.rpm
        %configure --with-linuxdir="%{develdir}"
        %{__make} clean
        %{__make} %{?_smp_mflags}
        %makeinstall \
            modulesdir="%{buildroot}/lib/modules/%{kernel}" \
            modulesdeveldir="%{buildroot}%{develdir}"
  done
done


%else # if %{post26}

%build
echo "Pre 2.6 build, kernel%{ktype}-%{krel}.%{_target_cpu} package"
%define develdir /usr/src/linux-%{krel}
sh autogen.sh || true
%configure \
    --with-rpm-target="%{_target_cpu}" \
    --with-kernel-release="%{kernel}" \
    --with-linuxdir="%{develdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
    modulesdir=%{buildroot}/lib/modules/%{kernel} \
    modulesdeveldir=%{buildroot}%{develdir}

%endif # if %{post26}, else


%clean
%{__rm} -rf %{buildroot}


%post %{kernel}
depmod -ae -F /boot/System.map-%{kernel} %{kernel} >/dev/null

%postun %{kernel}
depmod -ae -F /boot/System.map-%{kernel} %{kernel} >/dev/null


# This devel package is only useful for post 2.6
%if %{post26}
# Only create devel package for "lowest" archs (i.e. i386 for x86), and make
# it contain all possible devel files, so exclude "high" archs here
%ifnarch i586 i686 athlon
%files devel-%{krel}
%defattr(-, root, root, 0755)
%{basedeveldir}/*/*.symvers
%dir %{basedeveldir}/*/include/modules/hostap
%{basedeveldir}/*/include/modules/hostap/hostap_crypt.h
%endif
%endif

%ifnarch i386
%files %{kernel}
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%verify(not mtime) %config /etc/pcmcia/hostap_cs.conf
/lib/modules/%{kernel}/kernel/drivers/net/wireless/hostap*.*o
# For pre 2.6, we include the .ver files in the devel package directly
%if !%{post26}
/usr/src/linux-%{krel}/include/linux/modules/hostap.ver
/usr/src/linux-%{krel}/include/modules/hostap/hostap_crypt.h
%endif
%endif


%changelog
* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net/> 1.3-0
- Fork off, yes, I'm nasty and selfish.
- Changed most conditionals, the only remaining side-effect should be that
  no i386 kernel module will be built for kernels < 2.6.

* Tue Jun 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.3-0.fdr.3: never fail on autogen

* Thu Jun 03 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.3-0.fdr.2: integrated both pre and post 2.6 builds

* Sat May 22 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.3-0.fdr.1: new upstream version

* Sat May 22 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.2-0.fdr.6: use our patch system that works with linux 2.6

* Sat Apr 17 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.2-0.fdr.5: package hostap.ver so packages can be rebuilt that need it

* Wed Jan 14 2004 Steven Pritchard <steve@kspei.com> 0.1.2-0.fdr.4
- Add "--without download" to the description

* Sat Dec 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.fdr.3
- Really honor --target.
- New version of kmodhelper.

* Sat Dec 20 2003 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2-0.fdr.2
- Major specfile simplifications, no more hardcoded kernel variants.
- Honor --target and kernel CC properly.
- Run depmod only if installing/uninstalling modules for the running kernel.

* Thu Nov 20 2003 Steven Pritchard <steve@kspei.com> 0.1.2-0.fdr.1
- Second Fedora release candidate
- Fixed to (hopefully) easily allow building for various kernels

* Wed Nov 19 2003 Steven Pritchard <steve@kspei.com> 0.1.2-0.fdr.0.1
- First Fedora release candidate

* Mon Nov 17 2003 Steven Pritchard <steve@kspei.com> 0.1.2
- Updated to 0.1.2

* Thu Oct 30 2003 Steven Pritchard <steve@kspei.com> 0.1.1
- Initial packaging

