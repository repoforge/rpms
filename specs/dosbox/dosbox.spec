# $Id$
# Authority: dag

Summary: x86/DOS emulator with sound/graphics
Name: dosbox
Version: 0.65
Release: 1
License: GPL
Group: Applications/Emulators
URL: http://dosbox.sourceforge.net/

Source0: http://dl.sf.net/dosbox/dosbox-%{version}.tar.gz
Source1: dosbox.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, SDL-devel, alsa-lib-devel, xorg-x11-devel
BuildRequires: desktop-file-utils

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
	--enable-shots
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 dosbox.desktop %{buildroot}/etc/X11/applnk/Applications/dosbox.desktop
%else
	%{__mkdir_p} %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor} \
		--dir %{buildroot}%{_datadir}/applications  \
		dosbox.desktop
%endif

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
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 0.65-1
- Initialm package. (using DAR)
