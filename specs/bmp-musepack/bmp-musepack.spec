# $Id$
# Authority: matthias

#define prever RC1
%define bmp_inputdir %(pkg-config --variable=input_plugin_dir bmp 2>/dev/null || echo %{_libdir}/bmp/Input)

Summary: Mpegplus (mpc) playback plugin for the Beep Media Player
Name: bmp-musepack
Version: 1.2
Release: 3%{?prever:.%{prever}}%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.musepack.net/
Source: http://musepack.origean.net/files/linux/plugins/bmp-musepack-%{version}%{?prever:-%{prever}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: bmp-devel, libmpcdec-devel, taglib-devel, gcc-c++


%description
This package contains an MPC playback plugin for BMP (Beep Media Player),
a media player that uses a skinned user interface based on Winamp 2.x skins,
and is based on ("forked off") XMMS.


%prep
%setup -n %{name}-%{version}%{?prever:-%{prever}}


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
%doc ChangeLog COPYING
%exclude %{bmp_inputdir}/libmpc.la
%{bmp_inputdir}/libmpc.so


%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 1.2-3
- Rebuild against libmpcdec 1.2.6.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.2-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 1.2-1
- Update to 1.2 final.

* Mon May  9 2005 Matthias Saou <http://freshrpms.net/> 1.2-0.1.RC1
- Update to 1.2-RC1.
- Now build against new libmpcdec and not libmusepack.
- Added taglib-devel build depencency.

* Mon Apr 25 2005 Matthias Saou <http://freshrpms.net/> 1.1.2-1
- Initial rpm package.

