# $Id$
# Authority: matthias

%define bmp_inputdir %(pkg-config --variable=input_plugin_dir bmp 2>/dev/null || echo %{_libdir}/bmp/Input)

Summary: Monkey's Audio Codec (MAC/APE) playback plugin for the Beep Media Player
Name: bmp-mac
Version: 0.1.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://supermmx.org/linux/mac/
Source: http://supermmx.org/download/linux/mac/bmp-mac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bmp-devel, mac-devel


%description
This package contains a Monkey's Audio Codec (MAC/APE) playback plugin for BMP
(Beep Media Player), a media player that uses a skinned user interface based
on Winamp 2.x skins, and is based on ("forked off") XMMS.


%prep
%setup


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
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%exclude %{bmp_inputdir}/libbmp-mac.a
%exclude %{bmp_inputdir}/libbmp-mac.la
%{bmp_inputdir}/libbmp-mac.so


%changelog
* Thu May 26 2005 Matthias Saou <http://freshrpms.net/> 0.1.1-1
- Initial rpm package.

