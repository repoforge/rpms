# $Id$
# Authority: matthias

### EL6 ships with libtheora-1.1.0-2.el6
### EL5 ships with libtheora-1.0alpha7-1
### EL4 ships with libtheora-1.0alpha3-5
# ExclusiveDist: el2 el3

%{?el3:%define _without_alsa 1}
%{?el2:%define _without_alsa 1}

%define prever alpha3

Summary: Theora video compression codec
Name: libtheora
Version: 1.0
Release: %{?prever:0.%{prever}.}4%{?dist}
License: BSD
URL: http://www.theora.org/
Source: http://www.theora.org/files/libtheora-%{version}%{?prever}.tar.bz2
Patch0: libtheora-1.0alpha3-autotools.patch
Patch1: libtheora-1.0alpha3-mmx.patch
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libogg-devel >= 1.1, libvorbis-devel >= 1.0.1, SDL-devel, gcc-c++
# Fedora Core 2's SDL-devel forgot to require alsa-lib-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
# We patch Makefile.am, so we need to re-autotool
BuildRequires: autoconf, automake, libtool

%description
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.


%package devel
Summary: Headers for developing programs that will use libtheora
Group: Development/Libraries
Requires: %{name} = %{version}, libogg-devel >= 1.1

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%package -n theora-tools
Summary: Command line tools for Theora videos
Group: Applications/Multimedia
Requires: %{name} = %{version}

%description -n theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.


%prep
%setup -n %{name}-%{version}%{?prever}
%patch0 -p1 -b .autotools
%ifarch %{ix86}
%patch1 -p1 -b .mmx
%endif


%build
# autoreconf or autogen.sh doesn't work, due to wrong libtool.m4
aclocal
autoconf
libtoolize --force
automake
%configure \
    --enable-shared \
    --enable-static \
    --with-pic
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%makeinstall \
    docdir=$(pwd)/_docs

# Manually install tools
%{__install} -Dp -m0755 examples/.libs/dump_video \
    %{buildroot}%{_bindir}/theora_dump_video
%{__install} -Dp -m0755 examples/.libs/encoder_example \
    %{buildroot}%{_bindir}/theora_encode
%{__install} -Dp -m0755 examples/.libs/player_example \
    %{buildroot}%{_bindir}/theora_player


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/libtheora.so.*

%files devel
%defattr(-, root, root, 0755)
%doc _docs/*
%{_includedir}/theora/
%{_libdir}/libtheora.a
%exclude %{_libdir}/libtheora.la
%{_libdir}/libtheora.so

%files -n theora-tools
%defattr(-, root, root, 0755)
%{_bindir}/*


%changelog
* Mon Oct 25 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.4
- Include autotools and mmx patches from Thomasvs' GStreamer package.
- Added theora-tools package to do like the main Fedora Core package.
- Only apply mmx patch on i386, build fails on x86_64 with it.

* Wed Sep 22 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.3
- Enable shared library.

* Tue Jul  6 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.2
- Added --with-pic for x86_64 build.
- Simplified setting of the proper include dir.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.1
- Initial RPM release, only devel as there is only a static lib for now.

