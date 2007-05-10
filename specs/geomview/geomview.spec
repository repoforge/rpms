# $Id$
# Authority: dries

%{?dist: %{expand: %%define %dist 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{!?dist:%define _with_lesstif 1}
%{?fc6:%define _with_lesstif 1}
%{?fc3:%define _with_lesstif 1}
%{?el2:%define _with_lesstif 1}

Summary: View and manipulate 3D geometric objects
Name: geomview
Version: 1.9.1
Release: 1
License: Distributable
Group: Applications/Multimedia
URL: http://www.geomview.org/

Source: http://dl.sf.net/geomview/geomview-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{!?_without_modxorg:BuildRequires: mesa-libGL-devel, mesa-libGLU-devel, libXmu-devel, libXext-devel, libSM-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_lesstif:BuildRequires: lesstif-devel}

%description
Geomview is an interactive program written by the staff of the Geometry 
Center for viewing and manipulating 3D (and higher dimensional) geometric 
objects. It can be used as a standalone viewer for static object or as a 
display engine for other programs which produce dynamically changing 
geometry.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Geomview
Comment=View and manipulate 3D objects
#Icon=name.png
Exec=geomview
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Graphics;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} %{buildroot}%{_docdir}/geomview rpmdocs

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README rpmdocs/*
%doc %{_mandir}/man1/*1*
%doc %{_mandir}/man3/*3*
%doc %{_mandir}/man5/*5*
%{_bindir}/anytooff
%{_bindir}/anytoucd
%{_bindir}/bdy
%{_bindir}/bez2mesh
%{_bindir}/clip
%{_bindir}/geomview
%{_bindir}/hvectext
%{_bindir}/math2oogl
%{_bindir}/offconsol
%{_bindir}/oogl2rib
%{_bindir}/oogl2vrml
%{_bindir}/oogl2vrml2
%{_bindir}/polymerge
%{_bindir}/remotegv
%{_bindir}/togeomview
%{_bindir}/ucdtooff
%{_bindir}/vrml2oogl
%{_libdir}/libgeomview-*.so
%{_datadir}/geomview/
%{_libexecdir}/geomview/
%{_datadir}/applications/*geomview.desktop
%{_infodir}/geomview*
%{_infodir}/figs/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/geomview/
%{_libdir}/libgeomview.so
%exclude %{_libdir}/libgeomview.a
%exclude %{_libdir}/libgeomview.la

%changelog
* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 1.9.1-1
- Updated to release 1.9.1.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.1-1
- Initial package.
