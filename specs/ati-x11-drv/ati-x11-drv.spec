# $Id$
# Authority: matthias
# ExclusiveDist: fc6 fc7

%define fglrxlibdir    %{_libdir}/fglrx
%define fglrxlib32dir  %{_prefix}/lib/fglrx

%ifarch i386
%define atiarch x86
%endif

%ifarch x86_64
%define atiarch x86_64
%define xext _64a
%endif

Summary: Proprietary ATI hardware accelerated OpenGL display driver
Name: ati-x11-drv
Version: 8.41.7
Release: 1%{?dist}
License: Proprietary
Group: User Interface/X Hardware Support
URL: http://ati.amd.com/support/drivers/linux/linux-radeon.html
Source0: http://www2.ati.com/drivers/linux/ati-driver-installer-%{version}-x86.x86_64.run
Source1: Makefile.fglrx
Source2: README-rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Required for proper dkms operation
Requires: gcc
Requires(post): dkms, /sbin/ldconfig
Requires(preun): dkms, system-config-display
# Required by the ATI run file
Buildrequires: tar
# Required for our build
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
ExclusiveArch: i386 x86_64
Provides: dkms-fglrx = %{version}-%{release}
Provides: dkms-ati = %{version}-%{release}
Conflicts: xorg-x11-drv-fglrx

%description
Proprietary ATI GL libraries, Xorg and Linux module for hardware
accelerated OpenGL support.

INSTALLING THIS PACKAGE WILL TAINT YOUR KERNEL, SO PLEASE DO NOT REPORT *ANY*
BUGS BEFORE YOU UNINSTALL THE PACKAGE AND REBOOT THE SYSTEM.


%package devel
Summary: Development files for the proprietary ATI display driver
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the proprietary ATI display driver.


