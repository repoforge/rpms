# $Id$

# Authority: dries
# Upstream: Remko Tronçon <spike@ulyssis.org>
# Schreenshot: http://spit.sf.net/images/screenshot-kde.jpg

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Graphical picture indexing tool
Name: spit
Version: 0.3.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://spit.sf.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/spit/spit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, ImageMagick-c++-devel, libxml2-devel, libxslt-devel, gcc-c++, desktop-file-install

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
# export CXX=g++296
./configure \
	--prefix="%{_prefix}"
%{__make} src/Makefile

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/usr/bin|\$(bindir)|;
		s|/usr/share|\$(datadir)|;
	' src/Makefile

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_datadir}/spit/

# Makefile doesn't use the defines of makeinstall and doesn't use the
# default DESTDIR
%makeinstall INSTALL_ROOT=%{buildroot}

%{__install} -D -m0644 pixmaps/spit.svg %{buildroot}%{_datadir}/pixmaps/spit.svg

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
