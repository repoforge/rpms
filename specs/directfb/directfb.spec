# $Id$
# Authority: matthias

Summary: Hardware graphics acceleration library
Name: directfb
Version: 0.9.20
Release: 1
License: GPL
Group: System/Libraries
URL: http://www.directfb.org/
Source: http://www.directfb.org/download/DirectFB/DirectFB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpng-devel, libjpeg-devel, zlib-devel, freetype-devel >= 2.0
BuildRequires: SDL-devel, libtool

%description
DirectFB is a thin library that provides hardware graphics acceleration,
input device handling and abstraction, integrated windowing system with
support for translucent windows and multiple display layers on top of the
Linux Framebuffer Device. It is a complete hardware abstraction layer with
software fallbacks for every graphics operation that is not supported by
the underlying hardware. DirectFB adds graphical power to embedded systems
and sets a new standard for graphics under Linux.


%package devel
Summary: Development files for DirectFB
Group: Development/Libraries
Requires: %{name} = %{version}, SDL-devel

%description devel
DirectFB is a thin library that provides hardware graphics acceleration,
input device handling and abstraction, integrated windowing system with
support for translucent windows and multiple display layers on top of the
Linux Framebuffer Device. It is a complete hardware abstraction layer with
software fallbacks for every graphics operation that is not supported by
the underlying hardware. DirectFB adds graphical power to embedded systems
and sets a new standard for graphics under Linux.

Header files needed for building applications based on DirectFB.


%prep
%setup -q -n DirectFB-%{version}


%build
%configure \
    --enable-fbdev \
    --enable-static \
    --enable-linux-input \
    --disable-maintainer-mode \
    --disable-fast-install
%{__make}


%install
%{__rm} -rf %{buildroot}
# Ugly libtool hack!
#rm -f libtool && cp -a `which libtool` . || :
%{__make} install DESTDIR=%{buildroot}
# Remove all *.la files
find %{buildroot} -name "*.la" | xargs rm -f
# Clean up the docs
%{__rm} -f docs/html/Makefile*


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README fb.modes docs/README.screenshots
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/gfxdrivers
%dir %{_libdir}/%{name}-%{version}/inputdrivers
%dir %{_libdir}/%{name}-%{version}/interfaces
%dir %{_libdir}/%{name}-%{version}/interfaces/*
%dir %{_libdir}/%{name}-%{version}/systems
%{_libdir}/%{name}-%{version}/gfxdrivers/*.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_joystick.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_keyboard.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_linux_input.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_lirc.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_ps2mouse.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_serialmouse.so
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_sonypi.so
%{_libdir}/%{name}-%{version}/interfaces/*/*.so
%{_libdir}/%{name}-%{version}/systems/libdirectfb_fbdev.so
%{_datadir}/%{name}-%{version}
%{_mandir}/man5/*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/gfxdrivers
%dir %{_libdir}/%{name}-%{version}/inputdrivers
%dir %{_libdir}/%{name}-%{version}/interfaces
%dir %{_libdir}/%{name}-%{version}/interfaces/*
%dir %{_libdir}/%{name}-%{version}/systems
%{_libdir}/%{name}-%{version}/gfxdrivers/*.a
%{_libdir}/%{name}-%{version}/inputdrivers/*.a
%{_libdir}/%{name}-%{version}/inputdrivers/libdirectfb_sdlinput.so
%{_libdir}/%{name}-%{version}/interfaces/*/*.a
%{_libdir}/%{name}-%{version}/systems/*.a
%{_libdir}/%{name}-%{version}/systems/libdirectfb_sdl.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*


%changelog
* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> - 0.9.20-1
- Update to 0.9.20.
- Rebuild for Fedora Core 1.

* Mon Jul 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.19.
- Added systems directory, with the SDL plugin in the devel package.
- Removed /etc/fb.modes, which conflicts with the fbset rpm.
- Added libtool hack to get the proper binaries installed.

* Fri Jul 18 2003 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup... err, rewrite.

* Mon Jan 13 2003 Sven Neumann <neo@directfb.org> 0.9.16
- removed reference to avifile
- added rules for dfbg and its man-page

* Sun Oct 27 2002 Sven Neumann <neo@directfb.org> 0.9.14
- added this file as directfb.spec.in to the DirectFB source tree
- moved directfbrc manpage to the main package

* Fri Aug 23 2002 Götz Waschk <waschk@linux-mandrake.com> 0.9.13-1mdk
- add directfb-csource and man page
- 0.9.13

* Thu Jul 11 2002 Götz Waschk <waschk@linux-mandrake.com> 0.9.12-1mdk
- initial package based on PLD effort

