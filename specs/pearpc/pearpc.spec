# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: PowerPC Architecture Emulator
Name: pearpc
Version: 0.3.1
Release: 1
Group: Applications/Emulators
License: GPL
URL: http://pearpc.sourceforge.net/

Source0: http://dl.sf.net/pearpc/pearpc-%{version}.tar.bz2
Source1: http://pearpc.sourceforge.net/pearpc3.png
Source2: http://dl.sf.net/pearpc/pearpc-3gib.img.bz2
Source3: http://dl.sf.net/pearpc/pearpc-6gib.img.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, SDL-devel
BuildRequires: desktop-file-utils, gcc-c++
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
PearPC is an architecture-independent PowerPC platform emulator capable of
running most PowerPC operating systems.


%prep
%setup

### FIXME: Fix /usr/lib(64) for x86_64. (Please fix upstream)
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure


%build
%configure \
%ifarch %{ix86}
    --enable-cpu="jitc_x86" \
%endif
    --enable-ui="sdl"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=PearPC
Comment=PowerPC Architecture Emulator
Exec=ppc %{_sysconfdir}/ppc.conf
Icon=pearpc.png
Terminal=false
Type=Application
Categories=Application;Utility;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# Icon for the desktop file
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/pearpc.png

# Example (patched) configuration file
%{__install} -Dp -m 0644 ppccfg.example %{buildroot}%{_sysconfdir}/ppc.conf

# Empty compressed disk images + video driver
%{__mkdir_p} %{buildroot}%{_datadir}/pearpc/emptyimages
%{__install} -m 0644 %{SOURCE2} %{SOURCE3} \
    %{buildroot}%{_datadir}/pearpc/emptyimages/
%{__install} -m 0644 video.x %{buildroot}%{_datadir}/pearpc/

# Change some paths in the configuration file
%{__perl} -pi -e \
    's|^(prom_driver_graphic =).*|$1 "%{_datadir}/pearpc/video.x"|g;
     s|^(pci_ide0_master_image =).*|$1 "%{_datadir}/pearpc/pearpc-3gib.img"|g' \
    %{buildroot}%{_sysconfdir}/ppc.conf


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO ppccfg.example
%config(noreplace) %{_sysconfdir}/ppc.conf
%{_bindir}/ppc
%{_datadir}/pixmaps/pearpc.png
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/pearpc/
%{_mandir}/man1/ppc.1*


%changelog
* Wed Sep 22 2004 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Update to 0.3.1.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Added fixes for x86_64.

* Wed Aug 25 2004 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Update to 0.2.0 and cleanups.

* Tue May 11 2004 Che
- initial rpm release
- very quickly done but its an experimental release anyways

