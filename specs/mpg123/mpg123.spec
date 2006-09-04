# $Id$
# Authority: matthias

%{!?audio:%define audio alsa}

Summary: MPEG audio player
Name: mpg123
Version: 0.60
Release: 1
License: GPL/LGPL
Group: Applications/Multimedia
URL: http://mpg123.org/
Source: http://mpg123.org/download/mpg123-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig
# We actually only need one, but it doesn't hurt to have them all
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: esound-devel
BuildRequires: SDL-devel
BuildRequires: nas-devel
BuildRequires: portaudio-devel
BuildRequires: alsa-lib-devel
Obsoletes: mpg321 <= 0.2.10-9

%description
Real time command line MPEG audio player for Layer 1, 2 and Layer3.

Available rpmbuild rebuild option :
--define 'audio {alsa,esd,jack,nas,oss,portaudio,sdl}'


%prep
%setup


%build
%configure \
    --enable-gapless=yes \
    --with-audio=%{audio}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/
%{_bindir}/mpg123
%{_mandir}/man1/mpg123.1*


%changelog
* Mon Sep  4 2006 Matthias Saou <http://freshrpms.net/> 0.60-1
- Update to 0.60 final.
- Add support for all available compatible outputs, unfortunately it's a build
  time choice, so default to alsa.
- Obsolete mpg321 up to the last know package version.

* Tue Jul 25 2006 Matthias Saou <http://freshrpms.net/> 0.60-0.1.beta2
- Initial RPM release, now that mpg123 is maintained again and went GPL/LGPL.
- Audio output type is not (yet?) plugin-based, so use libao (for ALSA).

