# $Id$
# Authority: dag

Summary: Command line utilities for inotify
Name: inotify-tools
Version: 3.13
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://inotify-tools.sourceforge.net/

Source: http://dl.sf.net/inotify-tools/inotify-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: doxygen

%description
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

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
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-doxygen
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/inotifywait.1*
%doc %{_mandir}/man1/inotifywatch.1*
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_libdir}/libinotifytools.so.*

%files devel
%defattr(-, root, root, 0755)
%doc libinotifytools/src/doc/html/*
%{_includedir}/inotifytools/
%{_libdir}/libinotifytools.so
%exclude %{_libdir}/libinotifytools.la

%changelog
* Thu Mar 27 2008 Dag Wieers <dag@wieers.com> - 3.13-1
- Initial package. (using DAR)
