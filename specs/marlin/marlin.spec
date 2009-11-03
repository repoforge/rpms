# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: GNOME sample editor
Name: marlin
Version: 0.9
Release: 1%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://marlin.sourceforge.net/

Source: http://dl.sf.net/marlin/marlin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gstreamer-devel >= 0.7
BuildRequires: gtk2-devel, libgnomeui-devel, gcc-c++
BuildRequires: intltool, perl-XML-Parser, gettext


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
desktop-file-install --vendor %{desktop_vendor}    \
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
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-0.2
- Rebuild for Fedora Core 5.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
