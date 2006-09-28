# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?fc5:%define _with_modxorg 1}
%{?fc6:%define _with_modxorg 1}

%{?fc1:%define _without_kde32 1}
%{?el3:%define _without_kde32 1}
%{?rh9:%define _without_kde32 1}
%{?rh7:%define _without_kde32 1}
%{?el2:%define _without_kde32 1}

%ifarch x86_64
%define _without_kde32 1
%endif

Summary: Flash player
Name: gnash
Version: 0.7.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.gnu.org/software/gnash/

Source: ftp://ftp.belnet.be/mirror/ftp.gnu.org/gnu/gnash/%{version}/gnash-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: SDL-devel, libxml2-devel, SDL_mixer-devel
BuildRequires: libpng-devel, libmad-devel, libogg-devel, gcc-c++
%{!?_without_kde32:BuildRequires: kdebase-devel >= 3.2}
%{?_with_modxorg:BuildRequires: libGLU-devel, libXmu-devel, libXi-devel}
%{!?_with_modxorg:BuildRequires: XFree86-devel}

%description
A flash player.

%package -n konqueror-gnash
Summary: Konqueror plugin for playing Flash movies
Group: Applications/Multimedia
Requires: gnash = %{version}-%{release}
Requires: kdebase-core

%description -n konqueror-gnash
Konqueror plugin for playing Flash movies

%package -n mozilla-gnash
Summary: Mozilla plugin for playing Flash movies
Group: Applications/Multimedia
Requires: gnash = %{version}-%{release}

%description -n mozilla-gnash
Firefox plugin for playing Flash movies

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure

%build
#./autogen.sh
%configure \
	--disable-ghelp \
	--disable-docbook \
	--enable-dom \
	--enable-glext \
	--enable-http \
	--enable-jpeg \
%{!?_without_kde32:--enable-klash} \
%{?_without_kde32:--disable-klash} \
	--enable-mp3 \
	--enable-net-conn \
	--enable-ogg \
	--enable-plugin \
	--enable-pthreads \
	--enable-png \
	--enable-xmlreader \
	--with-plugindir="%{_libdir}/mozilla/plugins"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO
%{_bindir}/gnash
%{_bindir}/gparser
%{_bindir}/gprocessor
%exclude %{_libdir}/libgnashasobjs.a
%exclude %{_libdir}/libgnashasobjs.la
%{_libdir}/libgnashasobjs.so*
%exclude %{_libdir}/libgnashbackend.a
%exclude %{_libdir}/libgnashbackend.la
%{_libdir}/libgnashbackend.so*
%exclude %{_libdir}/libgnashbase.a
%exclude %{_libdir}/libgnashbase.la
%{_libdir}/libgnashbase.so*
%exclude %{_libdir}/libgnashgeo.a
%exclude %{_libdir}/libgnashgeo.la
%{_libdir}/libgnashgeo.so*
%exclude %{_libdir}/libgnashserver.a
%exclude %{_libdir}/libgnashserver.la
%{_libdir}/libgnashserver.so*

%if %{!?_without_kde32:1}0
%files -n konqueror-gnash
%defattr(-, root, root, 0755)
%config %{_datadir}/config/klashrc
%{_bindir}/klash
%{_datadir}/apps/klash
%{_datadir}/services/klash_part.desktop
%{_libdir}/kde3/libklashpart.la
%{_libdir}/kde3/libklashpart.so
%exclude %{_libdir}/kde3/libklashpart.a
%endif

%files -n mozilla-gnash
%defattr(-, root, root, 0755)
#%{_libdir}/libmozsdk.so*
%dir %{_libdir}/mozilla/
%{_libdir}/mozilla/plugins/

%changelog
* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package (using DAR)
