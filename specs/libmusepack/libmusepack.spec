# $Id$

Summary: Musepack audio decoding library
Name: libmusepack
Version: 1.0.2
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.musepack.net/
Source0: http://www.saunalahti.fi/grimmel/musepack.net/source/libmusepack-%{version}.zip
Source1: LGPL.txt
Patch: libmusepack-1.0.2-makefile.patch
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
%setup -c %{name}-%{version}
%patch -p0 -b .makefile


%build
# No autotools...
%{__make} %{?_smp_mflags} \
    libdir="%{_libdir}" \
    includedir="%{_includedir}" \
    CPPFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} %{?_smp_mflags} install \
    libdir="%{_libdir}" \
    includedir="%{_includedir}" \
    DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/musepack/
%{_libdir}/*.so


%changelog
* Fri Nov 26 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Initial RPM release.
- Include the mandatory copy of the LGPL (there is none in the sources...).

