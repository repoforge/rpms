# $Id$
# Authority: matthias

# ExclusiveDist: el4

%define majmin          1.0
%define relver          9639
%define nvidialibdir    %{_libdir}/nvidia
%define nvidialib32dir  %{_prefix}/lib/nvidia
%define desktop_vendor  rpmforge

#define beta .beta

%define debug_package   %{nil}

Summary: Proprietary NVIDIA hardware accelerated OpenGL display driver
Name: nvidia-x11-drv-96xx
Version: %{majmin}.%{relver}
Release: 1%{?beta}%{?dist}
License: Proprietary
Group: User Interface/X Hardware Support
URL: http://www.nvidia.com/object/unix.html
# i386
Source0: http://download.nvidia.com/XFree86/Linux-x86/%{majmin}-%{relver}/NVIDIA-Linux-x86-%{majmin}-%{relver}-pkg0.run
# x86_64
Source1: http://download.nvidia.com/XFree86/Linux-x86_64/%{majmin}-%{relver}/NVIDIA-Linux-x86_64-%{majmin}-%{relver}-pkg2.run
Source2: nvidia.sh
Source3: nvidia.csh
Source4: nvidia-config-display
Source5: nvidia.modprobe
Source6: nvidia.nodes
# http://www.nvnews.net/vbulletin/attachment.php?attachmentid=20486&d=1158955681
Patch0: NVIDIA_kernel-1.0-9625-NOSMBUS.diff.txt
# http://www.nvnews.net/vbulletin/showthread.php?t=77597
Patch1: NVIDIA-Linux-1.0-9629-xenrt.patch
Patch2: nvidia-x11-drv-1.0.9755-noxensanitycheck.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Required for proper dkms operation
Requires: gcc, make
Requires(post): dkms, /sbin/ldconfig
Requires(preun): dkms
# Required by the nvidia-config-display utility/script
Requires: pyxf86config
# Required by the NVIDIA run file
Buildrequires: tar
# Required for our build
BuildRequires: desktop-file-utils
ExclusiveArch: i386 x86_64
Provides: dkms-nvidia = %{version}-%{release}
Conflicts: xorg-x11-drv-nvidia
Conflicts: nvidia-x11-drv
Conflicts: nvidia-x11-drv-97xx

%description
Proprietary NVIDIA GL libraries, Xorg and Linux module for hardware
accelerated OpenGL support.

INSTALLING THIS PACKAGE WILL TAINT YOUR KERNEL, SO PLEASE DO NOT REPORT *ANY*
BUGS BEFORE YOU UNINSTALL THE PACKAGE AND REBOOT THE SYSTEM.


