# $Id$

# Authority: dries

Summary: A TV record sheduling program.
Name: shalvideo
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://shalvideo.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/shalvideo/%{name}-1.1-1.tar.bz2
Patch: no-default-vals-in-cpp-files.patch.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel,qt-devel
Requires: mplayer, at

#(d) primscreenshot: http://shalvideo.sourceforge.net/screenshot1.png
#(d) screenshotsurl: http://shalvideo.sourceforge.net/

%description
shalvideo allows you to program the TV recording feature of your computer
just like a video recorder. Just set the channel, quality, and start and end
times, and it uses mplayer and atd for the encoding and timing processes.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n %{name}-1.1-1
%patch -p1

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/locolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT/usr/share/shalvideo
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES
/usr/bin/install -c -p -m 644 shalvideo/kvideo.desktop $RPM_BUILD_ROOT/usr/share/applications/shalvideo.desktop
/usr/bin/install -c -p -m 644 shalvideo/lo32-app-kvideo.png $RPM_BUILD_ROOT/usr/share/icons/locolor/32x32/apps/kvideo.png
/usr/bin/install -c -p -m 644 shalvideo/es.ts $RPM_BUILD_ROOT/usr/share/shalvideo/es.ts
/usr/bin/install -c -p -m 644 shalvideo/es.qm $RPM_BUILD_ROOT/usr/share/shalvideo/es.qm
/usr/bin/install -c -p -m 644 po/es.gmo $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES/shalvideo.mo
strip shalvideo/shalvideo
cp shalvideo/shalvideo $RPM_BUILD_ROOT/usr/bin
cat > $RPM_BUILD_ROOT/usr/share/applications/shalvideo.desktop <<EOF
# KDE Config File
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=shalvideo -caption "%c" %i %m
Icon=kvideo.png
DocPath=kvideo/index.html
Comment=A video record programing application
Comment[es]=Un programa para grabar videos
Terminal=0
Name=Shalvideo
Categories=Application;AudioVideo;
EOF


%files
%defattr(-,root,root, 0755)
%doc AUTHORS COPYING FAQ README INSTALL TODO
/usr/bin/shalvideo
/usr/share/applications/shalvideo.desktop
/usr/share/icons/locolor/32x32/apps/kvideo.png
/usr/share/locale/es/LC_MESSAGES/shalvideo.mo
/usr/share/shalvideo/es.qm
/usr/share/shalvideo/es.ts

%changelog
* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1
