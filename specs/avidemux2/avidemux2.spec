# $Id$
# Authority: dag
# Upstream: <fixounet$free,fr>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define real_name avidemux

Summary: Graphical video editing tool
Name: avidemux2
Version: 2.0.24
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://fixounet.free.fr/avidemux/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fixounet.free.fr/avidemux/avidemux-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 3.0, glib-devel, gtk2-devel >= 2.0.0
BuildRequires: nasm >= 0.98.32
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX 
compatible encoder and the Gimp Toolkit (GTK) libraries.

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >avidemux2.desktop
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
%{__make} -f Makefile.dist
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|\$x_libraries|g' configure
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|%{_prefix}/X11R6/%{_lib}|g' Makefile.in */Makefile.in */*/Makefile.in

%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}" \
	--disable-warnings
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Base kde_locale on $(datadir). (Please fix upstream)
%makeinstall \
	kde_locale="%{buildroot}%{_datadir}/locale"
#%find_lang %{real_name}

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0755 avidemux2.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/avidemux2.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		avidemux2.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

#%files -f %{real_name}.lang
%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING History README TODO
%{_bindir}/*
%{!?_without_freedesktop:%{_datadir}/applications/gnome-avidemux2.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/avidemux2.desktop}

%changelog
* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 2.0.24-1
- Updated to release 2.0.24.

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
