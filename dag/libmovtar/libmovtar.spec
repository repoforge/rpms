# Authority: freshrpms
Summary: Tools for the movtar MJPEG video format.
Name: libmovtar
Version: 0.1.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/mjpeg/libmovtar-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: SDL-devel, glib-devel, libjpeg-mmx

%description
This package includes libmovtar, the support library, and various
tools which together implement the movtar MJPEG video format.

%package devel
Summary: Development headers and libraries for the movtar MJPEG video format.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains static libraries and C system header files
needed to compile applications that use the movtar MJPEG video format.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_bindir}/movtar_*
%{_bindir}/pnm2rtj
%{_bindir}/rtjshow

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/movtar-config
%{_includedir}/*.h
%{_libdir}/*.a
%{_datadir}/aclocal/*

%changelog
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.1.3-0
- Split from earlier "mjpegtools" package.
- Initial package. (using DAR)
