# Authority: dag
# Soapbox: 0

%define xfontdir	/usr/X11R6/lib/X11/fonts/misc
%define compileset	compiletime-settings.rpm

Summary: A DOS emulator.
Name: dosemu
Version: 1.1.4
Release: 0
License: distributable
Group: Applications/Emulators
URL: http://www.dosemu.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/home-made/apt/

Source0: ftp://ftp.dosemu.org/%{name}/%{name}-%{version}.tgz
Source8: autoexec.bat
Source9: config.sys
Source20: vga_cyr8x16.pcf.gz
Source21: vga_cyr8x16.pcf.README
Source22: dosemu-freedos-b8p-bin.tgz
Source23: dosemu-cp1125.tar.gz
Source24: dosemu-man_ru.tgz
Patch3: dosemu-1.1.4-security.patch
Patch4: dosemu-0.98.1-justroot.patch
Patch7: dosemu-1.0.0-man.patch
Patch14: dosemu-1.1.4-time.patch
Patch20: dosemu-1.1.4-instroot.asp.patch
Patch21: dpmi_sti4a.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}

Requires: kernel >= 2.0.28, mtools >= 3.6
#BuildPrereq: mtools >= 3.6
Obsoletes: dosemu-freedos
Exclusivearch: %{ix86}

%description
Dosemu is a DOS emulator.  Once you've installed dosemu, start the DOS
emulator by typing in the dos command.

You need to install dosemu if you use DOS programs and you want to be
able to run them on your Red Hat Linux system.

%package -n xdosemu
Summary: A DOS emulator for the X Window System.
Group: Applications/Emulators
Requires: %{name} = %{version}

%description -n xdosemu
Xdosemu is a version of the dosemu DOS emulator that runs with the X
Window System.  Xdosemu provides VGA graphics and mouse support.

Install xdosemu if you need to run DOS programs on your system, and
you'd like to do so with the convenience of graphics support and mouse
capabilities.

%prep
%setup -q
%patch3 -p1 -b .security
%patch4 -p1 -b .justroot
%patch7 -p1 -b .man
%patch14 -p1 -b .time
%patch20 -p1 -b .instroot
%patch21 -p0 -b .dpmi_sti4a

# Copy ukrainian package
cp -a %{SOURCE23} %{dosemuuk}

# Copy the russian manuals
mkdir -p man/ru
tar -xzf %{SOURCE24} -C man/ru

%build
perl -pi -e "s|/usr/X11/|/usr/X11R6/|g;s|/usr/X11$|/usr/X11R6|g" \
	base-configure \
	base-configure.in \
	etc/xterm*

export PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/X11R6/bin
export CXXFLAGS="$RPM_OPT_FLAGS -L/usr/X11R6/lib" 
export CFLAGS="$RPM_OPT_FLAGS -L/usr/X11R6/lib"
export LDFLAGS="-L/usr/X11R6/lib"
export XLIBRARY_DIR="/usr/X11R6/lib"

cat << EOF > %{compileset}
config {
  experimental off
  sbemu on
  mitshm on
  x on
  net on
  dodebug off
  slangforce on
  runasroot off
  linkstatic off
  cpuemu off
  aspi on
  svgalib off
  plugin_keyboard off
  plugin_kbd_unicode on
  plugin_extra_charsets on
  plugin_term on
  plugin_translate on
  plugin_demo off
  target_cpu auto
  prefix %{_prefix}
  bindir %{_prefix}/bin
  sysconfdir %{_sysconfdir}/dosemu
  datadir %{_prefix}/share
  mandir %{_mandir}
  docdir %{_docdir}/%{name}-%{version}
  syshdimagedir /var/lib/dosemu
  x11fontdir %{xfontdir}
  fdtarball %{freedos}
}
EOF

./default-configure %{compileset} --without-x
%{__make} %{?_smp_mflags} WAIT="no"

%{__mv} -f bin/dosemu.bin bin/noxdosemu.bin
%{__mv} -f bin/dosemu.map bin/noxdosemu.map

%{__rm} -f config.cache
find . -name "*.o" | xargs rm -f

./default-configure %{compileset} --with-x
%{__make} %{?_smp_mflags} WAIT="no"

%{__mv} -f bin/dosemu.bin bin/xdosemu.bin
%{__mv} -f bin/dosemu.map bin/xdosemu.map
%{__mv} -f bin/noxdosemu.bin bin/dosemu.bin
%{__mv} -f bin/noxdosemu.map bin/dosemu.map

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/pixmaps \
			%{buildroot}%{_mandir}/ru/man1 \
			%{buildroot}%{_sysconfdir}/X11/applnk/Emulators

