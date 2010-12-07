# $Id$
# Authority: dag
# Upstream: <fixounet$free,fr>

%define desktop_vendor rpmforge

Summary: Graphical video editing tool
Name: avidemux
Version: 2.4.4
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://fixounet.free.fr/avidemux/

Source: http://dl.sf.net/avidemux/avidemux_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: a52dec-devel
BuildRequires: alsa-lib-devel
BuildRequires: arts-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: faad2-devel
BuildRequires: gcc >= 3.0
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: glib-devel
BuildRequires: gtk2-devel >= 2.6
BuildRequires: libmad-devel
BuildRequires: libvorbis-devel, SDL-devel, lame-devel
BuildRequires: libxml2-devel
BuildRequires: nasm >= 0.98.32
BuildRequires: xvidcore-devel
BuildRequires: desktop-file-utils

Obsoletes: avidemux2 <= %{version}-%{release}
Provides: avidemux2 = %{version}-%{release}

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX
compatible encoder and the Gimp Toolkit (GTK) libraries.

%prep
%setup -n %{name}_%{version}

%{__cat} <<EOF >avidemux.desktop
[Desktop Entry]
Name=Avidemux Video Editor
Comment=Edit your videos in real-time
Icon=gnome-multimedia.png
Exec=avidemux2_gtk
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
MimeType=video/mp4v-es;video/mpeg;video/quicktime;video/x-msvideo;video/x-avi;audio/ac3;audio/x-mpeg;audio/x-mp3;audio/x-mp2;audio/x-wav;
EOF

%build
source /etc/profile.d/qt.sh
%{__make} -f Makefile.dist
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|\$x_libraries|g' configure
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|%{_prefix}/X11R6/%{_lib}|g' Makefile.in */Makefile.in */*/Makefile.in

%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}" \
    --disable-warnings
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
### FIXME: Base kde_locale on $(datadir). (Please fix upstream)
%makeinstall \
    kde_locale="%{buildroot}%{_datadir}/locale"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    avidemux.desktop

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING History README TODO
%{_bindir}/avidemux2_cli
%{_bindir}/avidemux2_gtk
%{_datadir}/applications/%{desktop_vendor}-avidemux.desktop

%changelog
* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 2.4.4-3
- Rebuild against newer x264.

* Fri Nov 06 2009 Dag Wieers <dag@wieers.com> - 2.4.4-2
- Rebuild against faad2 2.7.

* Sat Feb 21 2009 Dag Wieers <dag@wieers.com> - 2.4.4-1
- Updated to release 2.4.4.

* Sat Jul 26 2008 Dag Wieers <dag@wieers.com> - 2.4.3-1
- Updated to release 2.4.3.

* Mon Jan 07 2008 Dag Wieers <dag@wieers.com> - 2.4-1
- Updated to release 2.4.

* Tue Dec 12 2006 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Wed Mar 08 2006 Dag Wieers <dag@wieers.com> - 2.1.2-1
- Updated to release 2.1.2.

* Thu Jan 05 2006 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Updated to release 2.1.0.

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 2.0.40-1
- Updated to release 2.0.40.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 2.0.38-1
- Updated to release 2.0.38.

* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 2.0.36-2
- Rebuild against xvidcore 1.0.3.

* Fri Jan 14 2005 Dag Wieers <dag@wieers.com> - 2.0.36-1
- Updated to release 2.0.36.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 2.0.34-0.test2
- Updated to release 2.0.34-test2.

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 2.0.32-1
- Updated to release 2.0.32.

* Fri Aug 13 2004 Dag Wieers <dag@wieers.com> - 2.0.28-1
- Updated to release 2.0.28.

* Fri Jul 23 2004 Dag Wieers <dag@wieers.com> - 2.0.26-1
- Updated to release 2.0.26.

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
