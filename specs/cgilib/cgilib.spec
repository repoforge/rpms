# $Id$
# Authority: dag

%define debug_package %{nil}

Summary: C interface to CGI (common gateway interface)
Name: cgilib
Version: 0.5
Release: 2.2%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.infodrom.north.de/cgilib/

Source: http://www.infodrom.org/projects/cgilib/download/cgilib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cgilib is a simple library that provides an easy interface to the
common gateway interface, known as CGI. The purpose is to provide an
easy to use interface to CGI if you need to write your program in C
instead of perl.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
#Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%{__make} CFLAGS="%{optflags} -I." libcgi.a

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 cgi.h %{buildroot}%{_includedir}/cgi.h
%{__install} -Dp -m0644 libcgi.a %{buildroot}%{_libdir}/libcgi.a
%{__install} -Dp -m0644 cgi.5 %{buildroot}%{_mandir}/man5/cgi.5

for man in cgi*.3; do
	%{__install} -Dp -m0644 $man %{buildroot}%{_mandir}/man3/$man
done

%clean
%{__rm} -rf %{buildroot}

%files devel
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS cookies.txt readme
%doc cgitest.c jumpto.c
%doc %{_mandir}/man3/cgi*.3*
%doc %{_mandir}/man5/cgi.5*
%{_libdir}/libcgi.a
%{_includedir}/cgi.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-2.2
- Rebuild for Fedora Core 5.

* Thu May 19 2005 Matthias Saou <http://freshrpms.net/> 0.5-2
- Disable debuginfo package, as it ends up empty because there is only a
  static library.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
