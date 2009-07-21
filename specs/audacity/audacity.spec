# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_flac 1}

%{?el3:%define _without_alsa 1}
%{?el3:%define _without_flac 1}
%{?el3:%define _without_soundtouch 1}

Summary: Multitrack audio editor
Name: audacity
Version: 1.3.4
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://audacity.sourceforge.net/

Source: http://dl.sf.net/audacity/audacity-src-%{version}.tar.bz2
Patch0: audacity-1.3.4-portaudio.patch
Patch1: audacity-1.3.4-libmp3lame-default.patch
Patch2: audacity-1.3.4-libdir.patch
Patch3: audacity-1.3.5-gcc43.patch
Patch4: audacity-1.3.5-fr.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
%{!?_without_flac:BuildRequires: flac-devel}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: ladspa-devel
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel
BuildRequires: libogg-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
%{!?_without_soundtouch:BuildRequires: soundtouch-devel}
BuildRequires: zip
BuildRequires: zlib-devel
BuildRequires: wxGTK-devel >= 2.6.0

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
%patch0 -p1
### Substitute hardcoded library paths.
%patch1 -p1
%patch2 -p1
for file in src/effects/ladspa/LoadLadspa.cpp src/export/ExportMP3.cpp src/AudacityApp.cpp lib-src/libvamp/vamp-sdk/PluginHostAdapter.cpp
do
    %{__perl} -pi -e 's|__RPM_LIBDIR__|%{_libdir}|g' $file
    %{__perl} -pi -e 's|__RPM_LIB__|%{_lib}|g' $file
done
grep -s __RPM_LIB * -R && exit 1

%patch3 -p1 -b .gcc43
%patch4 -p1 -b .fr

### Substitute occurences of "libmp3lame.so" with "libmp3lame.so.0".
%{__perl} -pi.orig -e 's|libmp3lame.so\([^.]\)|libmp3lame.so.0\1|g' locale/*.po src/export/ExportMP3.cpp

%{__perl} -pi -e 's|SoundTouch::||g;' ./lib-src/soundtouch/include/SoundTouch.h

%build
%configure \
    --with-help \
    --with-expat="system" \
    --with-id3tag="system" \
    --with-ladspa \
%{?_without_flac:--without-libflac} \
%{!?_without_flac:--with-libflac="system"} \
    --with-libmad="system" \
    --with-libsamplerate="system" \
    --with-libsndfile="system" \
    --with-portaudio="v18" \
%{?_without_soundtouch:--without-soundtouch} \
%{!?_without_soundtouch:--with-soundtouch="system"} \
    --with-vorbis="system" \
    --without-libresample
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

### Install the icon (not automatically done in 1.3.0)
%{__install} -D -m 0644 images/AudacityLogo.xpm %{buildroot}%{_datadir}/pixmaps/audacity.xpm

### Remove those two text files we include in %%doc instead (1.3.0)
%{__rm} %{buildroot}%{_docdir}/audacity/{LICENSE.txt,README.txt}


%clean
%{__rm} -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database -q || :

%postun
umask 022
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc LICENSE.txt README.txt
%doc %{_mandir}/man1/audacity.1*
%{_bindir}/audacity
%{_datadir}/applications/audacity.desktop
%{_datadir}/audacity/
%{_datadir}/mime/packages/audacity.xml
%{_datadir}/pixmaps/audacity.xpm

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 1.3.4-1
- Rebuild against wxGTK 2.8.10.
- Updated to release 1.3.4.

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

