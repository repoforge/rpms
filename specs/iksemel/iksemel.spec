# $Id$
# Authority: dries

Summary: XML-parsing library
Name: iksemel
Version: 1.2
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://iksemel.jabberstudio.org/

Source: http://files.jabberstudio.org/iksemel/iksemel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gnutls-devel

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

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
%{_libdir}/libiksemel.a
%{_libdir}/libiksemel.so
%{_libdir}/pkgconfig/iksemel.pc
%exclude %{_libdir}/*.la

%changelog
* Thu Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
