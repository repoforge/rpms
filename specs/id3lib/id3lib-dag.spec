# Authority: freshrpms
Summary: A software library for manipulating ID3v1 and ID3v2 tags.
Name: id3lib
Version: 3.8.3
Release: 0
License: LGPL
Group: System Environment/Libraries
URL: http://id3lib.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include 
standards-compliant ID3v1/2 tagging capabilities in their applications.  
Features include identification of valid tags, automatic size conversions, 
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities.

%package devel
Summary: Headers and libraries for developing programs that will use id3lib.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use id3lib, the software library for ID3v1 and ID3v2
tag manipulation.

%prep
%setup

%build
%configure --enable-debug="no"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean docs for inclusion
%{__rm} -f doc/Doxyfile* doc/Makefile* doc/*.in examples/Makefile*
%{__rm} -rf examples/.deps/ examples/.libs/

### Clean up buildroot
%{__rm}  -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HISTORY NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/ examples/
%{_includedir}/id3/
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 3.8.3-0
- Updated to release 3.8.3.

* Tue Feb 11 2003 Dag Wieers <dag@wieers.com> - 3.8.2-0
- Initial package. (using DAR)
