# $Id$
# Authority: dag


%{!?dtag:%define mozilla xulrunner}
%{!?dtag:%define _without_gstreamer 1}
%{!?dtag:%define _without_mozilla 1}

%{?el5:%define mozilla xulrunner}
%{?el5:%define _without_gstreamer 1}
### Can't figure out why only EL5 produces swfdec-mozilla-player
%{?el5:%define _with_mozilla_player 1}

%{?el4:%define mozilla seamonkey}
%{?el4:%define _without_modxorg 1}

%{?el3:%define mozilla seamonkey}
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_gstreamer 1}
%{?el3:%define _without_modxorg 1}

Summary: Flash animations rendering library
Name: swfdec
Version: 0.4.5
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://swfdec.freedesktop.org/wiki/

Source: http://swfdec.freedesktop.org/download/swfdec/0.4/swfdec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: directfb
BuildRequires: ffmpeg-devel
BuildRequires: GConf2-devel
BuildRequires: gcc-c++
BuildRequires: gdk-pixbuf-devel
BuildRequires: gtk2-devel >= 2.1.2
BuildRequires: js-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libmad-devel
BuildRequires: liboil-devel
BuildRequires: SDL-devel
BuildRequires: x264-devel
%{?gimp_plugin:BuildRequires: gimp-devel >= 2.0}
#%{!?_without_mozilla:BuildRequires: %{mozilla}-devel}
%{!?_without_gstreamer:BuildRequires: gstreamer-plugins-devel}
%{!?_without_modxorg:BuildRequires: libXt-devel}

%description
Libswfdec is a library for rendering Flash animations. Currently it
handles most Flash 3 animations and some Flash 4. No interactivity is
supported yet.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}, glib2-devel, liboil-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n mozilla-swfdec
Summary: Mozilla plugin for Flash rendering
Group: Applications/Internet
Requires: %{name} = %{version}

%description -n mozilla-swfdec
Mozilla plugin for rendering of Flash animations based on the swfdec library.

%prep
%setup

%{__perl} -pi -e 's|<avcodec.h>|<libavcodec/avcodec.h>|g' libswfdec/swfdec_codec_ffmpeg.c

%build
export FFMPEG_CFLAGS="$(pkg-config --cflags libavcodec)"
export FFMPEG_LIBS="$(pkg-config --libs libavcodec)"
%configure \
%{?_without_mozilla:--disable-mozilla-plugin} \
    --enable-shared \
%{!?_without_alsa:--with-audio="alsa"}
%{__make} %{?_smp_mflags} 
%{__make} %{?_smp_mflags} -C player

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__make} -C player install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
[ -x %{_bindir}/update-gdk-pixbuf-loaders ] && \
    %{_bindir}/update-gdk-pixbuf-loaders $(uname -i)-redhat-linux-gnu || :

### Backward compatibility for gtk < 2.4.13-9
[ -x %{_bindir}/gdk-pixbuf-query-loaders ] && \
    %{_bindir}/gdk-pixbuf-query-loaders > \
        %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders || :

%postun
/sbin/ldconfig
[ -x %{_bindir}/update-gdk-pixbuf-loaders ] && \
    %{_bindir}/update-gdk-pixbuf-loaders $(uname -i)-redhat-linux-gnu || :

### Backward compatibility for gtk < 2.4.13-9
[ -x %{_bindir}/gdk-pixbuf-query-loaders ] && \
    %{_bindir}/gdk-pixbuf-query-loaders > \
        %{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README
%{_libdir}/libswfdec*.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/swfdec/
%{_includedir}/swfdec*/
%{_libdir}/libswfdec*.a
%exclude %{_libdir}/libswfdec*.la
%{_libdir}/libswfdec*.so
%{_libdir}/pkgconfig/swfdec*.pc

%changelog

* Thu Jul 09 2009 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.
- Rebuild against ffmpeg-0.5.
- Rebuild against x264-0.4.20090708.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.3.6-2
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net/> 0.3.6-1
- Update to 0.3.6.
- Add js-devel buil requirement, configure should check this.
- Remove no longer included swf_play.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.3.5-2
- Disable gstreamer support on FC5 (as it's for 0.8).
- Disable mozilla plugin on FC5 (no more mozilla-config script).
- Add modular xorg build conditional.

* Wed May 25 2005 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Update to 0.3.5.

* Thu May  5 2005 Matthias Saou <http://freshrpms.net/> 0.3.4-2
- Add missing glib2-devel and liboil-devel reqs in the devel package.

* Sat Apr  2 2005 Matthias Saou <http://freshrpms.net/> 0.3.4-1
- Update to 0.3.4.
- Change %%makeinstall for DESTDIR method because of the gimp plugin.

* Fri Nov 26 2004 Dag Wieers <dag@wieers.com> - 0.3.2-2
- Added update-gdk-pixbuf-loaders to scriptlets.

* Thu Nov 25 2004 Matthias Saou <http://freshrpms.net/> 0.3.2-2
- Make scriplets never return a failure.

* Wed Nov 24 2004 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3.2.

* Tue Nov  9 2004 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Make gimp plugin conditional and build only for FC2, FC3 and YD4 (gimp2).

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Wed Oct 20 2004 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.
- Added new liboil-devel and gimp2-devel dependencies.
- Added gimp plugin... strange, it goes into 1.3 :-/

* Tue Jan 20 2004 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Added missing swfdec requirement. (Alexandre Oliva)

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 0.2.2-0
- Initial package. (using DAR)

