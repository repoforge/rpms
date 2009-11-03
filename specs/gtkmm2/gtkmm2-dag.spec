# $Id$
# Authority: matthias

%define real_name gtkmm

Summary: C++ interface for GTK (a GUI library for X)
Name: gtkmm2
Version: 2.2.8
Release: 0%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://gtkmm.sourceforge.net/

Source: http://dl.sf.net/gtkmm/gtkmm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsigc++-devel >= 1.2.0, glib2-devel >= 2.0.4, gcc-c++
BuildRequires: atk-devel >= 1.0.0, pango-devel >= 1.0.0, gtk2-devel >= 2.0.5

%description
gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, gtk2-devel, libsigc++-devel >= 1.2.0

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--enable-static \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHANGES COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc PORTING
%doc %{_docdir}/gtkmm-2.0/
%{_includedir}/gtkmm-2.0/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/gtkmm-2.0/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/devhelp/books/gtkmm-2.0/*.devhelp
#exclude %{_libdir}/*.la

%changelog
* Wed Nov 12 2003 Dag Wieers <dag@wieers.com> - 2.2.8-0
- Updated to release 2.2.8.

* Fri Oct 19 2003 Dag Wieers <dag@wieers.com> - 2.2.3-0
- Updated to release 2.2.3.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 2.2.1-0
- Updated to release 2.2.1.

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.

* Sat Oct 19 2002 Dag Wieers <dag@wieers.com> - 1.3.26-0
- Updated to release 1.3.26.

* Sat Oct 12 2002 Dag Wieers <dag@wieers.com> - 1.3.24-0
- Updated to release 1.3.24.

* Wed Oct 2 2002 Dag Wieers <dag@wieers.com> - 1.3.23-0
- Initial package.
