# $Id$
# Authority: dries

%define real_version 040322

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Linux Video Editor
Name: lve
Version: 0.%{real_version}
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://lvempeg.sourceforge.net/

Source: http://dl.sf.net/lvempeg/lve-%{real_version}.src.tar.bz2
Source1: http://dl.sf.net/ffmpeg/ffmpeg-0.4.8.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: a52dec-devel
BuildRequires: ffmpeg-devel
BuildRequires: gcc-c++
BuildRequires: mpeg2dec-devel
BuildRequires: qt-devel
BuildRequires: SDL-devel

%description
LVE provides frame and GOP accurate editing of MPEG1/2 elementary ("ES") and
program streams ("PS"), including VOB format. The cutting engine is based on
a frame server (demuxer), which guarantees exact and fast seeking to every
frame. The GUI is based on libSDL. Video scenes are handled as thumbnails
movable by drag and drop. Final videos can be build with or without
re-encoding. Tools for shrinking and DVD authoring are also available.

%prep
%setup -n lve

%build
# fix permissions of devel dir
%{__chmod} -R u+w .
. /etc/profile.d/qt.sh
sed -i "s/liba52\//a52dec\//g;" src/*
%{__tar} -xzvf %{SOURCE1}
%{__rm} ffmpeg
ln -s ffmpeg-0.4.8 ffmpeg
sed -i "s/\/usr\/local\/lve\/bin\/lverequant/\/usr\/bin\/lverequant/g;" src/lvedump.c
sed -i "s/\/usr\/local\/lve\/lib/\/usr\/share\/lve\/lib/g;" src/lve.h
sed -i "s/\/usr\/local\/lve\/bin/\/usr\/bin/g;" src/lve.h
%{__make} all-recursive INCLUDE="-I../ffmpeg/libavcodec -I/usr/include/mpeg2dec" QT_DIR=${QTDIR} SUBDIRS="qdir src" %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/lve %{buildroot}%{_bindir}/lve
%{__install} -Dp -m0755 src/lvedemux %{buildroot}%{_bindir}/lvedemux
%{__install} -Dp -m0755 src/lvedump %{buildroot}%{_bindir}/lvedump
%{__install} -Dp -m0755 src/lvemkdvd %{buildroot}%{_bindir}/lvemkdvd
%{__install} -Dp -m0755 src/lvemkidx %{buildroot}%{_bindir}/lvemkidx
%{__install} -Dp -m0755 src/lvemux %{buildroot}%{_bindir}/lvemux
%{__install} -Dp -m0755 src/lverequant %{buildroot}%{_bindir}/lverequant
%{__install} -Dp -m0755 qdir/qdir %{buildroot}%{_bindir}/qdir
%{__install} -Dp -m0755 bin/lvefilter %{buildroot}%{_bindir}/lvefilter

%{__install} -d -m755 %{buildroot}%{_datadir}/lve/lib
%{__install} -p -m0755 lib/* %{buildroot}%{_datadir}/lve/lib/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING DVD-Authoring.txt Readme.avsync Readme.lvemux
%{_bindir}/*
%{_datadir}/lve/

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.040322-2
- Simplify buildequirements: SDL-devel already requires xorg-x11-devel/XFree86-devel

* Tue Jun 1 2004 Dries Verachtert <dries@ulyssis.org> - 0.040322-1
- Initial package.
