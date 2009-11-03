# $Id$
# Authority: dag
# Upstream: Jed Wing <jedwin$ugcs,caltech,edu>

Summary: Library for dealing with Microsoft ITSS/CHM format files
Name: chmlib
Version: 0.40
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.jedrea.com/chmlib/

Source: http://www.jedrea.com/chmlib/chmlib-%{version}.tar.bz2
#Patch0: chmlib-0.31-morearchs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libtool, gcc-c++

%description
chmlib is a library for dealing with Microsoft ITSS/CHM format files.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
#patch0 -p1

%build
%configure --disable-static
# %{?_smp_mflags}
%{__make}  INSTALLPREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__install} -d -m0755 %{buildroot}%{_includedir}
%{__make} install DESTDIR="%{buildroot}" INSTALLPREFIX="%{_prefix}" libdir="%{_libdir}"
#%{__install} -Dp -m0755 chm_http %{buildroot}%{_bindir}/chm_http
#%{__install} -Dp -m0755 enum_chmLib %{buildroot}%{_bindir}/enum_chmLib
#%{__install} -Dp -m0755 enumdir_chmLib %{buildroot}%{_bindir}/enumdir_chmLib
#%{__install} -Dp -m0755 extract_chmLib %{buildroot}%{_bindir}/extract_chmLib
#%{__install} -Dp -m0755 test_chmLib %{buildroot}%{_bindir}/test_chmLib

### Fix library symlinks
#for lib in $(ls %{buildroot}%{_libdir}); do
#        %{__ln_s} -f $lib %{buildroot}%{_libdir}/${lib//%\.?}
#        %{__ln_s} -f $lib %{buildroot}%{_libdir}/${lib//%\.?\.?}
#done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
#%{_bindir}/chm_http
#%{_bindir}/enum_chmLib
#%{_bindir}/enumdir_chmLib
#%{_bindir}/extract_chmLib
#%{_bindir}/test_chmLib
%{_libdir}/libchm.so.*

%files devel
%defattr(-, root, root, 0755)
%doc ChmLib-ds6.zip
%{_libdir}/libchm.la
%{_libdir}/libchm.so
%{_includedir}/chm_lib.h
%{_includedir}/lzx.h

%changelog
* Sun May 24 2009 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Thu Jan 25 2007 Dag Wieers <dag@wieers.com> - 0.39-1
- Updated to release 0.39.

* Thu Nov 17 2005 Dries Verachtert <dries@ulyssis.org> - 0.37.4-1
- Updated to release 0.37.4.

* Mon Nov 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Fri Sep 09 2005 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Tue Jun 29 2004 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.31-0
- Initial package. (using DAR)
