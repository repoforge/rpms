# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_version 2.35

Summary: 3D modeling, animation, rendering and post-production
Name: blender
Version: 2.35
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.blender.org/

Source: http://download.blender.org/source/blender-%{real_version}.tar.bz2
Source1: blender.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, glut, python-devel
BuildRequires: XFree86-devel, openssl-devel, SDL-devel, libvorbis-devel
BuildRequires: libogg-devel esound-devel, openal-devel, libtool, gettext
BuildRequires: scons, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

%description
Blender is the essential software solution you need for 3D, from modeling,
animation, rendering and post-production to interactive creation and
playback.

Professionals and novices can easily and inexpensively publish stand-alone,
secure, multi-platform content to the web, CD-ROMs, and other media, whether
they are users of Windows, Linux, Irix, Sun Solaris, FreeBSD or OSX.

#%package devel
#Summary: Header files, libraries and development documentation for %{name}
#Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}

#%description devel
#This package contains the header files, static libraries and development
#documentation for %{name}. If you like to develop programs using %{name},
#you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >blender.desktop
[Desktop Entry]
Name=Blender 3D Animations
Comment=Model, animate, render and post-produce 3D animations
Exec=blender -w
Icon=blender.png
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF

%build
# blender now works with a new build system, named Scons
sed -i "s/use_openal =.*/use_openal = 'true'/g;" SConstruct
scons

# {__aclocal}
# {__autoconf}
# {__autoheader}
# {__automake} \
#	--gnu \
#	--add-missing \
#	--foreign
#configure
#	--disable-dependency-tracking \
#	--disable-shared \
#	--disable-openal \
#	--disable-rpath
##	--enable-quicktime \
##	--enable-fmod
#{__make} {?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 blender %{buildroot}%{_bindir}/blender
%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/blender.png

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 blender.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/blender.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		blender.desktop
%endif

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README doc/*
%{_bindir}/blender
#%{_libdir}/*.so.*
%{_datadir}/pixmaps/blender.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/blender.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-blender.desktop}

#%files devel
#%defattr(-, root, root, 0755)
#%doc INSTALL doc/building_blender.html
#%{_libdir}/*.a
#%exclude %{_libdir}/*.la
#%{_libdir}/*.so

%changelog
* Tue Dec 14 2004 Dries Verachtert <dries@ulyssis.org> - 2.35-1
- Updated to release 2.35.

* Fri Sep 03 2004 Dries Verachtert <dries@ulyssis.org> - 2.34-1
- Updated to release 2.34.

* Tue May 25 2004 Dries Verachtert <dries@ulyssis.org> - 2.33-1.a
- use Scons for building

* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 2.33-0.a
- Updated to release 2.30.

* Wed Nov 05 2003 Dag Wieers <dag@wieers.com> - 2.30-0
- Updated to release 2.30.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 2.28-0
- Updated to release 2.28.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.26-0
- Initial package. (using DAR)
