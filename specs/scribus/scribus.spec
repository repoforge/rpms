# $Id$

# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Graphical desktop publishing (DTP) application
Name: scribus
Version: 1.2
Release: 0
License: GPL
Group: Applications/Productivity
URL: http://web2.altmuehlnet.de/fschmid/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://web2.altmuehlnet.de/fschmid/scribus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.0, XFree86-devel, gcc-c++
BuildRequires: zlib-devel, libjpeg-devel, libpng-devel, libtiff-devel
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Scribus is a GUI desktop publishing (DTP) application for GNU/Linux.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Scribus Desktop Publishing
Comment=%{summary}
Exec=scribus
Icon=scribus.png
Type=Application
Terminal=false
Categories=Application;Office;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
%configure \
	--disable-dependency-tracking \
	--with-xinerama
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 scribus/icons/scribusicon.png %{buildroot}%{_datadir}/pixmaps/scribus.png

%if %{?_without_freedesktop:1}0
        %{__install} -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Applications/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor kde                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

### Clean up buildroot
# %{__rm} -f %{buildroot}%{_libdir}/scribus/{libs,plugins}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/scribus/
%{_includedir}/scribus/
%{_datadir}/scribus
%{_datadir}/pixmaps/*
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/*.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/*.desktop}

%changelog
* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
