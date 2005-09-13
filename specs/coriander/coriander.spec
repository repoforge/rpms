# $Id$
# Authority: dries
# Upstream: Damien Douxchamps <ddouxchamps$users,sourceforge,net>

%define real_version 2.0.0-pre3

Summary: Control a 1394 digital camera interactively
Name: coriander
Version: 2.0.0
Release: 0.pre3
License: GPL
Group: Applications/Multimedia
URL: http://damien.douxchamps.net/ieee1394/coriander/

Source: http://dl.sf.net/coriander/coriander-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel, gettext, libraw1394-devel, libdc1394-devel
BuildRequires: desktop-file-utils, SDL-devel, automake, autoconf, ffmpeg-devel

%description
Coriander is a GUI that let you control your 1394 digital video camera 
interactively. It features SDL display, FTP image posting, file saving, 
and Real streaming. It is for IIDC cameras, not for consumer grade DV cameras.

%prep
%setup -n coriander-%{real_version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Control a 1394 digital video camera
Exec=coriander
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/coriander
%{_datadir}/pixmaps/coriander/coriander-*.png
%{_datadir}/applications/*-coriander.desktop

%changelog
* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.pre3
- Initial package.
