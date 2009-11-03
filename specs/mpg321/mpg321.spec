# $Id$
# Authority: matthias

Summary: MPEG audio player
Name: mpg321
Version: 0.2.10
Release: 8%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mpg321.sourceforge.net/
Source: http://dl.sf.net/mpg321/mpg321-%{version}.tar.gz
Patch: mpg321-0.2.10-printf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libao-devel >= 0.8.0, libmad-devel >= 0.14.2b, libid3tag-devel
BuildRequires: zlib-devel
Obsoletes: mpg123 < %{version}

%description
mpg321 is a Free replacement for mpg123, a very popular command-line mp3
player. mpg123 is used for frontends, as an mp3 player and as an mp3 to
wave file decoder (primarily for use with CD-recording software.) In all
of these capacities, mpg321 can be used as a drop-in replacement for
mpg123.


%prep
%setup
%patch -p1 -b .printf


%build
%configure --with-default-audio="alsa"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING HACKING NEWS README* THANKS TODO
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.2.10-8
- Release bump to drop the disttag number in FC5 build.

* Mon Sep 19 2005 Matthias Saou <http://freshrpms.net/> 0.2.10-7
- Change default audio from esd to alsa.

* Mon Jul  4 2005 Matthias Saou <http://freshrpms.net/> 0.2.10-6
- Include printf patch to fix CAN-2003-0969 (Jens Koerber).

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.2.10-5
- Rebuild for Fedora Core 2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.2.10-4
- Rebuild for Fedora Core 1.

* Mon Jul 21 2003 Matthias Saou <http://freshrpms.net/>
- Update libmad-devel and libid3tag-devel build deps.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Sep 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.10.
- Spec file cleanup.

* Tue Apr  9 2002 Bill Nottingham <notting@redhat.com> 0.2.9-3
- add patch from author to fix id3 segfaults (#62714)
- fix audio device fallback to match upstream behavior

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com> 0.2.9-2
- fix possible format string exploit
- add simple audio device fallback

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com> 0.2.9-1
- update to 0.2.9

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- update to 0.2.3, libmad is now separate

* Mon Aug 13 2001 Bill Nottingham <notting@redhat.com>
- update to 0.1.5
- fix build with new libao

* Fri Jul 20 2001 Bill Nottingham <notting@redhat.com>
- initial build
