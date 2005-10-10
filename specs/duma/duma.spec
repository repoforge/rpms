# $Id$
# Authority: dries
# Upstream:  Hayati Ayguen <h_ayguen$web,de>

%define real_version 2_4_19

Summary: Detect Unintended Memory Access
Name: duma
Version: 2.4.23
Release: 1
License: GPL
Group: Development/Tools
URL: http://www.pf-lug.de/projekte/haya/duma.php

Source: http://www.pf-lug.de/projekte/haya/duma_%{real_version}.tar.gz
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man3 %{buildroot}%{_libdir}
%makeinstall BIN_INSTALL_DIR=%{buildroot}%{_bindir} LIB_INSTALL_DIR=%{buildroot}%{_libdir} MAN_INSTALL_DIR=%{buildroot}%{_mandir}/man3/

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL README TODO
%doc %{_mandir}/man?/duma*
%{_bindir}/duma
%{_libdir}/libduma.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libduma.a
%{_libdir}/libduma.so

%changelog
* Sat Oct 08 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.23-1
- Updated to release 2.4.23.

* Fri Oct 07 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.22-1
- Updated to release 2.4.22.

* Tue Sep 20 2005 Dries Verachtert <dries@ulyssis.org> - 2.4.19-1
- Initial package.
