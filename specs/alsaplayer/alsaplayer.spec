# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Audio player for systems using the Advanced Linux Sound Architecture
Name: alsaplayer
Version: 0.99.76
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.alsaplayer.org/
Source0: http://www.alsaplayer.org/alsaplayer-%{version}.tar.bz2
Source1: alsaplayer.png
Source2: alsaplayer-small.png
Source3: alsaplayer-large.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: alsa-lib-devel, esound-devel, gtk+-devel, libvorbis-devel
BuildRequires: flac-devel, libmad-devel, libid3tag-devel, libsndfile-devel
BuildRequires: zlib-devel, libstdc++-devel, mikmod
BuildRequires: gcc-c++, doxygen, desktop-file-utils
BuildRequires: xosd-devel

%description
AlsaPlayer is a new PCM player developed on the Linux Operating System. Since
the first public beta release it support has been added for various other
Operating Systems (mostly Unix variants). AlsaPlayer was written in the first
place to excercise the new ALSA (Advanced Linux Sound Architecture) driver and
library system.

It has now developed into a versitile audio player with rich plugin system.
The  Input Plugins plugins include: OGG, MPEG, MAD, CDDA, MikMod, and
Audiofile. The Output Plugins include: ALSA, OSS and OSS/Lite, Esound,
Sparc (tested on UltraSparc), SGI, and JACK. There are also a few scope
plugins included.

Install AlsaPlayer if you want a versatile audio player.


%prep
%setup


%build
%configure --enable-audiofile
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Install icons
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} \
    %{buildroot}%{_datadir}/pixmaps/

# System menu entry
%{__cat} << EOF > %{name}.desktop
[Desktop Entry]
Name=ALSA Player
Comment=Audio player for the Advanced Linux Sound Architecture
Icon=alsaplayer.png
Exec=alsaplayer
Terminal=false
Type=Application
Encoding=UTF-8
Category=Application;AudioVideo;
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  %{name}.desktop

# Clean up for the docs
%{__rm} -f examples/Makefile*
%{__rm} -rf %{buildroot}%{_docdir}/%{name}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/reference/html README TODO
%doc examples
%{_bindir}/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}*


%changelog
* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 0.99.76-2
- Added ldconfig calls since there are libs included.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.99.76-2
- Rebuild for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.99.76-1
- Update to 0.99.76.
- Rebuild for Fedora Core 1.
- Added missing gcc-c++ build dependency.

* Fri May  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.75.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Fix build order.

* Sat Feb  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.74.
- Added xosd support.

* Mon Jan 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.73.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New desktop entry.

* Wed Sep 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.72.
- Further spec file changes and fixes.

* Thu Sep  5 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup to match freshrpms.net habits :-)

* Sat Jul 6 2002 Angles <angles@aminvestments.com>
- version 0.99.71

* Thu May 30 2002 Angles <angles@aminvestments.com>
- version 0.99.70
- updated summary and description to highlight the apps increased versitility
- minor spec file cleanup and desktop link update to latest usage

* Sun May 5 2002 Angles <angles@aminvestments.com>
- version 0.99.60
- package now has include files
- package has 4 files in libdir that actually belong there, not in a subdir
- made patch so rpm installs docs, not the app make install

* Sat Apr 6 2002 Angles <angles@phpgroupware.org>
- version 0.99.58

* Wed Mar 20 2002 Angles <angles@phpgroupware.org>
- version 0.99.57

* Sat Mar 02 2002 Angles <angles@phpgroupware.org>
- version 0.99.54

* Sat Feb 23 2002 Angles <angles@phpgroupware.org> 0.99.53-aap4
- customize for RedHat 7.2

* Sat Feb 16 2002 Yves Duret <yduret@mandrakesoft.com> 0.99.53-1mdk
- version 0.99.53
- %%makeinstall_std

* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 0.99.52-1mdk
- version 0.99.52
- build against mad
- png icons

* Sat Dec 22 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99.50-3mdk
- fix BuildRequires

* Fri Dec  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.50-2mdk
- s|Copyright|License|;

* Fri Sep 28 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.50-1mdk
- 0.99.50.
- Add --enable-alsa --enable-esd --disable-debug --enable-oggvorbis.

* Fri Aug 24 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.36-1mdk
- 0.99.36.

* Sat Jun 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99.33-0.2mdk
- BuildRequires: gtk+-devel

* Fri Jun 15 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.33-0.1mdk
- 0.99.33-pre3.

* Fri Feb  9 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 0.99.32-13mdk
- Do not exclude alpha from build.

* Thu Dec  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-12mdk
- Recompile with alsa-0.5.10.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-11mdk
- Add icons.

* Sat Nov 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-10mdk
- fix gcc2.96 compilation.

* Thu Oct 24 2000 David BAUDENS <baudens@mandrakesoft.com> 0.99.32-9mdk
- EcludeArch: ppc

* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-8mdk
- remove some debugging messages

* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-7mdk
- build against latest alsa-lib
- fix requires

* Sun Aug 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.32-6mdk
- disabled the use of makeinstall macro in order to have the libraries installed
  in the correct place (reported by Anton Graham <darkimage@bigfoot.com>)
- cleaner specfile
- more menu dir macros

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.99.32-5mdk
- automatically added BuildRequires

* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-4mdk
- fix macros

* Tue Jun 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-3mdk
- macroszifications.
- build against latest alsa-lib
- Use macros for update-menus.

* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-2mdk
- build against latest alsa-lib
- add url

* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-1mdk
- new release

* Fri May 19 2000 Francis Galiegue <fg@mandrakesoft.com> 0.99.31-2mdk

- ExcludeArch: alpha sparc sparc64

* Sun Apr 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.31-1mdk
- Add menu entry.
- Fix Requires.
- Fix titi sucks.
- Build again latest alsa-lib and libmikmod.

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.31-2mdk
- fixed group

* Thu Mar 09 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 99.31
- compiled against alsa-lib-0.5.5

* Tue Aug 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec
