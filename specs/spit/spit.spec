# $Id$

# Authority: dries
# Upstream: Remko Tronçon <spike@ulyssis.org>
# Schreenshot: http://spit.sourceforge.net/images/screenshot-kde.jpg
### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Graphical picture indexing tool
Name: spit
Version: 0.3
Release: 0
License: GPL
Group: Amusements/Graphics
URL: http://spit.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/spit/spit-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: qt-devel, ImageMagick-c++-devel, libxml2-devel, libxslt-devel

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
Icon=spit.xpm
Exec=spit
Terminal=false
Type=Application
Categories=KDE;Application;Graphics;
EOF

%build
source "/etc/profile.d/qt.sh"
export CXX=g++296
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
./configure \
	--prefix="%{_prefix}"
### FIXME: Rewrite Makefile to add Magick++ support
%{__make} src/Makefile
%{__perl} -pi.orig -e '
		s|DQT_THREAD_SUPPORT|DQT_THREAD_SUPPORT -DHAVE_IMAGEMAGICK -DHAVE_IMAGEMAGICKPP|;
		s|lpthread|lpthread -lMagick++|;
	' src/Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%makeinstall
#%{__install} -d -m0755 %{buildroot}%{_bindir} \
#%{__install} -m0755 spit %{buildroot}%{_bindir}

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 images/spit.xpm %{buildroot}%{_datadir}/pixmaps/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor kde                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm
%{_datadir}/spit/

%changelog
* Mon Jan 19 2004 Dag Wieers <dag@wieers.com> - 0.3-0
- Updated to release 0.3.

* Fri Jan 16 2004 Dag Wieers <dag@wieers.com> - 0.2-0
- Initial package. (using DAR)
