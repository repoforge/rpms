# $Id$
# Authority: dag

Summary: C++ bindings for the ORBit Corba ORB
Name: orbitcpp
Version: 0.30
Release: 0%{?dist}
#Icon: orbitcpp.png
License: GPL
Group: Development/Libraries
URL: http://orbitcpp.sourceforge.net/

Source: http://dl.sf.net/orbitcpp/orbitcpp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


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
Summary: C++ bindings for the ORBit Corba ORB
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This packages contains the header files, libraries and utilities
necessary to write programs that use orbitcpp. If you want to write
such programs, you'll also need to install the orbitcpp package.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/orb/*
%{_datadir}/aclocal/*
%exclude %{_libdir}/*.la

%changelog
* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 0.30
- Updated to release 0.30.

* Mon Apr 30 2001 Dag Wieers <dag@wieers.com> - 0.30
- Initial package.
