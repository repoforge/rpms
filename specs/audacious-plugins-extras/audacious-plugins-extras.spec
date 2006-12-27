# $Id$
# Authority: matthias
# ExclusiveDist: fc6

%define input_plugin_dir %(pkg-config --variable=input_plugin_dir audacious 2>/dev/null || echo %{_libdir}/audacious/Input)

Summary: Extra playback plugins (AAC, MP3 and WMA) for Audacious
Name: audacious-plugins-extras
Version: 1.2.5
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/
Source: http://audacious-media-player.org/release/audacious-plugins-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious-libs >= 1.2.0
Buildrequires: audacious-devel >= 1.2.0, gcc-c++
# Taglib is required, otherwise nothing will build
BuildRequires: taglib-devel
Obsoletes: audacious-extras < 1.1.2-2

%description
Audacious is a media player forked from BMP (Beep Media Player) which uses a
skinned interface based on Winamp 2.x skins, and in turn based on XMMS.

This package contains extra plugins (MP3 playback...)


%prep
%setup -n audacious-plugins-%{version}


%build
%configure --disable-rpath
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# We want aac alac mpg123 and wma plugins only
for file in aac/src/libaac alac/libalac mpg123/libmpg123 wma/libwma; do
    %{__install} -D -m 0755 src/${file}.so \
        %{buildroot}%{input_plugin_dir}/`basename ${file}.so`
done


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING
%doc src/mpg123/README src/mpg123/TODO
%{input_plugin_dir}/*.so


%changelog
* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Rename to audacious-plugins-extras and base on the new 1.2.x plugins.
- Obsolete audacious-extras < 1.1.2-2.

* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Split off -extras from main to make a simple add-on for the Extras package.
- Note that we make a full build anyway, as it's the easiest (not fastest...).

