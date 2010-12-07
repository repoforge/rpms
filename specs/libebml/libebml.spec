# $Id$
# Authority: matthias

Summary: Extensible Binary Meta Language library
Name: libebml
Version: 1.0.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.matroska.org/

Source: http://dl.matroska.org/downloads/libebml/libebml-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
This library is used for I/O operations in the Extensible Binary Meta Language
(EBML), which is a kind of binary version of XML.

%package devel
Summary: Development files for the Extensible Binary Meta Language
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This library is used for I/O operations in the Extensible Binary Meta Language
(EBML), which is a kind of binary version of XML.

This package contains the files required to rebuild applications which will
use the Extensible Binary Meta Language.

%prep
%setup

%build
# No autotools...
%{__make} -C make/linux %{?_smp_mflags} DEBUGFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} -C make/linux install \
    libdir="%{buildroot}%{_libdir}" \
    includedir="%{buildroot}%{_includedir}/ebml"

# Needed for proper stripping of the library (0.7.5)
%{__chmod} +x %{buildroot}%{_libdir}/libebml.so.*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE.LGPL
%{_libdir}/libebml.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ebml/
%{_libdir}/libebml.so
%exclude %{_libdir}/libebml.a

%changelog
* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Mon Sep 15 2008 Dag Wieers <dag@wieers.com> - 0.7.8-1
- Updated to release 0.7.8.

* Wed Apr 12 2006 Matthias Saou <http://freshrpms.net/> 0.7.7-1
- Update to 0.7.7.

* Sun Nov 27 2005 Matthias Saou <http://freshrpms.net/> 0.7.6-1
- Update to 0.7.6.

* Tue May 31 2005 Matthias Saou <http://freshrpms.net/> 0.7.5-1
- Update to 0.7.5.
- Shared lib is now built by default, so include it at last.
- Explicit chmod +x of the shared lib to get it stripped properly.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 0.7.3-1
- Update to 0.7.3.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.7.2-1
- Update to 0.7.2.

* Tue Aug  3 2004 Matthias Saou <http://freshrpms.net/> 0.7.1-1
- Update to 0.7.1.

* Thu Jul  1 2004 Matthias Saou <http://freshrpms.net/> 0.7.0-1
- Initial RPM release.

