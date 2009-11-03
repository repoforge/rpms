# $Id$
# Authority: dag
# Upstream: <warder$warder,ath,cx>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: GNOME frontend for the v4l (Video For Linux) functions of transcode
Name: gv4l
Version: 1.0.0
Release: 0%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://warderx.ath.cx:81/projects/

Source: http://warderx.ath.cx:81/projects/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: transcode

%description
Gv4l is a gui frontend for the v4l (Video For Linux) functions of transcode.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__cat} <<EOF >gv4l.desktop
[Desktop Entry]
Name=Gv4l
Comment=Edit video formats
Icon=gv4l/gv4l.png
Exec=gv4l
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%if %{!?_without_freedesktop:1}0
        %{__install} -Dp -m0644 gv4l.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/gv4l.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		gv4l.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/gv4l*
%{_datadir}/pixmaps/gv4l/gv4l.png
%{?_without_freedesktop:%{_datadir}/gnome/apps/Multimedia/gv4l.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-gv4l.desktop}

%changelog
* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
