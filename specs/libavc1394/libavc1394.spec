# $Id$
# Authority: matthias

# ExclusiveDist: el3

Summary: library for providing raw access to IEEE 1394 devices
Name: libavc1394
Version: 0.4.1
Release: 2
License: GPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libavc1394/

Source: http://dl.sf.net/libavc1394/libavc1394-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libraw1394-devel >= 0.8
Requires: libraw1394 >= 0.8

%description
libavc1394 is a programming interface for the 1394 Trade Association
AV/C (Audio/Video Control) Digital Interface Command Set.
s

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
#%{__libtoolize} --force --copy
#%{__aclocal}
#%{__automake}
##%{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

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

