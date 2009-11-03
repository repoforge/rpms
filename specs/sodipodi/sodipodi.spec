# $Id$
# Authority: dag
# Upstream: Lauris Kaplinski <lauris$kaplinski,com>

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Vector drawing application
Name: sodipodi
Version: 0.34
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://sodipodi.sourceforge.net/

Source: http://dl.sf.net/sodipodi/sodipodi-%{version}.tar.gz
Patch0: sodipodi-0.34-amd64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml-devel, libpng-devel, libglade-devel, gcc-c++
BuildRequires: gettext
%{?el5:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, freetype-devel}
%{?fc8:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, freetype-devel}
%{?fc7:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, freetype-devel}
%{?fc6:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, freetype-devel}
%{?fc5:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel, freetype-devel}
%{?fc4:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel}
%{?fc3:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel}
%{?fc2:BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel}
%{?rh9:BuildRequires: libgnomeprint22-devel, libgnomeprintui-devel}
%{?rh8:BuildRequires: libgnomeprint-devel >= 1.116, libgnomeprintui-devel >= 1.116}

%description
Sodipodi is a general purpose vector drawing application which uses a
subset of W3C SVG as its file format. It uses an advanced imaging engine,
with anti-aliased display, alpha transparency, and vector fonts.

%prep
%setup
%patch0 -p1 -b .amd64

%build
%configure \
	--with-gnome-print \
	--with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README samples/ TODO
%doc %{_mandir}/man1/sodipodi.1*
%{_bindir}/sodipodi
%{_libdir}/sodipodi/
%{_datadir}/applications/sodipodi.desktop
%{_datadir}/pixmaps/sodipodi.png
%{_datadir}/sodipodi/

%changelog
* Tue Dec 21 2004 Richard Koerber <shred@despammed.com> - 0.34-1
- Added a patch to fix a segfault on x86_64 startup.

* Thu Feb 12 2004 Dag Wieers <dag@wieers.com> - 0.34-0
- Updated to release 0.34.
- Added missing BuildRequires for RH90. (Juha Tuomala)

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 0.33-0
- Updated to release 0.33.

* Fri Jun 20 2003 Dag Wieers <dag@wieers.com> - 0.32-0
- Updated to release 0.32.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.31.1-0
- Updated to release 0.31.1.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.30.1-0
- Updated to release 0.30.1.

* Tue Jan 28 2003 Dag Wieers <dag@wieers.com> - 0.29-0
- Updated to release 0.29.

* Tue Jan 21 2003 Dag Wieers <dag@wieers.com> - 0.28.95-0
- Updated to release 0.28.95.

* Mon Nov 25 2002 Dag Wieers <dag@wieers.com> - 0.28-0
- Updated to release 0.28.

* Thu Oct 10 2002 Dag Wieers <dag@wieers.com> - 0.27-0
- Updated to release 0.27.

* Mon Sep 23 2002 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Thu Sep 12 2002 Dag Wieers <dag@wieers.com> - 0.25-0
- Updated to release 0.25.
- Changed SPEC to benefit from macros
