# $Id$
# Authority: dag

Summary: PostScript Type 1 font rasterizer
Name: t1lib
Version: 5.1.0
Release: 1%{?dist}
License: LGPL
Group: Applications/Publishing
URL: ftp://sunsite.unc.edu/pub/Linux/libs/graphics/

Source: ftp://sunsite.unc.edu/pub/Linux/libs/graphics/t1lib-%{version}.tar.gz
Patch0: t1lib-5.0.0-manpages.patch
Patch1: t1lib-5.0.0-xglyph-env.patch
Patch2: t1lib-5.0.0-t1libconfig.patch
Patch3: t1lib-5.1.0-destdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
T1lib is a rasterizer library for Adobe Type 1 Fonts. It supports
rotation and transformation, kerning underlining and antialiasing. It
does not depend on X11, but does provides some special functions for
X11.

AFM-files can be generated from Type 1 font files and font subsetting
is possible.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
#%{__make} %{?_smp_mflags} without_doc
%{__make} %{?_smp_mflags}
%{__ln_s} README.t1lib-%{version} README

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 debian/t1libconfig %{buildroot}%{_sbindir}/t1libconfig

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/t1lib/
touch %{buildroot}%{_sysconfdir}/t1lib/FontDatabase
touch %{buildroot}%{_sysconfdir}/t1lib/t1lib.config

%{__install} -Dp -m0644 debian/type1afm.1 %{buildroot}%{_mandir}/man1/type1afm.1
%{__install} -Dp -m0644 debian/xglyph.1 %{buildroot}%{_mandir}/man1/xglyph.1
%{__install} -Dp -m0644 debian/FontDatabase.5 %{buildroot}%{_mandir}/man5/FontDatabase.5
%{__install} -Dp -m0644 debian/t1libconfig.8 %{buildroot}%{_mandir}/man8/t1libconfig.8

%{__rm} -rf %{buildroot}%{_datadir}/t1lib/

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
%{_sbindir}/t1libconfig --force &>/dev/null || :

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc Changes LGPL LICENSE README
%doc %{_mandir}/man*/*
%dir %{_sysconfdir}/t1lib
%ghost %{_sysconfdir}/t1lib/t1lib.config
%ghost %{_sysconfdir}/t1lib/FontDatabase
%{_bindir}/type1afm
%{_bindir}/xglyph
%{_libdir}/libt1.so.*
%{_libdir}/libt1x.so.*
%{_sbindir}/t1libconfig

%files devel
%defattr(-, root, root, 0755)
%doc doc/t1lib_doc.pdf
%{_includedir}/t1lib.h
%{_includedir}/t1libx.h
%{_libdir}/libt1.a
%{_libdir}/libt1x.a
%exclude %{_libdir}/libt1.la
%exclude %{_libdir}/libt1x.la
%{_libdir}/libt1.so
%{_libdir}/libt1x.so

%changelog
* Mon Jan 22 2007 Dag Wieers <dag@wieers.com> - 5.1.0-1
- Initial package. (using DAR)
