# Authority: freshrpms
Summary: Tools for recording, editing, playing and encoding mpeg video.
Name: mjpegtools
Version: 1.6.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://mjpeg.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://prdownloads.sourceforge.net/mjpeg/mjpegtools-%{version}.tar.gz
Source1: http://prdownloads.sourceforge.net/mjpeg/quicktime4linux-1.4-patched-2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: SDL-devel, libjpeg-devel, libpng-devel, gtk+-devel, libdv-devel
BuildRequires: avifile-devel, libmovtar-devel
BuildRequires: nasm

%description
The MJPEG-tools are a basic set of utilities for recording, editing, 
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -a 1

%build
cd quicktime4linux*
%configure
%{__make} %{?_smp_mflags}
cd -

%configure \
	--enable-large-file \
	--enable-cmov-extension \
	--enable-simd-accel \
	--with-quicktime="%{_builddir}/%{buildsubdir}/quicktime4linux"
%{?rh90:echo -e "\n#define LIBDV_PRE_0_9_5 1" >>config.h}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING HINTS PLANS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/divxdec
%{_bindir}/glav
%{_bindir}/jpeg2yuv
%{_bindir}/lav*
%{_bindir}/mp*
%{_bindir}/ppm*
%{_bindir}/testrec
%{_bindir}/y4m*
%{_bindir}/ypipe
%{_bindir}/yuv*
%{_bindir}/*.flt
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*-config
%{_includedir}/mjpegtools/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 1.6.1-1
- Put libmovtar and libjpeg-mmx in seperate packages.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.6.1-0
- Initial package.
