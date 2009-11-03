# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

Summary: Simple API for su and sudo
Name: libgksu
Version: 1.3.8
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/old_stuff/libgksu1.2/libgksu1.2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, bison, pkgconfig, gtk-doc
BuildRequires: glib2-devel >= 2.2, gtk2-devel >= 2.2

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
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang libgksu1.2

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f libgksu1.2.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL
%doc %{_datadir}/gtk-doc/html/libgksu*/
%{_libdir}/libgksu1.2.so.*
%{_libdir}/libgksu1.2/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgksu1.2/
%{_libdir}/libgksu1.2.so
%{_libdir}/pkgconfig/libgksu1.2.pc
%exclude %{_libdir}/libgksu1.2*.la

%changelog
* Fri Oct 12 2007 Dag Wieers <dag@wieers.com> - 1.3.8-1
- Updated to release 1.3.8.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.7-1
- Initial package.
