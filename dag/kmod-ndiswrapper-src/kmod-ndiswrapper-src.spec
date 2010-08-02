# $Id$
# Authority: dag

# ExclusiveDist: el5
# Archs: i686 x86_64

# Tag: test

%define kversion 2.6.18-164.10.1.el5
%{!?kversion:%define kversion %(rpm -q kernel-devel --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

# Define the kmod package name here.
%define kmod_name ndiswrapper

Summary: Kernel module for the Microsoft NDIS (Network Driver Interface Specification) API
Name: kmod-ndiswrapper-src
Version: 1.54
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://ndiswrapper.sourceforge.net/

Source0: http://dl.sf.net/ndiswrapper/ndiswrapper-%{version}.tar.gz
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
This package provides the kernel module for the Microsoft NDIS (Network Driver
Interface Specification) API. It allows the use of binary drivers written to
this specification to be run natively in the Linux kernel.

It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the CentOS kernel and not on any one specific build.

%package -n ndiswrapper
Summary: Utilities for the ndiswrapper kernel module
Group: System Environment/Kernel

%description -n ndiswrapper
The ndiswrapper utils required to use ndiswrapper.

%prep
%setup -c -T -a 0
for kvariant in %{kvariants} ; do
    %{__cp} -av %{kmod_name}-%{version} _kmod_build_$kvariant
done

%build
%{__make} -C %{kmod_name}-%{version}/utils CFLAGS="%{optflags} -I../driver"

for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant/driver
    %{__make} -C "${ksrc}" modules M="$PWD" KBUILD="${ksrc}"
    popd
done

%install
%{__rm} -rf %{buildroot}
%{__make} -C %{kmod_name}-%{version}/utils install DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/ndiswrapper
%{__install} -Dp -m0644 %{kmod_name}-%{version}/ndiswrapper.8 %{buildroot}%{_mandir}/man8/ndiswrapper.8

export INSTALL_MOD_PATH="%{buildroot}"
export INSTALL_MOD_DIR="extra/%{kmod_name}"
for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant/driver
    %{__make} -C "${ksrc}" modules_install M="$PWD"
    %{__install} -d ${INSTALL_MOD_PATH}/usr/lib/debug
    popd
done

# Strip the module(s).
find %{buildroot} -type f -name \*.ko -exec strip --strip-debug \{\} \;

%clean
%{__rm} -rf %{buildroot}

%files -n ndiswrapper
%defattr(-, root, root, 0755)
%doc %{kmod_name}-%{version}/AUTHORS %{kmod_name}-%{version}/ChangeLog %{kmod_name}-%{version}/INSTALL %{kmod_name}-%{version}/README
%doc %{_mandir}/man8/ndiswrapper.8*
%dir %{_sysconfdir}/ndiswrapper/
/sbin/loadndisdriver
%{_sbindir}/ndiswrapper
%{_sbindir}/ndiswrapper-buginfo

%changelog
* Mon May 04 2009 Dag Wieers <dag@wieers.com> - 1.54-1
- Initial package. (using DAR)
