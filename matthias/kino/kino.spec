# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A simple non-linear video editor.
Name: kino
Version: 0.7.0
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://kino.schirmacher.de/filemanager/download/17/kino-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libdv-devel, libavc1394-devel, libraw1394-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel
BuildRequires: gtk+ >= 1.2, XFree86-devel, imlib-devel
BuildRequires: libxml2-devel, libquicktime-devel

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Kino Video Editor
Comment=%{summary}
Icon=gnome-multimedia.png
Exec=kino
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure \
	--disable-dependency-tracking \
	--with-quicktime \
	--with-avcodec
### FIXME: Buildtools don't use proper autotool directories (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/share/pixmaps/kino|\$(datadir)/pixmaps/kino|;
		s|^gnomedatadir = /usr/share$|gnomedatadir = \$(datadir)|;
	' Makefile help/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS BUGS ChangeLog NEWS README*
%defattr (-, root, root, 0755)
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/kino/
%{_bindir}/*
%{_datadir}/kino/
%if %{dfi}
	%{_datadir}/gnome/apps/Multimedia/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif
%{_includedir}/kino/

%changelog
* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to 0.7.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to 0.6.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to 0.6.4.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Initial package. (using DAR)
