# $Id$
# Authority: dag

Summary: Library for supporting Open Financial Exchange (OFX)
Name: libofx
Version: 0.9.1
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://libofx.sourceforge.net/

Source: http://dl.sf.net/libofx/libofx-%{version}.tar.gz
Patch1: libofx-assorted-c++-fu.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel
BuildRequires: opensp-devel
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
This is the LibOFX library.  It is a API designed to allow applications to
very easily support OFX command responses, usually provided by financial
institutions.  See http://www.ofx.net/ofx/default.asp for details and
specification.

%package -n ofx
Summary: Tools for manipulating OFX data
Group: Applications/Productivity
Requires: %{name} = %{version}-%{release}

%description -n ofx
The ofx package contains tools for manipulating OFX data from the
command line; they are often used when testing libofx.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: opensp-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch1 -p1 -b .c++-fu

%{__rm} -rf ./doc/ofx_sample_files/CVS
%{__chmod} 0644 ./doc/ofx_sample_files/*

%build
%configure \
    --disable-rpath \
    --disable-static \
    --with-opensp-libs="%{_libdir}"
%{__perl} -pi.orig -e '
        s|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g;
    ' libtool
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README totest.txt
%{_datadir}/libofx/
%{_libdir}/libofx.so.*

%files -n ofx
%defattr(-, root, root, 0755)
%{_bindir}/ofx2qif
%{_bindir}/ofxdump

%files devel
%defattr(-, root, root, 0755)
%doc doc/html doc/ofx_sample_files
%{_includedir}/libofx/
%{_libdir}/libofx.so
%{_libdir}/pkgconfig/libofx.pc
%exclude %{_libdir}/libofx.la

%changelog
* Thu Mar 24 2011 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
