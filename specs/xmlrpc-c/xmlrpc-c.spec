# $Id$
# Authority: dfateyev

# ExcludeDist: el2 el3 el4

### EL6 ships with xmlrpc-c-1.16.24-1200
### EL5 ships with xmlrpc-c-1.16.24-1206
# Tag: rfx

# more unification with curl version (7.19.7 shipped with el6)
%define curl_version 7.19.7

%{?el5:%define _with_curl_static 1}

%define _default_patch_fuzz	2

Summary: A lightweight RPC library based on XML and HTTP
Name: xmlrpc-c
# based on 'stable' svnrev 2077
Version: 1.25.1
Release: 1%{?dist}
# See COPYING for details.
# The Python 1.5.2 license used by a few files is just BSD.
License: BSD and MIT
Group: System Environment/Libraries
URL: http://xmlrpc-c.sourceforge.net/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# download from SF SVN (see below)
#Source0: xmlrpc-c-%{version}.tar.gz
Source1: http://curl.haxx.se/download/curl-%{curl_version}.tar.bz2
Source100: dfs.cc
Source101: dso-fixup

Patch100: xmlrpc-c-cmake.patch
Patch102: xmlrpc-c-printf-size_t.patch
Patch105: xmlrpc-c-longlong.patch
Patch107: xmlrpc-c-uninit-curl.patch
Patch108: xmlrpc-c-30x-redirect.patch
Patch109: xmlrpc-c-check-vasprintf-return-value.patch
Patch110: xmlrpc-c-include-string_int.h.patch

BuildRequires: wget
BuildRequires: cmake
BuildRequires: openldap-devel
BuildRequires: krb5-devel
BuildRequires: libidn-devel
%{!?_with_curl_static:BuildRequires: curl-devel}
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel


%package c++
Summary: C++ libraries for xmlrpc-c
Group: System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%package client
Summary: C client libraries for xmlrpc-c
Group: System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%package client++
Summary: C++ client libraries for xmlrpc-c
Group: System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%package devel
Summary: Development files for xmlrpc-c based programs
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-c++%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: %{name}-client++%{?_isa} = %{version}-%{release}

%package apps
Summary: Sample XML-RPC applications
Group: Applications/Internet


%description
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C.


%description c++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++.


%description client
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C
clients.

%description client++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++
clients.


%description devel
Static libraries and header files for writing XML-RPC applications in
C and C++.


%description apps
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This package contains some handy XML-RPC demo applications.


%prep
# download 'stable release' from SVN
%{__rm} -rf xmlrpc-c-%{version}*
wget -O xmlrpc-c-%{version}.tar.gz "http://xmlrpc-c.svn.sourceforge.net/viewvc/xmlrpc-c/stable/?view=tar"
%{__tar} -xvvf xmlrpc-c-%{version}.tar.gz
%{__mv} stable xmlrpc-c-%{version}
%setup -n xmlrpc-c-%{version} -T -D

%{?_with_curl_static:%setup -T -D -a 1}

%patch100 -p1
%patch102 -p1
%patch105 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1

## not needed...
%{__rm} doc/{INSTALL,configure_doc}


%build
%if %{?_with_curl_static:1}0
# Build curl
pushd curl-%{curl_version}
RESULT_DIR="$(pwd)/result"

./configure \
    --prefix="$RESULT_DIR" \
    --exec-prefix="$RESULT_DIR" \
    --disable-manual \
    --disable-shared \
    --enable-ipv6 \
    --enable-static \
    --without-libssh2 \
    --without-ssl \
    --with-gssapi="%{_prefix}/kerberos" \
    --with-libidn

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd

# Append pkgconfig info
PKG_CONFIG_PATH="$RESULT_DIR/lib/pkgconfig:$PKG_CONFIG_PATH" ; export PKG_CONFIG_PATH
%endif

%{__mkdir_p} fedora
cd fedora
export CFLAGS="$RPM_OPT_FLAGS -Wno-uninitialized -Wno-unknown-pragmas"
export CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="-lldap -lidn -lrt"
cmake .. \
	-D_lib:STRING=%{_lib}			\
	-DMUST_BUILD_CURL_CLIENT:BOOL=ON	\
	-DMUST_BUILD_LIBWWW_CLIENT:BOOL=OFF	\
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}	\
        -DBUILD_SHARED_LIBS:BOOL=ON		\
	-DENABLE_TOOLS:BOOL=ON
%{__make} VERBOSE=1 %{?_smp_mflags}

%{__cxx} $RPM_OPT_FLAGS %{SOURCE100} -o depsort


%install
%{__rm} -rf %{buildroot}
cd fedora
%{__make} install DESTDIR=%{buildroot}

