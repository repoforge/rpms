# $Id$
# Authority: matthias

Summary: VideoCD (pre-)mastering and ripping tool
Name: vcdimager
Version: 0.7.14
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.vcdimager.org/
Source: http://www.vcdimager.org/pub/vcdimager/vcdimager-0.7_UNSTABLE/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libxml2-devel >= 2.3.8, zlib-devel, pkgconfig, popt

%description 
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

VCDRip, which comes with VCDImager, does the reverse operation. That
is, ripping mpeg streams from images (and already burned VideoCDs)
and showing some information about the VideoCD.


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


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS FAQ TODO COPYING ChangeLog INSTALL NEWS README THANKS
%{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/*


%changelog
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

