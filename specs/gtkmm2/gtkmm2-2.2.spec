# $Id: gtkmm2.spec 4260 2006-03-29 17:04:33Z thias $
# Authority: matthias

Summary: The C++ interface for the GIMP ToolKit (GTK+) GUI library
Name: gtkmm2
Version: 2.2.12
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gtkmm.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/gtkmm/2.2/gtkmm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gtk2-devel >= 2.2.0, libsigc++-devel >= 1.2.0,
Requires: gtk2 >= 2.2.0, libsigc++ >= 1.2.0

%description
gtkmm (previously known as Gtk--) is the official C++ interface for the
popular GUI library GTK+. Highlights include typesafe callbacks, widgets
extensible via inheritance and a comprehensive set of widget classes that
can be freely combined to quickly create complex user interfaces.

%package devel
Summary: Development tools for gtkmm2 applications
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: gtk2-devel, libsigc++-devel >= 1.2.0

%description devel
gtkmm (previously known as Gtk--) is the official C++ interface for the
popular GUI library GTK+. Highlights include typesafe callbacks, widgets
extensible via inheritance and a comprehensive set of widget classes that
can be freely combined to quickly create complex user interfaces.

The gtkmm devel package contains the static libraries and header files
needed for developing GTK+ (GIMP ToolKit) applications in C++.


%prep
%setup -n gtkmm-%{version}

%build
%configure --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot} docs-to-include
%{__make} install DESTDIR="%{buildroot}"
# Move the docs back into place
%{__mkdir} docs-to-include
%{__mv} %{buildroot}%{_docdir}/gtkmm-2.0/* docs-to-include/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog CHANGES COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs-to-include/*
%{_includedir}/*
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/gtkmm-*
%{_libdir}/pkgconfig/*
%{_datadir}/devhelp/books/*

%changelog
* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 2.2.12-1
- Update to 2.2.12.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 2.2.9-2
- Rebuild for Fedora Core 2.

* Fri Mar  5 2004 Matthias Saou <http://freshrpms.net/> 2.2.9-1
- Update to 2.2.9.

* Thu Nov 12 2003 Matthias Saou <http://freshrpms.net/> 2.2.8-1
- Update to 2.2.8.
- Added devhelp book.
- Rebuild for Fedora Core 1.

* Tue Jul 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.5.

* Fri May 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.3.

* Thu May 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.2.2.

* Sun May  4 2003 Matthias Saou <http://freshrpms.net/>
- Initial release based on the gtkmm 1.x spec file.

