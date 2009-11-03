# $Id$
# Authority: matthias
# ExclusiveDist: fc4 fc5

# Stuff to be implemented externally :
Source10: kmodtool
%define   kmodtool sh %{SOURCE10}
# End stuff to be ...

# Temporarily hardcoded :
%{!?kver: %define kver 2.6.16-1.2080_FC5}
%ifarch i686
%define kvariants "" smp xen0 xenU
%endif
%ifarch x86_64
%define kvariants "" xen0 xenU
%endif

%define kmod_name ipw3945
%define kverrel %(%{kmodtool} verrel  %{?kver} 2>/dev/null)
%{!?kvariants: %global kvariants %(%{kmodtool} variant %{?kver} 2>/dev/null)}

Summary: Kernel module for Intel® PRO/Wirelss 3945 network adaptors
Name: %{kmod_name}-kmod
Version: 0.0.73
Release: 1.%(echo %{kverrel} | tr - _)%{?dist}
Group: System Environment/Kernel
License: GPL
URL: http://ipw3945.sourceforge.net/
Source0: http://dl.sf.net/ipw3945/ipw3945-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# ExclusiveArch to assist the FE build system.
ExclusiveArch: i686 x86_64

%description
This RPM contains a binary Linux kernel module built for %{kernel}. It 
provides a driver for Intel® PRO/Wireless3945 based wireless network
adapters.

# magic hidden here:
%{expand:%(%{kmodtool} rpmtemplate %{kmod_name} %{kverrel} %{kvariants} 2>/dev/null)}


%prep
# To understand the magic better or to debug it, uncomment this :
#{kmodtool} rpmtemplate %{kmod_name} %{kverrel} %{kvariants} 2>/dev/null
#sleep 5
%setup -c
for kvariant in %{kvariants}; do
    cp -a ipw3945-%{version} _kmod_build_$kvariant
done


%build
for kvariant in %{kvariants}; do
    ksrc=%{_usrsrc}/kernels/%{kverrel}${kvariant:+-$kvariant}-%{_target_cpu}
    cd _kmod_build_$kvariant
        make KSRC="${ksrc}" IEEE80211_INC="${ksrc}/include"
    cd ..
done


%install
%{__rm} -rf %{buildroot}
for kvariant in %{kvariants}; do
    %{__install} -D -m 0755 _kmod_build_${kvariant}/%{kmod_name}.ko \
        %{buildroot}/lib/modules/%{kverrel}${kvariant}/extra/%{kmod_name}/%{kmod_name}.ko
done


%clean
%{__rm} -rf %{buildroot}


%changelog
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.73-1
- Initial RPM release, based on the new Extras kernel module template,
  unfortunately the build fails and would require replacing the ieee80211
  kernel stack with a more recent one, which can't be done without messing
  with files installed by kernel and kernel-devel packages.

