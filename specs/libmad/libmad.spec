# $Id$

Summary: MPEG audio decoding library
Name: libmad
Version: 0.15.1b
Release: 1.fr
License: GPL
Group: System Environment/Libraries
URL: http://www.underbit.com/products/mad/
Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
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
Requires: %{name} = %{version}

%description devel
MAD (libmad) is a high-quality MPEG audio decoder. It currently supports
MPEG-1 and the MPEG-2 extension to Lower Sampling Frequencies, as well as
the so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

This package contains the header file as well as the static library needed
to develop programs that will use libmad for mpeg audio decoding.


%prep
%setup -q

%build
%configure --enable-accuracy --disable-debugging
make %{_smp_mflags}

cat << EOF > mad.pc
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

%install
rm -rf %{buildroot}
%makeinstall
install -m 644 -D mad.pc %{buildroot}%{_libdir}/pkgconfig/mad.pc

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 0.15.1b-1.fr
- Update to 0.15.1b.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.15.0b-3.fr
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

