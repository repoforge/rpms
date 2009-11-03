# $Id$
# Authority: dag

Summary: Lossless volume-adjusting utility for Ogg Vorbis files
Name: vorbisgain
Version: 0.36
Release: 2.2%{?dist}
License: LGPL
Group: Applications/Multimedia
URL: http://sjeng.org/vorbisgain.html

Source: http://sjeng.org/ftp/vorbis/vorbisgain-%{version}.zip
Patch: vorbisgain-0.36-double-fclose.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libogg, libogg-devel, libvorbis, libvorbis-devel
Requires: libogg, libvorbis

%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It is meant as a replacement for the normalization that is commonly used
before encoding. Although normalization will ensure that each song has the
same peak volume, this unfortunately does not say anything about the apparent
loudness of the music, with the end result being that many normalized files
still don't sound equally loud. VorbisGain uses psychoacoustics to address
this deficiency. Moreover, unlike normalization, it's a lossless procedure
which works by adding tags to the file. Additionally, it will add hints that
can be used to prevent clipping on playback. It is based upon the ReplayGain
technology.

%prep
%setup
%patch -p1

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS README vorbisgain.txt
%doc %{_mandir}/man1/vorbisgain.1*
%{_bindir}/vorbisgain

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.36-2.2
- Rebuild for Fedora Core 5.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 0.3.6-2
- Added patch fo a double free condition. (Noa Resare)

* Wed Jul 20 2005 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Updated to release 0.3.6.
