# $Id$

Summary: The C++ interface for the GIMP ToolKit (GTK+) GUI library
Name: gtkmm2
Version: 2.2.9
Release: 1
Group: System Environment/Libraries
License: LGPL
URL: http://www.gtkmm.org/
Source: http://dl.sf.net/gtkmm/gtkmm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk2 >= 2.2.0, libsigc++ >= 1.2.0
BuildRequires: gcc-c++, gtk2-devel, libsigc++-devel >= 1.2.0, 
BuildRequires: /usr/bin/sgml2html

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
%setup -q -n gtkmm-%{version}


%build
%configure --enable-static
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%makeinstall
# Move the docs back into place
mkdir docs-to-include
mv %{buildroot}%{_docdir}/gtkmm-2.0/* docs-to-include/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root)
%doc docs-to-include/*
%{_includedir}/*
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/gtkmm-*
%{_libdir}/pkgconfig/*
%{_datadir}/devhelp/books/*


%changelog
* Fri Mar  5 2004 Matthias Saou <http://freshrpms.net/> 2.2.9-1.fr
- Update to 2.2.9.

* Thu Nov 12 2003 Matthias Saou <http://freshrpms.net/> 2.2.8-1.fr
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

