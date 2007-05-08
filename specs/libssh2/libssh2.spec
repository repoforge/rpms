# $Id$
# Authority: stefan

Summary: Library implementing the SSH2 protocol
Name: libssh2
Version: 0.14
Release: 1
License: BSD
Group: System Environment/Libraries
URL: http://www.libssh2.org/

Source: http://heanet.dl.sourceforge.net/sourceforge/libssh2/libssh2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, openssl-devel, zlib-devel

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}
Obsoletes: %{name} <= %{version}-%{release}
Provides: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in */Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%defattr(-, root, root, 0755)
%doc LICENSE README ssh2_sample.c
%{_libdir}/libssh2.so
%{_includedir}/libssh2*.h

%changelog
* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.14-1
- Updated to release 0.14.
- Renamed to libssh2-devel.
- Cosmetic changes.

* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.12-1
- Update to new release.

* Tue Oct 25 2005 Stefan Pietsch <stefan.pietsch@eds.com> - 0.11-1
- First release.
