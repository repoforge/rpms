# $Id$

# Authority: dag
# Upstream: <fixounet@free.fr>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define rname avidemux

Summary: Graphical video editing tool.
Name: avidemux2
Version: 2.0.22
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://fixounet.free.fr/avidemux/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fixounet.free.fr/avidemux/avidemux-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gcc >= 3.0, glib-devel, gtk2-devel >= 2.0.0
BuildRequires: nasm >= 0.98.32

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX 
compatible encoder and the Gimp Toolkit (GTK) libraries.

%prep
%setup -n %{rname}-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Avidemux Video Editor
Comment=Edit your videos in real-time
Icon=gnome-multimedia.png
Exec=avidemux2
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure \
	--disable-dependency-tracking \
	--disable-warnings
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Base kde_locale on $(datadir). (Please fix upstream)
%makeinstall \
	kde_locale="%{buildroot}%{_datadir}/locale"
%find_lang %{rname}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING History README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 2.0.22-0
- Updated to release 2.0.22.

* Mon Dec 22 2003 Dag Wieers <dag@wieers.com> - 2.0.20-0
- Updated to release 2.0.20.

* Sun Nov 02 2003 Dag Wieers <dag@wieers.com> - 2.0.18-0
- Updated to release 2.0.18.

* Sun Sep 27 2003 Dag Wieers <dag@wieers.com> - 2.0.16-0
- Updated to release 2.0.16.

* Sat Aug 23 2003 Dag Wieers <dag@wieers.com> - 2.0.14-1
- Rebuild against xvidcore-0.9.2.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 2.0.14-0
- Updated to release 2.0.14.

* Sun Aug 03 2003 Dag Wieers <dag@wieers.com> - 2.0.12-0
- Updated to release 2.0.12.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 2.0.8-0
- Updated to release 2.0.8.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Updated to release 2.0.6.
- Updated to release 2.0.4.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.9-0
- Updated to release 0.9.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 0.8.93-0
- Updated to release 0.9rc3.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.8.92-0
- Updated to release 0.9rc2.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.8.91-0
- Updated to release 0.9rc1.

* Sat Feb 08 2003 Dag Wieers <dag@wieers.com> - 0.9pre32
- Initial package. (using DAR)
