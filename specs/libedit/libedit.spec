# $Id$
# Authority: shuff
# Upstream: Jess Thrysoee

### EL6 ships with libedit-2.11-4.20080712cvs.1.el6
# ExclusiveDist: el2 el3 el4 el5

%define tagnum 3.0

Summary: NetBSD Editline library
Name: libedit
Version: 20090923
Release: %{tagnum}_1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.thrysoee.dk/editline/

Source: http://www.thrysoee.dk/editline/libedit-%{version}-3.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: groff
BuildRequires: libtool
BuildRequires: make
BuildRequires: ncurses-devel

%description
This is an autotool- and libtoolized port of the NetBSD Editline library
(libedit). This Berkeley-style licensed command line editor library provides
generic line editing, history, and tokenization functions, similar to those
found in GNU Readline.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{version}-%{tagnum}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL THANKS
%doc doc/ examples/
%{_libdir}/libedit.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la
%{_libdir}/libedit.so

%changelog
* Tue Mar 16 2010 Steve Huff <shuff@vecna.org> - 20090923-3.0_1
- Initial package.
