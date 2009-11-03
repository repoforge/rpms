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

# The snapshot date
%define date 20040821

Summary: Driver for ADMTek 8211 network adaptors
Name: kernel-module-adm8211
Version: 0.0
Release: 0.%{date}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://aluminum.sourmilk.net/adm8211/
Source: http://aluminum.sourmilk.net/adm8211/adm8211-%{date}.tar.bz2
Patch: adm8211-20040821-autotools.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{post26}
BuildRequires: kernel-module-devel-%{krel}
%else
BuildRequires: kernel-source = %{krel}
%endif
BuildRequires: autoconf, automake

%description
This package contains a kernel module for the ADMTek 8211 based wireless
network adaptors.

To rebuild this package you should use :
--define "kernel <uname -r output>"
--target <arch>


%package %{kernel}
Summary: Driver for ADMTek 8211 network adaptors
Group: System Environment/Kernel
Provides: %{name} = %{version}-%{release}, kernel-module
Requires(post): modutils
Requires(postun): modutils
Requires: /boot/vmlinuz-%{kernel}

%description %{kernel}
This package contains a kernel module for the ADMTek 8211 based wireless
network adaptors.


%prep
%setup -n adm8211
%patch -p1


%build
sh autogen.sh || :
%if %{post26}
%configure \
    --with-linuxdir="%{develdir}"
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
/lib/modules/%{kernel}%{?updates}/kernel/drivers/net/wireless/adm8211.*o


%changelog
* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net> 0.0-0.20040821
- Update to 20040821, updated the autotools patch.

* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net> 0.0-0.20040705
- Initial RPM release with autotools patch based on Thomasvs' work.

