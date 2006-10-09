# $Id$
# Authority: matthias
# Dist: nodist

%define majmin          1.0
%define relver          8774
%define dkms_name       nvidia
%define nvidialibdir    %{_libdir}/nvidia
%define nvidialib32dir  %{_prefix}/lib/nvidia

%define debug_package   %{nil}

Summary: Proprietary NVIDIA hardware accelerated OpenGL driver
Name: nvidia-x11-drv
Version: %{majmin}.%{relver}
Release: 2.1
License: Proprietary
Group: User Interface/X Hardware Support
URL: http://www.nvidia.com/object/unix.html
# i386
Source0: http://download.nvidia.com/XFree86/Linux-x86/%{majmin}-%{relver}/NVIDIA-Linux-x86-%{majmin}-%{relver}-pkg1.run
# x86_64
Source1: http://download.nvidia.com/XFree86/Linux-x86_64/%{majmin}-%{relver}/NVIDIA-Linux-x86_64-%{majmin}-%{relver}-pkg2.run
Source2: nvidia.sh
Source3: nvidia.csh
Source4: nvidia-config-display
Source5: nvidia.modprobe
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Required for proper dkms operation
Requires: gcc
Requires(pre): dkms
Requires(post): dkms
# Required by the NVIDIA run file
Buildrequires: tar
# Required for our build
BuildRequires: desktop-file-utils
ExclusiveArch: i386 x86_64
Provides: dkms-nvidia = %{version}-%{release}
Conflicts: xorg-x11-drv-nvidia

%description
Proprietary NVIDIA GL libraries, Xorg and Linux module for hardware
accelerated OpenGL support.

INSTALLING THIS PACKAGE WILL TAINT YOUR KERNEL, SO PLEASE DO NOT REPORT *ANY*
BUGS BEFORE YOU UNINSTALL THE PACKAGE AND REBOOT THE SYSTEM.


%prep
%setup -T -c


%build


%install
%{__rm} -rf %{buildroot} pkg

# Extract the proper "sources" for the current architecture
%ifarch i386
sh %{SOURCE0} --extract-only --target pkg/
%endif
%ifarch x86_64
sh %{SOURCE1} --extract-only --target pkg/
%endif

# Copy dkms conf file
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{version}
MAKE[0]="make module KERNDIR=/lib/modules/$kernelver IGNORE_CC_MISMATCH=1"
BUILT_MODULE_NAME[0]=nvidia
DEST_MODULE_LOCATION[0]=/kernel/drivers/video/nvidia
AUTOINSTALL=YES
EOF

