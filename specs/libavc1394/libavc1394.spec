# $Id$
# Authority: matthias

Summary: A library for providing raw access to IEEE 1394 devices
Name: libavc1394
Version: 0.4.1
Release: 2
License: GPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libavc1394/
Source0: http://dl.sf.net/libavc1394/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libraw1394 >= 0.8
BuildRequires: libraw1394-devel >= 0.8

%description
libavc1394 is a programming interface for the 1394 Trade Association
AV/C (Audio/Video Control) Digital Interface Command Set.


%package devel
Summary: Files for developing applications that use libavc1394
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
The header files, static library, libtool library and man pages for
developing applications that use libavc1394.


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
%doc COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.4.1-2.fr
- Rebuild for Fedora Core 1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Added libraw1394 dependency.

* Mon Apr  7 2003 Tim Waugh <tim@cyberelk.net>
- Initial specfile.

