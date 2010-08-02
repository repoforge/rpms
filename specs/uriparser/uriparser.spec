# $Id$
# Authority: dag

Summary: URI parsing library - RFC 3986
Name: uriparser
Version: 0.7.5
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://uriparser.sourceforge.net/

Source: http://downloads.sourceforge.net/project/uriparser/Sources/%{version}/uriparser-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cpptest-devel
BuildRequires: doxygen
BuildRequires: graphviz
Requires: cpptest

%description
Uriparser is a strictly RFC 3986 compliant URI parsing library written
in C. uriparser is cross-platform, fast, supports Unicode and is
licensed under the New BSD license.

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
%configure --disable-static

### Remove qhelpgenerator stuff
pushd doc
%{__perl} -pi.orig -e '
        s/^QCH.*//;
        s/^QHG.*//
    ' Doxyfile.in
%configure
%{__make} %{?_smp_mflags}
popd
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"

%{__mv} %{buildroot}%{_docdir}/uriparser-doc/html/ %{buildroot}%{_docdir}/%{name}-%{version}/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING THANKS
%{_libdir}/liburiparser.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
%{_includedir}/uriparser/
%{_libdir}/liburiparser.so
%{_libdir}/pkgconfig/liburiparser.pc
%exclude %{_libdir}/liburiparser.la

%changelog
* Tue Jul 13 2010 Dag Wieers <dag@wieers.com> - 0.7.5-1
- Initial package. (using DAR)