# Install all the files, even the binary ones. Ick.
%{__install} -p -m 0644 pkg/usr/src/nv/{makefile,Makefile.kbuild} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
%{__install} -p -m 0644 pkg/usr/src/nv/*.{c,h,o} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
%{__install} -p -m 0755 pkg/usr/src/nv/*.sh \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

# Install libXvMCNVIDIA.*
%{__mkdir_p} %{buildroot}/%{nvidialibdir}/
%{__install} -p -m 0755 pkg/usr/X11R6/lib/libXvMCNVIDIA.so.* \
    %{buildroot}/%{nvidialibdir}/
#{__install} -p -m 0644 pkg/usr/X11R6/lib/libXvMCNVIDIA.a \
#   %{buildroot}/%{nvidialibdir}/

# Install X driver and extension (is the nvidia_drv.o useful?)
%{__mkdir_p} %{buildroot}%{_libdir}/xorg/modules/drivers/nvidia/
%{__install} -p -m 0644 pkg/usr/X11R6/lib/modules/drivers/*.so \
    %{buildroot}%{_libdir}/xorg/modules/drivers/
%{__mkdir_p} %{buildroot}%{_libdir}/xorg/modules/extensions/nvidia/
%{__install} -p -m 0755 pkg/usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
    %{buildroot}%{_libdir}/xorg/modules/extensions/nvidia/

# Install GL and tls libs
%{__mkdir_p} %{buildroot}/%{nvidialibdir}/tls/
%{__install} -p -m 0755 pkg/usr/lib/*.so.%{version} \
    %{buildroot}/%{nvidialibdir}/
%{__install} -p -m 0755 pkg/usr/lib/tls/*.so.%{version} \
    %{buildroot}/%{nvidialibdir}/tls/

%ifarch x86_64
# Install compat GL and tls libs
%{__mkdir_p} %{buildroot}/%{nvidialib32dir}/tls/
%{__install} -p -m 0755 pkg/usr/lib/*.so.%{version} \
    %{buildroot}/%{nvidialib32dir}/
%{__install} -p -m 0755 pkg/usr/lib/tls/*.so.%{version} \
    %{buildroot}/%{nvidialib32dir}/tls/
%endif

# Create .so symlinks
# (what was that libXvMCNVIDIA_dynamic for?)
for libname in libGLcore libGL libnvidia-cfg libnvidia-tls tls/libnvidia-tls; do
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}/%{nvidialibdir}/${libname}.so.1
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}/%{nvidialibdir}/${libname}.so
done
%ifarch x86_64
for libname in libGLcore libGL libnvidia-cfg libnvidia-tls tls/libnvidia-tls; do
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}/%{nvidialib32dir}/${libname}.so.1
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}/%{nvidialib32dir}/${libname}.so
done
%endif
%{__ln_s} libglx.so.%{version} \
    %{buildroot}/%{_libdir}/xorg/modules/extensions/nvidia/libglx.so

# Install useful nvidia tools
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__install} -p -m 0755 pkg/usr/bin/{nvidia-bug-report.sh,nvidia-settings} \
    %{buildroot}%{_bindir}/

# Install man page (the others aren't relevant)
%{__mkdir_p} %{buildroot}%{_mandir}/man1/
%{__install} -p -m 0644 pkg/usr/share/man/man1/nvidia-settings* \
    %{buildroot}%{_mandir}/man1/

# Install pixmap for the desktop entry
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps/
%{__install} -p -m 0644 pkg/usr/share/pixmaps/nvidia-settings.png \
    %{buildroot}%{_datadir}/pixmaps/

# Desktop entry for nvidia-settings
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor none \
    --dir %{buildroot}/%{_datadir}/applications/ \
    --add-category System \
    --add-category Application \
    --add-category GNOME \
    pkg/usr/share/applications/nvidia-settings.desktop

# Install modprobe.d file
%{__install} -D -p -m 0644 %{SOURCE5} \
    %{buildroot}%{_sysconfdir}/modprobe.d/nvidia

# Install ld.so.conf.d file
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo %{nvidialibdir} > %{buildroot}%{_sysconfdir}/ld.so.conf.d/nvidia.conf

# Install profile.d files
%{__install} -D -p -m 0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/profile.d/nvidia.sh
%{__install} -D -p -m 0755 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/profile.d/nvidia.csh

# Install X configuration script
%{__install} -D -p -m 0755 %{SOURCE4} \
    %{buildroot}%{_sbindir}/nvidia-config-display


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{version} -q --rpm_safe_upgrade
# Build now, so the current user can simply restart X
dkms build -m %{dkms_name} -v %{version} -q
dkms install -m %{dkms_name} -v %{version} -q

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{version} --all -q --rpm_safe_upgrade

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,0755)
%doc pkg/LICENSE pkg/usr/share/doc/*
# Kernel and dkms related bits
%config %{_sysconfdir}/modprobe.d/nvidia
%{_usrsrc}/%{dkms_name}-%{version}/
# fixme: use udev
%attr(0600,root,root) %dev(c,195,0) /dev/nvidia0
%attr(0600,root,root) %dev(c,195,1) /dev/nvidia1
%attr(0600,root,root) %dev(c,195,2) /dev/nvidia2
%attr(0600,root,root) %dev(c,195,3) /dev/nvidia3
%attr(0600,root,root) %dev(c,195,255) /dev/nvidiactl
%attr(0600,root,root) %dev(c,195,0) %{_sysconfdir}/udev/devices/nvidia0
%attr(0600,root,root) %dev(c,195,1) %{_sysconfdir}/udev/devices/nvidia1
%attr(0600,root,root) %dev(c,195,2) %{_sysconfdir}/udev/devices/nvidia2
%attr(0600,root,root) %dev(c,195,3) %{_sysconfdir}/udev/devices/nvidia3
%attr(0600,root,root) %dev(c,195,255) %{_sysconfdir}/udev/devices/nvidiactl
# Libraries and X modules
%config %{_sysconfdir}/ld.so.conf.d/nvidia.conf
%dir %{nvidialibdir}/
%{nvidialibdir}/*.so.*
%{nvidialibdir}/tls/
%ifarch x86_64
%dir %{nvidialib32dir}/
%{nvidialib32dir}/*.so.*
%{nvidialib32dir}/tls/
%endif
%{_libdir}/xorg/modules/drivers/nvidia*
%{_libdir}/xorg/modules/extensions/nvidia/
# Tools and utilities
%{_sysconfdir}/profile.d/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

# Hopefully not needed devel (might violate the license not to include them)
#files devel
#defattr(-,root,root,0755)
#{nvidialibdir}/*.a
%{nvidialibdir}/*.so
%ifarch x86_64
%{nvidialib32dir}/*.so
%endif


%changelog
* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 1.0.8774-2.1
- Add dkms-nvidia provides.
- Use %%{dkms_name} macro for the usr/src directory name.

* Sat Oct  7 2006 Matthias Saou <http://freshrpms.net/> 1.0.8774-2
- Include both x86 and x86_64 pkg.run files in the source rpm, so that the
  same can be used for both i386 and x86_64.

* Wed Oct  4 2006 Matthias Saou <http://freshrpms.net/> 1.0.8774-1
- Add x86_64 support.
- Rework into a single nvidia-x11-drv package.

* Mon Oct 02 2006 Richard Hughes <richard@hughsie.com> 8774-4
- 1st Release, First public build

