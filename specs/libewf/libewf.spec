# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define _sbindir /sbin

%{?el5:%define _without_fuse 1}
%{?el5:%define _without_libuuid 1}
%{?el5:%define _without_python25 1}

%{?el4:%define _without_libuuid 1}
%{?el4:%define _without_python25 1}

%{?el3:%define _without_fuse 1}
%{?el3:%define _without_libuuid 1}
%{?el3:%define _without_python25 1}

%{?el2:%define _without_fuse 1}
%{?el2:%define _without_libuuid 1}
%{?el2:%define _without_python25 1}

Summary: Library for the Expert Witness Compression Format (EWF)
Name: libewf
Version: 20100226
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.uitwisselplatform.nl/projects/libewf/

Source0: http://dl.sf.net/libewf/libewf-%{version}.tar.gz
Source1: http://dl.sf.net/libewf/mount_ewf-20090113.py
Patch0: libewf-20100226-pyver.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs-devel
%{!?_without_libuuid:BuildRequires: libuuid-devel}
BuildRequires: openssl-devel
BuildRequires: python-devel
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
%{!?_without_python25:Requires: fuse-python >= 0.2}
Requires: disktype

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
%setup
%patch0 -p1 -b .pyver

%build
%configure \
    --disable-static \
%{!?_without_python25:--enable-python} \
    --enable-wide-character-type
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%if %{!?_without_fuse:1}0
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}/sbin/mount.ewf
%{__ln_s} -f mount.ewf %{buildroot}/sbin/umount.ewf
%endif

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
%doc %{_mandir}/man1/ewfexport.1*
%doc %{_mandir}/man1/ewfinfo.1*
%doc %{_mandir}/man1/ewfverify.1*
%{_bindir}/ewfacquire
%{_bindir}/ewfacquirestream
%{_bindir}/ewfexport
%{_bindir}/ewfinfo
%{_bindir}/ewfverify
%if %{!?_without_fuse:1}0
%{_sbindir}/mount.ewf
%{_sbindir}/umount.ewf
%endif
%if %{!?_without_python25:1}0
%{python_sitearch}/pyewf.so
%exclude %{python_sitearch}/pyewf.la
%endif

%files devel
%defattr(-, root, root, 0755)
%dir %{_mandir}/man3/libewf.3*
%{_includedir}/libewf/
%{_includedir}/libewf.h
%{_libdir}/libewf.so
%{_libdir}/pkgconfig/libewf.pc

%changelog
* Sat Nov 20 2010 Dag Wieers <dag@wieers.com> - 20100226-1
- Updated to release 20100226.

* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 0.0.20080501-1
- Initial package. (using DAR)
