# $Id$
# Authority: leet

Summary: Fast, powerful, easy to use sound system
Name: fmod
Version: 3.75
%define real_version 375
Release: 1%{?dist}
License: FMOD Licence (free for non-commercial use)
Group: Development/Libraries
URL: http://www.fmod.org/

Source: http://www.fmod.org/files/fmodapi%{real_version}linux.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386

%description
FMOD is a fast, powerful, and easy to use sound system. It runs on
Windows, Linux, Windows CE, and now also on Macintosh, GameCube, PS2,
and XBox. FMOD supports 3d sound, midi, mods, mp3, ogg vorbis, wma, aiff,
recording, obstruction/occlusion, cd playback (analog or digital), cd ripping,
mmx, internet streaming, dsp effects, spectrum analysis, user created samples
and streams, synchronization support, ASIO, EAX 2&3, C/C++/VB/Delphi and more.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n fmodapi%{real_version}linux

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 api/libfmod-%{version}.so %{buildroot}%{_libdir}/libfmod-%{version}.so

%{__install} -d %{buildroot}%{_includedir}/fmod/
%{__cp} -auvx api/inc/*.h %{buildroot}%{_includedir}/fmod/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.TXT
%{_libdir}/*.so

%files devel
%defattr(-, root, root, 0755)
%doc documentation/* media/ samples/
%{_includedir}/fmod/

%changelog
* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 3.75-1
- Updated to release 3.75.

* Wed Oct 05 2005 Dag Wieers <dag@wieers.com> - 3.74.1-1
- Mostly cosmetic changes.

* Fri Sep 16 2005 C.Lee Taylor <leet@leenx.co.za>
- Update 3.74 and build for FC4

* Sun Oct 14 2004 Neil Zanella <nzanella@users.sourceforge.net>
- minor fixes

* Sun Oct 10 2004 Neil Zanella <nzanella@users.sourceforge.net>
- initial release
