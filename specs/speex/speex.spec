# $Id$
# Authority: matthias

### EL6 ships with speex-1.2-0.12.rc1.1.el6
# ExclusiveDist: el2 el3

Summary: Open-source, patent-free speech codec
Name: speex
Version: 1.0.5
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.speex.org/

Source: http://downloads.us.xiph.org/releases/speex/speex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: libspeex = %{version}-%{release}
Obsoletes: libspeex <= 1.0.0
BuildRequires: libogg-devel, gcc-c++

%description
Speex is a patent-free audio codec designed especially for voice (unlike
Vorbis which targets general audio) signals and providing good narrowband
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package devel
Summary: Speex development files
Group: Development/Libraries
Provides: libspeex-devel = %{version}-%{release}
Requires: %{name} = %{version}

%description devel
Speex development files.

%prep
%setup

%build
export CFLAGS="%{optflags} -DRELEASE"
%configure \
	--enable-shared \
	--enable-static \
	--with-ogg-libraries="%{_libdir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR="%{buildroot} install"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/manual.pdf NEWS README
%{_bindir}/speexdec
%{_bindir}/speexenc
%{_libdir}/libspeex.so.*
%{_mandir}/man1/speexdec.1*
%{_mandir}/man1/speexenc.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_includedir}/speex/
%{_libdir}/libspeex.a
%exclude %{_libdir}/libspeex.la
%{_libdir}/libspeex.so
%{_libdir}/pkgconfig/speex.pc
%{_datadir}/aclocal/speex.m4

%changelog
* Wed Jul 21 2004 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Wed Jul 21 2004 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-3
- Rebuild for Fedora Core 2.

* Thu Nov 20 2003 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.2-2
- Rebuild for Fedora Core 1.

* Thu Sep 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.

* Wed Aug 13 2003 Matthias Saou <http://freshrpms.net/>
- Added libspeex provides and obsoletes.

* Thu Jul 24 2003 Matthias Saou <http://freshrpms.net/>
- Update (at last!) to 1.0.1 and rebuilt with mach.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Mon Mar 24 2003 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup.
- Now exclude .la file.

* Thu Oct 03 2002 Jean-Marc Valin
- Added devel package inspired from PLD spec file

* Tue Jul 30 2002 Fredrik Rambris <boost@users.sourceforge.net> 0.5.2
- Added buildroot and docdir and ldconfig. Makes it builadble by non-roots
  and also doesn't write to actual library paths when building.

