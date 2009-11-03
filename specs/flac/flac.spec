# $Id$
# Authority: matthias

# ExcludeDist: fc2 fc3 el4
# Tag: test

%define xmms_inputdir %(xmms-config --input-plugin-dir)

Summary: Encoder/decoder for the Free Lossless Audio Codec
Name: flac
Version: 1.1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://flac.sourceforge.net/
Source: http://dl.sf.net/flac/flac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: flac-libs
BuildRequires: xmms-devel, id3lib-devel, libogg-devel, doxygen
# Actually, xmms-devel should be the one requiring gtk+-devel...
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
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{xmms_inputdir}
%makeinstall xmmsinputplugindir="%{buildroot}%{xmms_inputdir}"
find doc/ -name "Makefile*" -exec rm -f {} \;


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING* README doc
%{_bindir}/flac
%{_bindir}/metaflac
%{_libdir}/*.so.*
%{_mandir}/man1/flac.1*
%{_mandir}/man1/metaflac.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/*.m4
%exclude %{_libdir}/*.la

%files -n xmms-flac
%defattr(-, root, root, 0755)
%{xmms_inputdir}/libxmms-flac.so
%exclude %{xmms_inputdir}/libxmms-flac.la


%changelog
* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Fri Oct 01 2004 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 1.1.0-5
- Added obsoletes flac-libs from Dag's spec file.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.0-4
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

