# Authority: freshrpms
Summary: Fast Assembly MPEG Encoding library.
Name: libfame
Version: 0.9.0
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://fame.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:	http://prdownloads.sourceforge.net/fame/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
A library for fast (real-time) MPEG video encoding, written in C and assembly.
It currently allows encoding of fast MPEG-1 video, as well as MPEG-4 (OpenDivX
compatible) rectangular and arbitrary shaped video.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_includedir}/libfame/
%{__ln_s} -f %{_includedir}/fame.h %{buildroot}%{_includedir}/libfame/

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
%doc AUTHORS BUGS CHANGES README TODO 
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/libfame/
%{_datadir}/aclocal/*
#exclude %{_libdir}/*.la

%changelog
* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Added link for compatibility.

* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Initial package.
