# $Id$

# Authority: dag
# Upstream: Lauris Kaplinski <lauris@kaplinski.com>
# Archs: i686 i386

Summary: Vector drawing application.
Name: sodipodi
Version: 0.34
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://sodipodi.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/sodipodi/sodipodi-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libxml-devel, libpng-devel, libglade-devel
%{?rh90:BuildRequires: libgnomeprint22-devel, libgnomeprintui-devel}
%{?rh80:BuildRequires: libgnomeprint-devel >= 1.116, libgnomeprintui-devel >= 1.116}

%description
Sodipodi is a general purpose vector drawing application which uses a
subset of W3C SVG as its file format. It uses an advanced imaging engine,
with anti-aliased display, alpha transparency, and vector fonts.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--with-gnome-print \
	--with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

#desktop-file-install --vendor gnome --delete-original \
#	--add-category X-Red-Hat-Base                 \
#	--dir %{buildroot}%{_datadir}/applications    \
#	%{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO samples/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/sodipodi/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/sodipodi/

%changelog
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
