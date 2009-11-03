# $Id$
# Authority: matthias
# ExclusiveDist: fc6 el5

%define input_plugin_dir %(pkg-config --variable=input_plugin_dir audacious 2>/dev/null || echo %{_libdir}/audacious/Input)

Summary: Extra playback plugins (AAC, MP3 and WMA) for Audacious
Name: audacious-plugins-extras
Version: 1.3.3
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://audacious-media-player.org/
Source: http://static.audacious-media-player.org/release/audacious-plugins-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: audacious-libs >= 1.3.0
BuildRequires: audacious-devel >= 1.3.0
BuildRequires: lame-devel
BuildRequires: libmms-devel
BuildRequires: libmad-devel
# taglib is required, otherwise nothing will build
BuildRequires: taglib-devel
# gettext is required, otherwise we get a build error...
BuildRequires: gettext
Obsoletes: audacious-extras < 1.1.2-2
Provides: audacious-plugins-lame = %{version}-%{release}
Provides: audacious-plugins-mms = %{version}-%{release}
Provides: audacious-plugins-aac = %{version}-%{release}
Provides: audacious-plugins-alac = %{version}-%{release}
Provides: audacious-plugins-mad = %{version}-%{release}
Provides: audacious-plugins-wma = %{version}-%{release}

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
for file in lame/liblame mms/libmms aac/src/libaac alac/libalac madplug/libmadplug wma/libwma; do
    %{__install} -D -m 0755 src/${file}.so \
        %{buildroot}%{input_plugin_dir}/`basename ${file}.so`
done


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{input_plugin_dir}/*.so


%changelog
* Tue Apr 17 2007 Matthias Saou <http://freshrpms.net/> 1.3.3-1
- Update to 1.3.3.
- Provide all of the plugins we include.
- Add lame support.
- Add libmms support.
- The mp3 support is now through libmad.

* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 1.2.5-1
- Rename to audacious-plugins-extras and base on the new 1.2.x plugins.
- Obsolete audacious-extras < 1.1.2-2.

* Fri Sep 15 2006 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Split off -extras from main to make a simple add-on for the Extras package.
- Note that we make a full build anyway, as it's the easiest (not fastest...).

