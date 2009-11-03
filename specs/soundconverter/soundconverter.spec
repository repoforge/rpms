# $Id$
# Authority: dag
# Upstream: Gautier Portet <kassoulet$gmail,com>

%define desktop_vendor rpmforge

Summary: Simple sound converter application
Name: soundconverter
Version: 1.4.4
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://soundconverter.berlios.de/

Source: http://download.berlios.de/soundconverter/soundconverter-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gstreamer-python >= 0.10
BuildRequires: intltool
BuildRequires: perl(XML::Parser)
BuildRequires: python-devel >= 2.3.3
Requires: gnome-python2-gconf
Requires: gstreamer-python >= 0.10
Requires: pygtk2
Requires: python >= 2.3.3

%description
soundconverter is a sound conversion application. It reads anything the
GStreamer library can read (Ogg Vorbis, AAC, MP3, FLAC, WAV, AVI, MPEG,
MOV, M4A, AC3, DTS, ALAC, MPC, Shorten, APE, SID, etc...), and writes
WAV, FLAC, MP3, AAC, and Ogg Vorbis files. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_mandir}/man1/soundconverter.1*
%{_bindir}/soundconverter
%{_datadir}/applications/soundconverter.desktop
%{_datadir}/icons/hicolor/scalable/apps/soundconverter.svg
%{_datadir}/icons/hicolor/*/apps/soundconverter.png
%{_datadir}/soundconverter/

%changelog
* Sat Jul 04 2009 Dag Wieers <dag@wieers.com> - 1.4.4-1
- Updated to release 1.4.4.

* Thu Apr 16 2009 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4.3.

* Tue Jan 27 2009 Dag Wieers <dag@wieers.com> - 1.4.2-1
- Updated to release 1.4.2.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 1.4.0-2
- Added patch to make soundconverter work on python 2.4.

* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Sun Aug 03 2008 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Updated to release 1.3.2.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Thu Jan 10 2008 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.

* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Jun 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sat Jan 07 2006 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Initial package. (using DAR)
