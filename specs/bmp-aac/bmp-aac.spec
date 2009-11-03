# $Id$
# Authority: matthias

%define date 20041215
%define bmp_inputdir %(pkg-config --variable=input_plugin_dir bmp 2>/dev/null || echo %{_libdir}/bmp/Input)

Summary: AAC/MP4 playback plugin for the Beep Media Player
Name: bmp-aac
Version: 0
Release: 2.%{date}%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://fondriest.frederic.free.fr/realisations/
Source: http://fondriest.frederic.free.fr/fichiers/bmp-mp4_%{date}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bmp-devel
# No configure included
BuildRequires: autoconf, automake, libtool, gcc-c++


%description
This package contains an AAC/MP4 playback plugin for BMP (Beep Media Player),
a media player that uses a skinned user interface based on Winamp 2.x skins,
and is based on ("forked off") XMMS.


%prep
%setup -n bmp-mp4_%{date}
autoreconf -vifs


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING
%exclude %{bmp_inputdir}/libmp4.la
%{bmp_inputdir}/libmp4.so


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0-2.20041215
- Release bump to drop the disttag number in FC5 build.

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 0-1.20041215
- Initial rpm package.