%{__make} install INSTROOT="%{buildroot}" \
	bindir="%{_bindir}" \
	sysconfdir="%{_sysconfdir}/dosemu" \
	datadir="%{_datadir}" \
	mandir="%{_mandir}" \
	docdir="%{_docdir}/%{name}-%{version}" \
	x11fontdir="%{_prefix}/X11R6/lib/X11/fonts/misc"

%{__rm} -f %{buildroot}%{_bindir}/xdos*
%{__install} -m0755 bin/xdosemu.bin %{buildroot}%{_bindir}/xdos

VER=`cat VERSION`
if [ -z `echo $VER | cut -f4 -d.` ]; then
	VER=`echo ${VER}.0`
fi
%{__install} -m0644 bin/xdosemu.map %{buildroot}%{_datadir}/dosemu/xdos-${VER}.map

for file in dexeconfig hdinfo mkhdimage mkfatimage16; do
	%{__install} -m0755 src/tools/periph/$file %{buildroot}%{_bindir}
done

%{__install} -m0644 etc/dosemu.xpm %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 etc/dosemu.users.secure %{buildroot}%{_sysconfdir}/dosemu/dosemu.users

# Make rundos
cat <<EOF >%{buildroot}%{_bindir}/rundos
#!/bin/sh
export BINDIR=/bin
# ignore errors if user does not have module installed
exec %{_bindir}/dos $*
EOF
chmod 0755 %{buildroot}%{_bindir}/rundos

# Create .desktop file for KDE and GNOME menus...
cat >%{buildroot}%{_sysconfdir}/X11/applnk/Emulators/dosemu.desktop <<EOF
[Desktop Entry]
Name=DOSEmu
Type=Application
Description=DOS Emulator
Exec=xdos
Icon=dosemu.xpm
EOF

zcat %{SOURCE20} > %{buildroot}%{_prefix}/X11R6/lib/X11/fonts/misc/vga.pcf

%{__install} -m0644 %{SOURCE22} %{buildroot}%{_datadir}/dosemu/dosemu-freedos-bin.tgz
%{__install} -m0644 man/ru/*.1 %{buildroot}%{_mandir}/ru/man1

%post -n xdosemu
if [ -x /usr/X11R6/bin/mkfontdir ]; then
	(cd %{xfontdir}; /usr/X11R6/bin/mkfontdir)
fi
killall -USR1 xfs > /dev/null 2>&1 || :

%postun -n xdosemu
if [ -x /usr/X11R6/bin/mkfontdir ]; then
	(cd %{xfontdir}; /usr/X11R6/bin/mkfontdir)
fi
killall -USR1 xfs > /dev/null 2>&1 || :

%files
%defattr(-, root, root, 0755)
%doc QuickStart doc/* README*
%doc %{dosemuuk}
%doc %{_mandir}/man1/dosdebug.1*
%doc %{_mandir}/man1/dosemu*.1*
%doc %{_mandir}/man1/mkfatimage16.1*
%doc %{_mandir}/man1/xdos.1*
%doc %{_mandir}/*/man1/dosdebug.1*
%doc %{_mandir}/*/man1/dosemu*.1*
%doc %{_mandir}/*/man1/mkfatimage16.1*
%doc %{_mandir}/*/man1/xdos.1*

%config %{_sysconfdir}/dosemu/

%{_localstatedir}/lib/dosemu/

%attr(755, root, root, 0755) %{_bindir}/dosemu*
%{_bindir}/dosdebug
%{_bindir}/dexeconfig
%{_bindir}/hdinfo
%{_bindir}/midid
%{_bindir}/mkhdimage
%{_bindir}/mkfatimage
%{_bindir}/mkfatimage16
%{_bindir}/rundos

%dir %{_datadir}/dosemu

%dir %{_datadir}/dosemu/freedos
%{_datadir}/dosemu/freedos/*

%dir %{_datadir}/dosemu/keymap
%{_datadir}/dosemu/keymap/*

%{_datadir}/dosemu/dosemu-%{version}*.map
%{_datadir}/dosemu/dosemu-bin.tgz
%{_datadir}/dosemu/dosemu-freedos-bin.tgz

%files -n xdosemu
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/X11/applnk/Emulators/dosemu.desktop
%{_bindir}/xdos
%{_prefix}/X11R6/lib/X11/fonts/misc/vga.pcf
%{_datadir}/dosemu/xdos-%{version}*.map
%{_datadir}/pixmaps/dosemu.xpm

%clean
%{__rm} -rf %{buildroot}
%{__rm} -f dosemu.files

%changelog
* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 1.1.4-0
- Initial package. (using DAR)
