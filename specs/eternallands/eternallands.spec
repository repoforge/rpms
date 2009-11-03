# $Id$
# Authority: dries
# Screenshot: http://www.eternal-lands.com/gfx/screenshots/01.jpg
# ScreenshotURL: http://www.eternal-lands.com/index.php?content=screenshots

%define real_version 100

Summary: Free MMORPG in beta stage
Name: eternallands
Version: 1.0.1
Release: 2%{?dist}
License: Other
Group: Amusements/Games
URL: http://www.eternal-lands.com/

# cvs command: cvs -d :pserver:anonymous@cvs.elc.berlios.de:/cvsroot/elc co -r elc_0_9_9 elc
Source: eternallands-src-%{version}.tar.gz
Source1: http://el.tfm.ro/el_%{real_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, openal-devel, SDL_net-devel, libxml2-devel
BuildRequires: libogg-devel, libvorbis-devel
%{?el4:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc3:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc2:BuildRequires: xorg-x11-Mesa-libGL, xorg-x11-Mesa-libGLU}
%{?fc1:BuildRequires: XFree86-Mesa-libGL, XFree86-Mesa-libGLU}


%description
The eternallands package contains the Eternal Lands free MMMORPG (massive
multiplayer online roleplaying game) currently under development.

%prep
%setup -n elc

%{__sed} -i "s/^CFLAGS=/CFLAGS=-I\/usr\/include\/SDL /g;" Makefile.linux

%{__cat} <<EOF > eternallands
#!/bin/sh
cd %{_datadir}/games/eternallands
%{__mkdir_p} ~/.elc
if [[ ! -e ~/.elc/el.ini ]] ; then \
	%{__cp} -p el.ini ~/.elc/
fi
echo logs and config file are at ~/.elc/
./el.x86.linux.bin
EOF

%build
%{__make} %{?_smp_mflags} -f Makefile.linux

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/games/eternallands
%{__unzip} -d %{buildroot}%{_datadir}/games/eternallands %{SOURCE1}
%{__install} -Dp -m0755 el.x86.linux.bin %{buildroot}%{_datadir}/games/eternallands/el.x86.linux.bin
%{__install} -Dp -m0755 eternallands %{buildroot}%{_bindir}/eternallands
%{__install} -Dp -m0644 el.ini %{buildroot}%{_datadir}/games/eternallands/el.ini

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc eternal_lands_license.txt readme.txt
%{_bindir}/eternallands
%{_datadir}/games/eternallands/

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Update to release 1.0.1.

* Mon Aug 23 2004 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Update to version 1.0.0.

* Sat Jun 26 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.9
- Update to version 0.9.9.

* Tue Jan 6 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.3
- first packaging for Fedora Core 1

