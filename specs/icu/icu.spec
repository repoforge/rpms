# $Id$
# Authority: dag

### RHEL5 already ships with icu 3.6
# ExclusiveDist: el2 rh7 rh9 el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh9:%define _without_doxygen13 1}
%{?rh7:%define _without_doxygen13 1}
%{?el2:%define _without_doxygen13 1}

%define real_name icu4c
%define real_version 3_6

Summary: International Components for Unicode
Name: icu
Version: 3.6
Release: 1%{?dist}
License: X License
Group: System Environment/Libraries
URL: http://www.ibm.com/software/globalization/icu/

Source0: ftp://ftp.software.ibm.com/software/globalization/icu/%{version}/icu4c-%{real_version}-src.tgz
Source1: icu-config
Patch1: icu-3.4-multiarchdevel.patch
Patch3: icu.icu5365.dependantvowels.patch
Patch4: icu.icu5418.malayam.patch
Patch5: icu.icu5431.malayam.patch
Patch6: icu.icu5433.oriya.patch
Patch7: icu.icuXXXX.virama.prevnext.patch
Patch8: icu.icu5465.telegu.patch
Patch9: icu.icu5488.assamese.patch
Patch10: icu.icu5500.devicetablecrash.patch
Patch11: icu.icu5501.sinhala.biggerexpand.patch
Patch12: icu.icu5557.safety.patch
Patch13: icu.icu5506.multiplevowels.patch
Patch14: icu.icu5594.gujarati.patch
Patch15: icu.icuXXXX.malayalam.bysyllable.patch
Patch16: icu.regexp.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{!?_without_doxygen13:BuildRequires: doxygen >= 1.3}

%description
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU. It does not
contain any of the data files needed at runtime and present in the `icu'
and `icu-locales` packages.

%package -n libicu
Summary: International Components for Unicode
Group: System Environment/Libraries

%description -n libicu
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU. It does not
contain any of the data files needed at runtime and present in the `icu'
and `icu-locales` packages.

%package -n libicu-devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: libicu = %{version}-%{release}
Requires: pkgconfig

%description -n libicu-devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n libicu-doc
Summary: Development documentation for %{name}
Group: Documentation

%description -n libicu-doc
This package contains the development documentation for %{name}.

%prep
%setup -n %{name}
%patch1 -p1 -b .multiarchdevel
%patch3 -p1 -b .dependantvowels
%patch4 -p1 -b .icu5418.malayam.patch
%patch5 -p1 -b .icu5431.malayam.patch
%patch6 -p1 -b .icu5433.oriya.patch
%patch7 -p1 -b .icuXXXX.virama.prevnext.patch
%patch8 -p1 -b .icu5465.telegu.patch
%patch9 -p1 -b .icu5488.assamese.patch
%patch10 -p1 -b .icu5500.devicetablecrash.patch
%patch11 -p1 -b .icu5501.sinhala.biggerexpand.patch
%patch12 -p1 -b .icu5557.safety.patch
%patch13 -p1 -b .icu5506.multiplevowels.patch
%patch15 -p1 -b .icuXXXX.malayalam.bysyllable.patch
%patch16 -p1 -b .regexp.patch

%build
cd source
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
autoconf
%configure \
    --disable-samples \
    --with-data-packaging="library"
%{__make} #%{?_smp_mflags}
%{__make} doc || :

%install
%{__rm} -rf %{buildroot}
%{__make} -C source install DESTDIR="%{buildroot}"
%{__make} -C source install-doc docdir="rpm-doc" || :
%{__chmod} +x %{buildroot}%{_libdir}/*.so.*
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_bindir}/icu-config

%{__perl} -pi -e '
        s|\$\(THREADSCXXFLAGS\)||;
        s|\$\(THREADSCPPFLAGS\)|-D_REENTRANT|;
    ' %{buildroot}%{_libdir}/pkgconfig/icu.pc

%post -n libicu -p /sbin/ldconfig
%postun -n libicu -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.html readme.html
%doc %{_mandir}/man1/derb.1*
%doc %{_mandir}/man1/genbrk.1*
%doc %{_mandir}/man1/gencnval.1*
%doc %{_mandir}/man1/genctd.1*
%doc %{_mandir}/man1/genrb.1*
%doc %{_mandir}/man1/makeconv.1*
%doc %{_mandir}/man1/pkgdata.1*
%doc %{_mandir}/man1/uconv.1*
%doc %{_mandir}/man8/*.8*
%{_bindir}/derb
%{_bindir}/genbrk
%{_bindir}/gencnval
%{_bindir}/genctd
%{_bindir}/genrb
%{_bindir}/makeconv
%{_bindir}/pkgdata
%{_bindir}/uconv
%{_sbindir}/*

%files -n libicu
%defattr(-, root, root, 0755)
%doc license.html
%{_libdir}/*.so.*

%files -n libicu-devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/icu-config.1*
%{_bindir}/icu-config
%{_datadir}/icu/
%{_includedir}/layout/
%{_includedir}/unicode/
%{_libdir}/*.so
%{_libdir}/icu/
%{_libdir}/pkgconfig/icu.pc

%if %{!?_without_doxygen13:1}0
%files -n libicu-doc
%defattr(-, root, root, 0755)
%doc source/rpm-doc/icu/html/*
%endif

%changelog
* Sun Jul 13 2008 Dag Wieers <dag@wieers.com> - 3.6-1
- Updated to release 3.6.
- Included Fedora patches.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Fixed a typo in the dependencies "libuci" should be "libicu". (Daniel Demus)

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 2.6.2-0
- Initial package. (using DAR)
