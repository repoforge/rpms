# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>
# Upstream: <libdnet-devel$lists,sf,net>

Summary: Simple portable interface to lowlevel networking routines
Name: libdnet
Version: 1.11
Release: 1.2%{?dist}
License: BSD-like
Group: System Environment/Libraries
URL: http://libdnet.sourceforge.net/

Source: http://dl.sf.net/libdnet/libdnet-%{version}.tar.gz
Patch0: libdnet-1.7-fw-ipchains.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Libdnet provides a simple portable interface to lowlevel networking routines.

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
#patch0

%build
%configure
%{__make} %{?_smp_mflags} \
	COPTFLAG="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__rm} -f %{buildroot}%{_libdir}/libdnet %{buildroot}%{_libdir}/libdnet.1
%{__mv} -f %{buildroot}%{_libdir}/libdnet.1.0.1 %{buildroot}%{_libdir}/libdnet.so.1.0.1
%{__ln_s} -f libdnet.so.1.0.1 %{buildroot}%{_libdir}/libdnet.so.1
%{__ln_s} -f libdnet.so.1.0.1 %{buildroot}%{_libdir}/libdnet.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man8/dnet.8*
%{_libdir}/libdnet.so.*
%{_sbindir}/dnet

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/dnet.3*
%{_bindir}/dnet-config
%{_includedir}/dnet.h
%{_includedir}/dnet/
%{_libdir}/libdnet.a
%{_libdir}/libdnet.so
%exclude %{_libdir}/libdnet.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1.2
- Rebuild for Fedora Core 5.

* Tue Feb 21 2006 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Initial package. (using DAR)
