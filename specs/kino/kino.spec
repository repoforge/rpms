# $Id$
# Authority: dag
# Upstream: Dan Dennedy <ddennedy@users.sf.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Simple non-linear video editor
Name: kino
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://kino.schirmacher.de/filemanager/download/31/kino-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdv-devel >= 0.102, libavc1394-devel, libraw1394-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel
BuildRequires: gtk+ >= 1.2, XFree86-devel, imlib-devel
BuildRequires: libxml2-devel, libquicktime-devel
BuildRequires: libsamplerate

Obsoletes: kino-devel <= %{version}

%description
The new generation of digital camcorders use the Digital Video (DV) data
format. Kino allows you to record, create, edit, and play movies recorded
with DV camcorders. Unlike other editors, this program uses many keyboard
commands for fast navigating and editing inside the movie.

%prep
%setup

### FIXME: Buildtools don't use proper autotool directories (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/share/pixmaps/kino|\$(datadir)/pixmaps/kino|;
		s|^(gnomedatadir) = /usr/share$|$1 = \$(datadir)|;
		s|^(hotplugscriptdir) = .*|$1 = \$(sysconfdir)/hotplug/usb|;
		s|^(hotplugusermapdir) = .*|$1 = \$(libdir)/hotplug/kino|;
	' Makefile.in help/Makefile.in linux-hotplug/Makefile.in

%{__cat} <<EOF >kino.desktop
[Desktop Entry]
Name=Kino Video Editor
Comment=Edit non-linear videos in real-time
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{dfi}
	%{__install} -D -m0644 kino.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/kino.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		kino.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr (-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog NEWS README*
%doc %{_mandir}/man?/*
#%doc %{_datadir}/gnome/help/kino/
%config %{_sysconfdir}/hotplug/usb/*
%{_bindir}/*
%dir %{_libdir}/hotplug/
%{_libdir}/hotplug/kino/
%{_datadir}/kino/
%{_includedir}/kino/
%if %{dfi}
	%{_datadir}/gnome/apps/Multimedia/*.desktop
%else
	%{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Obsolete older kino-devel package. (Jeff Moe)

* Fri Dec 19 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to 0.7.0.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.6.5-0
- Updated to 0.6.5.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.4-0
- Updated to 0.6.4.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.3-0
- Initial package. (using DAR)
