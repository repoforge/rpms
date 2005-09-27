# $Id$
# Authority: leet

Summary: A fast, powerful, easy to use sound system.
Name: fmod
Version: 3.74.1
Release: 0
License: FMOD Licence (free for non-commercial use)
Group: Development/Libraries
Source: http://www.fmod.org/files/fmodapi3741linux.tar.gz
URL: http://www.fmod.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
FMOD is a fast, powerful, and easy to use sound system. It runs on
Windows, Linux, Windows CE, and now also on Macintosh, GameCube, PS2,
and XBox. FMOD supports 3d sound, midi, mods, mp3, ogg vorbis, wma, aiff,
recording, obstruction/occlusion, cd playback (analog or digital), cd ripping,
mmx, internet streaming, dsp effects, spectrum analysis, user created samples
and streams, synchronization support, ASIO, EAX 2&3, C/C++/VB/Delphi and more.

%prep
%setup -n fmodapi3741linux

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 755 -o root -g root api/libfmod-3.74.1.so %{buildroot}/%{_libdir}/libfmod-3.74.1.so
cd api/inc
for i in *; do
  %{__install} -D -m 644 -o root -g root $i %{buildroot}/%{_includedir}/fmod/$i
done
cd ../..
for i in media/* samples/*/*; do
  %{__install} -D -m 644 -o root -g root $i %{buildroot}/%{_datadir}/fmod/$i
done
for i in samples/*/*; do
  %{__install} -D -m 644 -o root -g root $i %{buildroot}/%{_datadir}/fmod/$i
done
cd documentation
for i in * */*; do
  if ! [ -d $i ]; then
    %{__install} -D -m 644 -o root -g root $i %{buildroot}/%{_docdir}/fmod/$i
  fi
done
cd ..

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_libdir}/libfmod-3.74.1.so
%dir %{_includedir}/fmod
%{_includedir}/fmod/*
%dir %{_datadir}/fmod
%{_datadir}/fmod/*
%dir %{_docdir}/fmod
%{_docdir}/fmod/*

%changelog
* Fri Sep 16 2005 C.Lee Taylor <leet@leenx.co.za>
- Update 3.74 and build for FC4

* Sun Oct 14 2004 Neil Zanella <nzanella@users.sourceforge.net>
- minor fixes

* Sun Oct 10 2004 Neil Zanella <nzanella@users.sourceforge.net>
- initial release
