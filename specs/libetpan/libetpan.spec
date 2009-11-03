# $Id$
# Authority: matthias

Summary: Portable mail access library
Name: libetpan
Version: 0.49
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.etpan.org/

Source: http://dl.sf.net/libetpan/libetpan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel, db4-devel, cyrus-sasl-devel, autoconf

%description
The purpose of this mail library is to provide a portable, efficient middleware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

%package devel
Summary: Development files for the libetpan mail access library
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: openssl-devel, db4-devel, cyrus-sasl-devel

%description devel
The purpose of this mail library is to provide a portable, efficient middleware
for different kinds of mail access. When using the drivers interface, the
interface is the same for all kinds of mail access, remote and local mailboxes.

This package contains the files required to develop applications that will use
the libetpan library.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Fix execution bit on the library to get it properly stripped (still in 0.40)
%{__chmod} +x %{buildroot}%{_libdir}/libetpan.so.*


%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT NEWS TODO
%{_libdir}/libetpan.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/API.html doc/DOCUMENTATION doc/README.html
%{_bindir}/libetpan-config
%{_includedir}/libetpan/
%{_includedir}/libetpan.h
%{_libdir}/libetpan.so
%exclude %{_libdir}/libetpan.a
%exclude %{_libdir}/libetpan.la

%changelog
* Sun Aug 12 2007 Heiko Adams <info@fedora-blog.de> - 0.49-1
- Updated to release 0.49.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.46-1
- Updated to release 0.46.

* Tue Jan 31 2006 Matthias Saou <http://freshrpms.net/> 0.42-1
- Update to 0.42.
- Add autoconf build requirement (autoheader is needed now apparently).

* Thu Nov 17 2005 Matthias Saou <http://freshrpms.net/> 0.40-1
- Update to 0.40.

* Mon Oct 11 2005 Matthias Saou <http://freshrpms.net/> 0.39.1-1
- Update to 0.39.1.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 0.38-1
- Initial RPM release.
