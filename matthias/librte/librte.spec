# Authority: freshrpms
%define rname rte

Summary: Real Time software audio/video Encoder library.
Name: librte
Version: 0.5.1
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://zapping.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/zapping/%{rname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%{!?rh62:BuildRequires: doxygen}

#Provides: %{rname}
Obsoletes: %{rname}

%description
The RTE library is a frontend or wrapper of other libraries or programs
for real time video and audio compression on Linux. Currently it works
on x86 CPUs only, sorry. The library is designed to interface between
codecs and the Zapping TV viewer: http://zapping.sourceforge.net,
precisely its recording plugin.

%package devel
Summary: Static library and API documentation of the Real Time Encoder.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Static library and API documentation of the Real Time Encoder.

%prep
%setup -n %{rname}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{rname}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
#exclude %{_libdir}/*.la

%changelog
* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to 0.5.1.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
