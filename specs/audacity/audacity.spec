# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_alsa 1}
%{?el3:%define _without_alsa 1}
%{?rh9:%define _without_alsa 1}
%{?rh8:%define _without_alsa 1}
%{?yd3:%define _without_alsa 1}

Summary: Powerful audio editor
Name: audacity
Version: 1.3.0b
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://audacity.sourceforge.net/
Source: http://dl.sf.net/audacity/audacity-src-%{version}.tar.gz
Patch0: audacity-src-1.3.0-beta-localeinstall.patch
Patch1: audacity-src-1.3.0-beta-desktop.patch
Patch2: audacity-src-1.3.0b-beta-samplerate.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: wxGTK >= 2.6.0
BuildRequires: gcc-c++, zip, zlib-devel, gettext, desktop-file-utils
BuildRequires: wxGTK-devel >= 2.6.0, libogg-devel, libvorbis-devel
BuildRequires: libmad-devel, flac-devel, libsndfile-devel
BuildRequires: libsamplerate-devel, libid3tag-devel
BuildRequires: autoconf
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Audacity is a free audio editor. You can record sounds, play sounds, import
and export WAV, AIFF, and MP3 files, and more. Use it to edit your sounds
using Cut, Copy and Paste (with unlimited Undo), mix tracks together, or
apply effects to your recordings. It also has a built-in amplitude envelope
editor, a customizable spectrogram mode and a frequency analysis window for
audio analysis applications. Built-in effects include Bass Boost, Wahwah,
and Noise Removal, and it also supports VST plug-in effects.


%prep
%setup -n %{name}-src-%{version}-beta
%patch0 -p1 -b .localeinstall
%patch1 -p1 -b .desktop
%patch2 -p1 -b .samplerate
%{__perl} -pi -e 's|SoundTouch::||g;' ./lib-src/soundtouch/include/SoundTouch.h

%build
%configure \
    --with-libsndfile="system" \
    --with-libsamplerate="system" \
    --with-portaudio="v18"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Install the icon (not automatically done in 1.3.0)
%{__install} -D -m 0644 images/AudacityLogo.xpm \
    %{buildroot}%{_datadir}/pixmaps/audacity.xpm

# Remove those two text files we include in %%doc instead (1.3.0)
%{__rm} %{buildroot}%{_docdir}/audacity/{LICENSE.txt,README.txt}


%clean
%{__rm} -rf %{buildroot}


%post
update-desktop-database -q || :

%postun
update-desktop-database -q || :


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc LICENSE.txt README.txt
%{_bindir}/audacity
%{_datadir}/applications/audacity.desktop
%{_datadir}/audacity/
%{_datadir}/mime/packages/audacity.xml
%{_datadir}/pixmaps/audacity.xpm
%{_mandir}/man1/audacity.1*


%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.3.0b-2
- Rebuild against wxGTK 2.8.8.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.3.0b-1
- Update to 1.3.0b.
- Explicitely pass --with-libsamplerate since libresample is used otherwise.
- Include patch to correct the version of libsamplerate being checked.

* Wed Nov 30 2005 Matthias Saou <http://freshrpms.net/> 1.3.0-1
- Update to 1.3.0, the wxGTK 2.6.x compatible development branch.
- Include patch to fix the locale installation (weird...).
- Include patch to fix the strange characters in the desktop file.
- Use the now included desktop file, but its ref to the image is broken,
  fixed in the desktop patch + "manually" install the xpm.
- The docs currently no longer include "help", so include the usual way.
- Add update-desktop-database scriplets for the mime types.

* Thu Nov 25 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-2
- Move back from postaudio v19 to v18 for now, as v19 has too many issues :-(
  (leave no longer relevant deps as-is, for later switching back to v19).

* Sat Nov 20 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Added libid3tag and libsamplerate support.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.

* Tue Jun 01 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-1
- Got 1.2.1 to build at last by running autoconf in the portaudio-v19 dir.

* Tue Mar  2 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-2
- Recompile with ALSA support (should be near stable now).

* Tue Mar  2 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0 final.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-0.pre3.2
- Rebuild against gtk+ wxGTK to fix crashes with the gtk2 version.

* Thu Nov 13 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-0.pre3.1
- Update to 1.2.0pre3.
- Added find_lang macro.
- Updated the menu entry.
- Added libmad, flac and libsndfile support.
- Rebuild for Fedora Core 1.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

