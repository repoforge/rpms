# $Id$
# Authority: dries
# Upstream: <gift-devel$lists,sourceforge,net>

Summary: Deamon for communicating with filesharing protocols
Name: gift
Version: 0.11.6
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.giftproject.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/gift/gift-%{version}.tar.bz2 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
giFT is a modular daemon capable of abstracting the communication between
the end user and specific filesharing protocols (peer-to-peer or otherwise).

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HACKING QUICKSTART README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/giFT/
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libgift/

%changelog
* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.11.6-1
- Yet some more cleanups.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.11.6-1
- Cosmetic cleanup.

* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> 0.11.6-1
- update to 0.11.6

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.11.5-1
- first packaging for Fedora Core 1
