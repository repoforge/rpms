# $Id$
# Authority: dries
# Upstream: Abderrahman Taha <taha_ab$yahoo,fr>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Visualize and manipulate multidimensional surfaces
Name: k3dsurf
Version: 0.6.2
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://k3dsurf.sourceforge.net/

Source: http://dl.sf.net/k3dsurf/k3dsurf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, desktop-file-utils
%{!?_without_modxorg:BuildRequires: libXmu-devel, libXext-devel, mesa-libGL-devel, mesa-libGLU-devel}

%description
K3DSurf is a program for visualizing and manipulating multidimensional
surfaces by using Mathematical equations. It's also a "modeler" for
POV-Ray in the area of parametric surfaces. It features 3D, 4D, 5D,
and 6D HyperObjects visualization, full support for all functions
(like the C language), support for mouse events in the drawing area,
animation and morph effects, Povscript and mesh file generation, and
support for VRML2 and OBJ files. More than 100 examples are provided.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=k3dsurf
Comment=manipulate multidimensional surfaces
Exec=k3dsurf
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Education;Science;Mathematics;
EOF

%build
qmake
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 bin/k3dsurf %{buildroot}%{_bindir}/k3dsurf

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc copying readme
%{_bindir}/k3dsurf
%{_datadir}/applications/*-k3dsurf.desktop

%changelog
* Thu Jun 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Updated to release 0.6.2.

* Sat Dec 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Mon Nov 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Sun Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.5-1
- Updated to release 0.5.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1.2
- Rebuild for Fedora Core 5.

* Mon Dec 12 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.4-1
- Updated to release 0.5.4.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Fri Aug 26 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Initial package.
