# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Real-time strategy game
Name: boson
Version: 0.11
Release: 2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://boson.eu.org/

Source: http://dl.sf.net/boson/boson-all-%{version}.tar.bz2
#Patch: python2.4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, gcc-c++, zlib-devel
BuildRequires: kdelibs-devel, gettext, libjpeg-devel
BuildRequires: libpng-devel, lib3ds, python
BuildRequires: automake, autoconf, m4, automake15

%description
Boson is an OpenGL real-time strategy game, with the feeling of
Command and Conquer(tm) or StarCraft(tm). It is designed to run on Unix (Linux)
computers, and is built on top of the KDE, Qt and kdegames libraries.
A minimum of two players is required, since there is no artificial
intelligence yet.

%prep
%setup -n boson-all-%{version}
#%patch -p1

%build
source "/etc/profile.d/qt.sh"
make -f Makefile.cvs
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%makeinstall kde_widgetdir=%{buildroot}%{_libdir}/kde3/plugins/designer

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
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.11-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Sep 09 2005 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Mon May 3 2004 Dries Verachtert <dries@ulyssis.org> 0.10-1
- Initial package.

