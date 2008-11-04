# $Id$
# Authority: dag
# Upstream: Christian Grothoff <libextractor$cs,purdue,edu>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el5:%define _with_libtoolltdl 1}
%{?fc6:%define _with_libtoolltdl 1}
%{?fc5:%define _with_libtoolltdl 1}
%{?fc4:%define _with_libtoolltdl 1}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Meta-data extraction library
Name: libextractor
Version: 0.5.21
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://gnunet.org/libextractor/

Source: http://gnunet.org/libextractor/download/libextractor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvorbis-devel, libogg-devel, gcc-c++
BuildRequires: ImageMagick, python-devel, gettext, pkgconfig, bzip2-devel
BuildRequires: intltool, glib2-devel, libvorbis-devel, gtk2-devel
BuildRequires: ImageMagick-devel, ImageMagick-c++-devel, exiv2, mpeg2dec-devel
%{?_with_libtoolltdl:BuildRequires: libtool-ltdl-devel}

%description
libextractor is a simple library for meta-data extraction.
libextractor uses a plugin-mechanism that makes it easy to add support
for more file formats, allowing anybody to add new extractors quickly.

libextractor currently features meta-data extractors for  HTML, PDF, PS,
MP3, OGG, JPEG, GIF, PNG, TIFF, RPM, ZIP, REAL, RIFF (AVI), MPEG, QT
and ASF. It also detects many more MIME-types in a fashion similar to
the well-known "file" tool.  Furthermore, a generic extractor that
extracts dictionary words from binaries is included.  Supported
dictionaries are currently da, en, de, it and no.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-extractor
Summary: Python bindings to libextractor
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description -n python-extractor
Python bindings to libextractor.

%prep
%setup

%build
%configure \
    --disable-static \
    --with-pic \
    CFLAGS="-I/usr/include/exiv2"
%{__make} %{?_smp_mflags} datadir="%{_datadir}" pkgconfigdatadir="%{_libdir}/pkgconfig"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" datadir="%{_datadir}" pkgconfigdatadir="%{_libdir}/pkgconfig"
%find_lang %{name}

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/extract.info %{_infodir}/dir 2>/dev/null || :


%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/extract.info %{_infodir}/dir 2>/dev/null || :
fi

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_infodir}/extractor.info*
%doc %{_mandir}/man1/extract.1*
%{_bindir}/extract
%{_libdir}/libextractor.so.*
%{_libdir}/libextractor/
#%exclude %{_libdir}/libextractor/libextractor_*.a
%exclude %{_libdir}/libextractor/libextractor_*.la

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/libextractor.3*
%{_includedir}/extractor.h
#%{_libdir}/libextractor.a
%{_libdir}/libextractor.so
%{_libdir}/pkgconfig/libextractor.pc
%exclude %{_libdir}/libextractor.la

#%files -n python-extractor
#%defattr(-, root, root, 0755)
#%{python_sitearch}/extractor.so

%changelog
* Mon Nov 03 2008 Dag Wieers <dag@wieers.com> - 0.5.21-1
- Updated to release 0.5.21.

* Mon Jul 14 2008 Dag Wieers <dag@wieers.com> - 0.5.20c-1
- Updated to release 0.5.20c.

* Sun Apr 27 2008 Dag Wieers <dag@wieers.com> - 0.5.20b-1
- Updated to release 0.5.20b.

* Sun Jan 13 2008 Dag Wieers <dag@wieers.com> - 0.5.19a-1
- Updated to release 0.5.19a.

* Mon Jan 07 2008 Dag Wieers <dag@wieers.com> - 0.5.19-1
- Updated to release 0.5.19.

* Thu Dec 06 2007 Dag Wieers <dag@wieers.com> - 0.5.18a-1
- Updated to release 0.5.18a.

* Sun Mar 18 2007 Dag Wieers <dag@wieers.com> - 0.5.18-1
- Updated to release 0.5.18.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 0.5.17a-1
- Updated to release 0.5.17a.

* Mon Jan 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.5.17-1
- Updated to release 0.5.17.

* Sun Nov 12 2006 Dag Wieers <dag@wieers.com> - 0.5.16-1
- Updated to release 0.5.16.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 0.5.15-1
- Updated to release 0.5.15.

* Fri May 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.14-1
- Updated to release 0.5.14.

* Sun Apr 30 2006 Dag Wieers <dag@wieers.com> - 0.5.13-1
- Updated to release 0.5.13.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.12-1
- Updated to release 0.5.12.

* Sun Mar 12 2006 Dag Wieers <dag@wieers.com> - 0.5.11-1
- Updated to release 0.5.11.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.9-1
- Updated to release 0.5.9.

* Thu Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.8-1
- Updated to release 0.5.8.

* Thu Sep 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.5-1
- Updated to release 0.5.5.

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.3-1
- Updated to release 0.5.3.

* Thu Jul 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.2-1
- Updated to release 0.5.2.

* Wed Jul 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.1-1
- Updated to release 0.5.1.

* Sun May 22 2005 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 0.3.11-1
- Updated to release 0.3.11.

* Sun Oct 03 2004 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Updated to release 0.3.6.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
