# $Id$
# Authority: matthias

Summary: Library for reading and writing files containing sampled sound
Name: libsndfile
Version: 1.0.8
Release: 1
License: LGPL
Group: System Environment/Libraries
Source: http://www.mega-nerd.com/libsndfile/%{name}-%{version}.tar.gz
URL: http://www.mega-nerd.com/libsndfile/
BuildRoot:%{_tmppath}/%{name}-%{version}-root
BuildRequires: gcc-c++

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.


%package devel
Summary: Header files and development documentation for libsndfile
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

This package contains the header files, static libraries and development
documentation for libsndfile.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc NEWS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*


%files devel
%defattr(-, root, root, 0755)
%doc doc/*.html doc/*.jpg
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_datadir}/octave


%changelog
* Mon Mar 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.8-1.fr
- Update to 1.0.8.

* Wed Feb 25 2004 Matthias Saou <http://freshrpms.net/> 1.0.7-1.fr
- Update to 1.0.7.
- Updated the URL and Source tags.

* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 1.0.6-1.fr
- Update to 1.0.6.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.0.5-2.fr
- Rebuild for Fedora Core 1.

* Sun May  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.5.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Spec file adapted from the PLD one.
- Update to 1.0.4.

