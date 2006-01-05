# $Id$
# Authority: leet

%define tarversion  2_7_0

Summary: Validating XML Parser
Name: xerces-c
License: Apache
Group: Development/Libraries
Version: 2.7.0
Release: 1
URL: http://xml.apache.org/xerces-c/

Source0: http://www.apache.org/dist/xml/xerces-c/source/xerces-c-src_%{tarversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards ( DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).

Authors:
--------
    The Apache Group <apache@apache.org>

%package devel
Requires:     xerces-c = %{version}
Group:        Development/Libraries/C and C++
Summary:      A validating XML parser - Development Files

%description devel
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents.

This package includes files needed for development with Xerces-c

Authors:
--------
    The Apache Group <apache@apache.org>

%prep
%setup -n xerces-c-src_%{tarversion}
%{__perl} -pi -e "s|{PREFIX}/lib|{PREFIX}\@libdir\@|g;" */Makefile.in
%{__perl} -pi -e "s|\(PREFIX\)/lib|\(PREFIX\)\@libdir\@|g;" */Makefile.in

%build
export XERCESCROOT=`pwd`
pushd src/xercesc
autoreconf --install --force
%ifarch alpha ppc64 s390x sparc64 x86_64
BITSTOBUILD=64
%else
BITSTOBUILD=32
%endif
./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -b "$BITSTOBUILD" -P /usr -C --libdir=%{_libdir}
%{__make}
popd

%install
rm -rf %{buildroot}
export XERCESCROOT=`pwd`
pushd src/xercesc
make install PREFIX=%{buildroot} PREFIX_INCLUDE=%{buildroot}/%{_includedir}/xercesc 
popd

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc LICENSE.txt Readme.html
%{_libdir}/lib%{name}.so.*
%{_libdir}/libxerces-depdom.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/libxerces-depdom.so
%attr( - ,root,root) %{_includedir}/xercesc/

%changelog
* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.7.0-1
- Updated to release 2.7.0.

* Thu Sep 22 2005 C.Lee Taylor <leet@leenx.co.za> 2.6.1-1
- Update to 2.6.1
- Build for FC4 32/64bit

* Sat Aug 20 2005 Che
- initial rpm release
