# $Id$
# Authority: dag

%{!?dtag:%define _with_avahi 1}

%{?el4:%define _without_modxorg 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: x86/DOS emulator with sound/graphics
Name: dosbox
Version: 0.73
Release: 1%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://dosbox.sourceforge.net/

Source0: http://dl.sf.net/dosbox/dosbox-%{version}.tar.gz
Source1: dosbox.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: desktop-file-utils
BuildRequires: libpng-devel
BuildRequires: SDL-devel
BuildRequires: SDL_net-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel libGLU-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
DOSBox is a DOS-emulator using SDL for easy portability to different
platforms. DOSBox has already been ported to several different platforms,
such as Windows, BeOS, Linux, Mac OS X...

DOSBox emulates a 286/386 realmode CPU, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older games...
You can "re-live" the good old days with the help of DOSBox, it can run plenty
of the old classics that don't run on your new computer!

%prep
%setup

%{__cat} <<EOF >dosbox.desktop
[Desktop Entry]
Encoding=UTF-8
Name=DOSBox
Comment=An x86/DOS emulator with sound/graphics
Exec=dosbox
Icon=dosbox.png
Terminal=false
Type=Application
Categories=Application;Utility;
EOF

%build
%configure \
    --program-prefix="%{?_program_prefix}" \
%{?_without_opengl:--disable-opengl} \
    --enable-core-inline \
    --enable-shots
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir_p} %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    dosbox.desktop

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/dosbox.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%doc %{_mandir}/man1/dosbox.1*
%{_bindir}/dosbox
%{_datadir}/applications/%{desktop_vendor}-dosbox.desktop
%{_datadir}/pixmaps/dosbox.png

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 0.73-1
- Updated to release 0.73.

* Tue Aug 28 2007 Dag Wieers <dag@wieers.com> - 0.72-1
- Updated to release 0.72.

* Sat Aug 11 2007 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Mon Mar 26 2007 Dag Wieers <dag@wieers.com> - 0.70-1
- Updated to release 0.70.

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 0.65-1
- Initial package. (using DAR)
