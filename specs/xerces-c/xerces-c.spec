# $Id$
# Authority: leet

### EL6 ships with xerces-c-3.0.1-20.el6
# ExclusiveDist: el2 el3 el4 el5

%define real_version 2_7_0

Summary: Validating XML Parser
Name: xerces-c
Version: 2.7.0
Release: 1%{?dist}
License: Apache
Group: Development/Libraries
URL: http://xml.apache.org/xerces-c/

Source: http://www.apache.org/dist/xml/xerces-c/source/xerces-c-src_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards ( DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n xerces-c-src_%{real_version}
%{__perl} -pi.orig -e 's|(PREFIX.)/lib\b|$1/%{_lib}|g' src/xercesc/configure */Makefile.in

%build
export XERCESCROOT="$PWD"
pushd src/xercesc
#autoreconf --install --force
%ifarch alpha ppc64 s390x sparc64 x86_64
./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -b64 -P %{_prefix} -C --libdir="%{_libdir}"
%else
./runConfigure -plinux -cgcc -xg++ -minmem -nsocket -tnative -b32 -P %{_prefix} -C --libdir="%{_libdir}"
%endif
%{__make}
popd

%install
%{__rm} -rf %{buildroot}
export XERCESCROOT="$PWD"
%{__make} install -C src/xercesc DESTDIR="%{buildroot}"
#	PREFIX="%{buildroot}%{_prefix}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.txt Readme.html
%{_libdir}/libxerces*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libxerces*.so
%{_includedir}/xercesc/

%changelog
* Fri Jan 06 2006 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Cleaned SPEC file.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.7.0-1
- Updated to release 2.7.0.

* Thu Sep 22 2005 C.Lee Taylor <leet@leenx.co.za> 2.6.1-1
- Update to 2.6.1
- Build for FC4 32/64bit

* Sat Aug 20 2005 Che
- initial rpm release
