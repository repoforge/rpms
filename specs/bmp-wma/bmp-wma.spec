# $Id$
# Authority: matthias

%define bmp_inputdir %(pkg-config --variable=input_plugin_dir bmp 2>/dev/null || echo %{_libdir}/bmp/Input)

Summary: Windows Media Audio (WMA) playback plugin for the Beep Media Player
Name: bmp-wma
Version: 0.1.1
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://bmp-plugins.berlios.de/
Source: http://download.berlios.de/bmp-plugins/bmp-wma-%{version}.tar.gz
Patch0: bmp-wma-0.1.1-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bmp-devel, gcc-c++


%description
This package contains a Windows Media Audio (WMA) playback plugin for BMP
(Beep Media Player), a media player that uses a skinned user interface based
on Winamp 2.x skins, and is based on ("forked off") XMMS.


%prep
%setup
%patch0 -p1 -b .gcc4


%build
export CFLAGS="%{optflags} -DHAVE_LRINTF -fPIC"
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
%exclude %{bmp_inputdir}/libwma.a
%exclude %{bmp_inputdir}/libwma.la
%{bmp_inputdir}/libwma.so


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.1.1-3
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.1.1-2
- Force -DHAVE_LRINTF in CFLAGS since it's not detected by configure on FC5
  as it should.
- Force -fPIC too as build fails otherwise.

* Thu Jul 21 2005 Matthias Saou <http://freshrpms.net/> 0.1.1-1
- Include bmp-wma-0.1.1-gcc4.patch with the "usual" ffmpeg common.h change.

* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 0.1.1-1
- Initial rpm package.

