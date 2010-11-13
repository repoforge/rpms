# $Id$
# Authority: stefan

### EL6 ships with libssh2-1.2.2-7.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Library implementing the SSH2 protocol
Name: libssh2
Version: 1.2.7
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.libssh2.org/

Source: http://www.libssh2.org/download/libssh2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

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

#%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in */Makefile.in

%build
%configure \
    --disable-rpath \
    --disable-static \
    --with-pic
#%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -pipe -I../include/ -fPIC"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING HACKING NEWS README
%{_libdir}/libssh2.so.*

%files devel
%defattr(-, root, root, 0755)
%doc example/
%doc %{_mandir}/man3/libssh2_*.3*
%{_includedir}/libssh2*.h
%{_libdir}/libssh2.so
%{_libdir}/pkgconfig/libssh2.pc
%exclude %{_libdir}/libssh2.la

%changelog
* Wed Aug 18 2010 Dag Wieers <dag@wieers.com> - 1.2.7-1
- Updated to release 1.2.7.

* Tue Jun 22 2010 Dag Wieers <dag@wieers.com> - 1.2.6-1
- Updated to release 1.2.6.

* Fri Sep 07 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.14-1
- Updated to release 0.14.
- Renamed to libssh2-devel.
- Cosmetic changes.

* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.12-1
- Update to new release.

* Tue Oct 25 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.11-1
- First release.
