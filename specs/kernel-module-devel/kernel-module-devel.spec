# $Id$
# Authority: matthias

# What kernel are we building for ?
%{!?kernel: %define kernel %(uname -r)}
# Get the correct kernel package release by stripping kernel modifiers
%define krel %(echo %{kernel} | sed -e s/smp//g -)

# We really don't need debug packages for this
%define debug_package %{nil}

Summary: Build files for all kernel arch/types for %{krel}
Name: kernel-module-devel-%{krel}
Version: 0.5
Release: 1%{?dist}
Group: System Environment/Kernel
License: GPL
URL: http://thomas.apestaart.org/
Source: %{name}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: /boot/vmlinuz-%{krel}

%description
This package contains a forest of symlinks and actual files copied from
all the kernel rpms.  This allows you to build external modules for
all architectures and types of kernels.


%prep
%setup -n %{name}


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_libdir}/kernel-module-devel
%{__cp} -a * %{buildroot}%{_libdir}/kernel-module-devel/
%{__ln_s} /lib/modules/%{krel}/build \
    %{buildroot}%{_libdir}/kernel-module-devel/%{krel}-common


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_libdir}/kernel-module-devel/


%changelog
* Tue Nov  9 2004 Matthias Saou <http://freshrpms.net/> 0.5-1
- Update to match Thomas' latest changes.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net/> 0.2-1
- Shamelessly borrow this cool piece of work.

* Tue Jun 15 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.2-0.fdr.2: require vmlinuz-(krel) since that actually works

* Fri May 21 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.2-0.fdr.1: Initial package

