# $Id$
# Authority: dag

%{!?audio:%define audio alsa esd oss}

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _without_jack 1}
%{?el5:%define _without_nas 1}

%{?el4:%define _without_jack 1}
%{?el4:%define _without_nas 1}

%{?fc3:%define _without_jack 1}
%{?fc3:%define _without_nas 1}

%{?fc2:%define _without_jack 1}
%{?fc2:%define _without_nas 1}

%{?fc1:%define audio esd oss}
%{?fc1:%define _without_alsa 1}
%{?fc1:%define _without_jack 1}
%{?fc1:%define _without_nas 1}

%{?el3:%define audio esd oss}
%{?el3:%define _without_alsa 1}
%{?el3:%define _without_jack 1}
%{?el3:%define _without_nas 1}

%{?rh9:%define audio esd oss}
%{?rh9:%define _without_alsa 1}
%{?rh9:%define _without_jack 1}
%{?rh9:%define _without_nas 1}

%{?rh7:%define audio esd oss}
%{?rh7:%define _without_alsa 1}
%{?rh7:%define _without_jack 1}
%{?rh7:%define _without_nas 1}

%{?el2:%define audio oss}
%{?el2:%define _without_alsa 1}
%{?el2:%define _without_esound 1}
%{?el2:%define _without_jack 1}
%{?el2:%define _without_nas 1}

Summary: MPEG audio player
Name: mpg123
Version: 1.6.2
Release: 1
License: GPL/LGPL
Group: Applications/Multimedia
URL: http://mpg123.org/

Source: http://mpg123.org/download/mpg123-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig
BuildRequires: portaudio-devel
BuildRequires: SDL-devel
# We actually only need one, but it doesn't hurt to have them all
%{!?_without_jack:BuildRequires: jack-audio-connection-kit-devel}
%{!?_without_esound:BuildRequires: esound-devel}
%{!?_without_nas:BuildRequires: nas-devel}
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
Obsoletes: mpg321 <= 0.2.10-9

%description
Real time command line MPEG audio player for Layer 1, 2 and Layer3.

Available rpmbuild rebuild option :
--define 'audio {alsa,esd,jack,nas,oss,portaudio,sdl}'

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export SDL_CFLAGS="$(sdl-config --cflags)"
export SDL_LIBS="$(sdl-config --libs)"
%configure \
    --program-prefix="%{?_program_prefix}" \
    --enable-gapless="yes" \
    --with-audio="%{audio}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/
%doc %{_mandir}/man1/mpg123.1*
%{_bindir}/mpg123
%{_libdir}/libmpg123.so.*
%{_libdir}/mpg123/
#exclude %{_libdir}/mpg123/*.la

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mpg123.h
%{_libdir}/libmpg123.so
%{_libdir}/pkgconfig/libmpg123.pc
%exclude %{_libdir}/libmpg123.la

%changelog
* Wed Nov 12 2008 Dag Wieers <dag@wieers.com> - 1.6.2-1
- Updated to release 1.6.2.

* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Updated to release 1.6.1.

* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Aug 30 2008 Dag Wieers <dag@wieers.com> - 1.5.1-1
- Updated to release 1.5.1.

* Sun Aug 03 2008 Dag Wieers <dag@wieers.com> - 1.5.0-1
- Updated to release 1.5.0.

* Tue May 27 2008 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4.3.

* Tue Apr 22 2008 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Updated to release 1.4.2.

* Tue Apr 08 2008 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Sun Mar 09 2008 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Sun Feb 03 2008 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Fri Jan 18 2008 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.
- Added devel subpackage.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.68-1
- Updated to release 0.68.

* Mon Jun 04 2007 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Wed Feb 07 2007 Dag Wieers <dag@wieers.com> - 0.65-1
- Updated to release 0.65.

* Tue Jan 16 2007 Dag Wieers <dag@wieers.com> - 0.64-1
- Updated to release 0.64.

* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 0.63-1
- Updated to release 0.63.

* Sun Oct 22 2006 Dag Wieers <dag@wieers.com> - 0.61-1
- Updated to release 0.61.

* Mon Sep  4 2006 Matthias Saou <http://freshrpms.net/> 0.60-1
- Update to 0.60 final.
- Add support for all available compatible outputs, unfortunately it's a build
  time choice, so default to alsa.
- Obsolete mpg321 up to the last know package version.

* Tue Jul 25 2006 Matthias Saou <http://freshrpms.net/> 0.60-0.1.beta2
- Initial RPM release, now that mpg123 is maintained again and went GPL/LGPL.
- Audio output type is not (yet?) plugin-based, so use libao (for ALSA).
