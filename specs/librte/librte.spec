# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%define real_name rte

Summary: Real Time software audio/video Encoder library
Name: librte
Version: 0.5.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://zapping.sourceforge.net/

Source: http://dl.sf.net/zapping/rte-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{!?rh6:BuildRequires: doxygen}

Obsoletes: rte < %{version}

%description
The RTE library is a frontend or wrapper of other libraries or programs
for real time video and audio compression on Linux. Currently it works
on x86 CPUs only, sorry. The library is designed to interface between
codecs and the Zapping TV viewer: http://zapping.sf.net,
precisely its recording plugin.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{real_name}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
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
* Sun May 23 2004 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Latest release, not obsoleting rte.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
