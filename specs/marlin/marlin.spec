# $Id$

# Authority: dag

Summary: GNOME sample editor
Name: marlin
Version: 0.1
Release: 0
Group: Applications/Multimedia
License: GPL
URL: http://marlin.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/marlin/marlin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gstreamer-devel >= 0.7

%description
Marlin is a sample editor for GNOME 2. It uses GStreamer for file
operations and for recording and playback, meaning it can handle
a great number of formats and work with most sound systems.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

cat <<EOF >gnome-%{name}.desktop
[Desktop Entry]
Name=Gv4l
Comment=%{summary}
Icon=gv4l/gv4l.png
Exec=%{_bindir}/%{name}
Terminal=false
Type=Application
EOF

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category AudioVideo                  \
	--dir %{buildroot}%{_datadir}/applications \
	gnome-%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