%{__chmod} +x %{buildroot}/%{_libdir}/*.so

%{SOURCE101} "%{buildroot}" "%{_libdir}" 'libxmlrpc' %{buildroot}/%{_libdir}/libxmlrpc*.so.[0-9]


%check
unset PKG_CONFIG_PATH
%if %{?_with_curl_static:1}0
PKG_CONFIG_PATH="$(pwd)/curl-%{curl_version}/result/lib/pkgconfig" ; export PKG_CONFIG_PATH
%endif
export PKG_CONFIG_LIBDIR=%{buildroot}/%{_libdir}/pkgconfig:%{_libdir}/pkgconfig:%{_datadir}/pkgconfig
PATH=%{buildroot}/%{_bindir}:$PATH

_e() {
     echo "\$ $@"
     "$@"
}

set +x
_e xmlrpc-c-config --help
for comp in c++ cgi-server server-util abyss-server client libwww-client; do
	for opt in '--version' '--libs' 'c++2 --libs' 'c++ --libs --static'; do
		_e xmlrpc-c-config "$comp" $opt
	done
done
set -x


%clean
%{__rm} -rf %{buildroot}


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post client   -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%post c++   -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%post client++   -p /sbin/ldconfig
%postun client++ -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc doc/*
%{_libdir}/*.so.3*
%exclude %{_libdir}/libxmlrpc_client.so*


%files client
%defattr(-,root,root,-)
%{_libdir}/libxmlrpc_client.so.*


%files c++
%defattr(-,root,root,-)
%{_libdir}/*.so.7*
%exclude %{_libdir}/libxmlrpc_client++.so*


%files client++
%defattr(-,root,root,-)
%{_libdir}/libxmlrpc_client++.so.*


%files devel
%defattr(-,root,root,-)
%{_bindir}/xmlrpc-c-config
%{_includedir}/xmlrpc-c
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


%files apps
%defattr(-,root,root,-)
%doc tools/xmlrpc/xmlrpc.html
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%{_mandir}/man1/*
%{_bindir}/xmlrpc
%{_bindir}/xmlrpc_transport
%{_bindir}/xml-rpc-api2cpp
%{_bindir}/xmlrpc_cpp_proxy
%{_bindir}/xmlrpc_pstream

%exclude %{_bindir}/xml-rpc-api2txt


%changelog
* Mon May 07 2012 Denis Fateyev <denis@fateyev.com> - 1.25.1-1
- Updated to 1.25, synced with fedora spec

* Sun Mar 20 2011 Denis Fateyev <denis@fateyev.com> - 1.22.01-1
- Rebuild for 'denf' repo

* Sun Apr 18 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.22.01-1400.svn1907
- updated to 1.22.01 (svn 1907)

* Tue Feb 23 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.21.00-1401.1851
- require the various subpackages explicitly for -devel; the ld linker
  scripts broke rpm's autodetection (#567400)
- removed -devel Requires: which are covered by pkgconfig autodeps
- added %%{?_isa} annotations

* Sun Feb 21 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.21.00-1400.1851
- made linker scripts more 'ldconfig' friendly

* Mon Feb 15 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.21.00-1301.1851
- replaced .so symlinks by linker scripts which add all implicit
  dependencies in AS_NEEDED() commands (#564607, #565577)

* Thu Jan 14 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.21.00-1300.1851
- updated to 1.21.00 (rev 1851)
- removed curl-trace patch as applied upstream
- rediffed patches

* Sat Nov 21 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.20.3-1.1841
- updated to rev1841
- rediffed patches
- added patch to fix handling of wrong certificates (Nikola Pajkovsky)
- added support for $XMLRPC_TRACE_CURL env (John Dennis)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.6-3.1582
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.6-2.1582
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.16.6-1.1582
- updated to 1.16.6; rediffed patches
- fixed client headers (bug #475887)

* Sat Nov 15 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.16.4.1567-2
- updated to 1.16.4
- rediffed/updated patches
- splitted some subpackages (c++, client) out of main package as they
  introduce additional dependencies (c++, curl)

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.14.8-2
- fix license tag

* Sat Jun 21 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.14.8-1
- updated to 1.14.8

* Sun May 25 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.14.6-1
- updated to 1.14.6

* Sat Apr 12 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.14.2-1
- updated to 1.14.2
- rediffed patches
- added patch to fix broken usage of 'long long' datatype

* Mon Mar 17 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.13.8-2
- fixed cmake quoting so that pkgconfig files get correct version number
- fixed handling of 'server-util' and '--cflags' within xmlrpc-c-config

* Sun Mar 16 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.13.8-1
- updated to 1.13.8
- removed some patches which were applied upstream

* Tue Feb 26 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.13.07-2
- moved to advanced branched; rediffed/updated existing cmake patch
  and fixed other compilation issues (#369841)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.06.23-2
- Autorebuild for GCC 4.3

* Wed Jan  2 2008 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.23-1
- use correct pkg-config script for 'xmlrpc-config abyss-server'
  output (#355411)
- updated to 1.06.23 (#355411)

* Tue Sep  4 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.18-1
- updated to 1.06.18

* Thu Aug 16 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.17-1
- updated to 1.06.17

* Sun Jul 22 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.16-1
- updated to 1.06.16

* Thu Jun 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.14-1
- updated to 1.06.14

* Sun Apr  1 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.11-2
- rediffed cmake patch against current version
- made the xmlrpc-c-config compatible to the upstream version
- added compatibility symlinks for some header files (thx to Robert de
  Vries for reporting these two issues)

* Sat Mar 17 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.11-1
- updated to 1.06.11

* Sat Feb  3 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.09-1
- updated to 1.06.09
- removed -typo patch since applied upstream

* Mon Nov  6 2006 Jindrich Novy <jnovy@redhat.com> - 1.06.05-3
- rebuild against the new curl

* Mon Oct  2 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.05-2
- updated cmake patch
- strip installed libraries

* Wed Sep 20 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.05-1
- updated to 1.06.05
- merged + updated patches

* Sat Sep 16 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.06.04-1
- updated to 1.06.04
- patched the broken buildsystem
- disabled libwww backend explicitely

* Sun Jun  4 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.05-1
- updated to 1.05
- updated patches

* Sat Feb 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.04-2
- rebuilt for FC5

* Sun Dec 18 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.04-1
- added libxml2-devel and openssl-devel Requires: for the -devel
  subpackage
- ship doc/* instead of doc
- initial Fedora Extras package (review 175840)

* Thu Dec 15 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.04-0.1
- disabled w3c-libwww because it does not exist anymore in FC5 and
  seems to be unmaintained upstream
- added missing libxml2-devel
- cleaned up list of %%doc files
- fixed gcc4.1 build issues
- removed static libraries when there exists a corresponding dynamic one

* Tue Aug  2 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 1.03.02-1
- Initial build.
