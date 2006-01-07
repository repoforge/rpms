# $Id$
# Authority: dries

Summary: Shows dialogs for asking passwords
Name: libgksuui
Version: 1.0.7
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://savannah.nongnu.org/projects/gksu/

Source: http://people.debian.org/~kov/gksu/libgksuui1.0/libgksuui1.0-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, bison, gcc-c++, gtk-doc, pkgconfig, gtk2-devel

%description
Libgksuui uses the Gtk+2 library to show the dialog asking for the target 
user's password when needed. It is used by gksu.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libgksuui1.0-%{version}

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
%doc AUTHORS ChangeLog COPYING INSTALL
%{_libdir}/libgksuui*.so.*
%{_datadir}/gtk-doc/html/libgksuui*/
%{_datadir}/libgksuui*/gksu-auth.png
%{_datadir}/locale/*/*/libgksuui*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/libgksuui*.a
%{_libdir}/libgksuui*.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/libgksuui*.pc

%changelog
* Thu Jan 05 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Initial package.
