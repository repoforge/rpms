# $Id$

# Authority: dries

%define prever pre1
%define extra_release 1

Summary: A TV record sheduling program
Name: shalvideo
Version: 1.2
Release: 0.1%{?prever:.%{prever}}%{!?prever:.%{extra_release}}
License: GPL
Group: Applications/Multimedia
URL: http://shalvideo.sourceforge.net/
Source: http://dl.sf.net/shalvideo/%{name}-%{version}%{?prever:-%{prever}}%{!?prever:-%{extra_release}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: mplayer, at
BuildRequires: XFree86-devel, qt-devel, kdelibs-devel, arts-devel, gcc-c++
BuildRequires: libjpeg-devel, libpng-devel, zlib-devel
BuildRequires: gettext, libart_lgpl-devel

#(d) primscreenshot: http://shalvideo.sourceforge.net/screenshot1.png
#(d) screenshotsurl: http://shalvideo.sourceforge.net/

%description
shalvideo allows you to program the TV recording feature of your computer
just like a video recorder. Just set the channel, quality, and start and end
times, and it uses mplayer and atd for the encoding and timing processes.

%prep
%setup -n %{name}-%{version}-%{extra_release}

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%makeinstall
%find_lang %{name}
#export DESTDIR=$RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/usr/share/applications
#mkdir -p $RPM_BUILD_ROOT/usr/bin
#mkdir -p $RPM_BUILD_ROOT/usr/share/icons/locolor/32x32/apps
#mkdir -p $RPM_BUILD_ROOT/usr/share/shalvideo
#mkdir -p $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES
#/usr/bin/install -c -p -m 644 shalvideo/kvideo.desktop $RPM_BUILD_ROOT/usr/share/applications/shalvideo.desktop
#/usr/bin/install -c -p -m 644 shalvideo/lo32-app-kvideo.png $RPM_BUILD_ROOT/usr/share/icons/locolor/32x32/apps/kvideo.png
#/usr/bin/install -c -p -m 644 shalvideo/es.ts $RPM_BUILD_ROOT/usr/share/shalvideo/es.ts
#/usr/bin/install -c -p -m 644 shalvideo/es.qm $RPM_BUILD_ROOT/usr/share/shalvideo/es.qm
#/usr/bin/install -c -p -m 644 po/es.gmo $RPM_BUILD_ROOT/usr/share/locale/es/LC_MESSAGES/shalvideo.mo
#strip shalvideo/shalvideo
#cp shalvideo/shalvideo $RPM_BUILD_ROOT/usr/bin
#cat > $RPM_BUILD_ROOT/usr/share/applications/shalvideo.desktop <<EOF
## KDE Config File
#[Desktop Entry]
#Encoding=UTF-8
#Type=Application
#Exec=shalvideo -caption "%c" %i %m
#Icon=kvideo.png
#DocPath=kvideo/index.html
#Comment=A video record programing application
#Comment[es]=Un programa para grabar videos
#Terminal=0
#Name=Shalvideo
#Categories=Application;AudioVideo;
#EOF

%clean
%{__rm} -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FAQ README INSTALL TODO
%{_bindir}/shalvideo
%{_datadir}/applications/shalvideo.desktop
%{_datadir}/icons/locolor/32x32/apps/kvideo.png
%{_datadir}/shalvideo

%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net/> 1.2-0.1.pre1
- Update to 1.2-pre1.
- Removed obsolete patch.
- Spec file cleanup.

* Sun Feb  1 2004 Dries Verachtert <dries@ulyssis.org> 1.1.1-1
- first packaging for Fedora Core 1