%prep
%setup -T -c
# Extract the proper "sources" for the current architecture
# We need to extract to a "not yet existing" directory first, so no "."
%ifarch i386
sh %{SOURCE0} --extract-only --target tmp/
%endif
%ifarch x86_64
sh %{SOURCE1} --extract-only --target tmp/
%endif
# Move all the files back from tmp/ to the main directory
%{__mv} tmp/* .
%{__rm} -rf tmp/
%patch0 -p0
%patch1 -p0
%patch2 -p0


%build


%install
%{__rm} -rf %{buildroot}

# Fix for FC6 kernels
%{__perl} -pi -e 's|#include <linux/config.h>||g' usr/src/nv/nv-linux.h

%define dkms_name nvidia
%define dkms_vers %{version}-%{release}
%define quiet -q

# Copy dkms conf file
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make module KERNDIR=/lib/modules/$kernelver IGNORE_CC_MISMATCH=1 SYSSRC=$kernel_source_dir"
BUILT_MODULE_NAME[0]=nvidia
DEST_MODULE_LOCATION[0]=/kernel/drivers/video/nvidia
AUTOINSTALL=YES
EOF

# Install all the files, even the binary ones. Ick.
%{__install} -p -m 0644 usr/src/nv/{*.c,*.h,*.o,makefile,Makefile.kbuild} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__install} -p -m 0755 usr/src/nv/*.sh \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Install libXvMCNVIDIA.*
%{__mkdir_p} %{buildroot}%{nvidialibdir}/
%{__install} -p -m 0755 usr/X11R6/lib/libXvMCNVIDIA.so.* \
    %{buildroot}%{nvidialibdir}/
%{__install} -p -m 0644 usr/X11R6/lib/libXvMCNVIDIA.a \
    %{buildroot}%{nvidialibdir}/

# Install X driver and extension (is the nvidia_drv.o useful?)
%{__mkdir_p} %{buildroot}%{_libdir}/xorg/modules/drivers/
%{__install} -p -m 0755 usr/X11R6/lib/modules/drivers/nvidia_drv.so \
    %{buildroot}%{_libdir}/xorg/modules/drivers/
%{__mkdir_p} %{buildroot}%{_libdir}/xorg/modules/extensions/nvidia/
%{__install} -p -m 0755 usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
    %{buildroot}%{_libdir}/xorg/modules/extensions/nvidia/libglx.so

# Install GL and tls libs
%{__mkdir_p} %{buildroot}%{nvidialibdir}/tls/
%{__install} -p -m 0755 usr/lib/*.so.%{version} \
    %{buildroot}%{nvidialibdir}/
%{__install} -p -m 0755 usr/lib/tls/*.so.%{version} \
    %{buildroot}%{nvidialibdir}/tls/

%ifarch x86_64
# Install 32bit compat GL and tls libs
%{__mkdir_p} %{buildroot}%{nvidialib32dir}/tls/
%{__install} -p -m 0755 usr/lib32/*.so.%{version} \
    %{buildroot}%{nvidialib32dir}/
%{__install} -p -m 0755 usr/lib32/tls/*.so.%{version} \
    %{buildroot}%{nvidialib32dir}/tls/
%endif

# Create .so symlinks
for libname in libGLcore libGL libnvidia-cfg libnvidia-tls tls/libnvidia-tls; do
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}%{nvidialibdir}/${libname}.so.1
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}%{nvidialibdir}/${libname}.so
done
%ifarch x86_64
for libname in libGLcore libGL libnvidia-cfg libnvidia-tls tls/libnvidia-tls; do
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}%{nvidialib32dir}/${libname}.so.1
    %{__ln_s} `basename ${libname}`.so.%{version} \
        %{buildroot}%{nvidialib32dir}/${libname}.so
done
%endif

# Install useful nvidia tools
%{__mkdir_p} %{buildroot}%{_bindir}/
%{__install} -p -m 0755 usr/bin/{nvidia-bug-report.sh,nvidia-settings} \
    %{buildroot}%{_bindir}/
%{__mkdir_p} %{buildroot}%{_sbindir}/
%{__install} -p -m 0755 usr/bin/nvidia-xconfig \
    %{buildroot}%{_sbindir}/

# Install man pages (the other, nvidia-installer, isn't relevant)
%{__mkdir_p} %{buildroot}%{_mandir}/man1/
%{__install} -p -m 0644 usr/share/man/man1/nvidia-{settings,xconfig}* \
    %{buildroot}%{_mandir}/man1/

# Install pixmap for the desktop entry
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps/
%{__install} -p -m 0644 usr/share/pixmaps/nvidia-settings.png \
    %{buildroot}%{_datadir}/pixmaps/

# Remove "__UTILS_PATH__/" before the Exec command name
# Replace "__PIXMAP_PATH__/" with the proper pixmaps path
%{__perl} -pi -e 's|(Exec=).*/(.*)|$1$2|g;
                  s|(Icon=).*/(.*)|$1%{_datadir}/pixmaps/$2|g' \
    usr/share/applications/nvidia-settings.desktop

# Desktop entry for nvidia-settings
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}/%{_datadir}/applications/ \
    --add-category System \
    --add-category Application \
    --add-category GNOME \
    usr/share/applications/nvidia-settings.desktop

# Install modprobe.d file
%{__install} -D -p -m 0644 %{SOURCE5} \
    %{buildroot}%{_sysconfdir}/modprobe.d/nvidia

# Install ld.so.conf.d file
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo %{nvidialibdir} >    %{buildroot}%{_sysconfdir}/ld.so.conf.d/nvidia.conf
%ifarch x86_64
echo %{nvidialib32dir} >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/nvidia.conf
%endif

# Install profile.d files
%{__install} -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/profile.d/nvidia.sh
%{__install} -D -p -m 0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/profile.d/nvidia.csh

# Install X configuration script
%{__install} -D -p -m 0755 %{SOURCE4} \
    %{buildroot}%{_sbindir}/nvidia-config-display

# Install udev "configuration" file, required as of F7
%{__install} -D -p -m 0644 %{SOURCE6} \
    %{buildroot}%{_sysconfdir}/udev/makedev.d/60-nvidia.nodes


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
# Make sure we have a Files section in xorg.conf, otherwise create an empty one
XORGCONF=/etc/X11/xorg.conf
[ -w ${XORGCONF} ] && ! grep -q 'Section "Files"' ${XORGCONF} && \
    echo -e 'Section "Files"\nEndSection' >> ${XORGCONF}
# Enable the proprietary driver
%{_sbindir}/nvidia-config-display enable || :
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :
# Last removal, disable the proprietary driver
if [ $1 -eq 0 ]; then
    %{_sbindir}/nvidia-config-display disable || :
fi

%postun -p /sbin/ldconfig

%triggerin -- xorg-x11-server-Xorg
# Enable the proprietary driver
# Required since xorg-x11-server-Xorg empties the "Files" section
%{_sbindir}/nvidia-config-display enable || :


