# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: International Components for Unicode.
Name: icu24
Version: 2.4
Release: 0%{?dist}
License: X License
Group: System Environment/Libraries
URL: http://oss.software.ibm.com/icu/

Source: ftp://www-126.ibm.com/pub/icu/2.4/icu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}

%description
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU. It does not
contain any of the data files needed at runtime and present in the `icu'
and `icu-locales` packages.

%package -n libicu24
Summary: International Components for Unicode
Group: System Environment/Libraries

%description -n libicu24
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU. It does not
contain any of the data files needed at runtime and present in the `icu'
and `icu-locales` packages.

%package -n libicu24-devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: libicu = %{version}-%{release}

%description -n libicu24-devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using ICU,
you will need to install libicu-devel.

%prep
%setup -n icu-%{version}

%build
cd source
CFLAGS="-O3" \
CXXFLAGS="-O3" \
%configure \
	--disable-samples
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd source
%makeinstall

%post -n libicu24
/sbin/ldconfig 2>/dev/null

%postun -n libicu24
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.html readme.html
%doc %{_mandir}/man?/*
%{_sysconfdir}/icu/
%{_bindir}/*
%{_sbindir}/*
%dir %{_datadir}/icu/
%{_datadir}/icu/%{version}/mkinstalldirs

%files -n libicu24
%defattr(-, root, root, 0755)
%doc license.html
%{_libdir}/*.so.*

%files -n libicu24-devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/icu/%{version}/README
%dir %{_libdir}/icu/
%dir %{_datadir}/icu/
%{_includedir}/unicode/
%{_libdir}/*.so
%{_libdir}/icu/Makefile.inc
%{_libdir}/icu/%{version}/Makefile.inc
%{_datadir}/icu/%{version}/config/mh-linux

%changelog
* Fri Apr 02 2004 Bert de Bruijn <bert@debruijn.be> - 2.4-0
- new package for version 2.4

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 2.6.2-1
- Fixed a typo in the dependencies "libuci" should be "libicu". (Daniel Demus)

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 2.6.2-0
- Initial package. (using DAR)
