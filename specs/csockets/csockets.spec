# $Id$
# Authority: dries
# Upstream: 

Summary: C++ wrapper for sockets
Name: csockets
Version: 1.9.5
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.alhem.net/Sockets/index.html

Source: http://www.alhem.net/Sockets/Sockets-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openssl-devel

%description
C++ Sockets is a C++ wrapper for BSD-style sockets. Its features include 
transparent SOCKS4 client support and asynchronous DNS. It implements the TCP, 
UDP, ICMP, HTTP (GET, PUT, and POST), and HTTPS (using OpenSSL) protocols.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n Sockets-%{version}

%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix}

%install
%{__rm} -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/Sockets-config

%files devel
%{_includedir}/Sockets
%{_libdir}/*.a

%changelog
* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.5-1
- Update to release 1.9.5.

* Fri Aug 26 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.7-1
- Initial package.
