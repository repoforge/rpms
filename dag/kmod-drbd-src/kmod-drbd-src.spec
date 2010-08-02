# $Id$
# Authority: dag

# ExclusiveDist: el5
# Archs: i686 x86_64

# Tag: test

%define kversion 2.6.18-194.3.1.el5
%{!?kversion:%define kversion %(rpm -q kernel-devel --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

### Define the kmod package name here.
%define kmod_name drbd83
%define short_name drbd

Summary: Distributed Redundant Block Device driver for Linux
Name: kmod-drbd-src
Version: 8.3.8
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.drbd.org/

Source0: http://oss.linbit.com/drbd/8.3/drbd-%{version}.tar.gz
Source10: kmodtool-%{kmod_name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i686 x86_64

### We cannot obsolete all Linbit drbd-km-%{kversion} variants
Conflicts: kmod-drbd < 8.2
Obsoletes: kmod-drbd82 <= %{version}-%{release}

### Define the variants for each architecture.
%define basevar ""

%ifarch i686
%define paevar PAE
%endif
%ifarch i686 x86_64
%define xenvar xen
%endif

### If kvariants isn't defined on the rpmbuild line, build all variants for this architecture.
%{!?kvariants: %define kvariants %{?basevar} %{?xenvar} %{?paevar}}

### Magic hidden here.
%define kmodtool sh %{SOURCE10}
%{expand:%(%{kmodtool} rpmtemplate_kmp %{kmod_name} %{kversion} %{kvariants} 2>/dev/null)}

%description
Drbd is a distributed replicated block device. It mirrors a
block device over the network to another machine. Think of it
as networked raid 1. It is a building block for setting up
high availability (HA) clusters.

%prep
%setup -c -T -a 0

%define __find_requires sh %{_builddir}/%{buildsubdir}/filter-requires.sh
echo "/usr/lib/rpm/redhat/find-requires | sed -e '/^ksym.*/d'" >filter-requires.sh

pushd %{short_name}-%{version}
%configure \
    --with-km \
    --without-bashcompletion \
    --without-heartbeat \
    --without-pacemaker \
    --without-rgmanager \
    --without-udev \
    --without-utils \
    --without-xen
popd
for kvariant in %{kvariants} ; do
    %{__cp} -av %{short_name}-%{version} _kmod_build_$kvariant
done

%build
for kvariant in %{kvariants}; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant
    %{__make} KDIR="${ksrc}" module
    popd
done

%install
%{__rm} -rf %{buildroot}
export INSTALL_MOD_PATH="%{buildroot}"
export INSTALL_MOD_DIR="extra/%{kmod_name}"
for kvariant in %{kvariants}; do
    ksrc="%{_usrsrc}/kernels/%{kversion}${kvariant:+-$kvariant}-%{_target_cpu}"
    pushd _kmod_build_$kvariant/drbd
    %{__make} -C "${ksrc}" modules_install M="$PWD"
    popd
done
### Strip the module(s).
find %{buildroot} -type f -name \*.ko -exec strip --strip-debug \{\} \;

%clean
%{__rm} -rf %{buildroot}

%changelog
* Fri Jun 11 2010 Dag Wieers <dag@wieers.com> - 8.3.8-1
- Initial package. (using DAR)
