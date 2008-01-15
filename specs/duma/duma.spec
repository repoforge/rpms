# $Id$
# Authority: dries
# Upstream:  Hayati Ayguen <h_ayguen$web,de>

%define real_version 2_5_10

Summary: Detect Unintended Memory Access
Name: duma
Version: 2.5.10
Release: 1
License: GPL
Group: Development/Tools
URL: http://duma.sourceforge.net/

Source: http://dl.sf.net/duma/duma_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
DUMA (Detect Unintended Memory Access) stops your program on the exact
instruction that overruns (or underruns) a malloc() memory buffer. GDB
will then display the source-code line that causes the bug. It works by
using the virtual-memory hardware to create a red-zone at the border of
each buffer: touch that, and your program stops. It can catch formerly
impossible-to-catch overrun bugs. DUMA is a fork of Bruce Perens'
Electric Fence library.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n duma_%{real_version}

%build
# duma doesn't build with _smp_mflags
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man3/
%{__install} -d -m0755 %{buildroot}%{_libdir}
%makeinstall BIN_INSTALL_DIR="%{buildroot}%{_bindir}" \
    LIB_INSTALL_DIR="%{buildroot}%{_libdir}" \
    MAN_INSTALL_DIR="%{buildroot}%{_mandir}/man3/"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README.txt TODO
%doc %{_mandir}/man3/duma.3*
%{_bindir}/duma
%{_libdir}/libduma.so.*

%files devel
%defattr(-, root, root, 0755)
%exclude %{_libdir}/libduma.a
%{_libdir}/libduma.so

%changelog
* Tue Jan 15 2008 Dries Verachtert <dries@ulyssis.org> - 2.5.10-1
- Updated to release 2.5.10.

* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.8-2
- Fix build on systems with multiple processors, thanks to Brian Watt.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.8-1
- Updated to release 2.5.8.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.7-1
- Updated to release 2.5.7.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.6-1
- Updated to release 2.5.6.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.5-1
- Updated to release 2.5.5.

* Wed Aug 01 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.4-1
- Updated to release 2.5.4.

* Mon Jul 16 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.3-1
- Updated to release 2.5.3.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 2.5.1-1
- Updated to release 2.5.1.

* Thu Apr 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.27-1
- Updated to release 2.4.27.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.26-2
- Fixed the project url and source url.

* Fri Oct 28 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.26-1

- Updated to release 2.4.26.

* Sat Oct 08 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.23-1
- Updated to release 2.4.23.

* Fri Oct 07 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.22-1
- Updated to release 2.4.22.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.19-1
- Initial package.
