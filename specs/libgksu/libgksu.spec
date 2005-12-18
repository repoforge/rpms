# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

Summary: Simple API for su and sudo
Name: libgksu
Version: 1.3.7
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/libgksu1.2/libgksu1.2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, bison, pkgconfig, glib2-devel

%description
LibGKSu is a library from the gksu program that provides a simple API for 
using su and sudo in programs that need to execute tasks as other users. 
It provides X authentication facilities for running programs in a X session.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libgksu1.2-%{version}

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
%{_libdir}/libgksu*.so.*
%{_libdir}/libgksu*/
%{_datadir}/gtk-doc/html/libgksu*/
%{_datadir}/locale/*/*/libgksu*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gksu*.h
%{_libdir}/libgksu*.a
%{_libdir}/libgksu*.so
%{_libdir}/pkgconfig/libgksu*pc
%exclude %{_libdir}/libgksu*.la

%changelog
* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.7-1
- Initial package.
