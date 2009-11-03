# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define mozilla xulrunner-devel nspr-devel}

Summary: Flash player
Name: gnash
Version: 0.8.5
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.gnu.org/software/gnash/

Source: http://ftp.gnu.org/gnu/gnash/%{version}/gnash-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%{_arch}-root

BuildRequires: SDL-devel
BuildRequires: SDL_mixer-devel
BuildRequires: agg-devel
BuildRequires: atk-devel
BuildRequires: autotrace
BuildRequires: boost-devel
BuildRequires: curl-devel
BuildRequires: ffmpeg-devel
BuildRequires: gcc-c++
### Gstreamer 0.10 is a *hard* requirement
BuildRequires: gstreamer >= 0.10
BuildRequires: libjpeg-devel
BuildRequires: libmad-devel
BuildRequires: libogg-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
%{!?_without_modxorg:BuildRequires: libGLU-devel, libXmu-devel, libXi-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_mozilla:BuildRequires: %{mozilla}}

%description
Gnash is an open-source flash player.

%package -n mozilla-gnash
Summary: Mozilla plugin for playing Flash movies
Group: Applications/Multimedia
Requires: gnash = %{version}-%{release}

%description -n mozilla-gnash
Firefox plugin for playing Flash movies

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure
%{__perl} -pi.orig -e 's|spx_uint32_t|uint32_t|g;' libmedia/AudioDecoderSpeex.cpp

%build
#./autogen.sh
source %{_sysconfdir}/profile.d/qt.sh
%configure \
    --disable-dependency-tracking \
    --disable-ghelp \
    --disable-docbook \
    --disable-rpath \
    --disable-static \
    --enable-extensions="ALL" \
    --enable-glext \
%{!?_without_gstreamer:--enable-gstreamer} \
%{?_without_gstreamer:--disable-gstreamer} \
    --enable-gui="gtk" \
    --enable-jpeg \
    --enable-png \
    --with-boost_lib="%{_libdir}" \
    --with-plugindir="%{_libdir}/mozilla/plugins"
#   --with-qtdir="$QTDIR"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Clean up buildroot
%{__mv} -v %{buildroot}%{_docdir}/gnash/ rpm-docs/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS TODO rpm-docs/*
%doc %{_mandir}/man1/cygnal.1*
%doc %{_mandir}/man1/dumpshm.1*
%doc %{_mandir}/man1/flvdumper.1*
%doc %{_mandir}/man1/gnash.1*
%doc %{_mandir}/man1/gprocessor.1*
%doc %{_mandir}/man1/soldumper.1*
%config(noreplace) %{_sysconfdir}/gnashpluginrc
%config(noreplace) %{_sysconfdir}/gnashrc
%{_bindir}/dumpshm
%{_bindir}/flvdumper
%{_bindir}/gnash
%{_bindir}/gtk-gnash
#%{_bindir}/gparser
%{_bindir}/gprocessor
%{_bindir}/soldumper
%{_datadir}/gnash/
%{_libdir}/gnash/
%exclude %{_libdir}/gnash/*.la
%exclude %{_libdir}/gnash/plugins/*.la

%if %{!?_without_mozilla:1}0
%files -n mozilla-gnash
%defattr(-, root, root, 0755)
%dir %{_libdir}/mozilla/
%{_libdir}/mozilla/plugins/
%endif

%changelog
* Fri Mar 13 2009 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Wed Jun 18 2008 Dag Wieers <dag@wieers.com> - 0.8.3-1
- Updated to release 0.8.3.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Mon Sep 24 2007 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Updated to release 0.8.0.

* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Thu May 11 2006 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package (using DAR)
