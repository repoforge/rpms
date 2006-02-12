# $Id$
# Authority: dries
# Upstream: Bill Cheng <cheng$acm,org>

Summary: Vector-based drawing tool
Name: tgif
Version: 4.1.44
Release: 1
License: QPL
Group: Applications/Multimedia
URL: http://bourbon.usc.edu:8001/tgif/

Source: ftp://bourbon.usc.edu/pub/tgif/tgif-QPL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++

%description
tgif is a vector-based drawing tool, with the additional benefit of being 
sort of a web-browser. That is, you can fetch drawings from a web server 
with it, and you can make objects in your picture into hotlinks to other 
parts of the drawing, or to other drawings accessible via HTTP.

%prep
%setup -n tgif-QPL-%{version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Tgif
Comment=Vector-based drawing tool
Exec=tgif
Terminal=false
Type=Application
StartupNotify=true
Icon=/usr/lib/tgif/tgificon.xpm
Categories=Application;Graphics;
EOF

%build
xmkmf
%{__make} %{?_smp_mflags} BINDIR=%{_bindir} LIBDIR=%{_libdir}

%install
%{__rm} -rf %{buildroot}
%makeinstall BINDIR=%{buildroot}%{_bindir} LIBDIR=%{buildroot}%{_libdir}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY LICENSE.QPL README*
%{_bindir}/tgif
%{_libdir}/tgif/
%{_datadir}/applications/*-tgif.desktop

%changelog
* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 4.1.44-1
- Initial package.
