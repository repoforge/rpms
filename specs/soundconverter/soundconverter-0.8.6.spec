# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Simple sound converter application
Name: soundconverter
Version: 0.8.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://soundconverter.berlios.de/

Source: http://download.berlios.de/soundconverter/soundconverter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: desktop-file-utils
Requires: pygtk2, gstreamer-python, gnome-python2-gconf


%description
A simple sound converter application. It can convert from and to all
gstreamer supported formats.

%prep
%setup

%{__perl} -pi.orig -e 's|^GLADE\s*=.*|GLADE="%{_datadir}/soundconverter/soundconverter.glade"|' soundconverter.py

%{__cat} <<EOF >soundconverter.desktop
[Desktop Entry]
Encoding=UTF-8
Name=SoundConverter
Comment=Convert audio using GStreamer
Exec=soundconverter
Terminal=false
Type=Application
Icon=soundconverter.png
Categories=GNOME;Application;AudioVideo;
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 soundconverter.py %{buildroot}%{_bindir}/soundconverter
%{__install} -Dp -m0644 soundconverter.glade %{buildroot}%{_datadir}/soundconverter/soundconverter.glade
%{__install} -Dp -m0644 logo.png %{buildroot}%{_datadir}/soundconverter/logo.png
%{__install} -Dp -m0644 logo.png %{buildroot}%{_datadir}/pixmaps/soundconverter.png

desktop-file-install --vendor %{desktop_vendor}    \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category X-Red-Hat-Base              \
	soundconverter.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%{_bindir}/soundconverter
%{_datadir}/soundconverter/
%{_datadir}/applications/*soundconverter.desktop
%{_datadir}/pixmaps/soundconverter.png

%changelog
* Fri Jun 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sat Jan 07 2006 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Initial package. (using DAR)
