# $Id$
# Authority: matthias
# ExclusiveDist: fc4 fc5

%define snapshot 20060521

# Stuff to be implemented externally :
Source10: kmodtool
%define   kmodtool bash %{SOURCE10}
# End stuff to be ...

%{!?kversion: %define kversion 2.6.16-1.2122_FC5}

%define kmod_name acx
%define kverrel %(%{kmodtool} verrel  %{?kversion} 2>/dev/null)

%define upvar ""
%ifarch i586 i686 ppc
%define smpvar smp
%endif
%ifarch i686 x86_64
%define xenvar xen0 xenU
%define kdumpvar kdump
%endif
%{!?kvariants: %define kvariants %{?upvar} %{?smpvar} %{?xenvar} %{?kdumpvar}}

Summary: Kernel module for Texas Instruments ACX100/ACX111 based network adapters
Name: %{kmod_name}-kmod
Version: 0.0.0.%{snapshot}
Release: 1.%(echo %{kverrel} | tr - _)%{?dist}
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

%{expand:%(%{kmodtool} rpmtemplate %{kmod_name} %{kverrel} %{kvariants} 2>/dev/null)}


%prep
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
* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060521
- Enable i586 SMP since the kernel is available.

* Wed May 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060521
- Update to 20060521.
- Update kmodtool to 0.10.10.

* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060215
- Initial RPM release, based on the new Extras kernel module template.

