# Authority: freshrpms
Summary: An open-source, patent-free speech codec.
Name: speex
Version: 1.0.3
Release: 0
License: BSD
Group: System Environment/Libraries
URL: http://www.speex.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.speex.org/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libogg-devel
Obsoletes: libspeex <= 1.0

%description
Speex is a patent-free audio codec designed especially for voice (unlike 
Vorbis which targets general audio) signals and providing good narrowband 
and wideband quality. This project aims to be complementary to the Vorbis
codec.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: libspeex-devel <= 1.0

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--enable-shared \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/manual.pdf
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Updated to release 1.0.3.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Mon Mar 24 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
