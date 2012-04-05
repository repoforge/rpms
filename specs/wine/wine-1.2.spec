# $Id$
# Authority: dag

%define _without_freeglut 0
%define _without_glut 1

%{?el6:%define _without_esound 1}

%{?el4:%define _without_modxorg 1}

### EL3 has neither glut nor freeglut
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_freeglut 1}
%{?el3:%define _without_glut 1}
%{?el3:%define _without_ieee1284 1}
%{?el3:%define _without_isdn4k 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Windows 16/32/64 bit emulator
Name: wine
Version: 1.2.3
Release: 1%{?dist}
License: LGPLv2+
Group: Applications/Emulators
URL: http://www.winehq.org/

Source: http://dl.sf.net/sourceforge/wine/wine-%{version}.tar.bz2
Patch1: wine-1.2.1-rpath.patch
### Fix for RHbz #593140
Patch100: wine-1.2-fonts.patch
### Add wine-gecko support
Patch1000: wine-1.2.3-gecko.patch 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### 64bit build cannot run 32bit applications !
ExclusiveArch: %{ix86}
BuildRequires: audiofile-devel
BuildRequires: autoconf
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: flex >= 2.5.35
BuildRequires: fontforge
%ifarch x86_64
BuildRequires: gcc >= 4.4
%endif
BuildRequires: icoutils
BuildRequires: lcms-devel
BuildRequires: libjpeg-devel
BuildRequires: libstdc++-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: mpg123-devel
BuildRequires: ncurses-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel 
BuildRequires: sane-backends-devel
BuildRequires: unixODBC-devel
BuildRequires: zlib-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_cups:BuildRequires: cups-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{!?_without_glut:BuildRequires: glut-devel}
%{!?_without_gphoto2:BuildRequires: gphoto2-devel}
%{!?_without_isdn4k:BuildRequires: isdn4k-utils-devel}
%{!?_without_ieee1284:BuildRequires: libieee1284-devel}
%{!?_without_libusb:BuildRequires: libusb-devel}
%{!?_without_modxorg:BuildRequires: libXxf86dga-devel libXxf86vm-devel libXrandr-devel libXrender-devel libXext-devel libXinerama-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Requires: wine-capi = %{version}-%{release}
Requires: wine-cms = %{version}-%{release}
Requires: wine-core = %{version}-%{release}
Requires: wine-esd = %{version}-%{release}
Requires: wine-gecko = 1.0.0
Requires: wine-jack = %{version}-%{release}
Requires: wine-ldap = %{version}-%{release}
Requires: wine-nas = %{version}-%{release}
Requires: wine-twain = %{version}-%{release}

%description
While Wine is usually thought of as a Windows(TM) emulator, the Wine
developers would prefer that users thought of Wine as a Windows
compatibility layer for UNIX. This package includes a program loader,
which allows unmodified Windows 3.x/9x/NT binaries to run on x86 and x86_64
Unixes. Wine does not require MS Windows, but it can use native system
.dll files if they are available.

The wine package is actually a meta-package which will install everything
you need for wine to work smoothly. If you don't want to install everything
take a look at the wine-* packages.

%package core
Summary: Wine core package
Group: Applications/Emulators
Requires(post): /sbin/ldconfig, /sbin/chkconfig, /sbin/service,
Requires(preun): /sbin/chkconfig, /sbin/service
%{!?_without_modxorg:Requires: /usr/bin/xmessage}
%{?_without_modxorg:Requires: /usr/X11R6/bin/xmessage}
Obsoletes: wine-arts <= %{version}-%{release}
Obsoletes: wine-tools <= %{version}-%{release}
Provides: wine-tools = %{version}-%{release}

%description core
Wine core package includes the basic wine stuff needed by all other packages.

%package capi
Summary: ISDN support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description capi
ISDN support for wine.

%package cms
Summary: Color Managment for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description cms
Color Management for wine.

%package esd
Summary: ESD sound support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description esd
ESD sound support for wine.

%package jack
Summary: JACK sound support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description jack
JACK sound support for wine.

%package ldap
Summary: LDAP support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description ldap
LDAP support for wine.

%package nas
Summary: NAS sound support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description nas
NAS sound support for wine.

%package twain
Summary: Twain support for wine
Group: System Environment/Libraries
Requires: wine-core = %{version}-%{release}

%description twain
Twain support for wine.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: wine-core = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

#patch1
%patch100
%patch1000

%{__cat} <<EOF >wine-config.desktop
[Desktop Entry]
Name=Wine Configuration
Comment=Interface to set wine parameters
Exec=winecfg
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%{__cat} <<EOF >wine-fileman.desktop
[Desktop Entry]
Name=Wine File
Comment=Wine File Browser
Exec=winefile
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%{__cat} <<EOF >wine-regedit.desktop
[Desktop Entry]
Name=regedit
Comment=Wine registry editor
Exec=regedit
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%{__cat} <<EOF >wine-uninstaller.desktop
[Desktop Entry]
Name=Wine Software Uninstaller
Comment=Interface to uninstall software
Exec=uninstaller
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;System;
EOF

%{__cat} <<'EOF' >wine.sysv
#!/bin/sh
#
# wine  Allow users to run Windows(tm) applications by just clicking on them
#       (or typing ./file.exe)
#
# chkconfig: 35 98 10
# description: Allow users to run Windows(tm) applications by just clicking \
#              on them (or typing ./file.exe)

source %{_initrddir}/functions
RETVAL=0

start() {
    if [ -e /proc/sys/fs/binfmt_misc/windows ]; then
        echo -n $"Binary handler for Windows applications already registered"
    else
        echo -n $"Registering binary handler for Windows applications: "
        /sbin/modprobe binfmt_misc &>/dev/null
        echo ':windows:M::MZ::/usr/bin/wine:' >/proc/sys/fs/binfmt_misc/register || :
        echo ':windowsPE:M::PE::/usr/bin/wine:' >/proc/sys/fs/binfmt_misc/register || :
        RETVAL=$?
        [ $RETVAL -eq 0 ] && success || failure
    fi
    echo
}

stop() {
    echo -n $"Unregistering binary handler for Windows applications"
    echo "-1" >/proc/sys/fs/binfmt_misc/windows
    RETVAL=$?
    echo "-1" >/proc/sys/fs/binfmt_misc/windowsPE
    RETVAL=$((RETVAL + $?))
    [ $RETVAL -eq 0 ] && success || failure
    echo
}

reload() {
    stop
    start
}

wine_status() {
    if [ -e /proc/sys/fs/binfmt_misc/windows ]; then
        echo $"Wine binary format handlers are registered."
        return 0
    else
        echo $"Wine binary format handlers are not registered."
        return 3
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        wine_status
        RETVAL=$?
        ;;
    restart)
        stop
        start
        ;;
    condrestart|try-restart)
        if [ -e /proc/sys/fs/binfmt_misc/windows ]; then
            stop
            start
        fi
        ;;
    *)
        echo $"Usage: $prog {start|stop|status|restart|condrestart|try-restart}"
        exit 1
