# $Id$
# Authority: dag
# Upstream: Måns Rullgård <mru$inprovide,com>

Summary: Collection of useful functions for C programming
Name: libtc
Version: 1.1.0
Release: 1.2%{?dist}
License: MIT/X11
Group: System Environment/Libraries
URL: http://libtc.sourceforge.net/

Source: http://dl.sf.net/libtc/libtc-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, gcc-c++

%description
Libtc is a collection of useful functions for C programming. It
includes functions for linked lists, hash tables, red/black trees,
priority queueing, config-file parsing, reference counting and
other useful items. All thread-safe and reentrant.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post,preun): /sbin/install-info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post devel
/sbin/install-info %{_infodir}/libtc.info.gz %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/libtc.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_infodir}/*.info*
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1.2
- Rebuild for Fedora Core 5.

* Sat Apr 17 2004 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Fixed problem with installing the info files. (Laurent Papier)

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 1.1.0-0
- Updated to release 1.1.0.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.0.3-0
- Updated to release 1.0.3.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Tue Oct 04 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Initial package. (using DAR)
