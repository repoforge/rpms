# $Id$
# Authority: dries

# Screenshot: http://shalvideo.sourceforge.net/screenshot1.png
# ScreenshotURL: http://shalvideo.sourceforge.net/

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define real_version 1.1-1

Summary: TV record sheduling program
Name: shalvideo
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://shalvideo.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/shalvideo/shalvideo-%{real_version}.tar.bz2
Patch: no-default-vals-in-cpp-files.patch.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel, kdelibs-devel, gcc-c++
BuildRequires: XFree86-devel, qt-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: mplayer, at

%description
shalvideo allows you to program the TV recording feature of your computer
just like a video recorder. Just set the channel, quality, and start and end
times, and it uses mplayer and atd for the encoding and timing processes.

%prep
%setup -n %{name}-%{real_version}
%patch -p1

%{__cat} <<EOF >shalvideo.desktop
[Desktop Entry]
Name=Shalvideo
Comment=A video record programing application
Encoding=UTF-8
Type=Application
Exec=shalvideo -caption "%c" %i %m
Icon=shalvideo.png
DocPath=kvideo/index.html
Terminal=false
Categories=Application;AudioVideo;
EOF

%build
source /etc/profile.d/qt.sh
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall
strip shalvideo/shalvideo
%{__install} -D -m0755 shalvideo/shalvideo %{buildroot}%{_bindir}/shalvideo
%{__install} -D -m0644 shalvideo/lo32-app-kvideo.png %{buildroot}%{_datadir}/icons/locolor/32x32/apps/shalvideo.png
%{__install} -D -m0644 shalvideo/lo32-app-kvideo.png %{buildroot}%{_datadir}/pixmaps/shalvideo.png
%{__install} -D -m0644 shalvideo/es.ts %{buildroot}%{_datadir}/shalvideo/es.ts
%{__install} -D -m0644 shalvideo/es.qm %{buildroot}%{_datadir}/shalvideo/es.qm
%{__install} -D -m0644 po/es.gmo %{buildroot}%{_datadir}/locale/es/LC_MESSAGES/shalvideo.mo
%find_lang %{name}

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 shalvideo.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/shalvideo.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde --delete-original \
		--dir %{buildroot}%{_datadir}/applications  \
		--add-category X-Red-Hat-Base               \
		shalvideo.desktop
%endif

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ README INSTALL TODO
%{_bindir}/shalvideo
%{_datadir}/icons/locolor/32x32/apps/shalvideo.png
%{_datadir}/pixmaps/shalvideo.png
%{_datadir}/shalvideo/
%{!?_without_freedesktop:%{_datadir}/applications/kde-shalvideo.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/shalvideo.desktop}


%changelog
* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Cosmetic cleanup.

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1
