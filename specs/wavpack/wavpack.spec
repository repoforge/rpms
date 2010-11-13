# $Id$
# Authority: dag

### EL6 ships with wavpack-4.60-1.1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Completely open audiocodec
Name: wavpack
Version: 4.50.1
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://www.wavpack.com/

Source: http://www.wavpack.com/wavpack-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode. Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer unparalleled
performance and functionality.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README license.txt
%{_bindir}/wavpack
%{_bindir}/wvgain
%{_bindir}/wvunpack
%{_libdir}/libwavpack.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%{_includedir}/wavpack/
%{_libdir}/libwavpack.so
%{_libdir}/pkgconfig/wavpack.pc
%exclude %{_libdir}/libwavpack.la

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 4.50.1-1
- Initial package. (using DAR)
