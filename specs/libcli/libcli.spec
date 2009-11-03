# $Id$
# Authority: dag

Summary: Cisco-like telnet command-line library
Name: libcli
Version: 1.8.6
Release: 2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.sf.net/projects/libcli/

Source: http://dl.sf.net/libcli/libcli-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libcli provides a shared library for including a Cisco-like command-line
interface into other software. It's a telnet interface which supports
command-line editing, history, authentication and callbacks for a
user-definable function tree.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}/|g' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README Doc/usersguide.html
%{_libdir}/libcli.so.*

%files devel
%defattr(-, root, root, 0755)
%doc clitest.txt Doc/developers.html
%{_includedir}/libcli.h
%{_libdir}/libcli.so

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 1.8.6-2
- Fixed group name.

* Fri Aug 04 2006 Dag Wieers <dag@wieers.com> - 1.8.6-1
- Initial package. (using DAR)
