# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

Summary: Simple API for su and sudo
Name: libgksu
Version: 2.0.5
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/libgksu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, bison, pkgconfig, gtk-doc
BuildRequires: glib2-devel >= 2.6, gtk2-devel >= 2.6

Obsoletes: libgksuui <= %{version}-%{release}
Provides: libgksuui = %{version}-%{release}

%description
LibGKSu is a library from the gksu program that provides a simple API for
using su and sudo in programs that need to execute tasks as other users.
It provides X authentication facilities for running programs in a X session.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

Obsoletes: libgksuui-devel <= %{version}-%{release}
Provides: libgksuui-devel = %{version}-%{release}

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
%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL
%doc %{_datadir}/gtk-doc/html/libgksu*/
%config %{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu-properties
%{_datadir}/applications/gksu-properties.desktop
%{_datadir}/libgksu/
%{_datadir}/pixmaps/gksu.png
%{_libdir}/libgksu/gksu-run-helper
%{_libdir}/libgksu2.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgksu/
%{_libdir}/libgksu2.so
%{_libdir}/pkgconfig/libgksu2.pc
%exclude %{_libdir}/libgksu2.la

%changelog
* Fri Oct 12 2007 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.7-1
- Initial package.
