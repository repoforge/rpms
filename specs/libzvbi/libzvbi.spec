# $Id$

# Authority: dag

%define rname zvbi

Name: libzvbi
Summary: Raw VBI, Teletext and Closed Caption decoding library
Version: 0.2.4
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://zapping.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/zapping/zvbi-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


PreReq: /sbin/install-info
#Provides: %{rname}
Obsoletes: %{rname}

%description
Routines to access raw VBI capture devices (currently the V4L and
V4L2 API, and the *BSD bktr driver are supported), a versatile VBI
bit slicer, decoders for various data services and basic search,
render and export functions for Closed Caption and Teletext pages.

%package devel
Summary: Static library and API documentation of the VBI routines.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Static library and API documentation of the VBI routines.

%prep
%setup -n %{rname}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{rname}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{rname}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Initial package. (using DAR)
