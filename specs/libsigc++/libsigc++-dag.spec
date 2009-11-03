# $Id$
# Authority: matthias

Summary: Typesafe Signal Framework for C++
Name: libsigc++
Version: 1.2.5
Release: 3%{?dist}
### Needs epoch as el2 comes with version 1:1.0.3 ;-(
Epoch: 1
License: LGPL
Group: System Environment/Libraries
URL: http://libsigc.sourceforge.net/

Source: http://dl.sf.net/libsigc/libsigc++-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libsigc++-examples
### This doesn't work ;-(
#Obsoletes: libsigc++ = 1:1.2.4-0, libsigc++ = 1:1.2.5-0
#Obsoletes: libsigc++ = 1:1.0.3,

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched
by other C++ callback libraries. Libsigc++ is licensed under the GNU
LGPL.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

### This doesn't work ;-(
#Obsoletes: libsigc++-devel = 1:1.2.4, libsigc++-devel = 1:1.2.5
#Obsoletes: libsigc++-devel = 1:1.0.3,

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FEATURES IDEAS NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*
%{_libdir}/sigc++-1.2/
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sigc++-1.2/
#exclude %{_libdir}/*.la
#/usr/bin/*
#/usr/share/aclocal/*

%changelog
* Thu Feb 19 2004 Dag Wieers <dag@wieers.com> - 1:1.2.5-3
- Reintroduced epoch 1 for RHEL21.

* Mon Dec 01 2003 Dag Wieers <dag@wieers.com> - 1.2.5-2
- Removed the epoch. (Philip Trickett)

* Fri May 16 2003 Dag Wieers <dag@wieers.com> - 1:1.2.5-0
- Updated to release 1.2.5.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 1:1.2.4-0
- Updated to release 1.2.4.
- Bumped epoch to 1 (to stay in line with freshrpms).

* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Updated to release 1.2.3.

* Sat Dec 14 2002 Dag Wieers <dag@wieers.com> - 1.2.2-0
- Updated to release 1.2.2.

* Wed Oct 30 2002 Dag Wieers <dag@wieers.com> - 1.2.1-0
- Updated to release 1.2.1.

* Sat Oct 12 2002 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0.

* Wed Oct 2 2002 Dag Wieers <dag@wieers.com> - 1.1.13-0
- Initial release.
