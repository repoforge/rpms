# $Id$
# Authority: dries

Summary: XML-parsing library
Name: iksemel
Version: 1.4
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://code.google.com/p/iksemel/

Source: http://iksemel.googlecode.com/files/iksemel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: gnutls-devel

%description
This is an XML parser library mainly designed for Jabber applications.
It provides SAX, DOM, and special Jabber stream APIs. Library is coded
in ANSI C except the network code (which is POSIX compatible), thus
highly portable.

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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_infodir}/iksemel*
%{_bindir}/ikslint
%{_bindir}/iksperf
%{_bindir}/iksroster
%{_libdir}/libiksemel.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/iksemel.h
%{_libdir}/libiksemel.so
%{_libdir}/pkgconfig/iksemel.pc
%exclude %{_libdir}/libiksemel.la

%changelog
* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Fri Jul 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Thu Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
