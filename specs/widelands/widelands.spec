# $Id: $

# Authority: dries

Summary: Game like Settlers II
Name: widelands
Version: b6
Release: 2
License: GPL
Group: Amusements/Games
URL: http://widelands.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://dl.sf.net/widelands/widelands-%{version}-source.tar.bz2
Source1: http://dl.sf.net/widelands/widelands-%{version}-binary.tar.bz2
BuildRequires: SDL-devel, make, gcc-c++, SDL_image-devel
Requires: SDL

# Screenshot: http://widelands.sourceforge.net/images/screens/build-6/00.jpg
# ScreenshotURL: http://widelands.sourceforge.net/screenshots.html

%description
In Widelands, you are the regent of a small tribe. You start out with
nothing but your headquarters, a kind of castle in which all your resources
are stored. Every member of your tribe will do his or her part to produce
more resources - wood, food, iron, gold and more - to further this growth.
But you are not alone in the world, and you will meet other tribes sooner or
later. Some of them may be friendly and trade with you. However, if you want
to rule the world, you will have to train soldiers and fight.
 
%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -b 1 -n widelands

%build
rm -f widelands
make
mv widelands widelands.orig
(echo "#!/bin/bash";echo "cd /usr/share/widelands";echo "./widelands") > widelands
chmod +x widelands

cat > widelands.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Encoding=UTF-8
Name=Widelands
Exec=/usr/bin/widelands
Categories=Application;Game;ArcadeGame
EOF

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/widelands
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/

install -s -m 755 widelands.orig $RPM_BUILD_ROOT/usr/share/widelands/widelands
install -m 755 widelands $RPM_BUILD_ROOT/usr/bin/widelands
cp -r fonts maps pics tribes worlds $RPM_BUILD_ROOT/usr/share/widelands/
cp widelands.desktop $RPM_BUILD_ROOT/usr/share/applications/
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README COPYING AUTHORS
%{_bindir}/widelands
%{_datadir}/widelands
%{_datadir}/applications/widelands.desktop

%changelog
* Fri Jan 02 2004 Dries Verachtert <dries@ulyssis.org> b6-2
- added a desktop icon

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> b6-1
- first packaging for Fedora Core 1
