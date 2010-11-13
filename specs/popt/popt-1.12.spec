# $Id$
# Authority: dries

### EL6 ships with popt-1.13-7.el6
### EL5 ships with popt-1.10.2.3-20.el5_5.1
### EL4 ships with popt-1.9.1-33_nonptl.el4_8.1
### EL3 ships with popt-1.8.2-32_nonptl
### EL2 ships with popt-1.6.4-7x.20
# Tag: rft

Summary: A C library for parsing command line parameters.
Name: popt
Version: 1.12
Release: 1%{?dist}
License: X Consortium
Group: System Environment/Libraries
Source: http://rpm5.org/files/popt/%{name}-%{version}.tar.gz
BuildRequires: gettext
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Popt is a C library for parsing command line parameters. Popt was
heavily influenced by the getopt() and getopt_long() functions, but it
improves on them by allowing more powerful argument expansion. Popt
can parse arbitrary argv[] style arrays and automatically set
variables based on command line arguments. Popt allows command line
arguments to be aliased via configuration files and includes utility
functions for parsing arbitrary strings into argv[] arrays using
shell-like rules.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang popt

%clean
rm -rf $RPM_BUILD_ROOT

%files -f popt.lang
%defattr(-,root,root)
%{_libdir}/libpopt.*
%{_includedir}/popt.h
%{_mandir}/man3/popt.3*

%changelog
* Tue Jul 10 2007 Jeff Johnson <jbj@rpm5.org>
- release popt-1.12 through rpm5.org.

* Sat Jun  9 2007 Jeff Johnson <jbj@rpm5.org>
- release popt-1.11 through rpm5.org.

* Thu Dec 10 1998 Michael Johnson <johnsonm@redhat.com>
- released 1.2.2; see CHANGES

* Tue Nov 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- added man page to default install

* Thu Oct 22 1998 Erik Troan <ewt@redhat.com>
- see CHANGES file for 1.2

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- added ./configure step to spec file
