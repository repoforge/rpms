# $Id$
# Authority: dag
# Upstream: <fixounet@free.fr>
# Archs: i686 i386

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Graphical multiplex/demultiplex tool using GTK
Name: avidemux
Version: 0.9
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://fixounet.free.fr/avidemux/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://fixounet.free.fr/avidemux/avidemux-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 3.0, glib-devel, gtk+-devel >= 1.2.9
BuildRequires: nasm >= 0.98.32

%description
Avidemux is a graphical tool to edit AVI. It allows you to multiplex and
demultiplex audio to/from video.

It is able to cut video, import BMP, MJPEG and MPEG video, and encode them.
You can also process video with included filters. It requires a DivX 
compatible encoder and the Gimp Toolkit (GTK) libraries.

%prep
%setup

%{__cat} <<EOF >avidemux.desktop
[Desktop Entry]
Name=Video editing tool
Comment=Edit your videos in real-time
Icon=gnome-multimedia.png
Exec=avidemux
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
%configure \
	--disable-dependency-tracking \
	--disable-warnings
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{dfi}
	%{__install} -D -m0644 avidemux.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/avidemux.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications
        desktop-file-install --vendor gnome                \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                avidemux.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING History README TODO
%{_bindir}/*
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Aug 23 2003 Dag Wieers <dag@wieers.com>- 0.9-1
- Build against new xvidcore-0.9.2.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com>- 0.9-0
- Updated to release 0.9.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com>- 0.8.93-0
- Updated to release 0.9rc3.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com>- 0.8.92-0
- Updated to release 0.9rc2.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com>- 0.8.91-0
- Updated to release 0.9rc1.

* Sat Feb 08 2003 Dag Wieers <dag@wieers.com>- 0.9pre32
- Initial package. (using DAR)
