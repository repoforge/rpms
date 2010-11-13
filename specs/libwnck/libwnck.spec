# $Id$
# Authority: dag

### EL6 ships with libwnck-2.28.0-2.el6
### EL5 ships with libwnck-2.16.0-4.fc6
### EL4 ships with libwnck-2.8.1-7.el4
### EL3 ships with libwnck-2.2.3-1.rhel3
# ExclusiveDist: el2

Summary: Library for writing pagers and taskslists
Name: libwnck
Version: 0.18
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: ftp://ftp.gnome.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/libwnck/2.1/libwnck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2 >= 2.0, atk >= 1.0, pango >= 1.0, glib2 >= 2.0

%description
libwnck is a Window Navigator Construction Kit. I.e. a library
for writing pagers and taskslists.

%package devel
Summary: Headers for developing programs that will use %{name}
Group: Development/Libraries

Requires: %{name} = %{version}

%description devel
This package contains the static libraries and header files needed for
developing applications using libwnck.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc ABOUT-NLS
%{_includedir}/libwnck-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-0.2
- Rebuild for Fedora Core 5.

* Mon Feb 03 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
