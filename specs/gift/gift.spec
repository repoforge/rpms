# $Id$
# Authority: dries
# Upstream: <gift-devel$lists,sourceforge,net>

Summary: Deamon for communicating with filesharing protocols
Name: gift
Version: 0.11.8.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.giftproject.org/

Source: http://dl.sf.net/gift/gift-%{version}.tar.bz2
%{?fc4:BuildRequires: libtool-ltdl-devel, libtool-ltdl}
BuildRequires: libtool, gcc-c++, libvorbis-devel, libogg-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
# -O2 -Wp,-D_FORTIFY_SOURCE=2  causes compile problems, mail sent to
# gift-devel
%{__perl} -pi -e 's|-O2.*|-g -Wall|g;' Makefile */Makefile */*/Makefile
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
%{_libdir}/*.la
%{_datadir}/giFT/
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.so
%{_includedir}/libgift/
%{_libdir}/pkgconfig/libgift.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.11.8.1-1.2
- Rebuild for Fedora Core 5.

* Wed Feb 02 2005 Dries Verachtert <dries@ulyssis.org> 0.11.8.1-1
- Update to release 0.11.8.1.

* Fri Nov 26 2004 Dries Verachtert <dries@ulyssis.org> 0.11.8-1
- Update to release 0.11.8.

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.11.6-1
- Yet some more cleanups.

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 0.11.6-1
- Cosmetic cleanup.

* Sun May 16 2004 Dries Verachtert <dries@ulyssis.org> 0.11.6-1
- update to 0.11.6

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 0.11.5-1
- first packaging for Fedora Core 1
