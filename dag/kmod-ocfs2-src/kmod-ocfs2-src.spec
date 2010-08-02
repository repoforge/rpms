# $Id$
# Authority: dag

# ExclusiveDist: el5
# Archs: i686 x86_64

# Tag: test

%define kversion 2.6.18-164.10.1.el5
%{!?kversion:%define kversion %(rpm -q kernel-devel --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

# Define the kmod package name here.
%define kmod_name ocfs2

Summary: Kernel module for the OCFS2 cluster file system
Name: kmod-ocfs2-src
Version: 1.4.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://oss.oracle.com/projects/ocfs2/

Source0: http://oss.oracle.com/projects/ocfs2/dist/files/source/v1.4/ocfs2-%{version}.tar.gz
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
This package provides the kernel module for the OCFS2 cluster file system.

OCFS2 is a POSIX-compliant shared-disk cluster file system for Linux capable
of providing both high performance and high availability.

As it provides local file system semantics, it can be used with any
application. Cluster-aware applications can make use of parallel I/O for
higher performance. Applications, not able to benefit from parallel I/O,
can take advantage of the file system to provide a fail-over setup to
increase its availability. 

%prep
%setup -c -T -a 0
for kvariant in %{kvariants} ; do
    %{__cp} -av %{kmod_name}-%{version} _kmod_build_$kvariant
done

%build
for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant/
    %configure --with-vendor="rhel5" --with-vendorkernel="${kversion}"
    pushd fs
    %{__make} -C "${ksrc}" modules M="$PWD"
    popd
    popd
done

%install
export INSTALL_MOD_PATH="%{buildroot}"
export INSTALL_MOD_DIR="extra/%{kmod_name}"
for kvariant in %{kvariants} ; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant/
    %{__make} -C "${ksrc}" modules_install M="$PWD"
    %{__install} -d ${INSTALL_MOD_PATH}/usr/lib/debug
    popd
done
# Strip the module(s).
find %{buildroot} -type f -name \*.ko -exec strip --strip-debug \{\} \;

%clean
%{__rm} -rf %{buildroot}

%changelog
* Wed Aug 12 2009 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Initial package. (using DAR)
