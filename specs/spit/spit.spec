# $Id$
# Authority: dries
# Upstream: Remko Tronçon <spike$ulyssis,org>

# Screenshot: http://spit.sf.net/images/screenshot-kde.jpg

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: Graphical picture indexing tool
Name: spit
Version: 0.3.1
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://spit.sourceforge.net/

Source: http://dl.sf.net/spit/spit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, ImageMagick-c++-devel
BuildRequires: libxml2-devel, libxslt-devel, gcc-c++, desktop-file-utils
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Spit is a graphical picture indexing tool. It can be used to manage pictures,
and generate HTML pages for putting your pictures online. It is designed for
user-friendliness, portability and extensibility. It allows quick & easy
ordering, editing and adding captions for pictures.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Spit Picture Indexer
Comment=A graphical picture indexing tool.
Icon=spit.svg
Exec=spit
Terminal=false
Type=Application
Encoding=UTF-8
Categories=KDE;Application;Graphics;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
./configure \
	--debug \
	--prefix="%{_prefix}"
%{__make} src/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
# install part doesn't work in mach chroot without this
perl -i -npe "s/..INSTALL_ROOT.(\.\.\/)*(\/usr\/)?/${RPM_BUILD_ROOT//\//\\/}\/usr\//g;" src/Makefile
%makeinstall
%{__rm} -Rf %{buildroot}%{_datadir}/doc/spit
%{__install} -Dp -m0644 pixmaps/spit.svg %{buildroot}%{_datadir}/pixmaps/spit.svg

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor kde                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING INSTALL README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/spit/

%changelog
* Thu Apr 01 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
