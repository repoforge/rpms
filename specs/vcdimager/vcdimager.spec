# $Id$
# Authority: matthias

Summary: VideoCD (pre-)mastering and ripping tool
Name: vcdimager
Version: 0.7.23
Release: 5%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.vcdimager.org/
Source: ftp://ftp.gnu.org/pub/gnu/vcdimager/vcdimager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libcdio-devel >= 0.72, libxml2-devel >= 2.3.8
BuildRequires: zlib-devel, pkgconfig >= 0.9, popt, gcc-c++

%description
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

VCDRip, which comes with VCDImager, does the reverse operation. That
is, ripping mpeg streams from images (and already burned VideoCDs)
and showing some information about the VideoCD.


%package devel
Summary: Header files and static library for VCDImager
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

This package contains the header files and a static library to develop
applications that will use VCDImager.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
# Sometimes this file gets created... but we don't want it!
%{__rm} -f %{buildroot}%{_infodir}/dir


%clean
%{__rm} -rf %{buildroot}


%post
for infofile in vcdxrip.info vcdimager.info vcd-info.info; do
    /sbin/install-info %{_infodir}/${infofile} %{_infodir}/dir 2>/dev/null || :
done

%preun
if [ $1 -eq 0 ]; then
    for infofile in vcdxrip.info vcdimager.info vcd-info.info; do
        /sbin/install-info --delete %{_infodir}/${infofile} %{_infodir}/dir \
            2>/dev/null || :
    done
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FAQ NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/libvcdinfo.so.*
%{_infodir}/vcdxrip.info*
%{_infodir}/vcdimager.info*
%{_infodir}/vcd-info.info*
#{_infodir}/vcddump.info*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libvcd/
%{_libdir}/libvcdinfo.a
%exclude %{_libdir}/libvcdinfo.la
%{_libdir}/libvcdinfo.so
%{_libdir}/pkgconfig/libvcdinfo.pc


%changelog
* Sun Sep 24 2006 Matthias Saou <http://freshrpms.net/> 0.7.23-5
- Rebuild against new libcdio.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.7.23-4
- Release bump to drop the disttag number in FC5 build.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 0.7.23-3
- Silence install-info scriplets.

* Sat Jul 30 2005 Matthias Saou <http://freshrpms.net/> 0.7.23-2
- Rebuild against new libcdio.

* Tue Jul 12 2005 Matthias Saou <http://freshrpms.net/> 0.7.23-1
- Update to 0.7.23.
- Update libcdio-devel requirement to >= 0.72.
- Change source location from vcdimager.org to gnu.org for this release...

* Tue Jun 28 2005 Matthias Saou <http://freshrpms.net/> 0.7.22-2
- Prevent scriplets from failing if the info calls return an error.

* Tue May 17 2005 Matthias Saou <http://freshrpms.net/> 0.7.22-1
- Update to 0.7.22.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 0.7.21-1
- Update to 0.7.21 at last.
- Split off new -devel package.
- Added libcdio build requirement.
- Update Source URL, it's not "UNSTABLE" anymore.
- Remove vcddump.info and add vcd-info.info. Remove .gz from scriplets.

* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 0.7.14-4
- Added missing install-info calls.

* Mon May 24 2004 Matthias Saou <http://freshrpms.net/> 0.7.14-3
- Tried and update to 0.7.20, but the looping libcd* deps are a problem.
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.7.14-2
- Rebuild for Fedora Core 1.

* Fri May  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.14.
- Remove infodir/dir, thanks to Florin Andrei.
- Updated URL/Source.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Fri Feb 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.13.
- Removed the now unnecessary libxml fix.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Fix xmlversion.h include path in configure since xml is disabled otherwise,
  thanks to Rudolf Kastl for spotting the problem.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Let's try the 1 year old 0.7 development branch!

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.

* Sat Jan 20 2001 Herbert Valerio Riedel <hvr@gnu.org>
- added THANKS file as doc

* Thu Jan  4 2001 Herbert Valerio Riedel <hvr@gnu.org>
- fixed removal of info pages on updating packages

* Sat Dec 23 2000 Herbert Valerio Riedel <hvr@gnu.org>
- added vcdrip
- removed glib dependancy

* Sat Aug 26 2000 Herbert Valerio Riedel <hvr@gnu.org>
- spec file improvements

* Mon Aug 14 2000 Herbert Valerio Riedel <hvr@gnu.org>
- first spec file

