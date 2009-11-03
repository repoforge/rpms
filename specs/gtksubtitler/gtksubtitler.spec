# $Id$
# Authority: dag

Summary: Tool for editing and converting subtitles for DivX films
Name: GTKsubtitler
Version: 0.2.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.gtksubtitler.prv.pl/

Source: http://matrix.kamp.pl/~pawelb/gtksubtitler/download/GTKsubtitler-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, gnome-libs-devel, desktop-file-utils

%description
Tool for editing and converting subtitles for DivX films. It supports
mergeing, moveing, changeing format of sub-file and converting (to
iso-8859-1/2) divix subtitles.

%prep
%setup -n %{name}-v%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=GTKsubtitler
Comment=Edit subtitles
Icon=/usr/share/pixmaps/GTKsubtitler/GTKsubtitler.xpm
Exec=GTKsubtitler
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README SUB_FORMATS
%{_bindir}/GTKsubtitler
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/GTKsubtitler/GTKsubtitler.xpm
%{_datadir}/GTKsubtitler

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.4-0
- Update to release 0.2.4-0.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Initial package. (using DAR)
