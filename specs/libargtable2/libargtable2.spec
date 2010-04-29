# $Id$
# Authority: shuff
# Upstream: Stewart Heitmann <sheitmann$users,sourceforge,net>

%define real_name argtable

# change this with each version update
%define real_version 2-12

Summary: An ANSI C command line parser
Name: libargtable2
Version: 2.12
Release: 2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://argtable.sourceforge.net/

Source: http://prdownloads.sourceforge.net/argtable/argtable%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: glibc-devel

%description
Argtable is an ANSI C library for parsing GNU style command line options with a
minimum of fuss. It enables a program's command line syntax to be defined in
the source code as an array of argtable structs. The command line is then
parsed according to that specification and the resulting values are returned in
those same structs where they are accessible to the main program. Both tagged
(-v, --verbose, --foo=bar) and untagged arguments are supported, as are
multiple instances of each argument. Syntax error handling is automatic and the
library also provides the means for generating a textual description of the
command line syntax.

The argtable parsing, validation, and error reporting routines may be replaced
by user-defined callbacks if desired and new argtable data types may be created
to parse user-defined argument types. The parsing itself is done using GNU
getopt so the parser is 100% GNU compatible. Care has also been taken to make
the internal command line buffer handling secure against buffer overun attacks,
as might be attempted with maliciously long command lines.

%package devel
Summary: Headers and development files for argtable.
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Install this package if you want to develop software that uses libargtable.

%prep
%setup -n %{real_name}%{real_version}

%build
%configure
CFLAGS="%{optflags}" %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# we'll handle documentation
%{__rm} -rf %{buildroot}/%{_docdir}/argtable2

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%doc doc/
%doc %{_mandir}/man?/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%doc example/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Thu Apr 29 2010 Steve Huff <shuff@vecna.org> - 2.12-1
- Initial package.
