# $Id: libavc1394.spec,v 1.1 2004/02/26 17:54:29 thias Exp $

Summary: A library for providing raw access to IEEE 1394 devices
Name: libavc1394
Version: 0.4.1
Release: 2.fr
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
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
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

