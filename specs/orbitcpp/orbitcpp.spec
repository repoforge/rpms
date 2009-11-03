# $Id$
# Authority: dag

Summary: C++ bindings for the ORBit Corba ORB
Name: orbitcpp
Version: 1.3.9
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://orbitcpp.sourceforge.net/

Source: http://dl.sf.net/orbitcpp/orbitcpp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: ORBit2 >= 2.5.0
BuildRequires: gcc-c++, autoconf, automake

%description
ORBit-C++ is a project to develop C++ bindings for the ORBit Corba
ORB. ORBit-C++ is Free Software (OpenSource), copyrighted under the
GPL and LGPL.

Primary Objectives
 * Provide a spec-compliant C++ corba mapping for ORBit
 * To allow programmers to use and write ORBit objects and gnome
   components in C++ with little or no runtime overhead (compared to
   writing C ones)
 * Allow C programmers to use C++ objects without having to deal with
   any of that 'horrible C++ syntax'

In short, to C++ programmers, all ORBit objects look like C++
objects, and to C programmers, all ORBit objects should look like C
 objects.

Secondary Objectives
 * Allow C and C++ objects in the same address space to short-circuit
   calls (i.e. no on-the-wire marshalling) for maximum speed.

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	ORBIT_BACKEND_DIR="%{buildroot}%{_libdir}/orbit-2.0/idl-backends"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*
%{_libdir}/orbit-2.0/idl-backends/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/orbitcpp-2.0/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/orbit-2.0/idl-backends/*.a
%exclude %{_libdir}/orbit-2.0/idl-backends/*.la
%{_libdir}/orbit-2.0/idl-backends/*.so

%changelog
* Tue Nov 18 2003 Dag Wieers <dag@wieers.com> - 1.3.8-0
- Updated to release 1.3.8.

* Thu Apr 03 2003 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Updated to release 1.3.5.

* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 0.30.4-0
- Updated to release 0.30.4.

* Mon Apr 30 2001 Dag Wieers <dag@wieers.com> - 0.30-0
- Initial package.
