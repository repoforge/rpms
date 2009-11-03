# $Id$
# Authority: dag

# ExcludeDist: el4

Summary: Accessibility implementation for GTK+ and GNOME libraries
Name: gail
Version: 1.8.11
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://developer.gnome.org/projects/gap/

Source: http://ftp.gnome.org/pub/GNOME/sources/gail/1.8/gail-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: atk-devel >= 1.2.0
BuildRequires: libgnomecanvas-devel >= 2.0.1
BuildRequires: gcc-c++
BuildRequires: gettext

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --enable-static --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*
%{_libdir}/gtk-2.0/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.11-1
- Updated to release 1.8.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.2-0.2
- Rebuild for Fedora Core 5.

* Fri Jul 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.8.2-1
- Update to release 1.8.2.

* Sat Jun 28 2003 Dag Wieers <dag@wieers.com> - 2.3.3-0
- Initial package. (using DAR)
