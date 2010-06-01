# $Id$
# Authority: shuff
# Upstream: <confuse-devel$nongnu,org>

%define real_name confuse

Summary: Configuration file parser library
Name: libconfuse
Version: 2.6
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.nongnu.org/confuse/

Source: http://bzero.se/confuse/confuse-%{version}.tar.gz
Patch0: libconfuse-2.6_werror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gawk
BuildRequires: libtool
BuildRequires: xmlto

%description
libConfuse is a configuration file parser library, licensed under the terms of
the ISC license, and written in C. It supports sections and (lists of) values
(strings, integers, floats, booleans or other sections), as well as some other
features (such as single/double-quoted strings, environment variable expansion,
functions and nested include statements). It makes it very easy to add
configuration file capability to a program using a simple API.

The goal of libConfuse is not to be the configuration file parser library with
a gazillion of features. Instead, it aims to be easy to use and quick to
integrate with your code. libConfuse was called libcfg before, but was changed
to not confuse with other similar libraries. 

%package devel
Summary: Header files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
Install this package if you want to develop software that uses libConfuse.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" %configure \
    --disable-static \
    --enable-shared \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

# install the man pages by hand
%{__install} -m0755 -d %{buildroot}%{_mandir}/man3
%{__mv} doc/man/man3/* %{buildroot}%{_mandir}/man3/
%{__gzip} %{buildroot}%{_mandir}/man3/*
%{__rm} -rf %{buildroot}%{_docdir}/man

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS INSTALL NEWS README 
%{_libdir}/*.so.*
%{_datadir}/locale/*/LC_MESSAGES/*

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS INSTALL NEWS README doc/ examples/
%doc %{_mandir}/man?/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*la

%changelog
* Tue Jun 01 2010 Steve Huff <shuff@vecna.org> - 2.6-2
- Default build is static-only, huh?

* Thu Feb 18 2010 Steve Huff <shuff@vecna.org> - 2.6-1
- Initial package.
