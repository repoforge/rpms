# $Id$
# Authority: matthias

%define prever alpha3

Summary: Theora video compression codec
Name: libtheora
Version: 1.0
Release: %{?prever:0.%{prever}.}2
License: BSD
URL: http://www.theora.org/
Source: http://www.theora.org/files/libtheora-%{version}%{?prever}.tar.bz2
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libogg-devel >= 1.1, libvorbis-devel >= 1.0.1, SDL-devel,gcc-c++
# Fedora Core 2's SDL-devel forgot to require alsa-lib-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}

%description
Ogg Theora is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed video format.


%package devel
Summary: Headers for developing programs that will use libtheora
Group: Development/Libraries
Requires: libogg-devel >= 1.0.1

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.


%prep
%setup -n %{name}-%{version}%{?prever}


%build
%configure \
    --includedir="%{_includedir}/theora" \
    --with-pic
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} installed-docs
%makeinstall includedir="%{buildroot}%{_includedir}/theora"
%{__mv} %{buildroot}%{_datadir}/doc/libtheora* installed-docs


%clean
%{__rm} -rf %{buildroot}


%files devel
%defattr(-, root, root, 0755)
%doc README COPYING installed-docs/*
%{_includedir}/theora/
%exclude %{_libdir}/libtheora.la
%{_libdir}/libtheora.a


%changelog
* Tue Jul  6 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.2
- Added --with-pic for x86_64 build.
- Simplified setting of the proper include dir.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.alpha3.1
- Initial RPM release, only devel as there is only a static lib for now.

