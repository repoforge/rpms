# $Id$
# Authority: shuff
# Upstream: Michael Clark <michael$metaparadigm,com>

Summary: JSON implementation in C
Name: json-c
Version: 0.11
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: https://github.com/json-c/json-c/wiki/

Source: https://s3.amazonaws.com/json-c_releases/releases/json-c-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
JSON-C implements a reference counting object model that allows you to easily
construct JSON objects in C, output them as JSON formatted strings and parse
JSON formatted strings back into the C representation of JSON objects.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package compat
Summary: Compatibility files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}
Requires: pkgconfig

%description compat
This package contains backwards compatilibility header files and static
libraries for %{name}.

%prep
%setup

%build
CFLAGS="-Wno-error" %configure \
    --disable-dependency-tracking \
    --disable-static
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
/sbin/ldconfig 2>/dev/null

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README 
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/json-c/
%{_libdir}/libjson-c.so
%{_libdir}/pkgconfig/json-c.pc
%exclude %{_libdir}/*.la

%files compat
%defattr(-, root, root, 0755)
%{_includedir}/json
%{_libdir}/libjson.so
%{_libdir}/pkgconfig/json.pc

%changelog
* Sun Jul 28 2013 Steve Huff <shuff@vecna.org> - 0.11-1
- Initial package.