esac
exit $RETVAL
EOF

echo "%{_libdir}/wine/" >wine.ld.conf

%build
export CFLAGS="%{optflags} -Wno-error"
%configure \
    --sysconfdir="%{_sysconfdir}/wine" \
    --disable-tests \
    --enable-maintainer-mode \
%ifarch x86_64
    --enable-win64 \
%endif 
    --with-x \
%{?_without_opengl:--without-opengl}
%{__make} depend
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    dlldir="%{_libdir}/wine" \
    includedir="%{_includedir}/wine" \
    libdir="%{_libdir}" \
    sysconfdir="%{_sysconfdir}/wine" \
    LDCONFIG="/bin/true" \
    UPDATE_DESKTOP_DATABASE="/bin/true"

%{__install} -Dp -m0755 wine.sysv %{buildroot}%{_initrddir}/wine
%{__install} -Dp -m0644 wine.ld.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/wine-%{_arch}.conf

desktop-file-install --delete-original             \
    --vendor="%{desktop_vendor}"                   \
    --dir="%{buildroot}%{_datadir}/applications"   \
    %{buildroot}%{_datadir}/applications/wine.desktop

desktop-file-install                               \
    --vendor="%{desktop_vendor}"                   \
    --dir="%{buildroot}%{_datadir}/applications"   \
    wine-config.desktop

desktop-file-install                               \
    --vendor="%{desktop_vendor}"                   \
    --dir="%{buildroot}%{_datadir}/applications"   \
    wine-fileman.desktop

desktop-file-install                               \
    --vendor="%{desktop_vendor}"                   \
    --dir="%{buildroot}%{_datadir}/applications"   \
    wine-regedit.desktop

desktop-file-install                               \
    --vendor="%{desktop_vendor}"                   \
    --dir="%{buildroot}%{_datadir}/applications"   \
    wine-uninstaller.desktop

%post core
/sbin/ldconfig
update-desktop-database &>/dev/null || :
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add wine
    /sbin/chkconfig --level 2345 wine on
    /sbin/service wine start &>/dev/null || :
fi

%preun core
if [ $1 -eq 0 ]; then
    /sbin/service wine stop &>/dev/null
    /sbin/chkconfig --del wine
fi

%postun core
/sbin/ldconfig
update-desktop-database &>/dev/null || :

%post capi -p /sbin/ldconfig
%postun capi -p /sbin/ldconfig

%post cms -p /sbin/ldconfig
%postun cms -p /sbin/ldconfig

%post esd -p /sbin/ldconfig
%postun esd -p /sbin/ldconfig

%post jack -p /sbin/ldconfig
%postun jack -p /sbin/ldconfig

%post ldap -p /sbin/ldconfig
%postun ldap -p /sbin/ldconfig

%post nas -p /sbin/ldconfig
%postun nas -p /sbin/ldconfig

%post twain -p /sbin/ldconfig
%postun twain -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)

