# Authority: freshrpms
# Upstream: <libmpeg2-devel@lists.sourceforge.net>

Summary: MPEG-2 and MPEG-1 decoding library and test program
Name: mpeg2dec
Version: 0.4.0
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://libmpeg2.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://libmpeg2.sourceforge.net/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: XFree86-devel, pkgconfig, SDL-devel

%description
A free library for decoding MPEG-2 and MPEG-1 video streams.

%package devel
Summary: Development files for mpeg2dec's libmpeg2
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
A free library for decoding MPEG-2 and MPEG-1 video streams.

This package contains files needed to build applications that use mpeg2dec's
libmpeg2.

%prep
%setup

%build
%configure \
	--enable-shared
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
%doc AUTHORS COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc doc/*.txt doc/*.c
%{_includedir}/mpeg2dec/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
#exclude %{_libdir}/*.la

%changelog
* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Updated to release 0.4.0.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.3.1-0
- Initial package. (using DAR)
