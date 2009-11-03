# $Id$
# Authority: dag

Summary: CD-ROM input and control library
Name: libcdio
Version: 0.77
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.gnu.org/software/libcdio/

Source: http://ftp.gnu.org/gnu/libcdio/libcdio-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, pkgconfig, gcc-c++
Requires: /sbin/ldconfig
Requires: /sbin/install-info

%description
This library provides an interface for CD-ROM access. It can be used
by applications that need OS- and device-independent access to CD-ROM
devices.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--disable-cddb \
	--disable-dependency-tracking \
	--disable-rpath \
	--disable-vcd-info
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
if [ -e "%{_infodir}/libcdio.info.gz" ]; then
	/sbin/install-info %{_infodir}/libcdio.info.gz %{_infodir}/dir
fi

%preun
if [ -e "%{_infodir}/libcdio.info.gz" ]; then
	/sbin/install-info --delete %{_infodir}/libcdio.info.gz %{_infodir}/dir
fi

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README* THANKS TODO
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/jp/man1/*.1*
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/libcdio.info*

%files devel
%defattr(-, root, root, 0755)
%doc example/
%{_includedir}/cdio/
%{_includedir}/cdio++/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Sep 24 2006 Matthias Saou <http://freshrpms.net/> 0.77-1
- Update to 0.77.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.76-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 10 2005 Dag Wieers <dag@wieers.com> - 0.76-1
- Initial package. (using DAR)

