# $Id$
# Authority: dag
# Upstream: Martin Pool <mbp$sourcefrog,net>
# Upstream: <librsync-devel$lists,sf,net>

Summary: Library that implements the rsync remote-delta algorithm
Name: librsync
Version: 0.9.7
Release: 1.2
License: LGPL
Group: System Environment/Libraries
URL: http://librsync.sourceforge.net/

Source: http://dl.sf.net/librsync/librsync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libhsync <= %{version}
Provides: rdiff = %{version}-%{release}
Obsoletes: rdiff <= %{version}-%{release}

%description
librsync implements the "rsync" algorithm, which allows remote
differencing of binary files.  librsync computes a delta relative to a
file's checksum, so the two files need not both be present to generate
a delta.

This library was previously known as libhsync up to version 0.9.0.

The current version of this package does not implement the rsync
network protocol and uses a delta format slightly more efficient than
and incompatible with rsync 2.4.6.

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
%ifnarch %{ix86}
	--with-pic
%endif

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 rdiff %{buildroot}%{_bindir}/rdiff

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man1/rdiff.1*
%{_bindir}/rdiff
#%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/librsync.3*
%{_includedir}/*.h
%{_libdir}/librsync.a
%exclude %{_libdir}/librsync.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1.2
- Rebuild for Fedora Core 5.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.9.7-1
- Updated to release 0.9.7.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.9.6-3
- Added -fPIC for x86_64.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Cosmetic changes.

* Wed May 05 2004 Wim Vandersmissen <wim@bofh.be> - 0.9.6-0
- Initial package.
