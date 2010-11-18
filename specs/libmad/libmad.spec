# $Id$
# Authority: matthias

### EL2 ships with libmad-0.14.2b-3
# ExcludeDist: el2

Summary: MPEG audio decoding library
Name: libmad
Version: 0.15.1b
Release: 4%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.underbit.com/products/mad/

Source: ftp://ftp.mars.org/pub/mpeg/libmad-%{version}.tar.gz
Patch0: libmad-0.15.1b-multiarch.patch
Patch1: libmad-0.15.1b-ppc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
Provides: mad = %{version}-%{release}

%description
MAD (libmad) is a high-quality MPEG audio decoder. It currently supports
MPEG-1 and the MPEG-2 extension to Lower Sampling Frequencies, as well as
the so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

MAD does not yet support MPEG-2 multichannel audio (although it should be
backward compatible with such streams) nor does it currently support AAC.

%package devel
Summary: Header and library for developing programs that will use libmad
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
MAD (libmad) is a high-quality MPEG audio decoder. It currently supports
MPEG-1 and the MPEG-2 extension to Lower Sampling Frequencies, as well as
the so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

This package contains the header file as well as the static library needed
to develop programs that will use libmad for mpeg audio decoding.

%prep
%setup
%patch0 -p1 -b .multiarch
%patch1 -p1 -b .ppc

### Disable -fforce-mem to compile with gcc44
sed -i -e "/-fforce-mem/d" configure*

# Create an additional pkgconfig file
%{__cat} <<EOF >mad.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: mad
Description: MPEG Audio Decoder
Requires:
Version: %{version}
Libs: -L%{_libdir} -lmad -lm
Cflags: -I%{_includedir}
EOF

%build
%configure \
    --disable-debugging \
    --disable-dependency-tracking \
    --disable-static \
%ifarch x86_64 ia64 ppc64
    --enable-fpm="64bit" \
%endif
    --enable-accuracy
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 mad.pc %{buildroot}%{_libdir}/pkgconfig/mad.pc

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/libmad.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mad.h
%{_libdir}/libmad.so
%{_libdir}/pkgconfig/mad.pc
%exclude %{_libdir}/libmad.la

%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.15.1b-4
- Release bump to drop the disttag number in FC5 build.

* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 0.15.1b-3
- Added missing /sbin/ldconfig calls.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 0.15.1b-2
- Rebuilt for Fedora Core 2.
- Added pkgconfig dependency to the devel package.

* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 0.15.1b-1
- Update to 0.15.1b.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.15.0b-3
- Rebuild for Fedora Core 1.

* Thu Aug 28 2003 Matthias Saou <http://freshrpms.net/>
- Added mad.pc required by gstreamer-plugins.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.15.0b.
- Split a devel package.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added mad provides.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Rebuild for Red Hat Linux 8.0 (missing because of license issues).
- Spec file cleanup.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com> 0.14.2b-3
- ship libid3tag too

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- split libmad off into a separate package

