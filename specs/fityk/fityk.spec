# $Id$
# Authority: dag

Summary: Tool for fitting and analyzing data
Name: fityk
Version: 0.8.6
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.unipress.waw.pl/fityk/

Source: http://dl.sf.net/fityk/fityk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, wxGTK-devel >= 2.6.1, readline-devel 
#BuildRequires: desktop-file-utils

### Builds against own boost headers
#Requires: boost-devel
### gnuplot is recommended, but not required
#Requires: gnuplot

%description
Fityk is a program for nonlinear fitting of analytical functions 
(especially peak-shaped) to data (usually experimental data).
It can be also used for visualization of x-y data only.

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

%build
%configure LDFLAGS="-s"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up docs
%{__rm} -f samples/Makefile* doc/fitykhelp_img/Makefile*

%post
update-desktop-database || :
/sbin/ldconfig

%postun
update-desktop-database || :
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL NEWS README TODO doc/ samples/
%doc %{_mandir}/man1/fityk.1*
%{_bindir}/cfityk
%{_bindir}/fityk
%{_datadir}/applications/fityk.desktop
%{_datadir}/fityk/
%{_datadir}/mime/packages/fityk.xml
%{_datadir}/pixmaps/fityk.png
%{_libdir}/libfityk.so.*
%{_libdir}/libxy.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/fityk/
%{_includedir}/fityk.h
%{_libdir}/libfityk.so
%{_libdir}/libxy.so
%exclude %{_libdir}/libfityk.la
%exclude %{_libdir}/libxy.la

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 0.8.6-2
- Rebuild against wxGTK 2.8.8.
- Updated to release 0.8.6.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Initial package. (Marcin Wojdyr)
