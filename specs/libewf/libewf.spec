# $Id$
# Authority: dag

Summary: Library for the Expert Witness Compression Format (EWF)
Name: libewf
%define real_version 20080501
Version: 0.0.20080501
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.uitwisselplatform.nl/projects/libewf/

Source: http://www.uitwisselplatform.nl/frs/download.php/529/libewf-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01). 
Libewf allows you to read and write media information within the EWF files.

%package -n ewftools
Summary: Utilities for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Provides: %{name}-tools = %{version}-%{release}
Obsoletes: %{name}-tools <= %{version}-%{release}

%description -n ewftools
The ewftools package contains tools for %{name}.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: zlib-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%build
%configure \
    --disable-static \
    --enable-wide-character-type
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS
%{_libdir}/libewf.so.*
%exclude %{_libdir}/libewf.la

%files -n ewftools
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/ewfacquire.1*
%doc %{_mandir}/man1/ewfacquirestream.1*
#%doc %{_mandir}/man1/ewfalter.1*
%doc %{_mandir}/man1/ewfexport.1*
%doc %{_mandir}/man1/ewfinfo.1*
%doc %{_mandir}/man1/ewfverify.1*
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
%{_bindir}/ewfalter
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfverify

%files devel
%defattr(-, root, root, 0755)
%dir %{_mandir}/man3/*.3*
%{_includedir}/libewf/
%{_includedir}/libewf.h
%{_libdir}/libewf.so
%{_libdir}/pkgconfig/libewf.pc

%changelog
* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 0.0.20080501-1
Initial package. (using DAR)
