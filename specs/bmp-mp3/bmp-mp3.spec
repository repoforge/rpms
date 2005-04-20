# $Id$
# Authority: matthias

Summary: MP3 playback plugin for the Beep Media Player
Name: bmp-mp3
Version: 0.9.7
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://beepmp.sourceforge.net/
Source: http://dl.sf.net/beepmp/bmp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: bmp >= %{version}
BuildRequires: XFree86-devel, gtk2-devel, libglade2-devel, libvorbis-devel
BuildRequires: id3lib-devel

%description
This package contains an MP3 playback plugin for BMP (Beep Media Player),
a media player that uses a skinned user interface based on Winamp 2.x skins,
and is based on ("forked off") XMMS. 


%prep
%setup -n bmp-%{version}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 Input/mpg123/.libs/libmpg123.so \
    %{buildroot}%{_libdir}/bmp/Input/libmpg123.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING
%{_libdir}/bmp/Input/libmpg123.so


%changelog
* Wed Apr 13 2005 Matthias Saou <http://freshrpms.net/> 0.9.7-1
- Initial RPM release, rebuild the whole application and take only mpg123
  plugin. Pure packager laziness in action.

