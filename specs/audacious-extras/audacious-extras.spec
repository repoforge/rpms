# $Id$
# Authority: matthias
# ExclusiveDist: fc6

%define input_plugin_dir %(pkg-config --variable=input_plugin_dir audacious 2>/dev/null || echo %{_libdir}/audacious/Input)

Summary: Extra playback plugins (AAC, MP3 and WMA) for Audacious
Name: audacious-extras
Version: 1.1.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/
Source: http://audacious-media-player.org/release/audacious-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious = %{version}
BuildRequires: gtk2-devel, libglade2-devel, gettext-devel
# The bare minimum required to get things to build for the plugins we want
BuildRequires: taglib-devel, libvorbis-devel
# To get the pkgconfig file for the Input directory location
BuildRequires: audacious-devel
Provides: audacious-aac = %{version}-%{release}
Provides: audacious-mp3 = %{version}-%{release}
Provides: audacious-wma = %{version}-%{release}

%description
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

This package contains a plugin to enable MP3 playback.


%prep
%setup -n audacious-%{version}


%build
%configure --disable-rpath
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# aac
%{__install} -D -m 0755 Plugins/Input/aac/src/libaac.so \
    %{buildroot}%{input_plugin_dir}/libaac.so
# mp3
%{__install} -D -m 0755 Plugins/Input/mpg123/libmpg123.so \
    %{buildroot}%{input_plugin_dir}/libmpg123.so
# wma
%{__install} -D -m 0755 Plugins/Input/wma/libwma.so \
    %{buildroot}%{input_plugin_dir}/libwma.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING
%doc Plugins/Input/mpg123/README Plugins/Input/mpg123/TODO
%{input_plugin_dir}/libaac.so
%{input_plugin_dir}/libmpg123.so
%{input_plugin_dir}/libwma.so


%changelog
* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Split off -extras from main to make a simple add-on for the Extras package.
- Note that we make a full build anyway, as it's the easiest (not fastest...).

