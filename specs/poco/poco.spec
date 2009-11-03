# $Id$
# Authority: dag

Summary: Next generation C++ class libraries for network-centric applications
Name: poco
Version: 1.3.0
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.appinf.com/poco/

Source: http://dl.sf.net/poco/poco-%{version}-ssl.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
POCO, the C++ Portable Components, is a collection of open source C++ class
libraries that simplify and accelerate the development of network-centric,
portable applications in C++. The libraries integrate perfectly with the
C++ Standard Library and fill many of the functional gaps left open by it.

Their modular and efficient design and implementation makes the C++ Portable
Components extremely well suited for embedded development, an area where the
C++ programming language is becoming increasingly popular, due to its
suitability for both low-level (device I/O, interrupt handlers, etc.) and
high-level object-oriented development. Of course, POCO is also ready for
enterprise-level challenges.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{version}-ssl

%{__perl} -pi.orig -e 's|\$\(INSTALLDIR\)/lib\b|\$\(INSTALLDIR\)/%{_lib}|g' Makefile

%build
%configure
%{__make} %{?_smp_mflags} \
	CXXFLAGS="%{optflags} $(pkg-config --cflags openssl)"
	LINKFLAGS="$LDFLAGS $(pkg-config --libs-only-L openssl)"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG CONTRIBUTORS LICENSE MANIFEST NEWS README doc/*.html
%{_libdir}/libPocoFoundation.so.*
%{_libdir}/libPocoFoundationd.so.*
%{_libdir}/libPocoNet.so.*
%{_libdir}/libPocoNetSSL.so.*
%{_libdir}/libPocoNetSSLd.so.*
%{_libdir}/libPocoNetd.so.*
%{_libdir}/libPocoUtil.so.*
%{_libdir}/libPocoUtild.so.*
%{_libdir}/libPocoXML.so.*
%{_libdir}/libPocoXMLd.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Poco/
%{_libdir}/libPocoFoundation.so
%{_libdir}/libPocoFoundationd.so
%{_libdir}/libPocoNet.so
%{_libdir}/libPocoNetSSL.so
%{_libdir}/libPocoNetSSLd.so
%{_libdir}/libPocoNetd.so
%{_libdir}/libPocoUtil.so
%{_libdir}/libPocoUtild.so
%{_libdir}/libPocoXML.so
%{_libdir}/libPocoXMLd.so

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.7-1
- Initial package. (using DAR)