%files core
%defattr(-, root, root, 0755)
%doc ANNOUNCE AUTHORS COPYING.LIB LICENSE* README VERSION
%doc documentation/ChangeLog* documentation/README.*
%doc %{_mandir}/man1/msiexec.1*
%doc %{_mandir}/man1/notepad.1*
%doc %{_mandir}/man1/regedit.1*
%doc %{_mandir}/man1/regsvr32.1*
%doc %{_mandir}/man1/wine.1*
%doc %{_mandir}/man1/wineboot.1*
%doc %{_mandir}/man1/winecfg.1*
%doc %{_mandir}/man1/winecpp.1*
%doc %{_mandir}/man1/wineconsole.1*
%doc %{_mandir}/man1/winefile.1*
%doc %{_mandir}/man1/winemine.1*
%doc %{_mandir}/man1/winepath.1*
%doc %{_mandir}/man1/wineserver.1*
%doc %{_mandir}/*/man1/wine.1*
%doc %{_mandir}/*/man1/winemaker.1*
%doc %{_mandir}/*/man1/wineserver.1*
%config %{_initrddir}/wine
%config %{_sysconfdir}/ld.so.conf.d/wine-%{_arch}.conf
%{_bindir}/msiexec
%{_bindir}/notepad
%{_bindir}/regedit
%{_bindir}/regsvr32
%{_bindir}/wine
%{_bindir}/wineboot
%{_bindir}/winecfg
%{_bindir}/wineconsole
%{_bindir}/winedbg
%{_bindir}/winedump
%{_bindir}/winefile
#%{_bindir}/winelauncher
%{_bindir}/winemaker
%{_bindir}/winemine
%{_bindir}/winepath
%{_bindir}/wineserver
%{_bindir}/wine-preloader
%{_datadir}/applications/%{desktop_vendor}-wine.desktop
%{_datadir}/applications/%{desktop_vendor}-wine-config.desktop
%{_datadir}/applications/%{desktop_vendor}-wine-fileman.desktop
%{_datadir}/applications/%{desktop_vendor}-wine-regedit.desktop
%{_datadir}/applications/%{desktop_vendor}-wine-uninstaller.desktop
%dir %{_datadir}/wine/
%{_datadir}/wine/fonts/
%{_datadir}/wine/generic.ppd
%{_datadir}/wine/l_intl.nls
%{_datadir}/wine/wine.inf
%{_libdir}/libwine.so.1*
%dir %{_libdir}/wine/
%{_libdir}/wine/fakedlls/

### exe16.so
%ifarch %{ix86}
%{_libdir}/wine/gdi.exe16.so
%{_libdir}/wine/krnl386.exe16.so
%{_libdir}/wine/user.exe16.so
%{_libdir}/wine/winhelp.exe16.so
%endif

### exe.so
%{_libdir}/wine/attrib.exe.so
%{_libdir}/wine/cacls.exe.so
%{_libdir}/wine/clock.exe.so
%{_libdir}/wine/cmd.exe.so
%{_libdir}/wine/control.exe.so
%{_libdir}/wine/cryptdlg.dll.so
%{_libdir}/wine/dxdiag.exe.so
%{_libdir}/wine/eject.exe.so
%{_libdir}/wine/expand.exe.so
%{_libdir}/wine/explorer.exe.so
%{_libdir}/wine/extrac32.exe.so
%{_libdir}/wine/hh.exe.so
%{_libdir}/wine/icinfo.exe.so
%{_libdir}/wine/iexplore.exe.so
%{_libdir}/wine/lodctr.exe.so
%{_libdir}/wine/mshta.exe.so
%{_libdir}/wine/msiexec.exe.so
%{_libdir}/wine/net.exe.so
%{_libdir}/wine/ngen.exe.so
%{_libdir}/wine/notepad.exe.so
%{_libdir}/wine/ntoskrnl.exe.so
%{_libdir}/wine/oleview.exe.so
%{_libdir}/wine/ping.exe.so
%{_libdir}/wine/progman.exe.so
%{_libdir}/wine/reg.exe.so
%{_libdir}/wine/regedit.exe.so
%{_libdir}/wine/regsvr32.exe.so
%{_libdir}/wine/rpcss.exe.so
%{_libdir}/wine/rundll32.exe.so
%{_libdir}/wine/secedit.exe.so
%{_libdir}/wine/services.exe.so
%{_libdir}/wine/sc.exe.so
%{_libdir}/wine/spoolsv.exe.so
%{_libdir}/wine/start.exe.so
%{_libdir}/wine/svchost.exe.so
%{_libdir}/wine/taskmgr.exe.so
%{_libdir}/wine/termsv.exe.so
%{_libdir}/wine/uninstaller.exe.so
%{_libdir}/wine/unlodctr.exe.so
%{_libdir}/wine/wineboot.exe.so
%{_libdir}/wine/winebrowser.exe.so
%{_libdir}/wine/winecfg.exe.so
%{_libdir}/wine/wineconsole.exe.so
%{_libdir}/wine/winedbg.exe.so
%{_libdir}/wine/winedevice.exe.so
%{_libdir}/wine/winefile.exe.so
%{_libdir}/wine/winemenubuilder.exe.so
%{_libdir}/wine/winemine.exe.so
%{_libdir}/wine/winepath.exe.so
%ifarch %{ix86}
%{_libdir}/wine/winevdm.exe.so
%endif
%{_libdir}/wine/winhlp32.exe.so
%{_libdir}/wine/winver.exe.so
%{_libdir}/wine/wordpad.exe.so
%{_libdir}/wine/write.exe.so
%{_libdir}/wine/xcopy.exe.so

### cpl.so
%{_libdir}/wine/appwiz.cpl.so

### dll16.so
%ifarch %{ix86}
%{_libdir}/wine/avifile.dll16.so
%{_libdir}/wine/commdlg.dll16.so
%{_libdir}/wine/compobj.dll16.so
%{_libdir}/wine/ctl3d.dll16.so
%{_libdir}/wine/ctl3dv2.dll16.so
%{_libdir}/wine/ddeml.dll16.so
%{_libdir}/wine/dispdib.dll16.so
%{_libdir}/wine/imm.dll16.so
%{_libdir}/wine/lzexpand.dll16.so
%{_libdir}/wine/mmsystem.dll16.so
%{_libdir}/wine/msacm.dll16.so
%{_libdir}/wine/msvideo.dll16.so
%{_libdir}/wine/ole2.dll16.so
%{_libdir}/wine/ole2conv.dll16.so
%{_libdir}/wine/ole2disp.dll16.so
%{_libdir}/wine/ole2nls.dll16.so
%{_libdir}/wine/ole2prox.dll16.so
%{_libdir}/wine/ole2thk.dll16.so
%{_libdir}/wine/olecli.dll16.so
%{_libdir}/wine/olesvr.dll16.so
%{_libdir}/wine/rasapi16.dll16.so
%{_libdir}/wine/setupx.dll16.so
%{_libdir}/wine/shell.dll16.so
%{_libdir}/wine/storage.dll16.so
%{_libdir}/wine/stress.dll16.so
%{_libdir}/wine/toolhelp.dll16.so
%{_libdir}/wine/twain.dll16.so
%{_libdir}/wine/typelib.dll16.so
%{_libdir}/wine/ver.dll16.so
%{_libdir}/wine/w32sys.dll16.so
%{_libdir}/wine/win32s16.dll16.so
%{_libdir}/wine/win87em.dll16.so
%{_libdir}/wine/winaspi.dll16.so
%{_libdir}/wine/windebug.dll16.so
%{_libdir}/wine/wing.dll16.so
%{_libdir}/wine/winnls.dll16.so
%{_libdir}/wine/winsock.dll16.so
%{_libdir}/wine/wintab.dll16.so
%endif

### dll.so
%{_libdir}/wine/acledit.dll.so
%{_libdir}/wine/aclui.dll.so
%{_libdir}/wine/activeds.dll.so
%{_libdir}/wine/actxprxy.dll.so
%{_libdir}/wine/advapi32.dll.so
%{_libdir}/wine/advpack.dll.so
%{_libdir}/wine/amstream.dll.so
%{_libdir}/wine/atl.dll.so
%{_libdir}/wine/authz.dll.so
%{_libdir}/wine/avicap32.dll.so
%{_libdir}/wine/avifil32.dll.so
%{_libdir}/wine/avrt.dll.so
%{_libdir}/wine/bcrypt.dll.so
%{_libdir}/wine/browseui.dll.so
%{_libdir}/wine/cabinet.dll.so
%{_libdir}/wine/cards.dll.so
%{_libdir}/wine/cfgmgr32.dll.so
%{_libdir}/wine/clusapi.dll.so
%{_libdir}/wine/comcat.dll.so
%{_libdir}/wine/comctl32.dll.so
%{_libdir}/wine/comdlg32.dll.so
%{_libdir}/wine/compstui.dll.so
%{_libdir}/wine/credui.dll.so
%{_libdir}/wine/crtdll.dll.so
%{_libdir}/wine/crypt32.dll.so
%{_libdir}/wine/cryptdll.dll.so
%{_libdir}/wine/cryptnet.dll.so
%{_libdir}/wine/cryptui.dll.so
%{_libdir}/wine/ctapi32.dll.so
%{_libdir}/wine/ctl3d32.dll.so
%{_libdir}/wine/d3d8.dll.so
%{_libdir}/wine/d3d9.dll.so
%{_libdir}/wine/d3d10.dll.so
%{_libdir}/wine/d3d10core.dll.so
%{_libdir}/wine/d3dim.dll.so
%{_libdir}/wine/d3drm.dll.so
%{_libdir}/wine/d3dx9_24.dll.so
%{_libdir}/wine/d3dx9_25.dll.so
%{_libdir}/wine/d3dx9_26.dll.so
%{_libdir}/wine/d3dx9_27.dll.so
%{_libdir}/wine/d3dx9_28.dll.so
%{_libdir}/wine/d3dx9_29.dll.so
%{_libdir}/wine/d3dx9_30.dll.so
%{_libdir}/wine/d3dx9_31.dll.so
%{_libdir}/wine/d3dx9_32.dll.so
%{_libdir}/wine/d3dx9_33.dll.so
%{_libdir}/wine/d3dx9_34.dll.so
%{_libdir}/wine/d3dx9_35.dll.so
%{_libdir}/wine/d3dx9_36.dll.so
%{_libdir}/wine/d3dx9_37.dll.so
%{_libdir}/wine/d3dx9_38.dll.so
%{_libdir}/wine/d3dx9_39.dll.so
%{_libdir}/wine/d3dx9_40.dll.so
%{_libdir}/wine/d3dx9_41.dll.so
%{_libdir}/wine/d3dx9_42.dll.so
%{_libdir}/wine/d3dxof.dll.so
%{_libdir}/wine/dbghelp.dll.so
%{_libdir}/wine/dciman32.dll.so
%{_libdir}/wine/ddraw.dll.so
%{_libdir}/wine/ddrawex.dll.so
%{_libdir}/wine/devenum.dll.so
%{_libdir}/wine/dinput.dll.so
%{_libdir}/wine/dinput8.dll.so
%{_libdir}/wine/dispex.dll.so
%{_libdir}/wine/dmband.dll.so
%{_libdir}/wine/dmcompos.dll.so
%{_libdir}/wine/dmime.dll.so
%{_libdir}/wine/dmloader.dll.so
%{_libdir}/wine/dmscript.dll.so
%{_libdir}/wine/dmstyle.dll.so
%{_libdir}/wine/dmsynth.dll.so
%{_libdir}/wine/dmusic.dll.so
%{_libdir}/wine/dmusic32.dll.so
%{_libdir}/wine/dnsapi.dll.so
%{_libdir}/wine/dplay.dll.so
%{_libdir}/wine/dplayx.dll.so
%{_libdir}/wine/dpnaddr.dll.so
%{_libdir}/wine/dpnet.dll.so
%{_libdir}/wine/dpnhpast.dll.so
%{_libdir}/wine/dpnlobby.dll.so
%{_libdir}/wine/dpwsockx.dll.so
%{_libdir}/wine/drmclien.dll.so
%{_libdir}/wine/dsound.dll.so
%{_libdir}/wine/dssenh.dll.so
%{_libdir}/wine/dswave.dll.so
%{_libdir}/wine/dwmapi.dll.so
%{_libdir}/wine/dxdiagn.dll.so
%{_libdir}/wine/dxgi.dll.so
%{_libdir}/wine/faultrep.dll.so
%{_libdir}/wine/fltlib.dll.so
%{_libdir}/wine/fwpuclnt.dll.so
%{_libdir}/wine/fusion.dll.so
%{_libdir}/wine/gdi32.dll.so
%{_libdir}/wine/gdiplus.dll.so
%{!?_without_opengl:%{_libdir}/wine/glu32.dll.so}
#%{_libdir}/wine/glut32.dll.so
%{_libdir}/wine/gpkcsp.dll.so
%{_libdir}/wine/hal.dll.so
%{_libdir}/wine/hid.dll.so
%{_libdir}/wine/hlink.dll.so
%{_libdir}/wine/hnetcfg.dll.so
%{_libdir}/wine/httpapi.dll.so
%{_libdir}/wine/iccvid.dll.so
%{_libdir}/wine/icmp.dll.so
%{_libdir}/wine/imagehlp.dll.so
%{_libdir}/wine/imm32.dll.so
%{_libdir}/wine/inetcomm.dll.so
%{_libdir}/wine/inetmib1.dll.so
%{_libdir}/wine/infosoft.dll.so
%{_libdir}/wine/initpki.dll.so
%{_libdir}/wine/inkobj.dll.so
%{_libdir}/wine/inseng.dll.so
%{_libdir}/wine/iphlpapi.dll.so
%{_libdir}/wine/itircl.dll.so
%{_libdir}/wine/itss.dll.so
%{_libdir}/wine/jscript.dll.so
%{_libdir}/wine/kernel32.dll.so
%{_libdir}/wine/loadperf.dll.so
%{_libdir}/wine/localspl.dll.so
%{_libdir}/wine/localui.dll.so
%{_libdir}/wine/lz32.dll.so
%{_libdir}/wine/mapi32.dll.so
%{_libdir}/wine/mapistub.dll.so
%{_libdir}/wine/mciavi32.dll.so
%{_libdir}/wine/mcicda.dll.so
%{_libdir}/wine/mciqtz32.dll.so
%{_libdir}/wine/mciseq.dll.so
%{_libdir}/wine/mciwave.dll.so
%{_libdir}/wine/midimap.dll.so
%{_libdir}/wine/mlang.dll.so
%{_libdir}/wine/mmdevapi.dll.so
%{_libdir}/wine/mpr.dll.so
%{_libdir}/wine/mprapi.dll.so
%{_libdir}/wine/msacm32.dll.so
%{_libdir}/wine/mscat32.dll.so
%{_libdir}/wine/mscoree.dll.so
%{_libdir}/wine/msctf.dll.so
%{_libdir}/wine/msdaps.dll.so
%{_libdir}/wine/msdmo.dll.so
%{_libdir}/wine/msftedit.dll.so
%{_libdir}/wine/mshtml.dll.so
%{_libdir}/wine/msi.dll.so
%{_libdir}/wine/msimg32.dll.so
%{_libdir}/wine/msimtf.dll.so
%{_libdir}/wine/msisip.dll.so
%{_libdir}/wine/msnet32.dll.so
%{_libdir}/wine/msrle32.dll.so
%{_libdir}/wine/mssign32.dll.so
%{_libdir}/wine/mssip32.dll.so
%{_libdir}/wine/mstask.dll.so
%{_libdir}/wine/msvcirt.dll.so
%{_libdir}/wine/msvcr100.dll.so
%{_libdir}/wine/msvcr70.dll.so
%{_libdir}/wine/msvcr71.dll.so
%{_libdir}/wine/msvcr80.dll.so
%{_libdir}/wine/msvcr90.dll.so
%{_libdir}/wine/msvcrt.dll.so
%{_libdir}/wine/msvcrt20.dll.so
%{_libdir}/wine/msvcrt40.dll.so
%{_libdir}/wine/msvcrtd.dll.so
%{_libdir}/wine/msvfw32.dll.so
%{_libdir}/wine/msvidc32.dll.so
%{_libdir}/wine/mswsock.dll.so
%{_libdir}/wine/msxml3.dll.so
%{_libdir}/wine/msxml4.dll.so
%{_libdir}/wine/nddeapi.dll.so
%{_libdir}/wine/netapi32.dll.so
%{_libdir}/wine/newdev.dll.so
%{_libdir}/wine/ntdll.dll.so
%{_libdir}/wine/ntdsapi.dll.so
%{_libdir}/wine/ntprint.dll.so
%{_libdir}/wine/objsel.dll.so
%{_libdir}/wine/odbc32.dll.so
%{_libdir}/wine/odbccp32.dll.so
%{_libdir}/wine/ole32.dll.so
%{_libdir}/wine/oleacc.dll.so
%{_libdir}/wine/oleaut32.dll.so
%{_libdir}/wine/olecli32.dll.so
%{_libdir}/wine/oledb32.dll.so
%{_libdir}/wine/oledlg.dll.so
%{_libdir}/wine/olepro32.dll.so
%{_libdir}/wine/olesvr32.dll.so
%{_libdir}/wine/olethk32.dll.so
%{!?_without_opengl:%{_libdir}/wine/opengl32.dll.so}
%{_libdir}/wine/pdh.dll.so
%{_libdir}/wine/pidgen.dll.so
%{_libdir}/wine/powrprof.dll.so
%{_libdir}/wine/printui.dll.so
%{_libdir}/wine/propsys.dll.so
%{_libdir}/wine/psapi.dll.so
%{_libdir}/wine/pstorec.dll.so
%{_libdir}/wine/qcap.dll.so
%{_libdir}/wine/qedit.dll.so
%{_libdir}/wine/qmgr.dll.so
%{_libdir}/wine/qmgrprxy.dll.so
%{_libdir}/wine/quartz.dll.so
%{_libdir}/wine/query.dll.so
%{_libdir}/wine/rasapi32.dll.so
%{_libdir}/wine/rasdlg.dll.so
%{_libdir}/wine/resutils.dll.so
%{_libdir}/wine/riched20.dll.so
%{_libdir}/wine/riched32.dll.so
%{_libdir}/wine/rpcrt4.dll.so
%{_libdir}/wine/rsabase.dll.so
%{_libdir}/wine/rsaenh.dll.so
%{_libdir}/wine/rtutils.dll.so
%{_libdir}/wine/samlib.dll.so
%{_libdir}/wine/sccbase.dll.so
%{_libdir}/wine/schannel.dll.so
%{_libdir}/wine/secur32.dll.so
%{_libdir}/wine/security.dll.so
%{_libdir}/wine/sensapi.dll.so
%{_libdir}/wine/serialui.dll.so
%{_libdir}/wine/setupapi.dll.so
%{_libdir}/wine/sfc.dll.so
%{_libdir}/wine/sfc_os.dll.so
%{_libdir}/wine/shdoclc.dll.so
%{_libdir}/wine/shdocvw.dll.so
%{_libdir}/wine/shell32.dll.so
%{_libdir}/wine/shfolder.dll.so
%{_libdir}/wine/shlwapi.dll.so
%{_libdir}/wine/slbcsp.dll.so
%{_libdir}/wine/slc.dll.so
%{_libdir}/wine/snmpapi.dll.so
%{_libdir}/wine/softpub.dll.so
%{_libdir}/wine/spoolss.dll.so
%{_libdir}/wine/sti.dll.so
%{_libdir}/wine/svrapi.dll.so
%{_libdir}/wine/sxs.dll.so
%{_libdir}/wine/t2embed.dll.so
%{_libdir}/wine/tapi32.dll.so
%{_libdir}/wine/traffic.dll.so
%{_libdir}/wine/unicows.dll.so
%{_libdir}/wine/updspapi.dll.so
%{_libdir}/wine/url.dll.so
%{_libdir}/wine/urlmon.dll.so
%{_libdir}/wine/user32.dll.so
%{_libdir}/wine/userenv.dll.so
%{_libdir}/wine/usp10.dll.so
%{_libdir}/wine/uxtheme.dll.so
%{_libdir}/wine/vdmdbg.dll.so
%{_libdir}/wine/version.dll.so
%ifarch %{ix86}
%{_libdir}/wine/w32skrnl.dll.so
%endif
%{_libdir}/wine/wbemprox.dll.so
%{_libdir}/wine/wiaservc.dll.so
%{_libdir}/wine/windowscodecs.dll.so
%{!?_without_opengl:%{_libdir}/wine/wined3d.dll.so}
%{_libdir}/wine/winemapi.dll.so
%{_libdir}/wine/wing32.dll.so
%{_libdir}/wine/winhttp.dll.so
%{_libdir}/wine/wininet.dll.so
%{_libdir}/wine/winmm.dll.so
%{_libdir}/wine/winnls32.dll.so
%{_libdir}/wine/winscard.dll.so
%{_libdir}/wine/wintab32.dll.so
%{_libdir}/wine/wintrust.dll.so
%{_libdir}/wine/wmi.dll.so
%{_libdir}/wine/wmiutils.dll.so
%{_libdir}/wine/wnaspi32.dll.so
%ifarch %{ix86}
%{_libdir}/wine/wow32.dll.so
%endif
%{_libdir}/wine/ws2_32.dll.so
%{_libdir}/wine/wsock32.dll.so
%{_libdir}/wine/wtsapi32.dll.so
%{_libdir}/wine/wuapi.dll.so
%{_libdir}/wine/wuaueng.dll.so
%{_libdir}/wine/xinput1_1.dll.so
%{_libdir}/wine/xinput1_2.dll.so
%{_libdir}/wine/xinput1_3.dll.so
%{_libdir}/wine/xinput9_1_0.dll.so
%{_libdir}/wine/xmllite.dll.so

### ds.so
%{_libdir}/wine/gphoto2.ds.so
%{_libdir}/wine/sane.ds.so

### drv16.so
%{_libdir}/wine/comm.drv16.so
%{_libdir}/wine/display.drv16.so
%{_libdir}/wine/keyboard.drv16.so
%{_libdir}/wine/mouse.drv16.so
%{_libdir}/wine/sound.drv16.so
%{_libdir}/wine/system.drv16.so
%{_libdir}/wine/wineps16.drv16.so

### drv.so
%{_libdir}/wine/msacm32.drv.so
%{_libdir}/wine/wineaudioio.drv.so
%{_libdir}/wine/winecoreaudio.drv.so
%{_libdir}/wine/winejoystick.drv.so
%{_libdir}/wine/wineoss.drv.so
%{_libdir}/wine/winex11.drv.so
%{_libdir}/wine/winspool.drv.so
%{_libdir}/wine/winealsa.drv.so
%{_libdir}/wine/wineps.drv.so

### vxd
%ifarch %{ix86}
%{_libdir}/wine/ifsmgr.vxd.so
%{_libdir}/wine/mmdevldr.vxd.so
%{_libdir}/wine/monodebg.vxd.so
%{_libdir}/wine/vdhcp.vxd.so
%{_libdir}/wine/vmm.vxd.so
%{_libdir}/wine/vnbt.vxd.so
%{_libdir}/wine/vnetbios.vxd.so
%{_libdir}/wine/vtdapi.vxd.so
%{_libdir}/wine/vwin32.vxd.so
%endif

### acm.so
%{_libdir}/wine/imaadp32.acm.so
%{_libdir}/wine/msadp32.acm.so
%{_libdir}/wine/msg711.acm.so
%{_libdir}/wine/msgsm32.acm.so
%{_libdir}/wine/winemp3.acm.so

### tlb.so
%{_libdir}/wine/mshtml.tlb.so
%{_libdir}/wine/stdole2.tlb.so
%{_libdir}/wine/stdole32.tlb.so

### ocx.so
%{_libdir}/wine/hhctrl.ocx.so
%{_libdir}/wine/msisys.ocx.so

### mod16
%{_libdir}/wine/winoldap.mod16.so

### sys.so
%{_libdir}/wine/mountmgr.sys.so
%{_libdir}/wine/usbd.sys.so

%files capi
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/capi2032.dll.so

%files cms
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/mscms.dll.so

%files esd
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/wineesd.drv.so

%files jack
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/winejack.drv.so

%files ldap
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/wldap32.dll.so

%files nas
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/winenas.drv.so

%files twain
%defattr(-, root, root, 0755)
%dir %{_libdir}/wine/
%{_libdir}/wine/twain_32.dll.so

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/widl.1*
%doc %{_mandir}/man1/winebuild.1*
%doc %{_mandir}/man1/winedbg.1*
%doc %{_mandir}/man1/winedump.1*
%doc %{_mandir}/man1/wineg++.1*
%doc %{_mandir}/man1/winegcc.1*
%doc %{_mandir}/man1/winemaker.1*
%doc %{_mandir}/man1/wmc.1*
%doc %{_mandir}/man1/wrc.1*
%{_bindir}/function_grep.pl
%{_bindir}/widl
%{_bindir}/winebuild
%{_bindir}/winecpp
%{_bindir}/winedump
%{_bindir}/wineg++
%{_bindir}/winegcc
%{_bindir}/winemaker
%{_bindir}/wmc
%{_bindir}/wrc
%{_includedir}/wine/
%{_libdir}/*.so
%dir %{_libdir}/wine/
%{_libdir}/wine/*.a
%{_libdir}/wine/*.def

%changelog
* Fri Apr 15 2011 Dag Wieers <dag@wieers.com> - 1.2.3-1
- Updated to release 1.2.3.

* Fri Feb 11 2011 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Updated to release 1.2.2.

* Sat Oct 09 2010 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Sat Sep 18 2010 Dag Wieers <dag@wieers.com> - 1.2-3
- Moved gecko cabinet file in separate wine-gecko package.

* Tue Aug 24 2010 Dag Wieers <dag@wieers.com> - 1.2-2
- Added gecko cabinet file. (Bart Schaefer)

* Thu Aug 12 2010 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.
- Added a few fedora patches.

* Fri Oct 31 2008 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Tue Jun 17 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Sun Jun 08 2008 Dag Wieers <dag@wieers.com> - 1.0-0.rc3
- Updated to release 1.0-rc3.

* Tue May 27 2008 Dag Wieers <dag@wieers.com> - 1.0-0.rc2
- Updated to release 1.0-rc2.

* Tue May 13 2008 Dag Wieers <dag@wieers.com> - 1.0-0.rc1
- Updated to release 1.0-rc1.

* Fri May 09 2008 Dag Wieers <dag@wieers.com> - 0.9.61-1
- Updated to release 0.9.61.

* Sun Apr 13 2008 Dag Wieers <dag@wieers.com> - 0.9.59-1
- Updated to release 0.9.59.

* Tue Jan 08 2008 Dag Wieers <dag@wieers.com> - 0.9.52-1
- Updated to release 0.9.52.

* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.9.50-1
- Updated to release 0.9.50.

* Tue Oct 30 2007 Dag Wieers <dag@wieers.com> - 0.9.48-1
- Updated to release 0.9.48.

* Sun Oct 14 2007 Dag Wieers <dag@wieers.com> - 0.9.47-1
- Updated to release 0.9.47.

* Sat Sep 29 2007 Dag Wieers <dag@wieers.com> - 0.9.46-1
- Updated to release 0.9.46.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.9.45-1
- Updated to release 0.9.45.

* Sat Aug 25 2007 Dag Wieers <dag@wieers.com> - 0.9.44-1
- Updated to release 0.9.44.

* Sun Aug 12 2007 Dag Wieers <dag@wieers.com> - 0.9.43-1
- Updated to release 0.9.43.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 0.9.42-1
- Updated to release 0.9.42.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 0.9.41-1
- Updated to release 0.9.41.

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 0.9.40-1
- Updated to release 0.9.40.

* Sat Jun 16 2007 Dag Wieers <dag@wieers.com> - 0.9.39-1
- Updated to release 0.9.39.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 0.9.38-1
- Updated to release 0.9.38.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 0.9.37-1
- Updated to release 0.9.37.

* Sat Apr 28 2007 Dag Wieers <dag@wieers.com> - 0.9.36-1
- Updated to release 0.9.36.

* Sun Apr 15 2007 Dag Wieers <dag@wieers.com> - 0.9.35-1
- Updated to release 0.9.35.

* Mon Apr 02 2007 Dag Wieers <dag@wieers.com> - 0.9.34-1
- Updated to release 0.9.34.

* Wed Mar 21 2007 Dag Wieers <dag@wieers.com> - 0.9.33-2
- Fixed a dependency reference to /usr/X11R6/bin/xmessage on EL5.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.9.33-1
- Updated to release 0.9.33.

* Sat Mar 03 2007 Dag Wieers <dag@wieers.com> - 0.9.32-1
- Updated to release 0.9.32.
- Fixed the depenency to update-desktop-database. (Bart Schaefer)

* Sat Feb 17 2007 Dag Wieers <dag@wieers.com> - 0.9.31-1
- Initial package. (using DAR)
