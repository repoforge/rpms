# $Id: $

# Authority: dries
# Upstream: 

Summary: Real-time strategy game
Name: boson
Version: 0.10
Release: 1
License: GPL
Group: Amusements/Games
URL: http://boson.eu.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/boson/boson-all-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, gcc-c++, XFree86-devel, zlib-devel, qt-devel, kdelibs-devel, gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, lib3ds
%{?fc2:BuildRequires: xorg-x11-Mesa-libGLU, libselinux-devel}

%description
Boson is an OpenGL real-time strategy game, with the feeling of
Command and Conquer(tm) or StarCraft(tm). It is designed to run on Unix (Linux)
computers, and is built on top of the KDE, Qt and kdegames libraries.
A minimum of two players is required, since there is no artificial
intelligence yet.

%prep
%setup -n boson-all-%{version}

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall kde_widgetdir=%{buildroot}/usr/lib/kde3/plugins/designer

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_datadir}/doc/HTML/en/boson-apidocs
%doc %{_datadir}/doc/HTML/en/boson
%{_datadir}/icons/*/*/apps/boson.png
%{_datadir}/apps/boson
%{_datadir}/applnk/Games/TacticStrategy/boson/*.desktop
%{_datadir}/config/bodebug*
%{_bindir}/bo*
%{_libdir}/kde3/plugins/designer/bosonwidgets.so
%{_libdir}/kde3/plugins/designer/bosonwidgets.la
%{_libdir}/kde3/plugins/boson
%{_libdir}/kde3/plugins/boson/libbomeshrendererplugin.so.0.0.0
%{_libdir}/kde3/plugins/boson/libbomeshrendererplugin.so.0
%{_libdir}/kde3/plugins/boson/libbomeshrendererplugin.so
%{_libdir}/kde3/plugins/boson/libbomeshrendererplugin.la
%{_libdir}/kde3/plugins/boson/libbogroundrendererplugin.so.0.0.0
%{_libdir}/kde3/plugins/boson/libbogroundrendererplugin.so.0
%{_libdir}/kde3/plugins/boson/libbogroundrendererplugin.so
%{_libdir}/kde3/plugins/boson/libbogroundrendererplugin.la

%changelog
* Mon May 3 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1 
- Initial package.

