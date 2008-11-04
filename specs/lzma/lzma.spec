# $Id$
# Authority: dag

Summary: Tools related to LZMA compression
Name: lzma
Version: 4.32.7
Release: 1
License: GPL
Group: Applications/File
URL: http://tukaani.org/lzma/

Source: http://tukaani.org/lzma/lzma-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: lzma-libs = %{version}-%{release}

%description
LZMA provides very high compression ratio and fast decompression. The
core of the LZMA utils is Igor Pavlov's LZMA SDK containing the actual
LZMA encoder/decoder. LZMA utils add a few scripts which provide
gzip-like command line interface and a couple of other LZMA related
tools. 

%package libs
Summary: Libraries for decoding LZMA compression
Group: System Environment/Libraries
License: LGPL

%description libs
Libraries for decoding LZMA compression.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%configure --disable-static
%{__perl} -pi -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__perl} -pi -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* README THANKS
%doc %{_mandir}/man1/lzcat.1*
%doc %{_mandir}/man1/lzcmp.1*
%doc %{_mandir}/man1/lzdiff.1*
%doc %{_mandir}/man1/lzegrep.1*
%doc %{_mandir}/man1/lzfgrep.1*
%doc %{_mandir}/man1/lzgrep.1*
%doc %{_mandir}/man1/lzless.1*
%doc %{_mandir}/man1/lzma.1*
%doc %{_mandir}/man1/lzmadec.1*
%doc %{_mandir}/man1/lzmainfo.1*
%doc %{_mandir}/man1/lzmore.1*
%doc %{_mandir}/man1/unlzma.1*
%{_bindir}/lzcat
%{_bindir}/lzcmp
%{_bindir}/lzdiff
%{_bindir}/lzegrep
%{_bindir}/lzfgrep
%{_bindir}/lzgrep
%{_bindir}/lzless
%{_bindir}/lzma
%{_bindir}/lzmadec
%{_bindir}/lzmainfo
%{_bindir}/lzmore
%{_bindir}/unlzma

%files libs
%defattr(-, root, root, 0755)
%doc COPYING*
%{_libdir}/liblzmadec.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/lzmadec.h
%{_libdir}/liblzmadec.so
%exclude %{_libdir}/liblzmadec.la

%changelog
* Tue Nov 04 2008 Dag Wieers <dag@wieers.com> - 4.32.7-1
- Initial package. (using DAR)
