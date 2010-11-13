# $Id$
# Authority: dag
# Upstream: Andrew Tridgell <tridge$samba,org>

Summary: Trivial database
Name: tdb
Version: 1.0.6
Release: 4.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://sf.net/projects/tdb/

Source: http://dl.sf.net/tdb/tdb-%{version}.tar.gz
Patch0: tdb-1.0.6-gcc33.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gdbm-devel, libtool, gettext, sed, grep

%description
TDB is a trivial database. In concept, it is very much like GDBM,
and BSD's DB except that it allows multiple simultaneous writers
and uses locking internally to keep writers from trampling on
each other. TDB is also extremely small.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -b .gcc3

%build
%{__libtoolize} --force --copy
%configure
%{__make} %{?_smp_mflags} SED=sed

%install
%{__rm} -rf %{buildroot}
%makeinstall SED=sed

### FIXME: Move tdbdump and tdbtool to resp. tdb-dump and tdb-tool to avoid samba conflict. (Please fix upstream)
%{__mv} -f %{buildroot}%{_bindir}/tdbdump %{buildroot}%{_bindir}/tdb-dump
%{__mv} -f %{buildroot}%{_bindir}/tdbtool %{buildroot}%{_bindir}/tdb-tool

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/tdb-dump
%{_bindir}/tdb-tool
%{_libdir}/libtdb.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_libdir}/libtdb.a
%exclude %{_libdir}/libtdb.la
%{_libdir}/libtdb.so
%{_includedir}/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.6-4.2
- Rebuild for Fedora Core 5.

* Wed Dec 01 2004 Dag Wieers <dag@wieers.com> - 1.0.6-4
- Move tdbdump and tdbtool to resp. tdb-dump and tdb-tool. (Matthew Miller)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 1.0.6-3
- Remove tdbdump from this package, conflicts with RHFC1 samba. (Bert de Bruijn)

* Fri Nov 21 2003 Dag Wieers <dag@wieers.com> - 1.0.6-2
- Patch to build with gcc-3.3.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
