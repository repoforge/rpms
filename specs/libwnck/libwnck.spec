# $Id$

# Authority: dag

Summary: A library for writing pagers and taskslists.
Name: libwnck
Version: 0.18
Release: 0
Group: System Environment/Libraries
License: GPL
#URL: http://

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.1/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: gtk2 >= 2.0, atk >= 1.0, pango >= 1.0, glib2 >= 2.0

%description
libwnck is a Window Navigator Construction Kit. I.e. a library
for writing pagers and taskslists.

%package devel
Summary: Headers for developing programs that will use %{name}.
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
%{_includedir}/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Mon Feb 03 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
