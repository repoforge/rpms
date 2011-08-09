# $Id$
# Authority: shuff

Summary: Next generation C++ class libraries for network-centric applications
Name: poco
Version: 1.3.5
Release: 1%{?dist}
License: Boost
Group: Development/Libraries
URL: http://pocoproject.org/

Source: http://downloads.sourceforge.net/poco/poco-%{version}-all.tar.bz2
Patch0: poco-1.3.5_syslibs.patch
Patch1: poco-1.3.5_RH-old-SQLite.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: cppunit
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: mysql-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: pkgconfig
BuildRequires: sqlite-devel
BuildRequires: unixODBC-devel
BuildRequires: zlib-devel

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
%setup -n %{name}-%{version}-all
%{__sed} -i.orig -e 's|ODBCLIBDIR = /usr/lib\b|ODBCLIBDIR = %{_libdir}|g' Data/ODBC/Makefile Data/ODBC/testsuite/Makefile
%{__sed} -i.orig -e 's|flags=""|flags="%{optflags}"|g' configure
%{__rm} -f Crypto/include/Poco/.*DS_Store
%{__rm} -f Foundation/src/MSG00001.bin
%patch0 -p1
%{__rm} -f Foundation/include/Poco/zconf.h
%{__rm} -f Foundation/include/Poco/zlib.h
%{__rm} -f Foundation/src/adler32.c
%{__rm} -f Foundation/src/compress.c
%{__rm} -f Foundation/src/crc32.c
%{__rm} -f Foundation/src/crc32.h
%{__rm} -f Foundation/src/deflate.c
%{__rm} -f Foundation/src/deflate.h
%{__rm} -f Foundation/src/gzio.c
%{__rm} -f Foundation/src/infback.c
%{__rm} -f Foundation/src/inffast.c
%{__rm} -f Foundation/src/inffast.h
%{__rm} -f Foundation/src/inffixed.h
%{__rm} -f Foundation/src/inflate.c
%{__rm} -f Foundation/src/inflate.h
%{__rm} -f Foundation/src/inftrees.c
%{__rm} -f Foundation/src/inftrees.h
%{__rm} -f Foundation/src/trees.c
%{__rm} -f Foundation/src/trees.h
%{__rm} -f Foundation/src/zconf.h
%{__rm} -f Foundation/src/zlib.h
%{__rm} -f Foundation/src/zutil.c
%{__rm} -f Foundation/src/zutil.h
%{__rm} -f Foundation/src/pcre*
%{__rm} -f Foundation/src/ucp.h
%{__rm} -f Data/SQLite/src/sqlite3.*
%{__rm} -f XML/include/Poco/XML/expat.h
%{__rm} -f XML/include/Poco/XML/expat_external.h
%{__rm} -f XML/src/ascii.h
%{__rm} -f XML/src/asciitab.h
%{__rm} -f XML/src/expat_config.h
%{__rm} -f XML/src/iasciitab.h
%{__rm} -f XML/src/internal.h
%{__rm} -f XML/src/latin1tab.h
%{__rm} -f XML/src/nametab.h
%{__rm} -f XML/src/utf8tab.h
%{__rm} -f XML/src/xmlparse.cpp
%{__rm} -f XML/src/xmlrole.c
%{__rm} -f XML/src/xmlrole.h
%{__rm} -f XML/src/xmltok.c
%{__rm} -f XML/src/xmltok.h
%{__rm} -f XML/src/xmltok_impl.c
%{__rm} -f XML/src/xmltok_impl.h
%{__rm} -f XML/src/xmltok_ns.c

# Support for older SQLite
%patch1 -p1 

%{__perl} -pi.orig -e 's|\$\(INSTALLDIR\)/lib\b|\$\(INSTALLDIR\)/%{_lib}|g' Makefile

%build
%configure --library-path=%{_libdir}/mysql
%{__make} \
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
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Poco/
%{_libdir}/*.so

%changelog
* Wed Aug 03 2011 Steve Huff <shuff@vecna.org> - 1.3.5-1
- Update to release 1.3.5 (ported from EPEL).
- Use system libraries instead of bundled.
- Update various metadata.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Initial package. (using DAR)
