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

# Where the kernel build tree lives for post 2.6
%define basedeveldir %{_libdir}/kernel-module-devel-%{krel}
%define develdir %{basedeveldir}/kernel%{ktype}-%{krel}.%{_target_cpu}.rpm

# Do we want to put the module into "updates" (don't define for "no")
#define updates /updates


Summary: Driver for Intel® PRO/Wireless 2100 network adaptors
Name: kernel-module-ipw2100
Version: 0.46_3
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://ipw2100.sourceforge.net/
Source: http://dl.sf.net/ipw2100/ipw2100-%{version}.tgz
Patch: ipw2100.autotools.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{post26}
BuildRequires: kernel-module-devel-%{krel}
BuildRequires: kernel-module-hostap-devel-%{krel}
%else
BuildRequires: kernel-source = %{krel}
BuildRequires: kernel-module-hostap-%{krel}
%endif
BuildRequires: autoconf, automake

%description
This package contains a kernel module for the Intel® PRO/Wireless 2100
network adaptors, found for instance in Centrino laptops.

To rebuild this package you should use :
--define "kernel <uname -r output>"
--target <arch>


%package %{kernel}
Summary: Driver for Intel® PRO/Wireless 2100 network adaptors
Group: System Environment/Kernel
Provides: %{name} = %{version}-%{release}, kernel-module
Requires(post): modutils
Requires(postun): modutils
Requires: /boot/vmlinuz-%{kernel}
# We require the hostap module
Requires: kernel-module-hostap-%{krel}
# And firmware too
Requires: ipw2100-firmware

%description %{kernel}
This package contains a kernel module for the Intel® PRO/Wireless 2100
network adaptors, found for instance in Centrino laptops.


%prep
%setup -q -n ipw2100-%{version}
%patch -p2


%build
sh autogen.sh || :
%if %{post26}
%configure \
    --with-linuxdir="%{develdir}"
#   --disable-legacy-fw-load
%else
%configure \
    --with-rpm-target="%{_target_cpu}" \
    --with-kernel-release="%{kernel}" \
    --with-linuxdir="/usr/src/linux-%{krel}"
%endif
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall modulesdir="%{buildroot}/lib/modules/%{kernel}%{?updates}"


%clean
%{__rm} -rf %{buildroot}


%post %{kernel}
depmod -ae -F /boot/System.map-%{kernel} %{kernel} >/dev/null

%postun %{kernel}
depmod -ae -F /boot/System.map-%{kernel} %{kernel} >/dev/null


%files %{kernel}
%defattr(-, root, root, 0755)
/lib/modules/%{kernel}%{?updates}/kernel/drivers/net/wireless/ipw2100.*o


%changelog
* Tue Jun 22 2004 Matthias Saou <http://freshrpms.net> 0.46_3-1
- Re-enable legacy firmware loading, since it fails a bootup otherwise.

* Thu Jun 17 2004 Matthias Saou <http://freshrpms.net> 0.46_3-0
- Takeover the spec, make changes and update to 0.46_3.

* Tue Jun 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.45-0.fdr.4: don't build debug packages

* Fri Jun 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.45-0.fdr.3: fix requires

* Fri Jun 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.45-0.fdr.2: rebuilt against new hostap build and kernel packages
- this one works for 2.4 and 2.6

* Sat May 22 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- rebuilt for 0.45 against new hostap build packages

* Thu Apr 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- Initial package

