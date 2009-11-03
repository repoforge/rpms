# $Id$
# Authority: dries
# Upstream: Bill Cheng <cheng$acm,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Vector-based drawing tool
Name: tgif
Version: 4.1.45
Release: 1%{?dist}
License: QPL
Group: Applications/Multimedia
URL: http://bourbon.usc.edu:8001/tgif/

Source: ftp://bourbon.usc.edu/pub/tgif/tgif-QPL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
%{!?_without_modxorg:BuildRequires: imake, libXmu-devel}

%description
tgif is a vector-based drawing tool, with the additional benefit of being
sort of a web-browser. That is, you can fetch drawings from a web server
with it, and you can make objects in your picture into hotlinks to other
parts of the drawing, or to other drawings accessible via HTTP.

%prep
%setup -n tgif-QPL-%{version}

%{__cat} <<EOF >tgif.desktop
[Desktop Entry]
Name=Tgif
Comment=Vector-based drawing tool
Exec=tgif
Terminal=false
Type=Application
StartupNotify=true
Icon=%{_libdir}/tgif/tgificon.xpm
Categories=Application;Graphics;
EOF

%build
xmkmf
%{__make} %{?_smp_mflags} BINDIR="%{_bindir}" LIBDIR="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall BINDIR="%{buildroot}%{_bindir}" LIBDIR="%{buildroot}%{_libdir}"

%if %{?_without_freedesktop:1}0
	%{__install} -D -m 0644 tgif.desktop %{buildroot}/etc/X11/applnk/Multimedia/tgif.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor %{desktop_vendor}    \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		tgif.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY LICENSE.QPL README*
%{_bindir}/tgif
%{_libdir}/tgif/
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-tgif.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/tgif.desktop}

%changelog
* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 4.1.45-1
- Updated to release 4.1.45.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.1.44-1.2
- Rebuild for Fedora Core 5.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 4.1.44-1
- Initial package.
