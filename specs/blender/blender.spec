# $Id$
# Authority: dries

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

%define real_version 2.33a

Summary: 3D modeling, animation, rendering and post-production
Name: blender
Version: 2.33
Release: 0.a
License: GPL
Group: Applications/Multimedia
URL: http://www.blender.org/

Source: http://download.blender.org/source/blender-%{real_version}.tar.bz2
Source1: blender.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, glut, python-devel
BuildRequires: XFree86-devel, openssl-devel, SDL-devel, libvorbis-devel
BuildRequires: libogg-devel esound-devel, openal-devel, libtool, gettext

%description
Blender is the essential software solution you need for 3D, from modeling,
animation, rendering and post-production to interactive creation and
playback.

Professionals and novices can easily and inexpensively publish stand-alone,
secure, multi-platform content to the web, CD-ROMs, and other media, whether
they are users of Windows, Linux, Irix, Sun Solaris, FreeBSD or OSX.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

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
EOF

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake} \
	--gnu \
	--add-missing \
	--foreign
%configure
	--disable-dependency-tracking \
	--disable-shared \
	--disable-openal \
	--disable-rpath
#	--enable-quicktime \
#	--enable-fmod
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/blender.png


%if %{dfi}
        %{__install} -D -m0644 blender.desktop %{buildroot}%{_datadir}/gnome/apps/Graphics/blender.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README release*.txt doc/*
%{_bindir}/*
#%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%if %{dfi}
        %{_datadir}/gnome/apps/Graphics/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

#%files devel
#%defattr(-, root, root, 0755)
#%doc INSTALL doc/building_blender.html
#%{_libdir}/*.a
#%exclude %{_libdir}/*.la
#%{_libdir}/*.so

%changelog
* Sat May 15 2004 Dag Wieers <dag@wieers.com> - 2.33-0.a
- Updated to release 2.30.

* Wed Nov 05 2003 Dag Wieers <dag@wieers.com> - 2.30-0
- Updated to release 2.30.

* Mon Jul 28 2003 Dag Wieers <dag@wieers.com> - 2.28-0
- Updated to release 2.28.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 2.26-0
- Initial package. (using DAR)
