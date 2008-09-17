# $Id$
# Authority: matthias

Summary: Multimedia container format library
Name: libmatroska
Version: 0.8.1
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.matroska.org/

Source: http://dl.matroska.org/downloads/libmatroska/libmatroska-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libebml-devel >= 0.7.6

%description
In short, matroska is a new Audio/Video container file format. It is an
advanced and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that allows
infinite extensibility of the format. And full featured because it includes
precise seeking, any audio/video/subtitle codec support including
VCM/ACM/DirectShow compatibility, timecode based format, complex frame
dependencies, chaptering, internationalisation, error protection, tagging,
file attachement, control track (to be defined), menu (to be defined), etc.
All these features are not yet implemented but already defined in the format.

%package devel
Summary: Development files for the Matroska container format library
Group: Development/Libraries
Requires: %{name} = %{version}, libebml-devel >= 0.7.5

%description devel
In short, matroska is a new Audio/Video container file format. It is an
advanced and full featured format.

Advanced because it is based on EBML, a kind of XML equivalent, that allows
infinite extensibility of the format. And full featured because it includes
precise seeking, any audio/video/subtitle codec support including
VCM/ACM/DirectShow compatibility, timecode based format, complex frame
dependencies, chaptering, internationalisation, error protection, tagging,
file attachement, control track (to be defined), menu (to be defined), etc.
All these features are not yet implemented but already defined in the format.

This package contains the required files to develop programs that will use
the Matroska container format library.

%prep
%setup

%build
# No autotools...
%{__make} -C make/linux %{?_smp_mflags} DEBUGFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} -C make/linux install \
    libdir="%{buildroot}%{_libdir}" \
    includedir="%{buildroot}%{_includedir}/matroska"

# Needed for proper stripping of the library (0.7.7)
%{__chmod} +x %{buildroot}%{_libdir}/*.so.*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.LGPL
%{_libdir}/libmatroska.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/matroska/
%{_libdir}/libmatroska.so
%exclude %{_libdir}/libmatroska.a

%changelog
* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Nov 27 2005 Matthias Saou <http://freshrpms.net/> 0.8.0-1
- Update to 0.8.0.

* Tue May 31 2005 Matthias Saou <http://freshrpms.net/> 0.7.7-1
- Update to 0.7.7.
- Shared lib is now built by default, so include it at last.
- Explicit chmod +x of the shared lib to get it stripped properly.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 0.7.5-1
- Update to 0.7.5.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.7.4-1
- Update to 0.7.4.

* Thu Sep 16 2004 Matthias Saou <http://freshrpms.net/> 0.7.3-1
- Update to 0.7.3.

* Fri Aug  6 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.

* Tue Aug  3 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Thu Jul  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Initial RPM release.