%prep
%setup -T -c
# Extract the "sources"
sh %{SOURCE0} --extract .
# Fix for FC6 kernels
%{__perl} -pi -e 's|#include <linux/config.h>||g' \
    common/lib/modules/fglrx/build_mod/*.{c,h}
# Our quick README to be included as %%doc
%{__install} -p -m 0644 %{SOURCE2} README-rpm


%build


%install
%{__rm} -rf %{buildroot} _doc

%define dkms_name fglrx
%define dkms_vers %{version}-%{release}
%define quiet -q

# Copy dkms conf file
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=fglrx
DEST_MODULE_LOCATION[0]=/kernel/drivers/video/aty
AUTOINSTALL=YES
EOF

# Install all the kernel module files, without make.sh or 2.6.x/
%{__cp} -a common/lib/modules/fglrx/build_mod/*.{c,h} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__install} -p -m 0644 \
    arch/%{atiarch}/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC4 \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
# Install our own Makefile, based on the one from 2.6.x/
%{__install} -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/Makefile

# Install utilities and atieventsd program with its init script and man page
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 arch/%{atiarch}/usr/X11R6/bin/* \
    %{buildroot}%{_bindir}/
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -D -p -m 0755 arch/%{atiarch}/usr/sbin/atieventsd \
                           common/usr/sbin/atigetsysteminfo.sh \
    %{buildroot}%{_sbindir}/
%{__install} -D -p -m 0755 packages/Fedora/atieventsd.init \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/atieventsd
%{__install} -D -p -m 0755 packages/Fedora/authatieventsd.sh \
    %{buildroot}%{_sysconfdir}/ati/authatieventsd.sh
%{__install} -D -p -m 0644 common/usr/share/man/man8/atieventsd.8 \
    %{buildroot}%{_mandir}/man8/atieventsd.8

# Install libaries
%{__mkdir_p} %{buildroot}%{fglrxlibdir}
%{__install} -p -m 0644 arch/%{atiarch}/usr/X11R6/%{_lib}/*.a \
    %{buildroot}%{fglrxlibdir}/
%{__install} -p -m 0755 arch/%{atiarch}/usr/X11R6/%{_lib}/*.so.* \
    %{buildroot}%{fglrxlibdir}/
%ifarch x86_64
%{__mkdir_p} %{buildroot}%{fglrxlib32dir}
%{__install} -p -m 0755 arch/%{atiarch}/usr/X11R6/lib/*.so.* \
    %{buildroot}%{fglrxlib32dir}/
%endif

# Install driver and extensions
# DRI modules, the absolute "compatibility" path is hardcoded, thus required
%{__mkdir_p} %{buildroot}%{_libdir}/dri
%{__mkdir_p} %{buildroot}%{_prefix}/X11R6/%{_lib}/modules/dri
%{__install} -p -m 0755 arch/%{atiarch}/usr/X11R6/%{_lib}/modules/dri/* \
        %{buildroot}%{_libdir}/dri/
for drilib in `cd %{buildroot}%{_libdir}/dri/ && echo *`; do
    %{__ln_s} %{_libdir}/dri/${drilib} \
        %{buildroot}%{_prefix}/X11R6/%{_lib}/modules/dri/${drilib}
done
# Driver modules
%{__mkdir_p} %{buildroot}%{_libdir}/xorg/modules/{drivers,linux}
%{__install} -p -m 0755 x710%{?xext}/usr/X11R6/%{_lib}/modules/drivers/* \
    %{buildroot}%{_libdir}/xorg/modules/drivers/
%{__install} -p -m 0755 x710%{?xext}/usr/X11R6/%{_lib}/modules/linux/* \
    %{buildroot}%{_libdir}/xorg/modules/linux/
%{__install} -p -m 0755 x710%{?xext}/usr/X11R6/%{_lib}/modules/*.* \
    %{buildroot}%{_libdir}/xorg/modules/

# Install ACPI config and scripts
%{__install} -D -p -m 0644 packages/Fedora/a-ac-aticonfig \
    %{buildroot}%{_sysconfdir}/acpi/events/ac-aticonfig
%{__install} -D -p -m 0644 packages/Fedora/a-lid-aticonfig \
    %{buildroot}%{_sysconfdir}/acpi/events/lid-aticonfig
%{__install} -D -p -m 0755 packages/Fedora/ati-powermode.sh \
    %{buildroot}%{_sysconfdir}/acpi/actions/ati-powermode.sh

# Install header files
%{__mkdir_p} %{buildroot}%{_includedir}/GL
%{__install} -p -m 0644 common/usr/include/GL/*.h \
    %{buildroot}%{_includedir}/GL/
%{__mkdir_p} %{buildroot}%{_includedir}/X11/extensions
%{__install} -p -m 0644 common/usr/X11R6/include/X11/extensions/fglrx_gamma.h \
    %{buildroot}%{_includedir}/X11/extensions/

# Install pixmaps for the amdcccle desktop entry
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps/
%{__install} -p -m 0644 common/usr/share/icons/*.xpm \
    %{buildroot}%{_datadir}/pixmaps/

# Desktop entry for amdcccle
%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install \
    --vendor "" \
    --dir %{buildroot}/%{_datadir}/applications/ \
    --add-category System \
    --remove-category Application \
    packages/Debian/dists/experimental/amdcccle.desktop

# Install the control file (new in 8.39.4, "AMD testing" watermark without)
# As well as the signature file
%{__install} -D -p -m 0644 common/etc/ati/control \
    %{buildroot}%{_sysconfdir}/ati/control
%{__install} -D -p -m 0644 common/etc/ati/signature \
    %{buildroot}%{_sysconfdir}/ati/signature

# Install ld.so.conf.d file
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ld.so.conf.d/
echo %{fglrxlibdir} >    %{buildroot}%{_sysconfdir}/ld.so.conf.d/fglrx.conf
%ifarch x86_64
echo %{fglrxlib32dir} >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/fglrx.conf
%endif

# We want to include all the docs except 'examples' since we already ship the
# ACPI config files and the init script, and it contains nothing more
%{__cp} -a common/usr/share/doc/fglrx _doc
%{__rm} -rf _doc/examples/
find _doc -type f -exec %{__chmod} -x {} \;


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
# Enable atieventsd and configure X for the driver
/sbin/chkconfig --add atieventsd
# Does strange stuff, like _adding_ screens and devices... so disable for now
#/usr/bin/aticonfig --initial &>/dev/null || :
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
    /sbin/chkconfig --del atieventsd
    # Disable for now, as going back to the previous driver would be best
    #%{_bindir}/system-config-display --set-driver=vesa || :
fi

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc _doc/* README-rpm
# Init script and control/signature files
%{_sysconfdir}/ati/
%{_sysconfdir}/rc.d/init.d/atieventsd
# ACPI stuff
%{_sysconfdir}/acpi/events/ac-aticonfig
%{_sysconfdir}/acpi/events/lid-aticonfig
%{_sysconfdir}/acpi/actions/ati-powermode.sh
# Kernel and dkms related bits
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
# Libraries and X modules
%config %{_sysconfdir}/ld.so.conf.d/fglrx.conf
%dir %{fglrxlibdir}/
%{fglrxlibdir}/*.so.*
%ifarch x86_64
%dir %{fglrxlib32dir}/
%{fglrxlib32dir}/*.so.*
%endif
%{_libdir}/dri/*.so
# Own the entire tree, since with Xorg 7.x no one else does anymore
%{_prefix}/X11R6/
%{_libdir}/xorg/modules/drivers/*.so
%{_libdir}/xorg/modules/linux/*.so
%{_libdir}/xorg/modules/*.so
%{_libdir}/xorg/modules/*.a
# Tools and utilities
%{_bindir}/amdcccle
%{_bindir}/aticonfig
%{_bindir}/fgl_glxgears
%{_bindir}/fglrxinfo
%{_bindir}/fglrx_xgamma
%{_sbindir}/atieventsd
%{_sbindir}/atigetsysteminfo.sh
%{_mandir}/man8/atieventsd.8.gz
%{_datadir}/applications/amdcccle.desktop
%{_datadir}/pixmaps/*.xpm

%files devel
%defattr(-,root,root,-)
%{_includedir}/GL/
%{_includedir}/X11/extensions/*
%{fglrxlibdir}/*.a


%changelog
* Thu Sep 13 2007 Matthias Saou <http://freshrpms.net/> 8.41.7-1
- Update to 8.41.7.
- The atieventsd.8 man page is no longer provided gzipped, go figure.

* Wed Aug 15 2007 Matthias Saou <http://freshrpms.net/> 8.40.4-2
- Include signature file to fix AMD testing watermark.
- Include quick README-rpm file with tips for typical gotchas.

* Tue Aug 14 2007 Matthias Saou <http://freshrpms.net/> 8.40.4-1
- Update to 8.40.4.

* Thu Jul 26 2007 Matthias Saou <http://freshrpms.net/> 8.39.4-3
- Include the control file to fix AMD testing watermark.

* Mon Jul 23 2007 Matthias Saou <http://freshrpms.net/> 8.39.4-2
- Update to 8.39.4 (yeah, the new one...).

* Fri Jul 20 2007 Matthias Saou <http://freshrpms.net/> 8.39.4-1
- Update to 8.39.4.

* Tue Jun 26 2007 Matthias Saou <http://freshrpms.net/> 8.38.6-1
- Update to 8.38.6.
- Remove no longer shipped fireglcontrolpanel.
- Include desktop entry for the new ATI Catalyst Control Center (amdcccle).
- Remove vendor prefix from the desktop file.

* Wed May  2 2007 Matthias Saou <http://freshrpms.net/> 8.36.5-2
- Include new esut.a and glesx.so files to fix Xv.

* Wed Apr 25 2007 Matthias Saou <http://freshrpms.net/> 8.36.5-1
- Update to 8.36.5.

* Mon Apr  2 2007 Matthias Saou <http://freshrpms.net/> 8.35.5-1
- Update to 8.35.5.
- Include new amdcccle (AMD Catalyst Control Centre: Linux Edition).

* Thu Mar 15 2007 Matthias Saou <http://freshrpms.net/> 8.34.8-2
- Include patch to rebuild against 2.6.20 kernels (FC6 updates testing).

* Thu Feb 22 2007 Matthias Saou <http://freshrpms.net/> 8.34.8-1
- Update to 8.34.8.

* Thu Jan 11 2007 Matthias Saou <http://freshrpms.net/> 8.33.6-1
- Update to 8.33.6.

* Thu Dec 14 2006 Matthias Saou <http://freshrpms.net/> 8.32.5-1
- Update to 8.32.5.

* Tue Nov 28 2006 Matthias Saou <http://freshrpms.net/> 8.31.5-1
- Update to 8.31.5.

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 8.30.3-1
- Update to 8.30.3.

* Tue Oct 31 2006 Matthias Saou <http://freshrpms.net/> 8.29.6-3
- Add /usr/X11R6 dri symlinks, required because of hardcoded paths inside the
  main libraries (Alexandre Silva Lopes).
- Add /etc/ati/authatieventsd.sh since it is required by the Fedora init script
  (Alexandre Silva Lopes).

* Wed Oct 25 2006 Matthias Saou <http://freshrpms.net/> 8.29.6-2
- Fix kernel module Makefile.
- Fix dri module location.

* Mon Oct 23 2006 Matthias Saou <http://freshrpms.net/> 8.29.6-1
- Initial RPM release, mostly reinventing the wheel from from scratch...

