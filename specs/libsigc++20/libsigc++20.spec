# $Id$
# Authority: dries
# Upstream: <libsigc-list$gnome,org>

Summary: Typesafe callback system for standard C++
Name: libsigc++20
Version: 2.0.17
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://libsigc.sourceforge.net/

Source: http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.0/libsigc++-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
libsigc++ implements a typesafe callback system for standard C++. It allows 
you to define signals and to connect those signals to any callback function, 
either global or a member function, regardless of whether it is static or 
virtual.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libsigc++-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} %{buildroot}%{_docdir}/libsigc-2.0 rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO rpmdocs/*
%{_libdir}/libsigc-2.0.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/sigc++-2.0/
%{_libdir}/libsigc-2.0.a
%{_libdir}/libsigc-2.0.so
%{_libdir}/pkgconfig/sigc++-2.0.pc
%{_libdir}/sigc++-2.0/
%exclude %{_libdir}/*.la

%changelog
* Sun Oct 15 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.17-1
- Initial package.
