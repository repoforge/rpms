# $Id: flac.spec,v 1.1 2004/02/26 17:54:29 thias Exp $

%define xmmsinputdir %(xmms-config --input-plugin-dir)

Summary: An encoder/decoder for the Free Lossless Audio Codec
Name: flac
Version: 1.1.0
Release: 4.fr
License: GPL
Group: Applications/Multimedia
Source: http://dl.sf.net/flac/%{name}-%{version}.tar.gz
URL: http://flac.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libogg
BuildRequires: xmms-devel, id3lib-devel, libogg-devel, doxygen
# Actually, xmms-devel should requires gtk+-devel itself
BuildRequires: gtk+-devel
%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC is
similar to MP3, but lossless. The FLAC project consists of the stream format,
reference encoders and decoders in library form, flac, a command-line program
to encode and decode FLAC files, metaflac, a command-line metadata editor for
FLAC files and input plugins for various music players (the xmms plugin is
in a sub-package).


%package devel
Summary: Static libraries and header files from FLAC
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC is
similar to MP3, but lossless.

This package contains all the files needed to develop applications that
will use the Free Lossless Audio Codec.


%package -n xmms-flac
Summary: X MultiMedia System input plugin to play FLAC files
Group: Applications/Multimedia
Requires: xmms >= 0.9.5.1, id3lib, %{name} = %{version}
Obsoletes: flac-xmms <= 1.1.0

%description -n xmms-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC is
similar to MP3, but lossless.

This package contains an input plugin that enables playback of FLAC files in
xmms.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{xmmsinputdir}
%makeinstall xmmsinputplugindir=%{buildroot}%{xmmsinputdir}
find doc/ -name "Makefile*" -exec rm -f {} \;

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING* README doc
%{_bindir}/flac
%{_bindir}/metaflac
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4

%files -n xmms-flac
%defattr(-, root, root)
%exclude %{xmmsinputdir}/*.la
%{xmmsinputdir}/*.so

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.0-4.fr
- Rebuild for Fedora Core 1.
- Added gtk+-devel build dep for the xmms plugin to build.
- Renamed the flac-xmms sub-package to xmms-flac for consistency.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.
- Updated description.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Fix nasm dep to be only for ix86.

* Mon Jan 27 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.1.0.

* Sun Jan  5 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt against the latest id3lib for the xmms plugin.

* Thu Oct 10 2002 Matthias Saou <http://freshrpms.net/>
- Fixed location of include files, doh!

* Sat Sep 28 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Sep 25 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.4.
- Removed obsolete build patch, the xmms plugin builds cleanly at last!

* Thu Jul  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.3.

* Tue Apr 23 2002 Daniel Resare <noa@resare.com>
- Fixed plugin build when flac is not already installed

* Mon Apr  8 2002 Matthias Saou <http://freshrpms.net/>
- Replaced the hard-coded xmms input path with an expansion.
- Fixed spec (License tag and redundant Group for devel package).
- Fixed defattr for the xmms plugin.

* Sat Apr  6 2002 Daniel Resare <noa@resare.com>
- Update to 1.0.2.
- Splitted out xmms plugin to a separate subpackage.

* Tue Nov 20 2001 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Sun Oct 21 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.2 and added xmms dependency.

* Thu Aug 16 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.
- You cannot rebuild this SRPM easily if you want the xmms plugin.

