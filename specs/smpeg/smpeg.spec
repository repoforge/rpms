# $Id$

# Authority: newrpms
Summary: MPEG library for SDL.
Name: smpeg
Version: 0.4.4
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://icculus.org/smpeg/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://sunsite.dk/pub/os/linux/loki/open-source/smpeg/%{name}-%{version}.tar.gz
Patch0: smpeg-0.4.4-gcc32.patch
Patch1: smpeg-0.4.4-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: SDL-devel, gtk+-devel
#BuildRequires: automake14
BuildRequires: automake, autoconf

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. SMPEG has
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -b .gcc32
%patch1 -b .fixes

%build
%{__automake} -a || %{__automake}-1.4 -a
%{__autoconf}
%configure \
	--disable-debug \
	--disable-opengl-player
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README TODO
%doc %{_mandir}/man[^3]/*
%{_bindir}/plaympeg
%{_bindir}/gtv
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/smpeg-config
%{_libdir}/*.a
%{_libdir}/*.so
%{_datadir}/aclocal/smpeg.m4
%{_includedir}/*
#exclude %{_libdir}/*.la

%changelog
* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 0.4.4-0
- Initial package. (using DAR)
