# $Id$
# Authority: matthias

%define real_version 0.15.1b

Summary: MPEG audio decoder library
Name: libmad
Version: 0.15.1
Release: 0.b
License: GPL
Group: System Environment/Libraries
URL: http://www.underbit.com/products/mad/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.mars.org/pub/mpeg/libmad-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Provides: mad = %{version}-%{release}

%description
MAD (libmad) is a high-quality MPEG audio decoder. It currently supports
MPEG-1 and the MPEG-2 extension to Lower Sampling Frequencies, as well as
the so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.
 
MAD does not yet support MPEG-2 multichannel audio (although it should be
backward compatible with such streams) nor does it currently support AAC.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >mad.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: mad
Description: MPEG Audio Decoder
Requires:
Version: %{real_version}
Libs: -L%{_libdir} -lmad -lm
Cflags: -I%{_includedir}
EOF

%build
%configure \
	--disable-dependency-tracking \
	--disable-debugging \
	--enable-accuracy
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0644 mad.pc %{buildroot}%{_libdir}/pkgconfig/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 0.15.1-0.b
- Updated to release 0.15.1b.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 0.15.0-0.b
- Taken from Matthias Saou (FreshRPMS) for compatibility.
- Added mad.pc (needed for gstreamer-plugins).

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.15.0b.
- Split a devel package.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Added mad provides.

* Fri Sep 27 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuild for Red Hat Linux 8.0 (missing because of license issues).
- Spec file cleanup.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com> 0.14.2b-3
- ship libid3tag too

* Thu Feb 21 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Mon Jan 28 2002 Bill Nottingham <notting@redhat.com>
- split libmad off into a separate package

