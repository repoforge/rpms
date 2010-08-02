# $Id$
# Authority: dag

### RHEL5 already ships with xz-4.999.9-0.3.beta.20091007git
# ExclusiveDist: el3 el4

%define git_date 20091007

Summary: LZMA compression utilities
Name: xz
Version: 4.999.9
Release: 0.2.beta.%{git_date}git%{?dist}
License: LGPLv2+
Group: Applications/File
URL: http://tukaani.org/xz/

Source: http://tukaani.org/xz/xz-%{version}beta.%{git_date}git.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: xz-libs = %{version}-%{release}

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package libs
Summary: Libraries for decoding LZMA compression
Group: System Environment/Libraries

%description libs
Libraries for decoding files compressed with LZMA or XZ utils.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package lzma-compat
Summary: Older LZMA format compatibility binaries
Group: Development/Libraries
License: GPLv2+ and LGPLv2+
Requires: %{name} = %{version}-%{release}
Obsoletes: lzma < 5
Provides: lzma = 5

%description  lzma-compat
The lzma-compat package contains compatibility links for older
commands that deal with the older LZMA format.

%prep
%setup -n %{name}-%{version}beta
%{__perl} -pi -e '
        s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g;
    ' libtool

%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" \
CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" \
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -p"

%check
LD_LIBRARY_PATH="$PWD/src/liblzma/.libs" %{__make} check

%clean
%{__rm} -rf %{buildroot}

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* README THANKS
%doc %{_mandir}/man1/*xz*
%{_bindir}/*xz*

%files libs
%defattr(-, root, root, 0755)
%doc COPYING.*
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/lzma/
%{_includedir}/lzma.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/liblzma.pc
%exclude %{_libdir}/*.la
%exclude %{_docdir}/xz/
#%exclude %{_libdir}/*.a
#%exclude %{_datadir}/locale/

%files lzma-compat
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/*lz*
%{_bindir}/*lz*

%changelog
* Tue Jul 20 2010 Dag Wieers <dag@wieers.com> - 4.999.9-0.3.beta.20091007
- Initial package. (using DAR)
