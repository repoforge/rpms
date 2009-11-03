# $Id$
# Authority: dag

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define real_version 0.4pre1

Summary: Tool for editing and converting DivX ;-) subtitles
Name: gsubedit
Version: 0.4
Release: 0.pre1.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://gsubedit.sourceforge.net/

Source: http://dl.sf.net/gsubedit/gsubedit-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ORBit-devel, gtk+-devel, gnome-libs-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
GSubEdit, or GNOME Subtitle Editor, is a tool for editing and converting
DivX ;-) subtitles. It currently features read/write of SubRip (.srt)
and MicroDVD (.sub) subtitles. Framerate conversion and frame displacement
(Increase/decrease all frames by a given offset) is also supported.

%prep
%setup -n %{name}-%{real_version}

### FIXME: Include improved desktop-file. (Please fix upstream)
%{__cat} <<EOF >gsubedit.desktop.in
[Desktop Entry]
Name=Subtitle Editor
Comment=Edit subtitle files
Icon=gsubedit.png
Exec=gsubedit
Terminal=false
Type=Application
Encoding=UTF-8
Categories=GNOME;Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 pixmaps/gsubedit_icon.png %{buildroot}%{_datadir}/pixmaps/gsubedit.png

%if %{!?_without_freedesktop:1}0
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor gnome --delete-original \
                --add-category X-Red-Hat-Base                 \
                --dir %{buildroot}%{_datadir}/applications    \
                %{buildroot}%{_datadir}/gnome/apps/Applications/gsubedit.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%doc %{_datadir}/gnome/help/gsubedit/
%{_bindir}/*
%{!?_without_freedesktop:%{_datadir}/applications/gnome-gsubedit.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Applications/gsubedit.desktop}
%{_datadir}/pixmaps/gsubedit.png
%{_datadir}/pixmaps/gsubedit/
%exclude %{_prefix}/doc/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-0.pre1.2
- Rebuild for Fedora Core 5.

* Mon Jun 07 2004 Dag Wieers <dag@wieers.com> - 0.4-0.pre1
- Added improved desktop file.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 0.3.20020604-0
- Initial package. (using DAR)
