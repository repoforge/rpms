# $Id$
# Authority: dag

Summary: Library implementing the SSH2 protocol (0xbadc0de version)
Name: libssh
Version: 0.5.0
Release: 1%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.libssh.org/

Source: http://www.libssh.org/files/0.5/libssh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
The ssh library was designed to be used by programmers needing a
working SSH implementation by the mean of a library. The complete
control of the client is made by the programmer. With libssh, you can
remotely execute programs, transfer files, use a secure and transparent
tunnel for your remote programs. With its Secure FTP implementation,
you can play with remote files easily, without third-party programs
others than libcrypto (from openssl).

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
mkdir obj
cd obj
%cmake ..
%{__make}

%install
%{__rm} -rf %{buildroot}
cd obj
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__chmod} 0644 %{buildroot}/usr/include/libssh/*

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BSD ChangeLog COPYING README
%{_libdir}/libssh.so.*
%{_libdir}/libssh_threads.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libssh/
%{_libdir}/libssh.so
%{_libdir}/libssh_threads.so
%{_libdir}/pkgconfig/libssh.pc
#exclude %{_libdir}/libssh.la
#exclude %{_libdir}/libssh_threads.la

%changelog
* Tue Jun 07 2011 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Tue Sep 07 2010 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Updated to release 0.4.6.

* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Initial package. (using DAR)
