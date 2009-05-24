%define desktop_vendor freshrpms
%define nvidialibdir   %{_libdir}/nvidia
%define nvidialib32dir %{_prefix}/lib/nvidia

%define debug_package  %{nil}

Summary: Proprietary NVIDIA hardware accelerated OpenGL display driver
Name: dkms-nvidia-x11-drv
Version: 180.51
Release: 1%{?dist}
License: Proprietary
Group: User Interface/X Hardware Support
URL: http://www.nvidia.com/object/unix.html

# i386
Source0: http://us.download.nvidia.com/XFree86/Linux-x86/%{version}/NVIDIA-Linux-x86-%{version}-pkg0.run
# x86_64
Source1: http://us.download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}-pkg2.run
Source2: nvidia.sh
Source3: nvidia.csh
Source4: nvidia-config-display
Source5: nvidia.modprobe
Source6: nvidia.nodes
# http://www.nvnews.net/vbulletin/attachment.php?attachmentid=20486&d=1158955681
Patch0: NVIDIA_kernel-1.0-9625-NOSMBUS.diff.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
# Required by the NVIDIA run file
Buildrequires: tar
# Required for our build
BuildRequires: desktop-file-utils
# Required for proper dkms operation
Requires: gcc, make
Requires(post): dkms, /sbin/ldconfig
Requires(preun): dkms
# Required by the nvidia-config-display utility/script
Requires: pyxf86config
Provides: dkms-nvidia = %{version}-%{release}
Conflicts: xorg-x11-drv-nvidia
Obsoletes: nvidia-x11-drv <= 173.08

%description
Proprietary NVIDIA GL libraries, Xorg and Linux module for hardware
accelerated OpenGL support.

INSTALLING THIS PACKAGE WILL TAINT YOUR KERNEL, SO PLEASE DO NOT REPORT *ANY*
BUGS BEFORE YOU UNINSTALL THE PACKAGE AND REBOOT THE SYSTEM.

%package 32bit
Summary: Compatibility 32bit files for the 64bit Proprietary NVIDIA driver
Group: User Interface/X Hardware Support
Requires: %{name} = %{version}-%{release}

%description 32bit
Compatibility 32bit files for the 64bit Proprietary NVIDIA driver.

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

%build

%install
%{__rm} -rf %{buildroot}

# Fix for FC6 kernels
#{__perl} -pi -e 's|#include <linux/config.h>||g' usr/src/nv/nv-linux.h

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
%{__install} -p -m 0755 usr/X11R6/lib/modules/libnvidia-wfb.so.%{version} \
    %{buildroot}%{_libdir}/xorg/modules/libwfb.so

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
%defattr(-, root, root, 0755)
%doc LICENSE usr/share/doc/*
# Kernel and dkms related bits
%config %{_sysconfdir}/modprobe.d/nvidia
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
# udev "configuration"
%config %{_sysconfdir}/udev/makedev.d/60-nvidia.nodes
# Libraries and X modules
%config %{_sysconfdir}/ld.so.conf.d/nvidia.conf
%dir %{nvidialibdir}/
%{nvidialibdir}/*.so.*
%{nvidialibdir}/tls/
%{_libdir}/xorg/modules/drivers/nvidia_drv.so
%dir %{_libdir}/xorg/modules/extensions/nvidia/
%{_libdir}/xorg/modules/extensions/nvidia/libglx.so
%{_libdir}/xorg/modules/libwfb.so
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
%files 32bit
%defattr(-, root, root, 0755)
%dir %{nvidialib32dir}/
%{nvidialib32dir}/*.so.*
%{nvidialib32dir}/tls/
# Not needed devel but would violate the license not to include them
#files 32bit-devel
#defattr(-,root,root,-)
%{nvidialib32dir}/*.so
%endif

%changelog
* Sun May 24 2009 Dag Wieers <dag@wieers.com> - 180.51-1
- Updated to release 180.51.

* Wed May 14 2008 Matthias Saou <http://freshrpms.net/> 173.08-1
- Update to 173.08 beta, which includes support for Fedora 9's X snapshot.

* Tue Mar  4 2008 Matthias Saou <http://freshrpms.net/> 169.12-1
- Update to 169.12.

* Mon Feb 18 2008 Matthias Saou <http://freshrpms.net/> 169.09-1
- Update to 169.09.

* Sat Feb  9 2008 Matthias Saou <http://freshrpms.net/> 169.07-1
- Update to 169.07.

* Wed Sep 19 2007 Matthias Saou <http://freshrpms.net/> 100.14.19-1
- Update to 100.14.19.

* Sat Jul 14 2007 Matthias Saou <http://freshrpms.net/> 100.14.11-1
- Update to 100.14.11.
- Split out 32bit "compat" files to a sub-package on x86_64.
- Remove Xen patches, as parts seem to be merged (but enough?).

* Wed Jun 13 2007 Matthias Saou <http://freshrpms.net/> 100.14.09-1
- Update to new 100.14.09 stable release... weird version jump, though.
- Add triggerin to re-enable driver after xorg-x11-server-Xorg update.

* Tue Jun  5 2007 Matthias Saou <http://freshrpms.net/> 1.0.9762-3
- Remove included udev nodes, since they're redundant with the previous change.

* Tue Jun  5 2007 Matthias Saou <http://freshrpms.net/> 1.0.9762-2
- Add 60-nvidia.nodes udev file to have device nodes copied in F7 and get
  things right with selinux.

* Fri May 18 2007 Matthias Saou <http://freshrpms.net/> 1.0.9762-1
- Update to 1.0-9762.

* Fri May 18 2007 Matthias Saou <http://freshrpms.net/> 1.0.9755-3
- Include missing libwfb.so (Simone Caronni).

* Thu Mar 15 2007 Matthias Saou <http://freshrpms.net/> 1.0.9755-2
- Disable Xen sanity check since it fails, but the module actually works.

* Mon Mar 12 2007 Matthias Saou <http://freshrpms.net/> 1.0.9755-1
- Update to 1.0-9755 (stable).
- Change profile.d sourced files from mode 755 to 644, as they should be.

* Fri Dec 22 2006 Matthias Saou <http://freshrpms.net/> 1.0.9746-1
- Update to 1.0-9746 (stable).

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

