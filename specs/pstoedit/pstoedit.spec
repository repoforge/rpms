# $Id$
# Authority: dag

### EL6 ships with pstoedit-3.45-10.el6
%{?el6:# Tag: rfx}

Summary: Translates PostScript and PDF graphics into other vector formats
Name: pstoedit
Version: 3.50
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://www.pstoedit.net/

Source: http://dl.sf.net/pstoedit/pstoedit-%{version}.tar.gz
#Patch0: pstoedit-3.44-cxxflags.patch
#Patch1: pstoedit-3.44-quiet.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gd-devel, libpng-devel, libEMF-devel
BuildRequires: ImageMagick-c++-devel, plotutils-devel
BuildRequires: dos2unix, ghostscript
Requires: ghostscript

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ImageMagick-c++-devel
Requires: libpng-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
#patch0 -p1 -b .cxxflags
#patch1 -p1 -b .quiet
dos2unix doc/*.htm doc/readme.txt

%build
%configure \
	--disable-static \
	--with-emf \
	--without-swf
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 doc/pstoedit.1 %{buildroot}%{_mandir}/man1/pstoedit.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc copying doc/*.htm doc/*.txt
%doc %{_mandir}/man1/pstoedit.1*
%{_bindir}/pstoedit
%{_datadir}/pstoedit/
%{_libdir}/libpstoedit.so.*
%{_libdir}/pstoedit/

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/pstoedit.m4
%{_includedir}/pstoedit/
%{_libdir}/libpstoedit.so
%{_libdir}/pkgconfig/pstoedit.pc
%exclude %{_libdir}/libpstoedit.la

%changelog
* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 3.50-1
- Updated to release 3.50.

* Mon Sep 10 2007 Dries Verachtert <dries@ulyssis.org> - 3.45-1
- Updated to release 3.45.

* Thu May 24 2007 Dag Wieers <dag@wieers.com> - 3.44-1
- Initial package. (using DAR)
