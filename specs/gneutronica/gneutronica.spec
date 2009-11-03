# $Id$
# Authority: dries
# Upstream: Stephen Cameron <smcameron$yahoo,com>

Summary: MIDI drum machine
Name: gneutronica
Version: 0.33
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/gneutronica/

Source: http://dl.sf.net/gneutronica/gneutronica-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, desktop-file-utils, alsa-lib-devel

%description
Gneutronica is a MIDI drum machine for Linux with a Gnome/GTK user interface 
which provides a means to easily create and play back drum tracks to MIDI 
devices (and to softsynths via snd_virmidi).

%prep
%setup
%{__perl} -pi -e 's|/usr/share/man|\$\{mandir\}|g;' Makefile
%{__perl} -pi -e 's|/usr/share/pixmaps|\$\{datadir\}/pixmaps|g;' Makefile
%{__perl} -pi -e 's|/usr/local/share|%{_datadir}|g;' *.c

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gneutronica
Comment=MIDI drum machine
Icon=gneutronica_icon.png
Exec=gneutronica
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_mandir}/man1
%makeinstall BINDIR=%{buildroot}%{_bindir} SHAREDIR=%{buildroot}%{_datadir}/gneutronica

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL TODO
%doc %{_mandir}/man1/gneutronica*
%{_bindir}/gneutronica
%{_datadir}/gneutronica/
%{_datadir}/pixmaps/gneutronica_icon.png
%{_datadir}/applications/*-gneutronica.desktop

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Tue May 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
