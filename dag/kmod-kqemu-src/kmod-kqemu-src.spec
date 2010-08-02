# $Id$
# Authority: dag

# ExclusiveDist: el5
# Archs: i686 x86_64

# Tag: test

%define kversion 2.6.18-164.10.1.el5
%{!?kversion:%define kversion %(rpm -q kernel-devel --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

# Define the kmod package name here.
%define kmod_name kqemu

Summary: Kernel module for the QEMU accelerator
Name: kmod-kqemu-src
%define real_version 1.4.0pre1
Version: 1.4.0
Release: 0.1.pre1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://fabrice.bellard.free.fr/qemu/

Source: http://www.nongnu.org/qemu/kqemu-%{real_version}.tar.gz
Source10: kmodtool-%{kmod_name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i686 x86_64

# Define the variants for each architecture.
%define basevar ""
%ifarch i686
%define paevar PAE
%endif
%ifarch i686 x86_64
%define xenvar xen
%endif

# If kvariants isn't defined on the rpmbuild line, build all variants for this architecture.
%{!?kvariants: %define kvariants %{?basevar} %{?xenvar} %{?paevar}}

# Magic hidden here.
%define kmodtool sh %{SOURCE10}
%{expand:%(%{kmodtool} rpmtemplate_kmp %{kmod_name} %{kversion} %{kvariants} 2>/dev/null)}

%description
This package provides the kernel module for the QEMU accelerator.
The QEMU accelerator kernel module, a host driver to achieve near native
performances when using QEMU as a virtualizer.

It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the CentOS kernel and not on any one specific build.

%prep
%setup -c -T -a 0
for kvariant in %{kvariants} ; do
    %{__cp} -av %{kmod_name}-%{real_version} _kmod_build_$kvariant
done

%build
for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant
    ./configure --kernel-path="${ksrc}"
    %{__make}
    popd
done

%install
export INSTALL_MOD_PATH="%{buildroot}"
export INSTALL_MOD_DIR="extra/%{kmod_name}"
for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant
    %{__make} -C "${ksrc}" modules_install M="$PWD"
    %{__install} -d ${INSTALL_MOD_PATH}/usr/lib/debug
    popd
done

# Strip the module(s).
find %{buildroot} -type f -name \*.ko -exec strip --strip-debug \{\} \;

# Configuration for udev
%{__mkdir_p} %{buildroot}/etc/udev/rules.d
%{__cat} > %{buildroot}/etc/udev/rules.d/60-kqemu.rules << 'EOF'
KERNEL=="kqemu", NAME="%k", MODE="0666"
EOF

%clean
%{__rm} -rf %{buildroot}

%changelog
* Mon May 04 2009 Dag Wieers <dag@wieers.com> - 1.4.0-0.1.pre1
- Initial package. (using DAR)