%files
%defattr(-,root,root,-)
%doc LICENSE usr/share/doc/*
# Kernel and dkms related bits
%config %{_sysconfdir}/modprobe.d/nvidia
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
# udev "configuration"
%config %{_sysconfdir}/udev/makedev.d/60-nvidia.nodes
# Devices for udev to copy directly - No longer needed thanks to the above
#attr(0600,root,root) %dev(c,195,0) %{_sysconfdir}/udev/devices/nvidia0
#attr(0600,root,root) %dev(c,195,1) %{_sysconfdir}/udev/devices/nvidia1
#attr(0600,root,root) %dev(c,195,2) %{_sysconfdir}/udev/devices/nvidia2
#attr(0600,root,root) %dev(c,195,3) %{_sysconfdir}/udev/devices/nvidia3
#attr(0600,root,root) %dev(c,195,4) %{_sysconfdir}/udev/devices/nvidia4
#attr(0600,root,root) %dev(c,195,5) %{_sysconfdir}/udev/devices/nvidia5
#attr(0600,root,root) %dev(c,195,6) %{_sysconfdir}/udev/devices/nvidia6
#attr(0600,root,root) %dev(c,195,7) %{_sysconfdir}/udev/devices/nvidia7
#attr(0600,root,root) %dev(c,195,8) %{_sysconfdir}/udev/devices/nvidia8
#attr(0600,root,root) %dev(c,195,9) %{_sysconfdir}/udev/devices/nvidia9
#attr(0600,root,root) %dev(c,195,255) %{_sysconfdir}/udev/devices/nvidiactl
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
%{_libdir}/xorg/modules/drivers/nvidia_drv.so
%dir %{_libdir}/xorg/modules/extensions/nvidia/
%{_libdir}/xorg/modules/extensions/nvidia/libglx.so
# Tools and utilities
%{_sysconfdir}/profile.d/*
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

# Not needed devel but would violate the license not to include them
#files devel
#defattr(-,root,root,-)
%{nvidialibdir}/*.a
%{nvidialibdir}/*.so
%ifarch x86_64
%{nvidialib32dir}/*.so
%endif


%changelog
* Wed Jun 13 2007 Matthias Saou <http://freshrpms.net/> 1.0.9639-1
- Update to 1.0-9639 (legacy 96xx).
- Add explicit conflicts with nvidia-x11-drv and nvidia-x11-drv-97xx.
- Backport Xen patch from 97xx.
- Backport udev changes from 97xx.
- Backport profile file mode fixes from 97xx.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 1.0.9631-1
- Fork 96xx legacy driver (required for older video cards).

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 1.0.9631-1
- Update to 1.0-9631 (stable).

* Thu Nov 30 2006 Matthias Saou <http://freshrpms.net/> 1.0.9742-1.beta
- Update to the latest 1.0-9742 beta driver.

* Thu Nov 30 2006 Matthias Saou <http://freshrpms.net/> 1.0.9629-3
- Use the pkg0 file for i386 since it's the same as the pkg1 but without all
  of the precompiled kernel modules we don't use anyway. We save 6MB+ of SRPM.
- For x86_64 there are no precompiled modules (ATM) so pkg0 and pkg1 are the
  same, but pkg2 has the lib32 files in addition, so it makes sense to use
  pkg2 there.

* Thu Nov 16 2006 Matthias Saou <http://freshrpms.net/> 1.0.9629-2
- Include Xen patch and spec fixes from Juliano F. Ravasi.

* Wed Nov  8 2006 Matthias Saou <http://freshrpms.net/> 1.0.9629-1
- Update to 1.0-9629.

* Tue Oct 31 2006 Matthias Saou <http://freshrpms.net/> 1.0.9626-4
- Include patch to fix black X screen on startup (disables i2c, though).

* Mon Oct 30 2006 Matthias Saou <http://freshrpms.net/> 1.0.9626-3
- 32bit libs weren't being included on x86_64, the 64bits were twice instead.

* Tue Oct 24 2006 Matthias Saou <http://freshrpms.net/> 1.0.9626-2
- Include nvidia-xconfig, Edward Rudd.
- Move extracting the installer to the %%prep stage, Edward Rudd.
- No longer do everything from the pkg/ directory.

* Mon Oct 16 2006 Matthias Saou <http://freshrpms.net/> 1.0.9626-1
- Update to 1.0-9626.

* Wed Oct 11 2006 Matthias Saou <http://freshrpms.net/> 1.0.9625-2
- Fix desktop entry.
- Remove static dev entries, let udev take care of copying them to /dev.
- Small fix to the driver file mode and remove the created empty directory.
- Add %%{nvidialib32dir} to the ld.so.conf.d file on x86_64.
- Make sure we have a Files section in xorg.conf, otherwise create an empty
  one for the nvidia-config-display utility/script to work properly.
- Run the nvidia-config-display utility/script in %%post.

* Tue Oct 10 2006 Matthias Saou <http://freshrpms.net/> 1.0.9625-1
- Update to the 1.0-9625 beta drivers.

* Tue Oct 10 2006 Matthias Saou <http://freshrpms.net/> 1.0.8774-3
- Add the rpm release to the dkms module version, to make updating the module
  to a fixed same version work (--rpm_safe_upgrade doesn't work as advertised).
- Force modules install so that the same version can be overwritten instead of
  uninstalled by the old package's %%preun when updating.
- Add build time quiet flag for the scriplets. Undefine to do verbose testing.

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

