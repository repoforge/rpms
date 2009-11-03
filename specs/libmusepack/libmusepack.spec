# $Id$
# Authority: matthias

Summary: Musepack audio decoding library
Name: libmusepack
Version: 1.1.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.musepack.net/
Source: http://www.saunalahti.fi/grimmel/musepack.net-files/source/libmusepack-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

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
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/html/*
%{_includedir}/musepack/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
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

