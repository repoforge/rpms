# $Id$
# Authority: stefan

Summary: A library implementing the SSH2 protocol
Name: libssh2
Version: 0.12
Release: 1
Group: System Environment/Libraries
Source: http://heanet.dl.sourceforge.net/sourceforge/libssh2/libssh2-%{version}.tar.gz
URL: http://www.libssh2.org/
License: BSD
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

BuildRequires: pkgconfig, openssl-devel, zlib-devel

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libssh2.so
%{_includedir}/libssh2*

%changelog
* Tue Dec 06 2005 Stefan Pietsch <stefan.pietsch@eds.com> 0.12
- update to new release

* Tue Oct 25 2005 Stefan Pietsch <stefan.pietsch@eds.com> 0.11
- first release
