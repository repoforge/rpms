# $Id$
# Authority: matthias

#define prever         pre3
%define desktop_vendor freshrpms

Summary: Powerful audio editor
Name: audacity
Version: 1.2.1
Release: %{?prever:0.%{prever}.}1
License: GPL
Group: Applications/Multimedia
URL: http://audacity.sf.net/
Source: http://dl.sf.net/audacity/audacity-src-%{version}%{?prever:-%{prever}}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: wxGTK >= 2.4.0, libogg, libvorbis
Requires: libmad, flac, libsndfile
BuildRequires: gcc-c++, zip, zlib-devel, gettext, desktop-file-utils
BuildRequires: wxGTK-devel >= 2.4.0, libogg-devel, libvorbis-devel
BuildRequires: libmad-devel, flac-devel, libsndfile-devel, alsa-lib-devel
BuildRequires: autoconf

%description
Audacity is a free audio editor. You can record sounds, play sounds, import
and export WAV, AIFF, and MP3 files, and more. Use it to edit your sounds
using Cut, Copy and Paste (with unlimited Undo), mix tracks together, or
apply effects to your recordings. It also has a built-in amplitude envelope
editor, a customizable spectrogram mode and a frequency analysis window for
audio analysis applications. Built-in effects include Bass Boost, Wahwah,
and Noise Removal, and it also supports VST plug-in effects. 


%prep
%setup -n %{name}-src-%{version}%{?prever:-%{prever}}


%build
# This is required or the configure in that directory will fail (1.2.1)
(cd lib-src/portaudio-v19/ && autoconf)
%configure \
    --with-libsndfile=system \
    --with-portaudio=v19 \
    --without-portmixer
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Create a desktop entry
%{__cat} << EOF > %{name}.desktop
[Desktop Entry]
Name=Audacity Audio Editor
Comment=Audio editor to record, play sounds and import, export files
Icon=%{name}.xpm
Exec=%{name}
Terminal=false
Type=Application
EOF

# Complete the modifications
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications  \
    --add-category Application                  \
    --add-category AudioVideo                   \
    %{name}.desktop

# Install the image used in the desktop entry
%{__install} -D -m 644 images/AudacityLogo.xpm \
    %{buildroot}%{_datadir}/pixmaps/%{name}.xpm


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
# The help is actually in %{_docdir}/%{name} in order to be accessible directly
#doc LICENSE.txt README.txt help
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/*


%changelog
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

