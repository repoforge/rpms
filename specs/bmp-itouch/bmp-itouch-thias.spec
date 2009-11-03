# $Id$
# Authority: matthias

%define bmp_general %(pkg-config --variable=general_plugin_dir bmp)
%define bmp_datadir %(pkg-config --variable=data_dir bmp)

Summary: iTouch keyboard control plugin for the Beep Media Player
Name: bmp-itouch
Version: 1.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://bmp-itouch.sourceforge.net/
Source: http://dl.sf.net/bmp-itouch/bmp-itouch-%{version}.tar.gz
Patch: bmp-itouch-1.1.0-cosmetic.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: bmp >= 0.9.7
BuildRequires: bmp-devel, gettext, pkgconfig

%description
With this BMP plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch or compatible keyboard. When the
plugin is used you can use the keys regardless of the current input focus. The
plugin won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.


%prep
%setup
%patch -p1 -b .cosmetic


%build
%configure \
    --libdir=%{bmp_general} \
    --datadir=%{bmp_datadir}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install \
    libdir=%{buildroot}%{bmp_general} \
    datadir=%{buildroot}%{bmp_datadir}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING
%exclude %{bmp_general}/libitouch.so
%{bmp_general}/libKeyBoardPlayFunction.so
%exclude %{bmp_general}/libitouch.la
%exclude %{bmp_general}/libKeyBoardPlayFunction.la
%config %{bmp_datadir}/bmp-itouch.config


%changelog
* Wed Apr 20 2005 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Update to "unstable" 1.1.0, as unlike 1.0.1, it works.
- Exclude the old 1.0.1 plugin to avoid confusion, and remove "EXPERIMENTAL"
  from the plugin description to not scare users away.

* Wed Apr 13 2005 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Initial RPM release.

