# $Id$
# Authority: dag

### EL6 ships with check-0.9.8-1.1.el6
### EL5 ships with check-0.9.3-5.fc6
# ExclusiveDist: el2 el3 el4

Summary: Unit test framework for C
Name: check
Version: 0.9.3
Release: 1%{?dist}
License: LGPL
Group: Development/Tools
URL: http://check.sourceforge.net/

Source: http://dl.sf.net/check/check-%{version}.tar.gz
Patch0: check-0.9.2-fPIC.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: docbook-utils

%description
Check is a unit test framework for C. It features a simple interface for 
defining unit tests, putting little in the way of the developer. Tests 
are run in a separate address space, so Check can catch both assertion 
failures and code errors that cause segmentation faults or other signals. 
The output from unit tests can be used within source code editors and IDEs.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Provides: %{name} = %{version}-%{release}
#Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/

%clean
%{__rm} -rf %{buildroot}

%files devel
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING NEWS README doc/
%{_datadir}/aclocal/check.m4
%{_includedir}/check.h
### Static link required !
%{_libdir}/libcheck.a

%changelog
* Wed May 23 2007 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Initial package. (using DAR)
