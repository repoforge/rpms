# $Id$
# authority: matthias
# ExclusiveDist: fc4 fc5

%define snapshot 20060215

# Stuff to be implemented externally :
Source10: kmodtool
%define   kmodtool sh %{SOURCE10}
# End stuff to be ...

# Temporarily hardcoded :
%{!?kver: %define kver 2.6.16-1.2080_FC5}
%ifnarch i686 x86_64 ppc
%define kvariants ""
%else
%ifarch i686
%define kvariants "" smp xen0 xenU
%endif
%ifarch x86_64
%define kvariants "" xen0 xenU
%endif
%ifarch ppc
%define kvariants "" smp
%endif
%endif

%define kmod_name acx
%define kverrel %(%{kmodtool} verrel  %{?kver} 2>/dev/null)
%{!?kvariants: %global kvariants %(%{kmodtool} variant %{?kver} 2>/dev/null)}

Summary: Kernel module for Texas Instruments ACX100/ACX111 based network adapters
Name: %{kmod_name}-kmod
Version: 0.0.0
Release: 1.%{snapshot}.%(echo %{kverrel} | tr - _)
Group: System Environment/Kernel
License: GPL
URL: http://acx100.sourceforge.net/
Source0: http://acx100.erley.org/acx-%{snapshot}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# ExclusiveArch to assist the FE build system.
ExclusiveArch: i586 i686 x86_64 ppc

%description
This RPM contains a binary Linux kernel module built for %{kernel}. It 
provides a driver for Texas Instruments ACX100/ACX111 based wireless network
adapters.

# magic hidden here:
%{expand:%(%{kmodtool} rpmtemplate %{kmod_name} %{kverrel} %{kvariants} 2>/dev/null)}


%prep
# To understand the magic better or to debug it, uncomment this :
#{kmodtool} rpmtemplate %{kmod_name} %{kverrel} %{kvariants} 2>/dev/null
#sleep 5
%setup -c -T
# Can't think of any better way to do this since we basically need -c twice
for kvariant in %{kvariants}; do
    mkdir _kmod_build_$kvariant
    cd    _kmod_build_$kvariant
        tar xjvf %{SOURCE0}
    cd ..
done
# Permissions in the original source are really bad (as of 20060215)
chmod -Rf a+rX,u+w,g-w,o-w .


%build
for kvariant in %{kvariants}; do
    ksrc=%{_usrsrc}/kernels/%{kverrel}${kvariant:+-$kvariant}-%{_target_cpu}
    cd _kmod_build_$kvariant
        make -C "${ksrc}" M=`pwd`
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
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060215
- Initial RPM release, based on the new Extras kernel module template.

