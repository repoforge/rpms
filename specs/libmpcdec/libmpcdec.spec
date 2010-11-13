# $Id$
# Authority: dag

### EL6 ships with libmpcdec-1.2.6-6.1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Musepack audio decoding library
Name: libmpcdec
Version: 1.2.6
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.musepack.net/

Source: http://files2.musepack.net/source/libmpcdec-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#BuildRequires: autoconf >= 2.58

%description
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller
MPC file.
It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed
and vastly improved and is now at an advanced stage in which it contains
heavily optimized and patentless code.

%package devel
Summary: Development files for the Musepack audio decoding library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller
MPC file.
It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed
and vastly improved and is now at an advanced stage in which it contains
heavily optimized and patentless code.

%prep
%setup

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libmpcdec.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/mpcdec/
%{_libdir}/libmpcdec.so
%exclude %{_libdir}/libmpcdec.la

%changelog
* Mon Dec 17 2007 Dag Wieers <dag@wieers.com> - 1.2.6-1
- Updated to release 1.2.6.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.2.2-2
- Release bump to drop the disttag number in FC5 build.

* Fri Jan 13 2006 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.

* Mon May  9 2005 Matthias Saou <http://freshrpms.net/> 1.2-1
- Update to 1.2 and rename to libmpcdec.
- Don't obsolete libmusepack just yet, wait for apps to use this new lib.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.1.1-1
- Update to 1.1.1, that's a lot of 1's :-)

* Wed Feb 23 2005 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.
- Switch build to use autotools as it's now possible.
- Remove no longer needed Makefile patch.
- Change License to BSD, as the new included COPYING is definitely BSD.

* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Initial RPM release.
- Include the mandatory copy of the LGPL (there is none in the sources...).
