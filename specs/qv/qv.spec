# $Id: $
# Authority: dries
# Upstream: Hasanen Nawfal <hasanen$iraqilinux,com>

compiles without problems but does not work: 100% cpu usage and no window

Summary: Image viewer
Name: qv
Version: 0.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://hasanen.iraqilinux.com/qv/

Source: http://hasanen.iraqilinux.com/qv/files/qv-%{version}-beta-src.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel

%description
QV is an image viewer with the following features:
 * Thumbnails Viewing.
 * Thumbnails Caching.
 * Converting image formats.
 * Viewing multiple image formats.
 * Slide Show.
 * Image resizing.
 * Color converting.
 * Copy/cut/paste/rename/delete operations.
 * Copy to / move to operations.
 * File searching.
 * Sorting images.
 * Viewing hidden files and directores.
 * Viewing images with untraditional file extentions.
 * Mirroring image ( vertical and horizontal ).
 * Zooming images.

%prep
%setup -n qv

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Qv
Comment=Image viewer
Exec=qv
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF

%build
%{__rm} -f config.cache config.log config.status
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 09 2004 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
