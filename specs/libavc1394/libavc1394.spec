# $Id$
# Authority: matthias

# ExcludeDist: el4

Summary: Audio/Video Control library for IEEE-1394 devices
Name: libavc1394
Version: 0.5.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libavc1394/
Source: http://dl.sf.net/libavc1394/libavc1394-%{version}.tar.gz
Patch: libavc1394-0.5.1-librom.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libraw1394-devel, pkgconfig
Obsoletes: librom1394 <= 0.5.0

%description
The libavc1394 library allows utilities to control IEEE-1394 devices
using the AV/C specification.  Audio/Video Control allows applications
to control devices like the tape on a VCR or camcorder.

%package devel
Summary: Development libs for libavc1394
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libraw1394-devel
Obsoletes: librom1394-devel <= 0.5.0

%description devel
Development libraries required to build applications using libavc1394.


%prep
%setup
%patch -p1 -b .librom


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libavc1394/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libavc1394.pc


%changelog
* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 0.5.1-1
- Add obsoletes for librom1394 <= 0.5.0 to enable upgrade path for users
  with atrpms packages installed.

* Fri Dec  9 2005 Matthias Saou <http://freshrpms.net/> 0.5.1-0
- Update to 0.5.1.
- Sync with Fedora Core spec file.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.4.1-2
- Rebuild for Fedora Core 1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Added libraw1394 dependency.

* Mon Apr  7 2003 Tim Waugh <tim@cyberelk.net>
- Initial specfile.

